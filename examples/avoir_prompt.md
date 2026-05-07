# Prompt for FrenchCards: avoir

Generate Anki-ready TSV content for my existing Anki note type `FrenchCards`.

Target verb: `avoir`
Provided root verb meaning: `to have`
Target construction: `avoir besoin de quelque chose`
Construction metadata supplied by user:
- ConstructionID: `avoir_besoin_de_qqch`
- ConstructionMeaningEN: `to need something`
- SemanticFrame: `need/requirement`
- ValencyClass: `de-complement`
- ArgumentStructure: `subject experiencer + avoir besoin de + needed thing/action`
- ArgumentSlots: `subject; de-complement`
- ComplementTypes: `de + noun; de + infinitive; thing/idea/action`
- PrepositionBehavior: `requires de before the needed complement`
- PronounBehavior: `de + thing/idea/action -> en`
- ConstructionContrastNote: `avoir quelque chose uses direct object pronouns le/la/les; avoir besoin de uses en`
- AllowedForms: `ordinary finite forms; infinitive; participles; gerund; imperative only when semantically natural`
Scope: `full`
Subject policy: `split. Generate separate finite non-imperative notes for je, tu, il, elle, on, nous, vous, ils, and elles. Use j’ before a vowel or mute h where appropriate.`
Form repair policy: `auto. Fill form repair fields only when the form is irregular, confusable, pronunciation-sensitive, or worth isolating.`

This is an active-production deck, not a recognition deck. Generate one note per exact target form inside the target construction, with one main production sentence per note.

Important: the target is a verb construction, not the whole dictionary verb. Keep the same `ConstructionID`, `ConstructionFR`, `ConstructionMeaningEN`, `SemanticFrame`, `ValencyClass`, `ArgumentStructure`, `ArgumentSlots`, `ComplementTypes`, `PrepositionBehavior`, `PronounBehavior`, `CliticOrderNote`, `ConstructionConstraints`, `ConstructionContrastNote`, and `AllowedForms` metadata consistent across rows unless a row-specific restriction genuinely applies.

## Canonical Field Order

1. Verb
2. VerbIPA
3. VerbCoreMeaning
4. ConstructionID
5. ConstructionFR
6. ConstructionMeaningEN
7. SemanticFrame
8. ValencyClass
9. ArgumentStructure
10. ArgumentSlots
11. ComplementTypes
12. PrepositionBehavior
13. PronounBehavior
14. CliticOrderNote
15. ConstructionConstraints
16. ConstructionContrastNote
17. AllowedForms
18. Regularity
19. VerbGroup
20. PatternRule
21. StemChangeNote
22. IrregularityNote
23. Auxiliary
24. PastParticiple
25. AgreementNote
26. Register
27. FrequencyTier
28. Mood
29. Tense
30. Person
31. SubjectFR
32. CorePromptEN
33. CoreAnswerFR
34. CoreAnswerIPA
35. CorePronunciationNote
36. AlternateAcceptedAnswers
37. ConstructionPromptEN
38. ConstructionAnswerFR
39. ConstructionAnswerIPA
40. ConstructionPronunciationNote
41. FormPrompt
42. FormAnswerFR
43. FormAnswerIPA
44. FormPronunciationNote
45. UsageNote
46. AudioFR

## Field Summary

