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

## Construction Subpatterns

Some constructions are one valency family but allow several complement subpatterns. Keep these together when they share the same construction identity, but make the subpatterns explicit and train them deliberately.

For example, `avoir besoin de + complément` can cover:

- `de + thing/idea noun phrase`: `J’ai besoin de ce document.` -> `J’en ai besoin.`
- `de + infinitive/action`: `J’ai besoin de dormir.` -> `J’en ai besoin` when referring back to the action as a known idea.
- `de + person`: `J’ai besoin de Marie.` -> `J’ai besoin d’elle.`

Do not flatten these into the vague rule `de becomes en`. The correct behavior depends on complement type:

- thing/idea/action complements can normally be replaced by `en`
- infinitive complements keep `de + infinitive` in the full construction, with `en` available only when the action is being referred back to as an established idea
- specific people normally remain after `de` as stressed pronouns: `de moi`, `de toi`, `de lui`, `d’elle`, `de nous`, `de vous`, `d’eux`, `d’elles`

When a construction has subpatterns, rotate them through Core Production rows instead of generating separate full conjugation files by default.

Use `ComplementTypes`, `PronounBehavior`, `ConstructionConstraints`, and `ConstructionContrastNote` to explain the subpatterns. For `avoir besoin de`, make clear that neutral French does not say `J’en ai besoin de ce document`; use either `J’ai besoin de ce document` or `J’en ai besoin`.

## Sentence Quality

English prompts must be natural, varied, and grammatically correct. Do not produce cues like `he need`, `she need`, or `they was`.

The prompt must cue the construction and the target tense/mood through meaning, not only by naming the grammar label.

French answers should be natural, concise, and high-value. For typed-answer cards, the English prompt should be specific enough that one French answer is clearly expected.

## Tense-Aligned Production Prompts

The English production prompt must express the meaning of the target French tense, not merely name the grammatical label.

Good prompts make the tense obvious in English:

- présent: `Say: he needs a clear answer.`
- imparfait: `Say: he used to need a quiet office.`
- passé composé: `Say: he needed help yesterday.`
- plus-que-parfait: `Say: he had already needed help before the meeting.`
- futur simple: `Say: he will need a new document by Friday.`
- futur antérieur: `Say: he will have needed enough time by Friday.`
- conditionnel présent: `Say: he would need a better chance.`
- conditionnel passé: `Say: he would have needed a better chance.`
- subjonctif présent: `Say: it is possible that he needs a valid reason.`
- subjonctif passé: `Say: I am sorry that he needed help.`

## Didactic Variety

Do not overuse the same nouns, adjectives, chunks, time anchors, or sentence frames across a generated file.

Across a full construction file, vary:

- concrete and abstract nouns
- adjectives and short modifiers
- affirmative and negative sentences
- direct statements and questions
- time expressions
- causes, contrasts, and conditions
- spoken, formal, and literary contexts where appropriate

Avoid nine consecutive prompts ending in `today`, `tomorrow`, `every evening`, `soon`, or `if possible`. Variation must remain didactic: every sentence should still clearly train the exact target form and construction.

## Interaction Mix

A strong construction file should train the ways the construction is normally used, not only plain affirmative statements. Across the generated rows, include a controlled mix of:

- affirmative statements
- negative statements
- questions
- pronominalization or complement-replacement drills
- register contrasts when the construction has a common spoken form and a standard written form

Do not force every behavior into every tense. Use the behavior where it is natural, useful, and compatible with the target form.

## Negation

Include negative production rows regularly. Negation is part of the verb construction and must be trained, not treated as an afterthought.

For spoken or mixed-register rows, use natural conversational French by dropping `ne` when that is the expected everyday form:

- `J’ai pas besoin de ce document.`
- `Elle a pas besoin de dormir.`
- `Nous avons pas besoin de lui.`
- `J’en ai pas besoin.`

