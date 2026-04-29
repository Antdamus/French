# Prompt for FrenchCards: avoir

Generate Anki-ready TSV content for my existing Anki note type `FrenchCards`.

Target verb: `avoir`
Provided English meaning: not supplied; infer the compact core meaning.
Scope: `full`
Subject policy: `split. Generate separate finite non-imperative notes for je, tu, il, elle, on, nous, vous, ils, and elles. Use j’ before a vowel or mute h where appropriate.`
Idiom policy: `auto. Fill idiom fields only for genuine high-value idioms or chunks.`
Form repair policy: `auto. Fill form repair fields only when the form is irregular, confusable, or worth isolating.`

This is an active-production deck, not a recognition deck. Generate one note per exact target form, with one main production sentence per note.

## Canonical Field Order

1. Verb
2. VerbIPA
3. Meaning
4. Regularity
5. VerbGroup
6. PatternRule
7. StemChangeNote
8. IrregularityNote
9. Auxiliary
10. PastParticiple
11. AgreementNote
12. Register
13. FrequencyTier
14. Mood
15. Tense
16. Person
17. SubjectFR
18. CorePromptEN
19. CoreAnswerFR
20. CoreAnswerIPA
21. CorePronunciationNote
22. AlternateAcceptedAnswers
23. IdiomPromptEN
24. IdiomAnswerFR
25. IdiomAnswerIPA
26. IdiomPronunciationNote
27. FormPrompt
28. FormAnswerFR
29. FormAnswerIPA
30. FormPronunciationNote
31. UsageNote
32. AudioFR

## Field Summary

- `Verb` (required): Infinitive of the target French verb.
- `VerbIPA` (required): Broad modern Parisian / standard metropolitan French IPA for the infinitive.
- `Meaning` (required): Compact core English meaning.
- `Regularity` (required): One of: regular / irregular / semi-irregular.
- `VerbGroup` (required): One of: -er / -ir / -re / irregular family / other.
- `PatternRule` (required): Concise conjugation rule or pattern.
- `StemChangeNote` (optional): Concise stem alternation note if relevant.
- `IrregularityNote` (optional): Concise warning for unusual forms if relevant.
- `Auxiliary` (required): One of: avoir / être / both / N/A.
- `PastParticiple` (required): Past participle of the verb.
- `AgreementNote` (optional): Participle agreement or other important agreement note.
- `Register` (required): One of: spoken / standard written / literary / formal / mixed.
- `FrequencyTier` (required): One of: high / medium / literary.
- `Mood` (required): Grammatical mood.
- `Tense` (required): Grammatical tense or non-finite form name.
- `Person` (required): Grammatical person label, or N/A for non-finite forms.
- `SubjectFR` (required): Exact surface French subject, such as je, j’, tu, il, elle, on, nous, vous, ils, elles, or —.
- `CorePromptEN` (required): Main natural English production prompt.
- `CoreAnswerFR` (required): Main French answer as a natural sentence or phrase that realizes the exact target form.
- `CoreAnswerIPA` (required): Broad Parisian IPA for the entire CoreAnswerFR.
- `CorePronunciationNote` (optional): Short practical pronunciation note.
- `AlternateAcceptedAnswers` (optional): Optional semicolon-separated alternate accepted answers; empty if none.
- `IdiomPromptEN` (optional): Optional English prompt for a genuine high-value idiom or chunk.
- `IdiomAnswerFR` (optional): Optional French answer for the idiom production card.
- `IdiomAnswerIPA` (optional): Optional broad Parisian IPA for IdiomAnswerFR.
- `IdiomPronunciationNote` (optional): Optional short practical pronunciation note for the idiom answer.
- `FormPrompt` (optional): Optional repair prompt for an irregular, confusable, or otherwise high-value isolated form.
- `FormAnswerFR` (optional): Optional isolated French form answer.
- `FormAnswerIPA` (optional): Optional broad Parisian IPA for FormAnswerFR.
- `FormPronunciationNote` (optional): Optional short practical pronunciation note for the isolated form.
- `UsageNote` (optional): Short note about use, nuance, style, or literary status.
- `AudioFR` (optional): Audio field; leave blank for now.

## Card Type Rules

# FrenchCards Card Types

The Anki note type `FrenchCards` has exactly 3 card types. This repository documents how prompts should fill the note fields that drive those cards. It does not modify the Anki templates directly.

## 1. Core Production

Core Production is the main card and should always be meaningful.

- Prompt side: `CorePromptEN`
- Answer side: `CoreAnswerFR`
- Supporting fields: `CoreAnswerIPA`, `CorePronunciationNote`, `AlternateAcceptedAnswers`, `UsageNote`

