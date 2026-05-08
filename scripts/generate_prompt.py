"""Generate strict prompts for producing FrenchCards Anki TSV rows."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIELDS_PATH = ROOT / "specs" / "frenchcards_fields.json"
CARD_TYPES_PATH = ROOT / "specs" / "frenchcards_card_types.md"
SCOPE_PATH = ROOT / "specs" / "conjugation_scope.md"
TARGETS_PATH = ROOT / "specs" / "conjugation_targets.json"
PRONUNCIATION_PATH = ROOT / "specs" / "pronunciation_policy.md"
PEDAGOGY_PATH = ROOT / "specs" / "pedagogy_rubric.md"
RULES_PATH = ROOT / "specs" / "generation_rules.md"
TEMPLATE_PATH = ROOT / "prompts" / "base_prompt.md"


REQUIRED_PLACEHOLDERS = {
    "VERB",
    "OPTIONAL_MEANING",
    "CONSTRUCTION_TARGET",
    "CONSTRUCTION_METADATA",
    "NOTE_TYPE",
    "FIELD_ORDER",
    "FIELD_SUMMARY",
    "CARD_TYPE_RULES",
    "CONJUGATION_SCOPE",
    "CONJUGATION_TARGETS",
    "PRONUNCIATION_POLICY",
    "PEDAGOGY_RUBRIC",
    "GENERATION_RULES",
    "AUDIT_RULES",
    "OUTPUT_INSTRUCTIONS",
    "SUBJECT_POLICY",
    "SCOPE_LABEL",
}


def read_text(path: Path) -> str:
    """Read UTF-8 text from a repository file."""
    try:
        return path.read_text(encoding="utf-8").strip()
    except FileNotFoundError as exc:
        raise SystemExit(f"Missing required file: {path}") from exc


def load_json(path: Path) -> dict:
    """Load a UTF-8 JSON file."""
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise SystemExit(f"Missing required file: {path}") from exc
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid JSON in {path}: {exc}") from exc


def load_field_spec(path: Path) -> dict:
    """Load and lightly validate the canonical FrenchCards field spec."""
    spec = load_json(path)
    fields = spec.get("fields")
    field_count = spec.get("field_count")
    if not isinstance(fields, list) or not fields:
        raise SystemExit(f"{path} must contain a non-empty 'fields' list.")
    if field_count != len(fields):
        raise SystemExit(
            f"{path} field_count is {field_count}, but {len(fields)} fields were found."
        )
    return spec


def field_order_text(fields: list[dict]) -> str:
    """Render the canonical field order as a numbered Markdown list."""
    return "\n".join(f"{index}. {field['name']}" for index, field in enumerate(fields, 1))


def field_summary_text(fields: list[dict]) -> str:
    """Render field descriptions from the canonical spec."""
    lines = []
    for field in fields:
        requirement = "required" if field.get("required") else "optional"
        lines.append(f"- `{field['name']}` ({requirement}): {field['description']}")
    return "\n".join(lines)


def subject_policy_text(subjects: str) -> str:
    """Describe split or merged subject behavior for the rendered prompt."""
    if subjects == "split":
        return (
            "split. Generate separate finite non-imperative notes for je, tu, il, "
            "elle, on, nous, vous, ils, and elles. Use j’ before a vowel or mute h "
            "where appropriate."
        )
    return (
        "merged. Merge subjects only when the surface verb form and production "
        "behavior are genuinely identical and pedagogically safe. Use slash-separated "
        "labels such as il/elle/on or ils/elles in Person and SubjectFR. When unsure, split."
    )


def construction_target_text(args: argparse.Namespace) -> str:
    """Render construction target summary."""
    if args.construction_fr:
        return f"Target construction: `{args.construction_fr}`"
    return (
        "Target construction: not supplied; infer one high-value construction for this "
        "verb and keep the entire TSV limited to that construction."
    )


def construction_metadata_text(args: argparse.Namespace) -> str:
    """Render optional construction metadata supplied by the user."""
    items = [
        ("ConstructionID", args.construction_id),
        ("ConstructionMeaningEN", args.construction_meaning),
        ("SemanticFrame", args.semantic_frame),
        ("ValencyClass", args.valency_class),
        ("ArgumentStructure", args.argument_structure),
        ("ArgumentSlots", args.argument_slots),
        ("ComplementTypes", args.complement_types),
        ("ConstructionSubpatterns", args.subpatterns),
        ("PrepositionBehavior", args.preposition_behavior),
        ("PronounBehavior", args.pronoun_behavior),
        ("CliticOrderNote", args.clitic_order_note),
        ("ConstructionConstraints", args.construction_constraints),
        ("ConstructionContrastNote", args.construction_contrast_note),
        ("AllowedForms", args.allowed_forms),
    ]
    filled = [(name, value) for name, value in items if value]
    if not filled:
        return (
            "Construction metadata: not supplied; infer accurate construction metadata "
            "and keep it consistent across rows."
        )
    lines = ["Construction metadata supplied by user:"]
    lines.extend(f"- {name}: `{value}`" for name, value in filled)
    return "\n".join(lines)


def conjugation_targets_text(scope: str) -> str:
    """Render canonical target rows for the selected scope."""
    data = load_json(TARGETS_PATH)
    lines = [
        f"Finite subjects: {', '.join(data['finite_subjects'])}",
        f"Imperative subjects: {', '.join(data['imperative_subjects'])}",
        f"Non-finite forms: Person = {data['non_finite_person']}; SubjectFR = {data['non_finite_subject']}",
        "",
        f"Generate these target categories for `{scope}` scope:",
    ]
    for target in data["targets"]:
        if scope in target["scopes"]:
            lines.append(f"- {target['mood']} — {target['tense']} ({target['kind']})")
    return "\n".join(lines)


def audit_rules_text(field_count: int) -> str:
    """Return the mandatory private audit checklist."""
    return f"""Perform a private self-audit before producing the final TSV. Do not show the audit.

