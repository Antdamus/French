# FrenchCards Card Types

The Anki note type `FrenchCards` has exactly 3 card types. This repository documents how prompts should fill the note fields that drive those cards. It does not modify the Anki templates directly.

## 1. Core Production

Core Production is the main card and should always be meaningful.

- Prompt side: `CorePromptEN` plus typed answer entry for `CoreAnswerFR`
- Answer side: Anki typed-answer comparison for `CoreAnswerFR`, then `CoreAnswerFR`
- Supporting fields: `CoreAnswerIPA`, `CorePronunciationNote`, `AlternateAcceptedAnswers`, `UsageNote`

Every note must include one exact target verb form in `CoreAnswerFR`. The English prompt should be natural, varied, and designed for active production rather than recognition.

Use Anki's built-in typed-answer syntax rather than adding a new field:

- Front template should include `{{type:CoreAnswerFR}}`
- Back template should include `{{type:CoreAnswerFR}}`

## 2. Idiom Production

Idiom Production is optional. Fill idiom fields only when the verb form naturally supports a genuinely high-value idiom, expression, or reusable chunk.

- Prompt side: `IdiomPromptEN` plus typed answer entry for `IdiomAnswerFR`
- Answer side: Anki typed-answer comparison for `IdiomAnswerFR`, then `IdiomAnswerFR`
- Supporting fields: `IdiomAnswerIPA`, `IdiomPronunciationNote`

Leave all idiom fields blank when there is no strong idiom or chunk. Do not invent weak idioms just to fill the card.

Use Anki's built-in typed-answer syntax:

- Front template should include `{{type:IdiomAnswerFR}}`
- Back template should include `{{type:IdiomAnswerFR}}`

## 3. Form Repair

Form Repair is optional. Fill form repair fields only when the target form is irregular, easy to confuse, unusually spelled, pronunciation-sensitive, or otherwise worth isolating.

- Prompt side: `FormPrompt` plus typed answer entry for `FormAnswerFR`
- Answer side: Anki typed-answer comparison for `FormAnswerFR`, then `FormAnswerFR`
- Supporting fields: `FormAnswerIPA`, `FormPronunciationNote`

Example:

- `FormPrompt`: `avoir — présent — nous`
- `FormAnswerFR`: `nous avons`

Leave all form repair fields blank when the form does not need isolated repair practice.

Use Anki's built-in typed-answer syntax:

- Front template should include `{{type:FormAnswerFR}}`
- Back template should include `{{type:FormAnswerFR}}`
