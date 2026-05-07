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