1. STRUCTURE AUDIT
- every row has exactly {field_count} fields
- field order exactly matches `FrenchCards`
- no header row
- no missing cells caused by forgotten tabs
- optional blanks are represented by empty cells, not omitted columns
- no tabs or line breaks inside cell content

2. CONSTRUCTION AND CONJUGATION AUDIT
- the French answer actually contains the target form for this verb, mood, tense, and person
- the French answer uses the target construction, not another construction of the same root verb
- the person and `SubjectFR` are correct
- imperative rows only use `tu`, `nous`, and `vous`
- non-finite rows use `Person = N/A` and `SubjectFR = ?`
- construction metadata is consistent with syntax, complement behavior, and pronoun behavior
- if the construction has subpatterns, the file rotates them intentionally and the metadata explains the pronoun behavior for each complement type

3. NATURALNESS AUDIT
- English prompts are natural and varied
- English prompts are grammatically correct, including subject-verb agreement
- English prompts cue the correct tense, mood, and construction
- negative rows are included when useful, with spoken dropped-ne only in appropriate spoken or mixed contexts
- question rows are included when useful, with question strategy matching register
- register contrasts are marked when they affect the expected answer
- clitic behavior is taught when the construction naturally supports it, without artificial stacks
- French answers are natural, concise, and high-value for learning
- avoid awkward literal translations when better French exists
- avoid near-duplicate prompts whenever reasonably possible

4. TENSE REFERENCE AUDIT
- `TenseOverview` correctly identifies the practical time/aspect/mood value
- `TenseUseNote` gives a useful operational rule
- `TenseParadigmFR` matches the current mood/tense of the target verb
- `TenseParadigmIPA` matches `TenseParadigmFR` in broad modern Parisian IPA

5. PRONUNCIATION AUDIT
- IPA is broad modern Parisian / standard metropolitan
- pronunciation notes are short and practical
- liaison, elision, encha?nement, nasal vowels, silent final consonants, h aspir? behavior, and /y/ vs /u/ are noted when relevant
- no overlong phonetics essays