When `CoreAnswerFR` or `ConstructionAnswerFR` uses conversational dropped-`ne` negation, put the full standard/written version in `AlternateAcceptedAnswers` when it corresponds to the core answer:

- `Je n’ai pas besoin de ce document.`
- `Elle n’a pas besoin de dormir.`
- `Nous n’avons pas besoin de lui.`
- `Je n’en ai pas besoin.`

Also add a short `UsageNote` reminder when useful:

- `Spoken French often drops ne; standard written form: Je n’ai pas besoin de ce document.`

For formal, standard written, and literary rows, prefer full `ne ... pas` negation when a negative row is used. Do not use dropped `ne` in literary forms unless the prompt deliberately asks for spoken contrast.

Negation should rotate across complement subpatterns too:

- thing/idea: `J’ai pas besoin de ce document.`
- infinitive/action: `Elle a pas besoin de partir.`
- person: `Ils ont pas besoin de moi.`
- pronominalized thing/action: `J’en ai pas besoin.`
- standard reminder: `Je n’en ai pas besoin.`

## Questions

Include question production rows regularly. Questions are high-value because they change word order, intonation, punctuation, and sometimes register.

Use a mix of natural question strategies:

- conversational intonation: `Tu as besoin de ce document ?`
- neutral `est-ce que`: `Est-ce que tu as besoin de ce document ?`
- formal inversion when appropriate: `Avez-vous besoin de ce document ?`
- embedded/subjunctive question frames when the target tense naturally supports them: `Penses-tu qu?il ait besoin de ce document ?`

For spoken or mixed-register rows, conversational intonation and `est-ce que` are usually better production targets than inversion. For formal or standard written rows, inversion may be useful. For literary rows, questions should fit the style rather than sound like casual speech.

Question answers must include a French question mark. If a question row has a common alternate register form, put it in `AlternateAcceptedAnswers` or `UsageNote`.

## Register Contrast

Use register as a production dimension, especially when French offers a normal spoken form and a more standard written form.

Examples:

- spoken/mixed: `J?ai pas besoin de ce document.`
- standard written: `Je n?ai pas besoin de ce document.`
- spoken/mixed question: `Tu as besoin de ce document ?`
- standard written question: `Est-ce que tu as besoin de ce document ?`
- formal question: `Avez-vous besoin de ce document ?`

Do not over-label every row. Use `UsageNote` when the contrast changes what the learner should type or notice.

## Clitic Stacking

When a construction licenses multiple clitics, teach the clitic stack explicitly and carefully. The standard order is:

`me/te/se/nous/vous` + `le/la/les` + `lui/leur` + `y` + `en`

Examples:

- `Je le lui donne.`
- `Je leur en parle.`
- `Je m?en souviens.`
- `Je n?en ai pas besoin.`

Use `CliticOrderNote` to describe the relevant stack. Do not create artificial clitic stacks for constructions that do not naturally take them. For `avoir besoin de`, the high-value clitic is usually `en`; person complements normally remain as `de lui`, `d?elle`, `d?eux`, or `d?elles`.

## Tense Reference Fields

Fill these fields on every row:

- `TenseOverview`
- `TenseUseNote`
- `TenseParadigmFR`
- `TenseParadigmIPA`

`TenseOverview` should name the practical time/aspect/mood value of the current row, such as current state, background past, completed past, future completion, hypothetical, subjunctive dependency, literary narration, imperative command, infinitive, participle, or gerund.

`TenseUseNote` should give a short operational rule for production. For example:

- `Use the imparfait for background, habit, description, or ongoing past state.`
- `Use the passé composé for a completed past event viewed as finished.`
- `Use the futur antérieur for something completed before a future reference point.`

`TenseParadigmFR` should show the target verb conjugated across the relevant pronouns/forms for the current mood/tense. For finite tenses, include all split subjects: `j’/je`, `tu`, `il`, `elle`, `on`, `nous`, `vous`, `ils`, `elles`. For imperatives, include `tu`, `nous`, `vous`. For non-finite forms, show the relevant non-finite form and any closely related support form when helpful.

