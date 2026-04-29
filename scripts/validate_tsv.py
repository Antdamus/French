"""Validate FrenchCards TSV files against canonical structural rules."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIELDS_PATH = ROOT / "specs" / "frenchcards_fields.json"
TARGETS_PATH = ROOT / "specs" / "conjugation_targets.json"

ENUMS = {
    "Regularity": {"regular", "irregular", "semi-irregular"},
    "VerbGroup": {"-er", "-ir", "-re", "irregular family", "other"},
    "Auxiliary": {"avoir", "être", "both", "N/A"},
    "Register": {"spoken", "standard written", "literary", "formal", "mixed"},
    "FrequencyTier": {"high", "medium", "literary"},
}

IDIOM_FIELDS = [
    "IdiomPromptEN",
    "IdiomAnswerFR",
    "IdiomAnswerIPA",
    "IdiomPronunciationNote",
]

FORM_REPAIR_FIELDS = [
    "FormPrompt",
    "FormAnswerFR",
    "FormAnswerIPA",
    "FormPronunciationNote",
]


def load_json(path: Path) -> dict:
    """Load a UTF-8 JSON file."""
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise SystemExit(f"Missing required file: {path}") from exc
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid JSON in {path}: {exc}") from exc


def load_specs() -> tuple[list[dict], dict]:
    """Load canonical field and conjugation target specs."""
    field_spec = load_json(FIELDS_PATH)
    fields = field_spec.get("fields", [])
    if not isinstance(fields, list) or field_spec.get("field_count") != len(fields):
        raise SystemExit(f"Invalid field specification in {FIELDS_PATH}")
    return fields, load_json(TARGETS_PATH)


def target_lookup(target_spec: dict) -> dict[tuple[str, str], dict]:
    """Index target policies by mood and tense."""
    return {
        (target["mood"], target["tense"]): target
        for target in target_spec.get("targets", [])
    }


def expected_rows_for_scope(
    target_spec: dict, scope: str, subjects: str
) -> set[tuple[str, str, str]]:
    """Build expected Mood/Tense/Person rows for optional coverage checks."""
    finite_subjects = target_spec["finite_subjects"]
    imperative_subjects = target_spec["imperative_subjects"]
    non_finite_person = target_spec["non_finite_person"]
    expected: set[tuple[str, str, str]] = set()

    for target in target_spec["targets"]:
        if scope not in target["scopes"]:
            continue
        if target["kind"] == "finite":
            people = finite_subjects if subjects == "split" else ["*"]
        elif target["kind"] == "imperative":
            people = imperative_subjects
        else:
            people = [non_finite_person]
        for person in people:
            expected.add((target["mood"], target["tense"], person))
    return expected


def line_to_row(field_names: list[str], fields: list[str]) -> dict[str, str]:
    """Map a parsed TSV line to a row dictionary."""
    return dict(zip(field_names, fields))


def validate_enum_fields(row: dict[str, str], line_number: int) -> list[str]:
    """Validate finite enum fields."""
    errors = []
    for field_name, allowed_values in ENUMS.items():
        value = row[field_name]
        if value and value not in allowed_values:
            allowed = " / ".join(sorted(allowed_values))
            errors.append(
                f"Line {line_number}: {field_name} must be one of {allowed}; found {value!r}."
            )
    return errors


def validate_optional_group(
    row: dict[str, str], line_number: int, group_name: str, group_fields: list[str]
) -> list[str]:
    """Ensure optional card field groups are all filled or all blank."""
    filled = [name for name in group_fields if row[name]]
    if filled and len(filled) != len(group_fields):
        missing = [name for name in group_fields if not row[name]]
        return [
            f"Line {line_number}: {group_name} fields are partially filled; missing {', '.join(missing)}."
        ]
    return []


def validate_target_policy(
    row: dict[str, str],
    line_number: int,
    target_spec: dict,
    targets: dict[tuple[str, str], dict],
    scope: str | None,
    subjects: str,
) -> list[str]:
    """Validate mood, tense, person, and subject policy."""
    errors = []
    mood = row["Mood"]
    tense = row["Tense"]
    person = row["Person"]
    subject = row["SubjectFR"]
    target = targets.get((mood, tense))

    if target is None:
        return [f"Line {line_number}: unknown Mood/Tense combination {mood!r} / {tense!r}."]

    if scope and scope not in target["scopes"]:
        errors.append(
            f"Line {line_number}: {mood} / {tense} is not part of {scope!r} scope."
        )

    if target["kind"] == "finite":
        allowed_people = set(target_spec["finite_subjects"])
        allowed_subjects = allowed_people | {"j’"}
        people = person.split("/") if subjects == "merged" else [person]
        subject_parts = subject.split("/") if subjects == "merged" else [subject]
        invalid_people = [value for value in people if value not in allowed_people]
        invalid_subjects = [value for value in subject_parts if value not in allowed_subjects]
        if invalid_people:
            errors.append(
                f"Line {line_number}: finite row Person contains invalid subject label(s): {', '.join(invalid_people)}."
            )
        if invalid_subjects:
            errors.append(
                f"Line {line_number}: finite row SubjectFR contains invalid subject label(s): {', '.join(invalid_subjects)}."
            )
        if subjects == "split" and "/" in person + subject:
            errors.append(
                f"Line {line_number}: slash-separated merged subjects require --subjects merged."
            )
        if "j’" in subject_parts and "je" not in people:
            errors.append(f"Line {line_number}: SubjectFR j’ is only valid with Person je.")
    elif target["kind"] == "imperative":
        allowed_people = set(target_spec["imperative_subjects"])
        if person not in allowed_people:
            errors.append(
                f"Line {line_number}: imperative row Person must be tu, nous, or vous; found {person!r}."
            )
        if subject not in allowed_people:
            errors.append(
                f"Line {line_number}: imperative row SubjectFR must be tu, nous, or vous; found {subject!r}."
            )
    else:
        expected_person = target_spec["non_finite_person"]
        expected_subject = target_spec["non_finite_subject"]
        if person != expected_person or subject != expected_subject:
            errors.append(
                f"Line {line_number}: non-finite rows must use Person = {expected_person} and SubjectFR = {expected_subject}."
            )

    return errors


def validate_tsv(
    path: Path,
    field_defs: list[dict],
    target_spec: dict,
    scope: str | None,
    subjects: str,
    check_coverage: bool,
) -> list[str]:
    """Return validation errors for a TSV file."""
    errors: list[str] = []
    field_names = [field["name"] for field in field_defs]
    required_names = [field["name"] for field in field_defs if field.get("required")]
    expected_count = len(field_names)
    targets = target_lookup(target_spec)
    seen_targets: set[tuple[str, str, str]] = set()

    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return [f"Input file does not exist: {path}"]

    if not text.strip():
        return ["TSV file is empty."]

    lines = text.splitlines()
    first_fields = lines[0].split("\t") if lines else []
    if first_fields == field_names or first_fields[:3] == field_names[:3]:
        errors.append("Header row detected; FrenchCards imports require no header row.")

    for line_number, line in enumerate(lines, 1):
        if line == "":
            errors.append(f"Line {line_number}: blank lines are not valid TSV rows.")
            continue

        fields = line.split("\t")
        actual_count = len(fields)
        if actual_count != expected_count:
            errors.append(
                f"Line {line_number}: expected {expected_count} fields, found {actual_count}."
            )
            continue

        row = line_to_row(field_names, fields)
        for name in required_names:
            if row[name] == "":
                errors.append(f"Line {line_number}: required field {name} is blank.")

        errors.extend(validate_enum_fields(row, line_number))
        errors.extend(validate_optional_group(row, line_number, "Idiom", IDIOM_FIELDS))
        errors.extend(
            validate_optional_group(row, line_number, "Form repair", FORM_REPAIR_FIELDS)
        )
        errors.extend(
            validate_target_policy(row, line_number, target_spec, targets, scope, subjects)
        )

        if row["AudioFR"]:
            errors.append(f"Line {line_number}: AudioFR must be blank for now.")

        target = targets.get((row["Mood"], row["Tense"]))
        if target and target["kind"] == "finite" and subjects == "merged":
            seen_targets.add((row["Mood"], row["Tense"], "*"))
        else:
            seen_targets.add((row["Mood"], row["Tense"], row["Person"]))

    if check_coverage:
        if not scope:
            errors.append("--check-coverage requires --scope.")
        else:
            expected = expected_rows_for_scope(target_spec, scope, subjects)
            missing = sorted(expected - seen_targets)
            extra = sorted(seen_targets - expected)
            for mood, tense, person in missing:
                errors.append(
                    f"Coverage: missing target row for {mood} / {tense} / {person}."
                )
            for mood, tense, person in extra:
                errors.append(
                    f"Coverage: unexpected target row for {mood} / {tense} / {person}."
                )

    return errors


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Validate raw TSV for the FrenchCards Anki note type."
    )
    parser.add_argument("--input", required=True, type=Path, help="Path to TSV file.")
    parser.add_argument(
        "--scope",
        choices=("full", "modern", "literary"),
        help="Optional scope to enforce for Mood/Tense combinations.",
    )
    parser.add_argument(
        "--subjects",
        choices=("split", "merged"),
        default="split",
        help="Subject policy for optional coverage checks.",
    )
    parser.add_argument(
        "--check-coverage",
        action="store_true",
        help="Require all target rows for --scope to be present.",
    )
    return parser.parse_args()


def main() -> int:
    """CLI entry point."""
    args = parse_args()
    field_defs, target_spec = load_specs()
    errors = validate_tsv(
        args.input,
        field_defs,
        target_spec,
        args.scope,
        args.subjects,
        args.check_coverage,
    )
    if errors:
        print("TSV validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("TSV validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
