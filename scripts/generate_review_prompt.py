"""Generate a review prompt for auditing FrenchCards TSV output."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIELDS_PATH = ROOT / "specs" / "frenchcards_fields.json"
TARGETS_PATH = ROOT / "specs" / "conjugation_targets.json"
PRONUNCIATION_PATH = ROOT / "specs" / "pronunciation_policy.md"
PEDAGOGY_PATH = ROOT / "specs" / "pedagogy_rubric.md"
TEMPLATE_PATH = ROOT / "prompts" / "review_prompt.md"


REQUIRED_PLACEHOLDERS = {
    "VERB",
    "NOTE_TYPE",
    "FIELD_ORDER",
    "FIELD_SUMMARY",
    "CONJUGATION_TARGETS",
    "PRONUNCIATION_POLICY",
    "PEDAGOGY_RUBRIC",
    "SCOPE_LABEL",
    "SUBJECT_POLICY",
    "TSV_CONTENT",
}


def read_text(path: Path) -> str:
    """Read UTF-8 text from a repository file."""
    try:
        return path.read_text(encoding="utf-8").strip()
    except FileNotFoundError as exc:
        raise SystemExit(f"Missing required file: {path}") from exc


def read_json(path: Path) -> dict:
    """Read JSON from a repository file."""
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise SystemExit(f"Missing required file: {path}") from exc
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid JSON in {path}: {exc}") from exc


def load_field_spec() -> dict:
    """Load and validate the canonical field spec."""
    spec = read_json(FIELDS_PATH)
    fields = spec.get("fields")
    if not isinstance(fields, list) or spec.get("field_count") != len(fields):
        raise SystemExit(f"Invalid field specification in {FIELDS_PATH}")
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


def targets_summary(scope: str) -> str:
    """Render target rows for the selected scope."""
    data = read_json(TARGETS_PATH)
    lines = [
        f"Finite subjects: {', '.join(data['finite_subjects'])}",
        f"Imperative subjects: {', '.join(data['imperative_subjects'])}",
        f"Non-finite policy: Person = {data['non_finite_person']}; SubjectFR = {data['non_finite_subject']}",
        "",
        f"Targets included in `{scope}` scope:",
    ]
    for target in data["targets"]:
        if scope in target["scopes"]:
            lines.append(f"- {target['mood']} — {target['tense']} ({target['kind']})")
    return "\n".join(lines)


def subject_policy_text(subjects: str) -> str:
    """Describe subject behavior for the review prompt."""
    if subjects == "split":
        return "split subjects; finite non-imperative rows should separate je, tu, il, elle, on, nous, vous, ils, and elles."
    return "merged subjects; merged rows are acceptable only when pedagogically safe, using slash-separated labels such as il/elle/on or ils/elles."


def render_template(template: str, values: dict[str, str]) -> str:
    """Render the review prompt and fail on missing or unresolved placeholders."""
    missing = [name for name in REQUIRED_PLACEHOLDERS if f"{{{{{name}}}}}" not in template]
    if missing:
        raise SystemExit(
            "Template is missing required placeholder(s): " + ", ".join(sorted(missing))
        )

    rendered = template
    for key, value in values.items():
        rendered = rendered.replace(f"{{{{{key}}}}}", value)

    unresolved = sorted(set(part.split("}}", 1)[0] for part in rendered.split("{{")[1:]))
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
    """Build a TSV audit prompt."""
    spec = load_field_spec()
    tsv_content = read_text(args.input_tsv) if args.input_tsv else "PASTE TSV HERE"
    values = {
        "VERB": args.verb,
        "NOTE_TYPE": spec["note_type"],
        "FIELD_ORDER": field_order_text(spec["fields"]),
        "FIELD_SUMMARY": field_summary_text(spec["fields"]),
        "CONJUGATION_TARGETS": targets_summary(args.scope),
        "PRONUNCIATION_POLICY": read_text(PRONUNCIATION_PATH),
        "PEDAGOGY_RUBRIC": read_text(PEDAGOGY_PATH),
        "SCOPE_LABEL": args.scope,
        "SUBJECT_POLICY": subject_policy_text(args.subjects),
        "TSV_CONTENT": tsv_content,
    }
    return render_template(read_text(TEMPLATE_PATH), values)


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Generate a review prompt for FrenchCards TSV output."
    )
    parser.add_argument("--verb", required=True, help="French infinitive to review.")
    parser.add_argument(
        "--scope",
        choices=("full", "modern", "literary"),
        default="full",
        help="Conjugation scope expected in the TSV.",
    )
    parser.add_argument(
        "--subjects",
        choices=("split", "merged"),
        default="split",
        help="Subject policy expected in the TSV.",
    )
    parser.add_argument(
        "--input-tsv",
        type=Path,
        help="Optional TSV file to embed in the review prompt.",
    )
    parser.add_argument("--output", type=Path, help="Optional path to save the prompt.")
    parser.add_argument(
        "--no-clipboard",
        action="store_true",
        help="Do not copy the generated review prompt to the clipboard.",
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Do not print the generated review prompt to stdout.",
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
