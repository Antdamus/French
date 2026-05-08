# Anki Template Snippets

Use Anki's built-in typed-answer syntax for `FrenchCards`. This strengthens written recall without adding typed-answer fields.

The live `FrenchCards` templates should have these card types:

- Core Production: `{{type:CoreAnswerFR}}`
- Construction Production: `{{type:ConstructionAnswerFR}}`

The old Form Repair card type and fields are removed from this note type. If repair practice is needed later, use a focused Core Production note or a separate repair note type.

## Tense Block

Every back template should show the tense map:

```html
{{#TenseOverview}}
<div class="section tense-map">
  <div class="label">Tense map</div>
  <div class="value">
    <strong>{{Mood}} · {{Tense}}</strong><br>
    {{TenseOverview}}
    {{#TenseUseNote}}<br>{{TenseUseNote}}{{/TenseUseNote}}
  </div>
</div>
{{/TenseOverview}}

{{#TenseParadigmFR}}
<div class="section tense-paradigm">
  <div class="label">This tense of {{Verb}}</div>
  <div class="value">
    {{TenseParadigmFR}}
    {{#TenseParadigmIPA}}<br><span class="inline-ipa">{{TenseParadigmIPA}}</span>{{/TenseParadigmIPA}}
  </div>
</div>
{{/TenseParadigmFR}}
```

`TenseParadigmFR` should show the verb conjugated across the relevant pronouns or forms for the current mood/tense. `TenseParadigmIPA` should give broad modern Parisian / standard metropolitan French IPA for the same paradigm.

## Construction Block

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

Use grouped labels on the back side so multi-input constructions are easy to read:

```html
{{#ConstructionFR}}
<div class="section construction-map">
  <div class="label">Construction map</div>
  <div class="value">
    <strong>{{ConstructionFR}}</strong>
    {{#ConstructionMeaningEN}}<br>{{ConstructionMeaningEN}}{{/ConstructionMeaningEN}}
    {{#SemanticFrame}}<br>Frame: {{SemanticFrame}}{{/SemanticFrame}}
    {{#ValencyClass}}<br>Valency: {{ValencyClass}}{{/ValencyClass}}
  </div>
</div>
{{/ConstructionFR}}

<div class="section construction-inputs">
  <div class="label">Inputs</div>
  <div class="value">
    {{#ArgumentStructure}}Signature: {{ArgumentStructure}}<br>{{/ArgumentStructure}}
    {{#ArgumentSlots}}Slots: {{ArgumentSlots}}<br>{{/ArgumentSlots}}
    {{#ComplementTypes}}Complements: {{ComplementTypes}}{{/ComplementTypes}}
  </div>
</div>

<div class="section construction-pronouns">
  <div class="label">Pronouns and constraints</div>
  <div class="value">
    {{#PrepositionBehavior}}Preposition: {{PrepositionBehavior}}<br>{{/PrepositionBehavior}}
    {{#PronounBehavior}}Pronouns: {{PronounBehavior}}<br>{{/PronounBehavior}}
    {{#CliticOrderNote}}Order: {{CliticOrderNote}}<br>{{/CliticOrderNote}}
    {{#ConstructionConstraints}}Constraints: {{ConstructionConstraints}}{{/ConstructionConstraints}}
  </div>
</div>

{{#ConstructionContrastNote}}
<div class="section construction-contrast">
  <div class="label">Contrast</div>
  <div class="value">{{ConstructionContrastNote}}</div>
</div>
{{/ConstructionContrastNote}}

{{#AllowedForms}}
<div class="section">
  <div class="label">Allowed forms</div>
  <div class="value">{{AllowedForms}}</div>
</div>
{{/AllowedForms}}
```

For a construction such as `avoir besoin de + complément`, the `ComplementTypes` and `PronounBehavior` lines should make the subpatterns visible:

- `de + thing/idea -> en`
- `de + infinitive/action -> en when referring back to the action as an idea`
- `de + person -> de moi/toi/lui/elle/nous/vous/eux/elles`, not normally `en`

Do not add separate typed-answer fields unless you want a different accepted answer from the displayed answer. For this deck, the existing answer fields are the right typing targets.

Anki's typed-answer check is literal. Accents, apostrophes, punctuation, and capitalization may matter depending on Anki's comparison behavior, so keep `AlternateAcceptedAnswers` as a human hint rather than relying on it for automatic typed-answer acceptance.
