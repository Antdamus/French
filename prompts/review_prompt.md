# Review Prompt for FrenchCards: {{VERB}}

You are reviewing TSV generated for my existing Anki note type `{{NOTE_TYPE}}`.

Target verb: `{{VERB}}`
Scope: `{{SCOPE_LABEL}}`
Subject policy: `{{SUBJECT_POLICY}}`

Your job is to audit the TSV for structure, construction accuracy, valency metadata, conjugation accuracy, broad Parisian IPA quality, liaison/pronunciation notes, naturalness, register, and pedagogy. Do not rewrite the whole TSV unless explicitly asked. Find problems precisely.

## Canonical Field Order

{{FIELD_ORDER}}

## Field Summary

{{FIELD_SUMMARY}}

## Canonical Conjugation Targets

{{CONJUGATION_TARGETS}}

## Pronunciation Policy

{{PRONUNCIATION_POLICY}}

## Pedagogy Rubric

{{PEDAGOGY_RUBRIC}}

## Review Checklist

Check:

1. Structure
- no header row
- every row has exactly the canonical number of fields
- field order matches `FrenchCards`
- required fields are not blank
- optional blanks are represented by empty cells
- no tabs or line breaks inside cell content

2. Construction And Valency
- every row stays inside the target construction
- `ConstructionFR`, `ConstructionMeaningEN`, `SemanticFrame`, and `ValencyClass` are accurate
- `ArgumentStructure`, `ArgumentSlots`, and `ComplementTypes` correctly describe the construction's inputs
- `PrepositionBehavior` is accurate for à/de/zero-preposition behavior
- `PronounBehavior` correctly distinguishes le/la/les, lui/leur, y, en, tonic pronouns, and reflexive pronouns
- `CliticOrderNote`, `ConstructionConstraints`, and `ConstructionContrastNote` are filled when useful and not noisy
- the construction metadata matches the actual French answer

3. Conjugation
- `CoreAnswerFR` contains the exact target form for `Verb`, `Mood`, `Tense`, `Person`, and `SubjectFR`
- imperative rows use only `tu`, `nous`, and `vous`
- non-finite rows use `Person = N/A` and `SubjectFR = —`
- subject labels match the French answer, including `j’` before vowels or mute h
- merged subject rows, when allowed, use slash-separated labels and do not hide important production differences
- literary forms are correct and labeled accurately

4. IPA And Pronunciation
- IPA is broad modern Parisian / standard metropolitan French
- IPA covers the full answer, not only the target form
- liaison, elision, enchaînement, nasal vowels, semivowels, h aspiré, /y/, and silent final consonants are handled correctly where relevant
- pronunciation notes are short and practical
- liaison rules are explicitly noted when they are production-sensitive

5. Naturalness And Pedagogy
- English prompts are natural and varied
- English prompts cue the correct tense, mood, and construction
- French answers are concise, idiomatic, and useful
- rows avoid awkward literal translation
- construction-production fields are genuinely high-value
- optional form repair fields are justified
- usage notes are accurate and not noisy

## Output Format

Return a concise audit report in Markdown with these sections:

- `Blocking Issues`
- `Quality Issues`
- `Suggested Fixes`
- `Overall Verdict`

If there are no issues in a section, write `None found.`

## TSV To Review

```tsv
{{TSV_CONTENT}}
```
