# Review Prompt for FrenchCards: avoir

You are reviewing TSV generated for my existing Anki note type `FrenchCards`.

Target verb: `avoir`
Scope: `full`
Subject policy: `split subjects; finite non-imperative rows should separate je, tu, il, elle, on, nous, vous, ils, and elles.`

Your job is to audit the TSV for structure, construction accuracy, valency metadata, conjugation accuracy, broad Parisian IPA quality, liaison/pronunciation notes, naturalness, register, and pedagogy. Do not rewrite the whole TSV unless explicitly asked. Find problems precisely.

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

## Canonical Conjugation Targets

Finite subjects: je, tu, il, elle, on, nous, vous, ils, elles
Imperative subjects: tu, nous, vous
Non-finite policy: Person = N/A; SubjectFR = —

Targets included in `full` scope:
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
PASTE TSV HERE
```