Every note must include one exact target verb form in `CoreAnswerFR`. The English prompt should be natural, varied, and designed for active production rather than recognition.

## 2. Idiom Production

Idiom Production is optional. Fill idiom fields only when the verb form naturally supports a genuinely high-value idiom, expression, or reusable chunk.

- Prompt side: `IdiomPromptEN`
- Answer side: `IdiomAnswerFR`
- Supporting fields: `IdiomAnswerIPA`, `IdiomPronunciationNote`

Leave all idiom fields blank when there is no strong idiom or chunk. Do not invent weak idioms just to fill the card.

## 3. Form Repair

Form Repair is optional. Fill form repair fields only when the target form is irregular, easy to confuse, unusually spelled, pronunciation-sensitive, or otherwise worth isolating.

- Prompt side: `FormPrompt`
- Answer side: `FormAnswerFR`
- Supporting fields: `FormAnswerIPA`, `FormPronunciationNote`

Example:

- `FormPrompt`: `avoir — présent — nous`
- `FormAnswerFR`: `nous avons`

Leave all form repair fields blank when the form does not need isolated repair practice.

## Conjugation Scope

# Conjugation Scope

The deck is for active production. If a form is included, it is included so the learner can actively produce it, not merely recognize it.

## Scope Labels

### full

The full default scope includes all supported spoken, educated written, and literary production forms:

Indicatif:

- présent
- imparfait
- passé composé
- plus-que-parfait
- passé simple
- passé antérieur
- futur simple
- futur antérieur

Conditionnel:

- présent
- passé

Subjonctif:

- présent
- passé
- imparfait
- plus-que-parfait

Impératif:

- présent
- passé

Infinitif:

- présent
- passé

Participe:

- présent
- passé

Gérondif:

- présent
- passé

### modern

Modern scope targets spoken French and standard written high-value forms. It should emphasize forms that are useful in conversation, contemporary media, school/professional writing, and ordinary educated prose.

Modern scope should normally include:

- indicatif présent, imparfait, passé composé, plus-que-parfait, futur simple, futur antérieur
- conditionnel présent and passé
- subjonctif présent and passé
- impératif présent
- infinitif présent and passé
- participe présent and passé
- gérondif présent

It should usually exclude or sharply limit literary-only forms such as passé simple, passé antérieur, subjonctif imparfait, subjonctif plus-que-parfait, impératif passé, and gérondif passé unless the verb or requested use case strongly justifies them.

### literary

Literary scope is literary-heavy. It still treats forms as active-production targets, but emphasizes forms needed to read and actively produce educated or literary prose, including forms useful for authors in the range of Camus and Sartre.

Literary scope should include the modern high-value forms plus literary forms such as:

- passé simple
- passé antérieur
- subjonctif imparfait
- subjonctif plus-que-parfait
- other marked written or literary forms from the full scope when useful

## Subject Policy

Default behavior is split subjects.

For finite non-imperative forms, generate separate target rows for:

- `je`
- `tu`
- `il`
- `elle`
- `on`
- `nous`
- `vous`
- `ils`
- `elles`

Use `j’` before a vowel or mute h where appropriate.

## Merged-Subject Option

The prompt generator supports `--subjects merged`. In merged mode, the downstream model may combine forms only when the surface verb form and production behavior are genuinely identical and pedagogically safe to merge.

Merged mode must not hide important agreement, liaison, spelling, subject, register, or pronunciation differences. When unsure, split the subjects.

When subjects are merged, use slash-separated subject labels in `Person` and `SubjectFR`, such as `il/elle/on` or `ils/elles`. Do not merge subjects with different surface forms or important pronunciation behavior.

## Imperative

Imperative rows use only:

- `tu`
- `nous`
- `vous`

## Non-Finite Forms

For infinitive, participle, and gerund rows:

- `Person` = `N/A`
- `SubjectFR` = `—`

Non-finite rows should still contain production prompts and natural French answers or phrases that practice the target form actively.

## Canonical Conjugation Targets

Finite subjects: je, tu, il, elle, on, nous, vous, ils, elles
Imperative subjects: tu, nous, vous
Non-finite forms: Person = N/A; SubjectFR = —

Generate these target categories for `full` scope:
- indicatif — présent (finite)
- indicatif — imparfait (finite)
- indicatif — passé composé (finite)
- indicatif — plus-que-parfait (finite)
- indicatif — passé simple (finite)
- indicatif — passé antérieur (finite)
- indicatif — futur simple (finite)
- indicatif — futur antérieur (finite)
- conditionnel — présent (finite)
- conditionnel — passé (finite)
- subjonctif — présent (finite)
- subjonctif — passé (finite)
- subjonctif — imparfait (finite)
- subjonctif — plus-que-parfait (finite)
- impératif — présent (imperative)
- impératif — passé (imperative)
- infinitif — présent (non_finite)
- infinitif — passé (non_finite)
- participe — présent (non_finite)
- participe — passé (non_finite)
- gérondif — présent (non_finite)
- gérondif — passé (non_finite)

