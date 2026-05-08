# Prompt for FrenchCards: avoir

Generate Anki-ready TSV content for my existing Anki note type `FrenchCards`.

Target verb: `avoir`
Provided root verb meaning: `to have`
Target construction: `avoir besoin de + complément`
Construction metadata supplied by user:
- ConstructionID: `avoir_besoin_de`
- ConstructionMeaningEN: `to need something/someone; to need to do something`
- SemanticFrame: `need/requirement`
- ValencyClass: `de-complement with subpatterns`
- ArgumentStructure: `subject experiencer + avoir besoin de + needed complement`
- ArgumentSlots: `subject; de-complement`
- ComplementTypes: `de + thing/idea noun phrase; de + infinitive/action; de + person`
- ConstructionSubpatterns: `thing/idea -> en; infinitive/action -> en when referring back to the action as an idea; person -> de + stressed pronoun, not normally en`
- PrepositionBehavior: `requires de before the needed complement; de elides to d’ before a vowel`
- PronounBehavior: `thing/idea/action complements can be replaced by en; specific people normally use de moi/toi/lui/elle/nous/vous/eux/elles`
- CliticOrderNote: `en precedes the conjugated verb or auxiliary; in infinitive phrases en precedes avoir`
- ConstructionConstraints: `do not say j’en ai besoin de X in neutral French; use either j’ai besoin de X or j’en ai besoin`
- ConstructionContrastNote: `avoir quelque chose uses direct object pronouns le/la/les; avoir besoin de uses de-complement behavior`
- AllowedForms: `ordinary finite forms; infinitive; participles; gerund; imperative only when semantically natural`
Scope: `full`
Subject policy: `split. Generate separate finite non-imperative notes for je, tu, il, elle, on, nous, vous, ils, and elles. Use j’ before a vowel or mute h where appropriate.`

This is an active-production deck, not a recognition deck. Generate one note per exact target form inside the target construction, with one main production sentence per note.

Important: the target is a verb construction, not the whole dictionary verb. If the construction has complement subpatterns, rotate them deliberately across rows while keeping the construction identity stable. Keep the same `ConstructionID`, `ConstructionFR`, `ConstructionMeaningEN`, `SemanticFrame`, `ValencyClass`, `ArgumentStructure`, `ArgumentSlots`, `ComplementTypes`, `PrepositionBehavior`, `PronounBehavior`, `CliticOrderNote`, `ConstructionConstraints`, `ConstructionContrastNote`, and `AllowedForms` metadata consistent across rows unless a row-specific restriction genuinely applies.

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
41. TenseOverview
42. TenseUseNote
43. TenseParadigmFR
44. TenseParadigmIPA
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
- `TenseOverview` (required): Brief plain-English orientation for the current mood/tense or non-finite form, such as completed past, background past, future completion, hypothetical, or literary narrative form.
- `TenseUseNote` (required): Operational note explaining when to use the current mood/tense in production.
- `TenseParadigmFR` (required): The target verb conjugated across the relevant pronouns/forms for the current mood/tense, in French.
- `TenseParadigmIPA` (required): Broad modern Parisian / standard metropolitan French IPA for TenseParadigmFR.
- `UsageNote` (optional): Short note about use, nuance, style, construction restrictions, or literary status.
- `AudioFR` (optional): Audio field; leave blank for now.

## Card Type Rules

# FrenchCards Card Types

The Anki note type `FrenchCards` has exactly 2 card types. The deck is construction-aware: each note targets one exact conjugated form inside one verb construction or valency frame.

The core learning unit is:

`Verb + Construction + Valency + Semantic Frame + Exact Form`

Do not treat a verb as one flat dictionary meaning when its constructions behave differently. For example, `penser à quelque chose`, `penser à quelqu’un`, `penser que`, and `penser de` should be generated as separate construction targets because they differ in meaning, complement behavior, and pronoun behavior.

## 1. Core Production

Core Production is the main card and should always be meaningful.

