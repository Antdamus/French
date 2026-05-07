# Anki Template Snippets

Use Anki's built-in typed-answer syntax for `FrenchCards`. This strengthens written recall without adding typed-answer fields.

The live `FrenchCards` templates should have these card types:

- Core Production: `{{type:CoreAnswerFR}}`
- Construction Production: `{{type:ConstructionAnswerFR}}`
- Form Repair: `{{type:FormAnswerFR}}`

The back templates should show construction metadata prominently:

- `ConstructionFR`
- `ConstructionMeaningEN`
- `SemanticFrame`
- `ValencyClass`
- `ArgumentStructure`
- `ArgumentSlots`
- `ComplementTypes`
- `PrepositionBehavior`
- `PronounBehavior`
- `CliticOrderNote`
- `ConstructionConstraints`
- `ConstructionContrastNote`
- `AllowedForms`

This lets each card teach the function signature of the French construction while still testing the exact written answer.

Do not add separate typed-answer fields unless you want a different accepted answer from the displayed answer. For this deck, the existing answer fields are the right typing targets.

Anki's typed-answer check is literal. Accents, apostrophes, punctuation, and capitalization may matter depending on Anki's comparison behavior, so keep `AlternateAcceptedAnswers` as a human hint rather than relying on it for automatic typed-answer acceptance.