## Pronunciation Policy

# Pronunciation Policy

Use broad modern Parisian / standard metropolitan French IPA. The goal is production support, not ultra-narrow phonetic transcription.

## IPA Style

- Transcribe the whole French answer, not just the verb form.
- Prefer broad phonemic/practical IPA over narrow details.
- Preserve useful distinctions such as nasal vowels, /y/ vs /u/, /ø/ vs /œ/ when relevant, and semivowels such as /j/, /ɥ/, and /w/.
- Do not overload rows with optional variation unless the variation affects production.
- Keep the IPA plausible for careful standard metropolitan speech.

## Pronunciation Notes

Pronunciation notes should be short, practical, and production-oriented. Most notes should be one sentence fragment.

Focus on:

- liaison
- elision
- nasal vowels
- silent final consonants
- semivowels
- important standard metropolitan pronunciation points

Avoid:

- long phonetics essays
- dialect surveys
- ultra-narrow allophones
- repeating obvious information in every row

## Good Note Style

- `Elide je before ai.`
- `Liaison in nous avons.`
- `Final t is silent before a consonant.`
- `Watch the nasal vowel /ɔ̃/.`

## Bad Note Style

- Long explanations of French phonology.
- Notes that merely repeat the IPA.
- Notes unrelated to producing the answer aloud.

## Pedagogy Rubric

# Pedagogy Rubric

FrenchCards is an active-production system. A strong row helps the learner produce one exact form in a natural context.

## High-Value Rows

A good row:

- targets one exact verb form
- uses a natural English production prompt
- gives a concise, idiomatic French answer
- avoids translationese
- uses a prompt that differs meaningfully from nearby rows
- labels register accurately
- uses `UsageNote` only when it adds real value
- leaves optional fields blank when they are not justified

## Prompt Variation

Avoid repeating the same frame across many rows. The learner should not be able to answer from mechanical pattern alone.

Use varied situations such as:

- personal plans
- obligations
- memory and narration
- doubt and desire
- cause and consequence
- formal written prose
- literary narration

Variation should serve production. Do not make prompts strange just to be different.

## Literary Forms

Literary forms are active-production targets when included. Label them clearly and use contexts where they naturally belong, especially narration, formal prose, or literary style.

Do not mix literary forms into casual spoken prompts unless the contrast is intentional and explained in `UsageNote`.

## Idiom Discipline

Fill idiom fields only for genuine high-value idioms, expressions, or reusable chunks. A weak phrase is worse than a blank optional card.

## Form Repair Discipline

Fill form repair fields only when the isolated form deserves extra attention because it is irregular, confusable, pronunciation-sensitive, or especially common.

## Review Standard

When reviewing TSV, prefer fewer excellent cards over many mediocre cards. Flag rows that are structurally valid but pedagogically weak.

## Generation Rules

# Generation Rules

## Active Production First

The deck is for active production, not passive recognition. Every included form should be worth producing.

Each note represents:

- one exact verb form
- one main production sentence or phrase

The `CoreAnswerFR` must realize the target form exactly.

## Sentence Quality

English prompts must be natural and varied. Avoid recycling the same sentence pattern across many forms.

Whenever possible, each note should use a distinct prompt. Avoid near-duplicate prompts unless repetition is pedagogically useful for contrast.

French answers should be natural, concise, and high-value. Avoid awkward literal translations when better French exists.

## Register And Usage

Use register labels carefully:

- `spoken`
- `standard written`
- `literary`
- `formal`
- `mixed`

Use `UsageNote` for short notes about nuance, style, literary status, or common restrictions. Literary forms are still active-production targets when included.

## IPA And Pronunciation

Use broad modern Parisian / standard metropolitan French IPA. Do not use ultra-narrow phonetics.

Follow the detailed policy in `specs/pronunciation_policy.md`.

Pronunciation notes must be short, practical, and production-oriented. Focus on:

- liaison
- elision
- nasal vowels
- silent final consonants
- semivowels
- important standard metropolitan pronunciation points

Do not write long phonetics essays.

## Optional Fields

Fill idiom fields only when there is a genuine high-value idiom, expression, or reusable chunk:

- `IdiomPromptEN`
- `IdiomAnswerFR`
- `IdiomAnswerIPA`
- `IdiomPronunciationNote`