- Prompt side: `CorePromptEN` plus typed answer entry for `CoreAnswerFR`
- Answer side: Anki typed-answer comparison for `CoreAnswerFR`, then `CoreAnswerFR`
- Supporting fields: `CoreAnswerIPA`, `CorePronunciationNote`, `AlternateAcceptedAnswers`, `UsageNote`
- Tense fields shown on the answer side: `TenseOverview`, `TenseUseNote`, `TenseParadigmFR`, `TenseParadigmIPA`
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
- Tense fields shown on the answer side: `TenseOverview`, `TenseUseNote`, `TenseParadigmFR`, `TenseParadigmIPA`
- Construction fields shown on the answer side: the same construction map used by Core Production

Use this card to test high-value construction behavior such as:

- direct object pronouns: `le`, `la`, `les`
- indirect object pronouns: `lui`, `leur`
- `de`-complements becoming `en`
- `à` + thing/place/idea becoming `y`
- `à` + person staying tonic in constructions like `penser à lui`
- reflexive or lexicalized pronominal constructions
- clitic order such as `me/te/se/nous/vous + le/la/les + lui/leur + y + en`

When the construction has complement subpatterns, this card should usually test the transformation directly. For example:

- thing/idea complement: `Pronominalize: J’ai besoin de ce document.` -> `J’en ai besoin.`
- infinitive/action complement: `Refer back to the action with en: Elle a besoin de dormir.` -> `Elle en a besoin.`
- person complement: `Replace the person with the stressed pronoun: Nous avons besoin de Marie.` -> `Nous avons besoin d’elle.`

Do not create construction cards that teach bad neutral French, such as `J’en ai besoin de ce document`, or false indirect-object behavior, such as `Je lui ai besoin`.

Leave the construction-production fields blank only when the main core sentence already fully trains the construction and no additional construction behavior is worth isolating.

Use Anki's built-in typed-answer syntax:

- Front template should include `{{type:ConstructionAnswerFR}}`
- Back template should include `{{type:ConstructionAnswerFR}}`

Form Repair is not part of this note type anymore. If isolated repair practice is needed later, generate it as a focused Core Production row or use a separate repair note type.

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
- `TenseParadigmIPA` for the tense paradigm reference

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

Call out liaison when it helps production, and say whether it is required, optional, or blocked.

Required or expected liaison in careful standard speech:

- `nous avons` → /nuz‿avɔ̃/
- `vous avez` → /vuz‿ave/
- `ils ont` → /ilz‿ɔ̃/
- `elles ont` → /ɛlz‿ɔ̃/
- `nous avons eu` → /nuz‿avɔ̃z‿y/
- `vous avez eu` → /vuz‿avez‿y/
- `ils ont eu` → /ilz‿ɔ̃t‿y/

These are required or strongly expected because subject pronouns and many clitic-like function words link to a following vowel-initial verb in careful speech.

Optional liaison:

- often appears in careful/formal speech after short adverbs or prepositions, but may be absent in ordinary speech
- should be marked as optional if the learner can safely omit it in normal conversation

Forbidden or blocked liaison:

- no liaison after `et`
- no liaison before h aspiré
- avoid liaison across a strong syntactic break

Do not invent liaison where standard French would not normally make one.

## Good Note Style

- `Elide je before ai.`
- `Required liaison: nous avons links /z/ before vowel.`
- `Required liaison from avez into eu.`
- `Optional liaison in careful speech; often omitted casually.`
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
- uses grammatically correct English cueing, including correct subject-verb agreement
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

Avoid block-level monotony. A tense block should not reuse the same time phrase or sentence frame for every subject. Repeated anchors such as `today`, `tomorrow`, `soon`, or `if possible` across nine rows are a quality issue unless the block is intentionally contrasting forms.

## Negation Quality

Strong files include negative rows because negation changes production, rhythm, and pronoun placement. In spoken or mixed-register rows, conversational French may drop `ne`, such as `J’en ai pas besoin.` The full standard form should appear as a reminder in `AlternateAcceptedAnswers` or `UsageNote`, such as `Je n’en ai pas besoin.`

