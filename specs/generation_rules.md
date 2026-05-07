# Generation Rules

## Active Production First

The deck is for active production, not passive recognition. Every included form should be worth producing.

Each note represents:

- one exact verb construction or valency frame
- one exact verb form inside that construction
- one main production sentence or phrase

The `CoreAnswerFR` must realize the target form exactly and must use the target construction exactly. The target is not merely `verb -> translation`; it is `verb + construction + valency + semantic frame`.

## Construction Scope

Generate one verb construction at a time. Do not mix unrelated valency frames in the same TSV unless the user explicitly requests a comparison set.

Examples of separate construction targets:

- `avoir quelque chose` = to have/possess something
- `avoir besoin de quelque chose` = to need something
- `avoir envie de + infinitive` = to feel like doing something
- `penser à quelque chose` = to think about something; thing/idea can become `y`
- `penser à quelqu’un` = to think about someone; normally `penser à lui/à elle`, not `lui penser`
- `donner quelque chose à quelqu’un` = to give something to someone; direct object plus indirect object pronouns are possible
- `s’en aller` = to leave/go away as a lexicalized pronominal construction

Fill the construction metadata fields for every row:

- `ConstructionID`
- `ConstructionFR`
- `ConstructionMeaningEN`
- `SemanticFrame`
- `ValencyClass`
- `ArgumentStructure`
- `ArgumentSlots`
- `ComplementTypes`
- `AllowedForms`

Fill preposition, pronoun, clitic, constraint, and contrast fields when they are relevant. These fields are not decoration; they are the learner's map of the construction's input slots and syntactic behavior.

## Sentence Quality

English prompts must be natural and varied. Avoid recycling the same sentence pattern across many forms.

Whenever possible, each note should use a distinct prompt. Avoid near-duplicate prompts unless repetition is pedagogically useful for contrast.

French answers should be natural, concise, and high-value. Avoid awkward literal translations when better French exists.

For typed-answer cards, the English prompt should be specific enough that one French answer is clearly expected. If a prompt allows many natural answers, make it more specific.

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

The English prompt must also cue the construction. For example, if the target is `avoir besoin de quelque chose`, prompts should cue "need X", not merely "have X".

## Didactic Variety

Do not overuse the same nouns, adjectives, or chunks across a generated file. High-frequency chunks are valuable, but they should be distributed intentionally rather than repeated mechanically.

Across a full construction file, vary:

- concrete and abstract nouns
- adjectives and short modifiers
- affirmative and negative sentences
- direct statements and questions
- time expressions
- causes, contrasts, and conditions
- spoken, formal, and literary contexts where appropriate

Variation must remain didactic: every sentence should still clearly train the exact target form and construction.

## Register And Usage

Use register labels carefully:

- `spoken`
- `standard written`
- `literary`
- `formal`
- `mixed`

Use `UsageNote` for short notes about nuance, style, literary status, construction restrictions, or common traps. Literary forms are still active-production targets when included.

## IPA And Pronunciation

Use broad modern Parisian / standard metropolitan French IPA. Do not use ultra-narrow phonetics.

Follow the detailed policy in `specs/pronunciation_policy.md`.

Pronunciation notes must be short, practical, and production-oriented.

## Liaison, Elision, And Sound Rules

Pronunciation notes are required when the answer contains a production-sensitive sound rule. Use the appropriate field:

- `CorePronunciationNote` for `CoreAnswerFR`
- `ConstructionPronunciationNote` for `ConstructionAnswerFR`
- `FormPronunciationNote` for `FormAnswerFR`

Fill the note when relevant for:

- liaison, such as `nous avons`, `vous avez`, `ils ont`, `elles ont`
- liaison into compound forms, such as `nous avons eu`, `vous avez eu`, `ils ont eu`
- elision, such as `je` becoming `j’`
- enchaînement, where a final pronounced consonant links into the next word
- silent final consonants, especially in literary forms such as `eut`
- h aspiré blocking elision or liaison
- nasal vowels such as /ɔ̃/, /ɑ̃/, /ɛ̃/
- high-risk IPA contrasts such as /y/ in `eu`

Good pronunciation notes are short:

- `Elide je before ai.`
- `Liaison in nous avons.`
- `Liaison from avez into eu.`
- `Final t in eut is normally silent.`
- `Watch /y/ in eu.`
- `No liaison before h aspiré.`

## Optional Fields

Fill construction-production fields when there is a genuine high-value construction, pronoun, preposition, reflexive, clitic, or complement behavior worth isolating:

- `ConstructionPromptEN`
- `ConstructionAnswerFR`
- `ConstructionAnswerIPA`
- `ConstructionPronunciationNote`

Fill form repair fields only when the form is irregular, easy to confuse, pronunciation-sensitive, or worth isolating:

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
- exactly 46 tab-separated fields per line
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
- any row has fewer than 46 fields
- any row has more than 46 fields
- the column order differs from the specified order
- optional blanks are omitted instead of represented as empty cells
- any cell contains literal tabs or line breaks
- any accent, apostrophe, em dash, or IPA symbol has been replaced by `?` or mojibake

## Silent Audit Policy

Before producing the final TSV, the downstream model must privately perform this audit and then output only the final TSV.

### 1. Structure Audit

- every row has exactly 46 fields
- field order exactly matches `FrenchCards`
- no header row
- no missing cells caused by forgotten tabs
- optional blanks are represented by empty cells, not omitted columns
- no tabs or line breaks inside cell content

### 2. Construction And Conjugation Audit

- the French answer actually contains the target form for this verb, mood, tense, and person
- the French answer uses the target construction, not another construction of the same root verb
- the person and `SubjectFR` are correct
- imperative rows only use `tu`, `nous`, and `vous`
- non-finite rows use `Person = N/A` and `SubjectFR = —`
- construction metadata is consistent with the answer's syntax, complement behavior, and pronoun behavior

### 3. Naturalness Audit

- English prompts are natural and varied
- English prompts cue the correct tense, mood, and construction
- French answers are natural, concise, and high-value for learning
- awkward literal translations are avoided when better French exists
- near-duplicate prompts are avoided whenever reasonably possible

### 4. Pronunciation Audit

- IPA is broad modern Parisian / standard metropolitan
- pronunciation notes are short and practical
- liaison, elision, enchaînement, nasal vowels, silent final consonants, h aspiré behavior, and /y/ vs /u/ are noted when relevant
- no overlong phonetics essays

### 5. Optional-Field Audit

- construction-production fields are filled only when there is a genuine construction behavior or reusable chunk worth isolating
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
- no replacement question marks or mojibake in French, IPA, tense labels, construction fields, or form prompts