Fill form repair fields only when the form is irregular, easy to confuse, or worth isolating:

- `FormPrompt`
- `FormAnswerFR`
- `FormAnswerIPA`
- `FormPronunciationNote`

Unused optional fields must be empty strings, but their columns must remain present in TSV.

`AudioFR` must be left blank for now.

## Pedagogy

Follow the active-production rubric in `specs/pedagogy_rubric.md`. Prefer rows that are natural, useful, and easy to audit over rows that are merely exhaustive.

## TSV Output Rules

The downstream model must output:

- raw TSV only
- valid UTF-8 only
- no markdown code fences
- no explanation
- no commentary
- no numbering
- no header row
- no column titles
- exactly one note per line
- exactly 32 tab-separated fields per line
- fields in the exact `FrenchCards` order
- empty cells for unused optional fields
- every field on a single line
- no literal tab characters inside field content
- no literal line breaks inside field content
- internal line breaks normalized to spaces
- UTF-8 characters preserved exactly, including French accents, curly apostrophes, em dashes, and IPA symbols such as ʁ, ɛ, ɔ̃, œ, ø, ɥ, ʒ, and ‿
- no replacement question marks for unsupported Unicode; if UTF-8 cannot be preserved, stop instead of emitting damaged TSV

## Malformed TSV Failure Rules

The response is wrong if:

- there is any prose before or after the TSV
- there is a header row
- any row has fewer than 32 fields
- any row has more than 32 fields
- the column order differs from the specified order
- optional blanks are omitted instead of represented as empty cells
- any cell contains literal tabs or line breaks
- any accent, apostrophe, em dash, or IPA symbol has been replaced by `?` or mojibake

## Silent Audit Policy

Before producing the final TSV, the downstream model must privately perform this audit and then output only the final TSV.

### 1. Structure Audit

- every row has exactly 32 fields
- field order exactly matches `FrenchCards`
- no header row
- no missing cells caused by forgotten tabs
- optional blanks are represented by empty cells, not omitted columns
- no tabs or line breaks inside cell content

### 2. Conjugation Audit

- the French answer actually contains the target form for that verb, mood, tense, and person
- the person and `SubjectFR` are correct
- imperative rows only use `tu`, `nous`, and `vous`
- non-finite rows use `Person = N/A` and `SubjectFR = —`

### 3. Naturalness Audit

- English prompts are natural and varied
- French answers are natural, concise, and high-value for learning
- awkward literal translations are avoided when better French exists
- near-duplicate prompts are avoided whenever reasonably possible

### 4. Pronunciation Audit

- IPA is broad modern Parisian / standard metropolitan
- pronunciation notes are short and practical
- no overlong phonetics essays

### 5. Optional-Field Audit

- idiom fields are only filled when there is a genuine idiom or high-value chunk
- form repair fields are only filled when justified
- unused optional fields are left blank

### 6. Literary-Scope Audit

- literary forms are treated as active-production targets too
- literary labels and usage notes are accurate and not mixed carelessly with spoken-only labels

### 7. Final TSV Audit

- output contains only TSV rows
- no prose before or after
- no code fences
- no extra blank lines at start or end
- no replacement question marks or mojibake in French, IPA, tense labels, or form prompts

## Silent Self-Audit Required

Perform a private self-audit before producing the final TSV. Do not show the audit.

1. STRUCTURE AUDIT
- every row has exactly 32 fields
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
- no replacement question marks or mojibake in French, IPA, tense labels, or form prompts

## Output Instructions

Return RAW TSV ONLY.

Do not output Markdown code fences, explanations, commentary, numbering, a header row, or column titles.

Encoding requirement: output must be valid UTF-8. Preserve all Unicode characters exactly, including French accents, curly apostrophes, em dashes, and IPA symbols such as ʁ, ɛ, ɔ̃, œ, ø, ɥ, ʒ, and ‿. Do not replace unsupported characters with question marks or mojibake. If UTF-8 cannot be preserved, stop instead of emitting damaged TSV.

Output exactly one note per line. Each line must contain exactly 32 tab-separated fields in the exact `FrenchCards` field order. Optional unused fields must be empty cells, but their columns must still be preserved.

Every field must stay on a single line. Do not put literal tab characters or literal line breaks inside field content. Normalize internal line breaks to spaces. Preserve UTF-8 characters such as accents and IPA symbols.

Malformed TSV is a failure. The response is wrong if:
- there is any prose before or after the TSV
- there is a header row
- any row has fewer than 32 fields
- any row has more than 32 fields
- the column order differs from the specified order
- any accent, apostrophe, em dash, or IPA symbol has been replaced by `?` or mojibake