For formal, standard written, and literary rows, use full `ne ... pas` unless the row is deliberately contrasting spoken usage.

## Question Quality

Strong files include question rows because questions are a normal use of a verb construction. The question strategy should match register: intonation and `est-ce que` are common in speech, while inversion is more formal or written. Question rows should include the French question mark and should not hide the target form.

## Register And Clitic Quality

Use register contrast when it changes production: dropped `ne`, question strategy, liaison level, and formal inversion are all useful contrasts. For constructions with clitics, teach the natural clitic behavior directly. Do not invent clitic stacks for a construction just because clitic stacking exists elsewhere.

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

Rows are also weak if a construction has multiple complement subpatterns and the file hides them behind one vague label. For `avoir besoin de`, the learner should see that things/actions can become `en`, while specific people normally become `de moi/toi/lui/elle/nous/vous/eux/elles`.

Construction-production rows are also weak if they force a technically possible but unnatural clitic stack. For example, avoid optional construction cards whose answer is awkward enough that a learner would not confidently produce it in real French; leave the optional construction fields blank instead.

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

For constructions with pronoun behavior, construction-production prompts should often ask the learner to transform a full French sentence rather than simply telling them which pronoun to use. This is especially useful for contrasts like `de ce document -> en` versus `de Marie -> d’elle`.

When construction-production fields are used, the whole field group must be complete. A partially filled optional card is a bad row because it creates broken or confusing Anki cards.

## Tense Reference Discipline

Every row should include a compact tense reference on the back. Strong tense references include the current paradigm, matching Parisian IPA, and an operational note explaining when to use the tense. They should orient the learner without turning the front side into recognition.

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
- non-finite rows use `Person = N/A` and `SubjectFR = ?`
- construction metadata is consistent with syntax, complement behavior, and pronoun behavior
- if the construction has subpatterns, the file rotates them intentionally and the metadata explains the pronoun behavior for each complement type

3. NATURALNESS AUDIT
- English prompts are natural and varied
- English prompts are grammatically correct, including subject-verb agreement
- English prompts cue the correct tense, mood, and construction
- negative rows are included when useful, with spoken dropped-ne only in appropriate spoken or mixed contexts
- question rows are included when useful, with question strategy matching register
- register contrasts are marked when they affect the expected answer
- clitic behavior is taught when the construction naturally supports it, without artificial stacks
- French answers are natural, concise, and high-value for learning
- avoid awkward literal translations when better French exists
- avoid near-duplicate prompts whenever reasonably possible

4. TENSE REFERENCE AUDIT
- `TenseOverview` correctly identifies the practical time/aspect/mood value
- `TenseUseNote` gives a useful operational rule
- `TenseParadigmFR` matches the current mood/tense of the target verb
- `TenseParadigmIPA` matches `TenseParadigmFR` in broad modern Parisian IPA

5. PRONUNCIATION AUDIT
- IPA is broad modern Parisian / standard metropolitan
- pronunciation notes are short and practical
- liaison, elision, encha?nement, nasal vowels, silent final consonants, h aspir? behavior, and /y/ vs /u/ are noted when relevant
- no overlong phonetics essays

6. OPTIONAL-FIELD AUDIT
- construction-production fields are all-filled or all-blank; no partially filled construction-production groups
- construction-production fields are only filled when there is a genuine construction behavior or reusable chunk worth isolating
- construction-production prompts test useful transformations, such as pronominalization, when that is the construction behavior being isolated
- unused optional fields are left blank

7. LITERARY-SCOPE AUDIT
- literary forms are treated as active-production targets too
- literary labels and usage notes are accurate and not mixed carelessly with spoken-only labels

8. FINAL TSV AUDIT
- output contains only TSV rows
- no prose before or after
- no code fences
- no extra blank lines at start or end
- no replacement question marks or mojibake in French, IPA, tense labels, construction fields, or prompts

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
