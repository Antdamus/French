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
    "IDIOM_POLICY",
    "FORM_REPAIR_POLICY",
}


def read_text(path: Path) -> str:
    """Read UTF-8 text from a repository file."""
    try:
        return path.read_text(encoding="utf-8").strip()
    except FileNotFoundError as exc:
        raise SystemExit(f"Missing required file: {path}") from exc


def load_field_spec(path: Path) -> dict:
    """Load and lightly validate the canonical FrenchCards field spec."""
    try:
        spec = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise SystemExit(f"Missing required file: {path}") from exc
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid JSON in {path}: {exc}") from exc

    fields = spec.get("fields")
    field_count = spec.get("field_count")
    if not isinstance(fields, list) or not fields:
        raise SystemExit(f"{path} must contain a non-empty 'fields' list.")
    if field_count != len(fields):
        raise SystemExit(
            f"{path} field_count is {field_count}, but {len(fields)} fields were found."
        )
    return spec


def load_json(path: Path) -> dict:
    """Load a UTF-8 JSON file."""
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise SystemExit(f"Missing required file: {path}") from exc
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid JSON in {path}: {exc}") from exc


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


def idiom_policy_text(choice: str) -> str:
    """Describe how idiom fields should be handled."""
    policies = {
        "auto": "auto. Fill idiom fields only for genuine high-value idioms or chunks.",
        "always": "always. Include idiom fields wherever a strong, natural high-value idiom or chunk can be made.",
        "never": "never. Leave all idiom fields blank.",
    }
    return policies[choice]


def form_repair_policy_text(choice: str) -> str:
    """Describe how form repair fields should be handled."""
    policies = {
        "auto": "auto. Fill form repair fields only when the form is irregular, confusable, or worth isolating.",
        "always": "always. Include form repair fields for every row with a concise isolated target form.",
        "never": "never. Leave all form repair fields blank.",
    }
    return policies[choice]


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

2. CONJUGATION AUDIT
- the French answer actually contains the target form for this verb, mood, tense, and person
- the person and `SubjectFR` are correct
- imperative rows only use `tu`, `nous`, and `vous`
- non-finite rows use `Person = N/A` and `SubjectFR = —`

3. NATURALNESS AUDIT
- English prompts are natural and varied
- French answers are natural, concise, and high-value for learning
- avoid awkward literal translations when better French exists
- avoid near-duplicate prompts whenever reasonably possible

4. PRONUNCIATION AUDIT
- IPA is broad modern Parisian / standard metropolitan
- pronunciation notes are short and practical
- no overlong phonetics essays

5. OPTIONAL-FIELD AUDIT
- idiom fields are only filled when there is a genuine idiom or high-value chunk
- form repair fields are only filled when justified
- unused optional fields are left blank

6. LITERARY-SCOPE AUDIT
- literary forms are treated as active-production targets too
- literary labels and usage notes are accurate and not mixed carelessly with spoken-only labels

7. FINAL TSV AUDIT
- output contains only TSV rows
- no prose before or after
- no code fences
- no extra blank lines at start or end
- no replacement question marks or mojibake in French, IPA, tense labels, or form prompts"""


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
        f"Provided English meaning: `{args.meaning}`" if args.meaning else "Provided English meaning: not supplied; infer the compact core meaning."
    )

    values = {
        "VERB": args.verb,
        "OPTIONAL_MEANING": optional_meaning,
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
        "IDIOM_POLICY": idiom_policy_text(args.include_idioms),
        "FORM_REPAIR_POLICY": form_repair_policy_text(args.include_form_repair),
    }
    return render_template(read_text(TEMPLATE_PATH), values)


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Generate a strict prompt for FrenchCards TSV production."
    )
    parser.add_argument("--verb", required=True, help="French infinitive to generate.")
    parser.add_argument("--meaning", help="Optional compact English meaning.")
    parser.add_argument(
        "--scope",
        choices=("full", "modern", "literary"),
        default="full",
        help="Conjugation coverage scope.",
    )
    parser.add_argument(
        "--include-idioms",
        choices=("auto", "always", "never"),
        default="auto",
        help="How to fill optional idiom fields.",
    )
    parser.add_argument(
        "--include-form-repair",
        choices=("auto", "always", "never"),
        default="auto",
        help="How to fill optional form repair fields.",
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
