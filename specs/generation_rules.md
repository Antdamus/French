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

## Tense-Aligned Production Prompts

The English production prompt must express the meaning of the target French tense, not merely name the grammatical label.

Good prompts make the tense obvious in English:

- présent: `Say: he has a serious question.`
- imparfait: `Say: he used to have a quiet office.`
- passé composé: `Say: he had a clear answer yesterday.`
- plus-que-parfait: `Say: he had already had a warning.`
- futur simple: `Say: he will have a new role tomorrow.`
- futur antérieur: `Say: he will have had enough time by Friday.`
- conditionnel présent: `Say: he would have a better chance.`
- conditionnel passé: `Say: he would have had a better chance.`
- subjonctif présent: `Say: it is necessary that he have a valid reason.`
- subjonctif passé: `Say: I am glad that he had the courage to answer.`

The mood and tense label may appear as a short hint, but the English sentence itself must already cue the correct time, aspect, and mood. Avoid prompts such as `Say the il form of avoir in imparfait, in context` because they do not build active production.

For typed-answer cards, the English prompt should be specific enough that one French answer is clearly expected. If a prompt allows many natural answers, make it more specific.

## Didactic Variety

Do not overuse the same nouns, adjectives, or `avoir` chunks across a generated file. High-frequency chunks such as `avoir faim`, `avoir besoin de`, `avoir raison`, `avoir peur`, and `avoir envie de` are valuable, but they should be distributed intentionally rather than repeated mechanically.

Across a full verb file, vary:

- concrete and abstract nouns
- adjectives and short modifiers
- affirmative and negative sentences
- direct statements and questions
- time expressions
- causes, contrasts, and conditions
- spoken, formal, and literary contexts where appropriate

Variation must remain didactic: every sentence should still clearly train the exact target form.

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
