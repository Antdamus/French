# Anki Template Snippets

Use Anki's built-in typed-answer syntax for `FrenchCards`. This strengthens written recall without adding fields or changing the TSV format.

## Core Production

Front template:

```html
<div class="prompt">{{CorePromptEN}}</div>
<div class="typed-answer">{{type:CoreAnswerFR}}</div>
```

Back template:

```html
{{FrontSide}}

<hr>

<div class="answer">{{CoreAnswerFR}}</div>
<div class="ipa">{{CoreAnswerIPA}}</div>
{{#CorePronunciationNote}}<div class="note">{{CorePronunciationNote}}</div>{{/CorePronunciationNote}}
{{#AlternateAcceptedAnswers}}<div class="note">Also accepted: {{AlternateAcceptedAnswers}}</div>{{/AlternateAcceptedAnswers}}
{{#UsageNote}}<div class="note">{{UsageNote}}</div>{{/UsageNote}}
```

## Idiom Production

Front template:

```html
{{#IdiomPromptEN}}
<div class="prompt">{{IdiomPromptEN}}</div>
<div class="typed-answer">{{type:IdiomAnswerFR}}</div>
{{/IdiomPromptEN}}
```

Back template:

```html
{{FrontSide}}

<hr>

<div class="answer">{{IdiomAnswerFR}}</div>
<div class="ipa">{{IdiomAnswerIPA}}</div>
{{#IdiomPronunciationNote}}<div class="note">{{IdiomPronunciationNote}}</div>{{/IdiomPronunciationNote}}
```

## Form Repair

Front template:

```html
{{#FormPrompt}}
<div class="prompt">{{FormPrompt}}</div>
<div class="typed-answer">{{type:FormAnswerFR}}</div>
{{/FormPrompt}}
```

Back template:

```html
{{FrontSide}}

<hr>

<div class="answer">{{FormAnswerFR}}</div>
<div class="ipa">{{FormAnswerIPA}}</div>
{{#FormPronunciationNote}}<div class="note">{{FormPronunciationNote}}</div>{{/FormPronunciationNote}}
```

## Notes

Do not add separate typed-answer fields unless you want a different accepted answer from the displayed answer. For this deck, the existing answer fields are the right typing targets.

Anki's typed-answer check is literal. Accents, apostrophes, punctuation, and capitalization may matter depending on Anki's comparison behavior, so keep `AlternateAcceptedAnswers` as a human hint rather than relying on it for automatic typed-answer acceptance.