- `Verb` (required): Infinitive of the root French verb.
- `VerbIPA` (required): Broad modern Parisian / standard metropolitan French IPA for the infinitive.
- `VerbCoreMeaning` (required): Compact broad English meaning of the root verb before construction-specific narrowing.
- `ConstructionID` (required): Stable short identifier for this verb construction, such as avoir_besoin_de_qqch.
- `ConstructionFR` (required): French construction pattern, such as avoir besoin de quelque chose.
- `ConstructionMeaningEN` (required): English meaning of this construction or valency frame.
- `SemanticFrame` (required): Short semantic frame label, such as possession, need, desire, perception, transfer, motion, or opinion.
- `ValencyClass` (required): Concise valency class, such as direct object, à + person, à + thing/place, de-complement, reflexive, or infinitive complement.
- `ArgumentStructure` (required): Human-readable function signature showing arguments and complements.
- `ArgumentSlots` (required): Semicolon-separated input slots expected by the construction.
- `ComplementTypes` (required): Allowed complement types, such as person, thing/idea, place, noun phrase, que-clause, or infinitive.
- `PrepositionBehavior` (optional): Required preposition behavior, including à/de/zero-preposition restrictions.
- `PronounBehavior` (optional): How complements pronominalize: le/la/les, lui/leur, y, en, tonic à lui/à elle, or none.
- `CliticOrderNote` (optional): Relevant clitic ordering note if the construction combines pronouns.
- `ConstructionConstraints` (optional): Restrictions, incompatibilities, or special conditions for this construction.
- `ConstructionContrastNote` (optional): Contrast with nearby constructions of the same verb or misleading English patterns.
- `AllowedForms` (required): Forms in scope that are natural for this construction; note restrictions such as rare imperative or non-finite limitations.
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
- `Person` (required): Subject/person label, or N/A for non-finite forms.
- `SubjectFR` (required): Exact surface French subject, such as je, j’, tu, il, elle, on, nous, vous, ils, elles, or —.
- `CorePromptEN` (required): Main typed-answer English production prompt for the conjugated construction.
- `CoreAnswerFR` (required): Main French answer that realizes the exact target form and construction.
- `CoreAnswerIPA` (required): Broad Parisian IPA for the entire CoreAnswerFR.
- `CorePronunciationNote` (optional): Short practical pronunciation, liaison, elision, or sound-production note for CoreAnswerFR.
- `AlternateAcceptedAnswers` (optional): Optional semicolon-separated alternate accepted answers; empty if none.
- `ConstructionPromptEN` (optional): Optional typed-answer prompt specifically testing construction/pronoun behavior.
- `ConstructionAnswerFR` (optional): French answer for the construction/pronoun production card.
- `ConstructionAnswerIPA` (optional): Broad Parisian IPA for ConstructionAnswerFR.
- `ConstructionPronunciationNote` (optional): Short practical pronunciation note for ConstructionAnswerFR.
- `FormPrompt` (optional): Optional repair prompt for an irregular, confusable, pronunciation-sensitive, or otherwise high-value isolated form.
- `FormAnswerFR` (optional): Optional isolated French form answer.
- `FormAnswerIPA` (optional): Optional broad Parisian IPA for FormAnswerFR.
- `FormPronunciationNote` (optional): Short practical pronunciation note for the isolated form.
- `UsageNote` (optional): Short note about use, nuance, style, construction restrictions, or literary status.
- `AudioFR` (optional): Audio field; leave blank for now.

## Card Type Rules

# FrenchCards Card Types

The Anki note type `FrenchCards` has exactly 3 card types. The deck is now construction-aware: each note targets one exact conjugated form inside one verb construction or valency frame.

The core learning unit is:

`Verb + Construction + Valency + Semantic Frame + Exact Form`

Do not treat a verb as one flat dictionary meaning when its constructions behave differently. For example, `penser à quelque chose`, `penser à quelqu’un`, `penser que`, and `penser de` should be generated as separate construction targets because they differ in meaning, complement behavior, and pronoun behavior.

## 1. Core Production

Core Production is the main card and should always be meaningful.

- Prompt side: `CorePromptEN` plus typed answer entry for `CoreAnswerFR`
- Answer side: Anki typed-answer comparison for `CoreAnswerFR`, then `CoreAnswerFR`
- Supporting fields: `CoreAnswerIPA`, `CorePronunciationNote`, `AlternateAcceptedAnswers`, `UsageNote`
- Construction fields shown on the answer side: `ConstructionFR`, `ConstructionMeaningEN`, `SemanticFrame`, `ValencyClass`, `ArgumentStructure`, `ArgumentSlots`, `ComplementTypes`, `PrepositionBehavior`, `PronounBehavior`, `CliticOrderNote`, `ConstructionConstraints`, `ConstructionContrastNote`, `AllowedForms`

Every note must include one exact target verb form in `CoreAnswerFR` and must realize the target construction. The English prompt should cue both the tense/mood and the construction meaning.

Use Anki's built-in typed-answer syntax:

- Front template should include `{{type:CoreAnswerFR}}`
- Back template should include `{{type:CoreAnswerFR}}`

## 2. Construction Production

Construction Production is optional, but strongly recommended when the construction has important valency, pronoun, preposition, reflexive, or complement behavior.

- Prompt side: `ConstructionPromptEN` plus typed answer entry for `ConstructionAnswerFR`
- Answer side: Anki typed-answer comparison for `ConstructionAnswerFR`, then `ConstructionAnswerFR`
- Supporting fields: `ConstructionAnswerIPA`, `ConstructionPronunciationNote`