6. OPTIONAL-FIELD AUDIT
- construction-production fields are all-filled or all-blank; no partially filled construction-production groups
- construction-production fields are only filled when there is a genuine construction behavior or reusable chunk worth isolating
- construction-production prompts test useful transformations, such as pronominalization, when that is the construction behavior being isolated
- unused optional fields are left blank

7. LITERARY-SCOPE AUDIT
- literary forms are treated as active-production targets too
- literary labels and usage notes are accurate and not mixed carelessly with spoken-only labels

8. FINAL TSV AUDIT
- output contains only TSV rows
- no prose before or after
- no code fences
- no extra blank lines at start or end
- no replacement question marks or mojibake in French, IPA, tense labels, construction fields, or prompts"""

def output_instructions_text(field_count: int) -> str:
    """Return strict TSV output requirements."""
    return f"""Return RAW TSV ONLY.

Do not output Markdown code fences, explanations, commentary, numbering, a header row, or column titles.

Encoding requirement: output must be valid UTF-8. Preserve all Unicode characters exactly, including French accents, curly apostrophes, em dashes, and IPA symbols such as ʁ, ɛ, ɔ̃, œ, ø, ɥ, ʒ, and ‿. Do not replace unsupported characters with question marks or mojibake. If UTF-8 cannot be preserved, stop instead of emitting damaged TSV.

Output exactly one note per line. Each line must contain exactly {field_count} tab-separated fields in the exact `FrenchCards` field order. Optional unused fields must be empty cells, but their columns must still be preserved.

Every field must stay on a single line. Do not put literal tab characters or literal line breaks inside field content. Normalize internal line breaks to spaces. Preserve UTF-8 characters such as accents and IPA symbols.

