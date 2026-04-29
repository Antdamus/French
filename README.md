# FrenchCards Prompt Toolkit

This repository helps generate strict, ready-to-paste prompts for producing and reviewing Anki-ready TSV rows for the existing Anki note type `FrenchCards`.

The repository does not modify Anki templates. It documents the prompt contract, keeps the `FrenchCards` field order canonical, and provides small Python tools for prompt generation and TSV validation.

## FrenchCards

`FrenchCards` is an Anki note type for active French production. The central rule is:

> one note = one exact verb form + one main production sentence

The note type has 32 fields, stored canonically in [specs/frenchcards_fields.json](specs/frenchcards_fields.json). All prompts and validation tools use that file as the source of truth.

## Card Types

`FrenchCards` has exactly 3 card types:

- **Core Production**: the main card, always present, driven by `CorePromptEN -> CoreAnswerFR`.
- **Idiom Production**: optional, used only when the row contains a genuine high-value idiom or chunk.
- **Form Repair**: optional, used only when a form is irregular, easy to confuse, or worth isolating.

Each card should use Anki's built-in typed-answer syntax so the learner has to type the French answer before seeing it. This does not require extra note fields. Use:

- `{{type:CoreAnswerFR}}` on Core Production
- `{{type:IdiomAnswerFR}}` on Idiom Production
- `{{type:FormAnswerFR}}` on Form Repair

Template snippets are documented in [specs/anki_template_snippets.md](specs/anki_template_snippets.md).

## Workflow

1. Choose a French verb.
2. Run `scripts/generate_prompt.py`.
3. Paste the generated prompt into Codex or ChatGPT.
4. Receive raw TSV only.
5. Validate the returned TSV with `scripts/validate_tsv.py`.
6. Optionally generate a separate review prompt and ask a model to audit conjugation, IPA, naturalness, register, and pedagogy.
7. Import the TSV into Anki using the existing `FrenchCards` note type.

## Generate A Prompt

Print a prompt to stdout:

```bash
python scripts/generate_prompt.py --verb avoir
```

The generated prompt is copied to your clipboard automatically. Use `--quiet` when you only want the clipboard copy:

```bash
python scripts/generate_prompt.py --verb avoir --quiet
```

Use `--no-clipboard` if you only want terminal/file output.

Save a prompt to a file:

```bash
python scripts/generate_prompt.py --verb avoir --output examples/avoir_prompt.md
```

Useful options:

```bash
python scripts/generate_prompt.py \
  --verb être \
  --meaning "to be" \
  --scope full \
  --include-idioms auto \
  --include-form-repair auto \
  --subjects split
```

Scopes:

- `full`: all supported spoken, written, and literary production forms.
- `modern`: spoken and standard written high-value forms.
- `literary`: literary-heavy scope emphasizing literary forms as active-production targets.

Subject behavior defaults to `split`, creating separate notes for `je`, `tu`, `il`, `elle`, `on`, `nous`, `vous`, `ils`, and `elles` where applicable.

Merged mode is available when wanted, but should be used cautiously. Merged finite rows use slash-separated labels such as `il/elle/on` only when the surface form and production behavior are genuinely identical.

## Validate Returned TSV

```bash
python scripts/validate_tsv.py --input examples/avoir_tsv_example.tsv
```

The validator checks that the file is non-empty, has no header row, and that every row has exactly the canonical number of fields for `FrenchCards`. It also checks required fields, enum fields, `AudioFR`, imperative and non-finite policies, known mood/tense combinations, and whether optional idiom and form repair field groups are partially filled.

You can enforce scope membership:

```bash
python scripts/validate_tsv.py --input returned.tsv --scope full
```

For a complete generated verb file, you can also check target coverage:

```bash
python scripts/validate_tsv.py --input returned.tsv --scope full --subjects split --check-coverage
```

## Review Returned TSV

Use a second model pass for content quality that cannot be fully verified by deterministic code, especially conjugation accuracy, IPA quality, and pedagogy:

```bash
python scripts/generate_review_prompt.py --verb avoir --scope full --subjects split --input-tsv returned.tsv --output review_prompt.md
```

The review prompt is also copied to your clipboard automatically. Paste it into Codex or ChatGPT. The review prompt asks for a concise audit report, not rewritten TSV.

## Specifications

- [specs/frenchcards_fields.json](specs/frenchcards_fields.json): canonical field order and field metadata.
- [specs/frenchcards_card_types.md](specs/frenchcards_card_types.md): card type behavior.
- [specs/anki_template_snippets.md](specs/anki_template_snippets.md): typed-answer template snippets for the actual Anki note type.
- [specs/conjugation_scope.md](specs/conjugation_scope.md): scope, subject, and non-finite policies.
- [specs/conjugation_targets.json](specs/conjugation_targets.json): machine-readable target mood, tense, subject, and scope policy.
- [specs/pronunciation_policy.md](specs/pronunciation_policy.md): broad Parisian IPA and short pronunciation-note standards.
- [specs/pedagogy_rubric.md](specs/pedagogy_rubric.md): active-production quality rubric.
- [specs/generation_rules.md](specs/generation_rules.md): production, IPA, TSV, optional-field, and audit rules.