Use this card to test high-value construction behavior such as:

- direct object pronouns: `le`, `la`, `les`
- indirect object pronouns: `lui`, `leur`
- `de`-complements becoming `en`
- `à` + thing/place/idea becoming `y`
- `à` + person staying tonic in constructions like `penser à lui`
- reflexive or lexicalized pronominal constructions
- clitic order such as `me/te/se/nous/vous + le/la/les + lui/leur + y + en`

Leave the construction-production fields blank only when the main core sentence already fully trains the construction and no additional construction behavior is worth isolating.

Use Anki's built-in typed-answer syntax:

- Front template should include `{{type:ConstructionAnswerFR}}`
- Back template should include `{{type:ConstructionAnswerFR}}`

## 3. Form Repair

Form Repair is optional. Fill form repair fields only when the target form is irregular, easy to confuse, unusually spelled, pronunciation-sensitive, or otherwise worth isolating.

- Prompt side: `FormPrompt` plus typed answer entry for `FormAnswerFR`
- Answer side: Anki typed-answer comparison for `FormAnswerFR`, then `FormAnswerFR`
- Supporting fields: `FormAnswerIPA`, `FormPronunciationNote`

Example:

- `FormPrompt`: `avoir — indicatif présent — nous`
- `FormAnswerFR`: `nous avons`

Leave all form repair fields blank when the form does not need isolated repair practice.

Use Anki's built-in typed-answer syntax:

- Front template should include `{{type:FormAnswerFR}}`
- Back template should include `{{type:FormAnswerFR}}`

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

Use the pronunciation note fields actively:

- `CorePronunciationNote` for the main sentence
- `ConstructionPronunciationNote` for construction/pronoun cards
- `FormPronunciationNote` for isolated forms

Fill the relevant note field when the answer contains a production-sensitive issue:

- liaison
- elision
- enchaînement
- nasal vowels
- silent final consonants
- semivowels
- h aspiré blocking elision or liaison
- /y/ vs /u/, /ø/ vs /œ/, or other high-risk contrasts
- compound-tense liaison into `eu`

Leave the note blank only when there is no useful pronunciation warning.

## Liaison Guidance

Call out liaison when it helps production, especially in common verb forms:

- `nous avons` → /nuz‿avɔ̃/
- `vous avez` → /vuz‿ave/
- `ils ont` → /ilz‿ɔ̃/
- `elles ont` → /ɛlz‿ɔ̃/
- `nous avons eu` → /nuz‿avɔ̃z‿y/
- `vous avez eu` → /vuz‿avez‿y/
- `ils ont eu` → /ilz‿ɔ̃t‿y/

Do not invent liaison where standard French would not normally make one. Note h aspiré when it blocks elision or liaison.

## Good Note Style

- `Elide je before ai.`
- `Liaison in nous avons.`
- `Liaison from avez into eu.`
- `Final t in eut is normally silent.`
- `Watch the nasal vowel /ɔ̃/.`
- `Watch /y/ in eu.`
- `No liaison before h aspiré.`

## Bad Note Style

- Long explanations of French phonology.
- Notes that merely repeat the IPA.
- Notes unrelated to producing the answer aloud.

## Pedagogy Rubric

# Pedagogy Rubric

FrenchCards is an active-production system. A strong row helps the learner produce one exact form in a natural context.

The learning unit is construction-aware:

`verb + construction + valency + semantic frame + exact form`

Do not flatten a verb into one English translation when its constructions behave differently.

## High-Value Rows

A good row:

- targets one exact verb form
- targets one exact construction or valency frame
- uses a natural English production prompt
- makes the target tense or mood clear through the English meaning, not only through a grammar label
- makes the target construction clear through the English meaning
- gives a concise, idiomatic French answer
- avoids translationese
- uses a prompt that differs meaningfully from nearby rows
- gives typed-answer learners one predictable answer to produce
- gives accurate construction metadata, especially complement and pronoun behavior
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
- questions and negative statements
- nouns with useful adjectives
- time phrases that clarify tense and aspect

Variation should serve production. Do not make prompts strange just to be different.

## Construction Quality

Good construction cards identify:

- the construction pattern, such as `avoir besoin de quelque chose`
- the semantic frame, such as need/requirement
- the valency class, such as `de`-complement
- the input slots, such as subject plus needed thing/action
- complement types, such as noun phrase or infinitive
- pronoun behavior, such as `de + thing/action -> en`
- contrast with misleading nearby frames, such as direct-object `avoir quelque chose`

