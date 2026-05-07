# FrenchCards Prompt Toolkit

This repository helps generate strict, Anki-ready TSV prompts for the existing Anki note type `FrenchCards`.

The repository does not modify Anki directly. It documents the prompt contract, keeps the `FrenchCards` field order canonical, and provides small Python tools for prompt generation and TSV validation.

## FrenchCards

`FrenchCards` is an active French production note type. The central rule is:

> one note = one exact verb construction + one exact target form + one main typed production sentence

The note type has 46 fields, stored canonically in [specs/frenchcards_fields.json](specs/frenchcards_fields.json). All prompts and validation tools use that file as the source of truth.

The deck is construction-aware. It does not treat a French verb as a flat dictionary entry. It treats the learning unit as:

```text
verb + construction + valency + semantic frame
```

Examples:

- `avoir quelque chose`
- `avoir besoin de quelque chose`
- `penser à quelque chose`
- `penser à quelqu’un`
- `donner quelque chose à quelqu’un`
- `s’en aller`

Each of these can have different meaning, argument slots, complement types, preposition behavior, and pronoun behavior.

## Card Types

`FrenchCards` has exactly 3 card types:

- **Core Production**: the main typed card, driven by `CorePromptEN -> CoreAnswerFR`.
- **Construction Production**: optional typed card for valency, pronoun, preposition, reflexive, clitic, or reusable construction behavior.
- **Form Repair**: optional typed card for irregular, confusable, or pronunciation-sensitive isolated forms.

Each card should use Anki's built-in typed-answer syntax:

- `{{type:CoreAnswerFR}}` on Core Production
- `{{type:ConstructionAnswerFR}}` on Construction Production
- `{{type:FormAnswerFR}}` on Form Repair

Template notes are documented in [specs/anki_template_snippets.md](specs/anki_template_snippets.md).

## Workflow

1. Choose a French verb.
2. Choose one construction or valency frame for that verb.
3. Run `scripts/generate_prompt.py`.
4. Paste the generated prompt into Codex or ChatGPT.
5. Receive raw TSV only.
6. Validate the returned TSV with `scripts/validate_tsv.py`.
7. Optionally generate a separate review prompt and ask a model to audit construction accuracy, conjugation, IPA, naturalness, register, and pedagogy.
8. Import the TSV into Anki using the existing `FrenchCards` note type.

## Generate A Prompt

Minimal prompt:

```bash
python scripts/generate_prompt.py --verb avoir
```

Construction-aware prompt:

```bash
python scripts/generate_prompt.py \
  --verb avoir \
  --meaning "to have" \
  --construction-id avoir_besoin_de_qqch \
  --construction-fr "avoir besoin de quelque chose" \
  --construction-meaning "to need something" \
  --semantic-frame "need/requirement" \
  --valency-class "de-complement" \
  --argument-structure "subject experiencer + avoir besoin de + needed thing/action" \
  --argument-slots "subject; de-complement" \
  --complement-types "de + noun; de + infinitive; thing/idea/action" \
  --preposition-behavior "requires de before the needed complement" \
  --pronoun-behavior "de + thing/idea/action -> en" \
  --construction-contrast-note "avoir quelque chose uses direct object pronouns le/la/les; avoir besoin de uses en" \
  --allowed-forms "ordinary finite forms; infinitive; participles; gerund; imperative only when semantically natural" \
  --scope full \
  --subjects split
```

The generated prompt is copied to your clipboard automatically. Use `--quiet` when you only want the clipboard copy, or `--no-clipboard` if you only want terminal/file output.

Save a prompt to a file:

```bash
python scripts/generate_prompt.py --verb avoir --construction-fr "avoir besoin de quelque chose" --output examples/avoir_besoin_prompt.md
```

## Validate Returned TSV

```bash
python scripts/validate_tsv.py --input returned.tsv
```

You can enforce scope membership:

```bash
python scripts/validate_tsv.py --input returned.tsv --scope full
```

For a complete generated construction file, you can also check target coverage:

```bash
python scripts/validate_tsv.py --input returned.tsv --scope full --subjects split --check-coverage
```

The validator checks field count, required fields, enum fields, `AudioFR`, imperative and non-finite policies, known mood/tense combinations, optional construction-production groups, optional form-repair groups, and target coverage when requested.

## Review Returned TSV

Use a second model pass for content quality that cannot be fully verified by deterministic code, especially construction accuracy, pronoun behavior, conjugation accuracy, IPA quality, and pedagogy:

```bash
python scripts/generate_review_prompt.py --verb avoir --scope full --subjects split --input-tsv returned.tsv --output review_prompt.md
```

The review prompt is also copied to your clipboard automatically. Paste it into Codex or ChatGPT. The review prompt asks for a concise audit report, not rewritten TSV.

## Specifications

- [specs/frenchcards_fields.json](specs/frenchcards_fields.json): canonical field order and field metadata.
- [specs/frenchcards_card_types.md](specs/frenchcards_card_types.md): card type behavior.
- [specs/anki_template_snippets.md](specs/anki_template_snippets.md): typed-answer template notes for the actual Anki note type.
- [specs/conjugation_scope.md](specs/conjugation_scope.md): scope, subject, and non-finite policies.
- [specs/conjugation_targets.json](specs/conjugation_targets.json): machine-readable target mood, tense, subject, and scope policy.
- [specs/pronunciation_policy.md](specs/pronunciation_policy.md): broad Parisian IPA, liaison, elision, and pronunciation-note standards.
- [specs/pedagogy_rubric.md](specs/pedagogy_rubric.md): active-production and construction-quality rubric.
- [specs/generation_rules.md](specs/generation_rules.md): construction, production, IPA, TSV, optional-field, and audit rules.
