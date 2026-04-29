# Review Prompt for FrenchCards: {{VERB}}

You are reviewing TSV generated for my existing Anki note type `{{NOTE_TYPE}}`.

Target verb: `{{VERB}}`
Scope: `{{SCOPE_LABEL}}`
Subject policy: `{{SUBJECT_POLICY}}`

Your job is to audit the TSV for structure, conjugation accuracy, broad Parisian IPA quality, naturalness, register, and pedagogy. Do not rewrite the whole TSV unless explicitly asked. Find problems precisely.

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
- every row has exactly 32 fields
- field order matches `FrenchCards`
- required fields are not blank
- optional blanks are represented by empty cells
- no tabs or line breaks inside cell content

2. Conjugation
- `CoreAnswerFR` contains the exact target form for `Verb`, `Mood`, `Tense`, `Person`, and `SubjectFR`
- imperative rows use only `tu`, `nous`, and `vous`
- non-finite rows use `Person = N/A` and `SubjectFR = —`
- subject labels match the French answer, including `j’` before vowels or mute h
- merged subject rows, when allowed, use slash-separated labels and do not hide important production differences
- literary forms are correct and labeled accurately

3. IPA
- IPA is broad modern Parisian / standard metropolitan French
- IPA covers the full answer, not only the target form
- liaison, elision, nasal vowels, semivowels, and silent final consonants are handled correctly where relevant
- pronunciation notes are short and practical

4. Naturalness And Pedagogy
- English prompts are natural and varied
- French answers are concise, idiomatic, and useful
- rows avoid awkward literal translation
- optional idiom fields are genuinely high-value
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