Rows are weak if they conjugate the root verb correctly but train the wrong construction or hide a major pronoun/preposition distinction.

## Tense And Mood Cueing

The English prompt should teach the form's use:

- imparfait prompts should cue habit, background, description, or repeated past state
- passé composé prompts should cue a completed past event
- plus-que-parfait prompts should cue an event or state earlier than another past point
- futur antérieur prompts should cue completion before a future deadline
- conditionnel prompts should cue hypothetical, polite, or reported situations
- subjunctive prompts should include a natural trigger such as need, doubt, emotion, or judgment
- literary prompts should sound like formal or narrative prose

Rows that merely say `use the [tense] form` without an English tense meaning are pedagogically weak, especially now that cards require typed answers.

## Literary Forms

Literary forms are active-production targets when included. Label them clearly and use contexts where they naturally belong, especially narration, formal prose, or literary style.

Do not mix literary forms into casual spoken prompts unless the contrast is intentional and explained in `UsageNote`.

## Construction Production Discipline

Fill construction-production fields only for genuine high-value construction behavior, pronoun behavior, preposition behavior, reflexive behavior, clitic behavior, or reusable chunks. A weak extra card is worse than a blank optional card.

## Form Repair Discipline

Fill form repair fields only when the isolated form deserves extra attention because it is irregular, confusable, pronunciation-sensitive, or especially common.

## Review Standard

When reviewing TSV, prefer fewer excellent cards over many mediocre cards. Flag rows that are structurally valid but pedagogically weak.

## Generation Rules

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

## Silent Self-Audit Required

Perform a private self-audit before producing the final TSV. Do not show the audit.

1. STRUCTURE AUDIT
- every row has exactly 46 fields
- field order exactly matches `FrenchCards`
- no header row
- no missing cells caused by forgotten tabs
- optional blanks are represented by empty cells, not omitted columns
- no tabs or line breaks inside cell content

2. CONSTRUCTION AND CONJUGATION AUDIT
- the French answer actually contains the target form for this verb, mood, tense, and person
- the French answer uses the target construction, not another construction of the same root verb
- the person and `SubjectFR` are correct
- imperative rows only use `tu`, `nous`, and `vous`
- non-finite rows use `Person = N/A` and `SubjectFR = —`
- construction metadata is consistent with syntax, complement behavior, and pronoun behavior

3. NATURALNESS AUDIT
- English prompts are natural and varied
- English prompts cue the correct tense, mood, and construction
- French answers are natural, concise, and high-value for learning
- avoid awkward literal translations when better French exists
- avoid near-duplicate prompts whenever reasonably possible

4. PRONUNCIATION AUDIT
- IPA is broad modern Parisian / standard metropolitan
- pronunciation notes are short and practical
- liaison, elision, enchaînement, nasal vowels, silent final consonants, h aspiré behavior, and /y/ vs /u/ are noted when relevant
- no overlong phonetics essays

5. OPTIONAL-FIELD AUDIT
- construction-production fields are only filled when there is a genuine construction behavior or reusable chunk worth isolating
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
- no replacement question marks or mojibake in French, IPA, tense labels, construction fields, or form prompts

## Output Instructions

Return RAW TSV ONLY.

Do not output Markdown code fences, explanations, commentary, numbering, a header row, or column titles.

Encoding requirement: output must be valid UTF-8. Preserve all Unicode characters exactly, including French accents, curly apostrophes, em dashes, and IPA symbols such as ʁ, ɛ, ɔ̃, œ, ø, ɥ, ʒ, and ‿. Do not replace unsupported characters with question marks or mojibake. If UTF-8 cannot be preserved, stop instead of emitting damaged TSV.

Output exactly one note per line. Each line must contain exactly 46 tab-separated fields in the exact `FrenchCards` field order. Optional unused fields must be empty cells, but their columns must still be preserved.

Every field must stay on a single line. Do not put literal tab characters or literal line breaks inside field content. Normalize internal line breaks to spaces. Preserve UTF-8 characters such as accents and IPA symbols.

Malformed TSV is a failure. The response is wrong if:
- there is any prose before or after the TSV
- there is a header row
- any row has fewer than 46 fields
- any row has more than 46 fields
- the column order differs from the specified order
- any accent, apostrophe, em dash, or IPA symbol has been replaced by `?` or mojibake