Malformed TSV is a failure. The response is wrong if:
- there is any prose before or after the TSV
- there is a header row
- any row has fewer than {field_count} fields
- any row has more than {field_count} fields
- the column order differs from the specified order
- any accent, apostrophe, em dash, or IPA symbol has been replaced by `?` or mojibake"""


def render_template(template: str, values: dict[str, str]) -> str:
    """Render the base prompt and fail if placeholders are missing or unresolved."""
    missing = [name for name in REQUIRED_PLACEHOLDERS if f"{{{{{name}}}}}" not in template]
    if missing:
        raise SystemExit(
            "Template is missing required placeholder(s): " + ", ".join(sorted(missing))
        )

    rendered = template
    for key, value in values.items():
        rendered = rendered.replace(f"{{{{{key}}}}}", value)

    unresolved = sorted(
        set(
            name
            for name in (part.split("}}", 1)[0] for part in rendered.split("{{")[1:])
            if name in REQUIRED_PLACEHOLDERS
        )
    )
    if unresolved:
        raise SystemExit(
            "Template contains unresolved placeholder(s): "
            + ", ".join(f"{{{{{name}}}}}" for name in unresolved)
        )
    return rendered.rstrip() + "\n"


def copy_to_clipboard(text: str) -> str | None:
    """Copy text to the system clipboard, returning an error message on failure."""
    if sys.platform.startswith("win"):
        try:
            subprocess.run(
                [
                    "powershell",
                    "-NoProfile",
                    "-Command",
                    "Set-Clipboard -Value ([Console]::In.ReadToEnd())",
                ],
                input=text,
                text=True,
                encoding="utf-8",
                check=True,
            )
            return None
        except Exception as ps_error:
            powershell_error = ps_error
    else:
        powershell_error = None

    try:
        import tkinter

        root = tkinter.Tk()
        root.withdraw()
        root.clipboard_clear()
        root.clipboard_append(text)
        root.update()
        root.destroy()
        return None
    except Exception as tk_error:
        if powershell_error:
            return f"could not copy to clipboard: {powershell_error}; tkinter fallback failed: {tk_error}"
        return f"could not copy to clipboard with tkinter: {tk_error}"


def build_prompt(args: argparse.Namespace) -> str:
    """Build a ready-to-paste FrenchCards generation prompt."""
    spec = load_field_spec(FIELDS_PATH)
    fields = spec["fields"]
    field_count = spec["field_count"]
    optional_meaning = (
        f"Provided root verb meaning: `{args.meaning}`"
        if args.meaning
        else "Provided root verb meaning: not supplied; infer the compact broad root meaning."
    )

    values = {
        "VERB": args.verb,
        "OPTIONAL_MEANING": optional_meaning,
        "CONSTRUCTION_TARGET": construction_target_text(args),
        "CONSTRUCTION_METADATA": construction_metadata_text(args),
        "NOTE_TYPE": spec["note_type"],
        "FIELD_ORDER": field_order_text(fields),
        "FIELD_SUMMARY": field_summary_text(fields),
        "CARD_TYPE_RULES": read_text(CARD_TYPES_PATH),
        "CONJUGATION_SCOPE": read_text(SCOPE_PATH),
        "CONJUGATION_TARGETS": conjugation_targets_text(args.scope),
        "PRONUNCIATION_POLICY": read_text(PRONUNCIATION_PATH),
        "PEDAGOGY_RUBRIC": read_text(PEDAGOGY_PATH),
        "GENERATION_RULES": read_text(RULES_PATH),
        "AUDIT_RULES": audit_rules_text(field_count),
        "OUTPUT_INSTRUCTIONS": output_instructions_text(field_count),
        "SUBJECT_POLICY": subject_policy_text(args.subjects),
        "SCOPE_LABEL": args.scope,
    }
    return render_template(read_text(TEMPLATE_PATH), values)


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Generate a strict construction-aware prompt for FrenchCards TSV production."
    )
    parser.add_argument("--verb", required=True, help="French infinitive to generate.")
    parser.add_argument("--meaning", help="Optional broad English root meaning.")
    parser.add_argument("--construction-id", help="Stable construction identifier.")
    parser.add_argument("--construction-fr", help="Target French construction pattern.")
    parser.add_argument("--construction-meaning", help="English meaning of the construction.")
    parser.add_argument("--semantic-frame", help="Semantic frame label.")
    parser.add_argument("--valency-class", help="Valency class for the construction.")
    parser.add_argument("--argument-structure", help="Function-signature style argument structure.")
    parser.add_argument("--argument-slots", help="Semicolon-separated construction input slots.")
    parser.add_argument("--complement-types", help="Allowed complement types.")
    parser.add_argument(
        "--subpatterns",
        help=(
            "Optional semicolon-separated subpatterns to rotate inside one construction, "
            "such as thing -> en; infinitive -> en as known idea; person -> de + stressed pronoun."
        ),
    )
    parser.add_argument("--preposition-behavior", help="Required preposition behavior.")
    parser.add_argument("--pronoun-behavior", help="Pronoun behavior for complements.")
    parser.add_argument("--clitic-order-note", help="Relevant clitic order note.")
    parser.add_argument("--construction-constraints", help="Construction restrictions or constraints.")
    parser.add_argument("--construction-contrast-note", help="Contrast with nearby constructions.")
    parser.add_argument("--allowed-forms", help="Natural forms for this construction.")
    parser.add_argument(
        "--scope",
        choices=("full", "modern", "literary"),
        default="full",
        help="Conjugation coverage scope.",
    )
    parser.add_argument(
        "--subjects",
        choices=("split", "merged"),
        default="split",
        help="Subject generation behavior.",
    )
    parser.add_argument("--output", type=Path, help="Optional path to save the prompt.")
    parser.add_argument(
        "--no-clipboard",
        action="store_true",
        help="Do not copy the generated prompt to the clipboard.",
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Do not print the generated prompt to stdout.",
    )
    return parser.parse_args()


def main() -> int:
    """CLI entry point."""
    args = parse_args()
    prompt = build_prompt(args)
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    if not args.no_clipboard:
        clipboard_error = copy_to_clipboard(prompt)
        if clipboard_error:
            print(f"Warning: {clipboard_error}", file=sys.stderr)

    if not args.quiet:
        print(prompt, end="")

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(prompt, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