`TenseParadigmIPA` should give broad modern Parisian / standard metropolitan French IPA for the same paradigm, immediately matching the order of `TenseParadigmFR`.

## Register And Usage

Use register labels carefully: `spoken`, `standard written`, `literary`, `formal`, or `mixed`.

Use `UsageNote` for short notes about nuance, style, literary status, construction restrictions, or common traps.

## IPA And Pronunciation

Use broad modern Parisian / standard metropolitan French IPA. Do not use ultra-narrow phonetics.

Follow `specs/pronunciation_policy.md`. Pronunciation notes must be short, practical, and production-oriented.

Pronunciation notes are required when the answer contains a production-sensitive sound rule. Use:

- `CorePronunciationNote` for `CoreAnswerFR`
- `ConstructionPronunciationNote` for `ConstructionAnswerFR`
- `TenseParadigmIPA` for the tense paradigm reference

Call out liaison, elision, enchaînement, silent final consonants, h aspiré behavior, nasal vowels, and high-risk contrasts such as /y/ in `eu` when relevant.

## Optional Fields

Fill construction-production fields when there is a genuine high-value construction, pronoun, preposition, reflexive, clitic, or complement behavior worth isolating:

- `ConstructionPromptEN`
- `ConstructionAnswerFR`
- `ConstructionAnswerIPA`
- `ConstructionPronunciationNote`

All four construction-production fields must be either filled together or left blank together. If a construction-production answer would be grammatical but awkward, rare, or confusing, leave the construction-production fields blank for that row.

Construction-production cards should often be transformation drills when the construction has important pronoun behavior. Prefer prompts like:

- `Pronominalize the de-complement in French: J’ai besoin de ce document.`
- `Refer back to the action with en in French: Elle a besoin de dormir.`
- `Replace the person complement with the stressed pronoun in French: Nous avons besoin de Marie.`

Good answers:

- `J’en ai besoin.`
- `Elle en a besoin.`
- `Nous avons besoin d’elle.`

Bad default answers:

- `J’en ai besoin de ce document.`
- `Je lui ai besoin.`

`AudioFR` must be left blank for now.

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
- UTF-8 characters preserved exactly, including French accents, curly apostrophes, em dashes, and IPA symbols
- no replacement question marks for unsupported Unicode; if UTF-8 cannot be preserved, stop instead of emitting damaged TSV

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
- if a construction has subpatterns, the file rotates them intentionally

### 3. Tense Reference Audit

- `TenseOverview` correctly identifies the practical time/aspect/mood value
- `TenseUseNote` gives a useful operational rule
- `TenseParadigmFR` matches the current mood/tense of the target verb
- `TenseParadigmIPA` matches `TenseParadigmFR` in broad modern Parisian IPA

### 4. Naturalness Audit

- English prompts are natural, varied, and grammatically correct
- English prompts cue the correct tense, mood, and construction
- negative rows are included when useful, with spoken dropped-`ne` only in appropriate spoken or mixed contexts
- question rows are included when useful, with question strategy matching register
- register contrasts are marked when they affect the expected answer
- clitic behavior is taught when the construction naturally supports it, without artificial stacks
- French answers are natural, concise, and high-value for learning
- awkward literal translations are avoided when better French exists

### 5. Pronunciation Audit

- IPA is broad modern Parisian / standard metropolitan
- pronunciation notes are short and practical
- liaison, elision, enchaînement, nasal vowels, silent final consonants, h aspiré behavior, and /y/ vs /u/ are noted when relevant

### 6. Optional-Field Audit

- construction-production fields are all-filled or all-blank
- construction-production fields are filled only when there is a genuine construction behavior or reusable chunk worth isolating
- unused optional fields are left blank

### 7. Final TSV Audit

- output contains only TSV rows
- no prose before or after
- no code fences
- no extra blank lines at start or end
- no replacement question marks or mojibake in French, IPA, tense labels, construction fields, or prompts
