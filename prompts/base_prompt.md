# Prompt for FrenchCards: {{VERB}}

Generate Anki-ready TSV content for my existing Anki note type `{{NOTE_TYPE}}`.

Target verb: `{{VERB}}`
{{OPTIONAL_MEANING}}
{{CONSTRUCTION_TARGET}}
{{CONSTRUCTION_METADATA}}
Scope: `{{SCOPE_LABEL}}`
Subject policy: `{{SUBJECT_POLICY}}`

This is an active-production deck, not a recognition deck. Generate one note per exact target form inside the target construction, with one main production sentence per note.

Important: the target is a verb construction, not the whole dictionary verb. If the construction has complement subpatterns, rotate them deliberately across rows while keeping the construction identity stable. Keep the same `ConstructionID`, `ConstructionFR`, `ConstructionMeaningEN`, `SemanticFrame`, `ValencyClass`, `ArgumentStructure`, `ArgumentSlots`, `ComplementTypes`, `PrepositionBehavior`, `PronounBehavior`, `CliticOrderNote`, `ConstructionConstraints`, `ConstructionContrastNote`, and `AllowedForms` metadata consistent across rows unless a row-specific restriction genuinely applies.

## Canonical Field Order

{{FIELD_ORDER}}

## Field Summary

{{FIELD_SUMMARY}}

## Card Type Rules

{{CARD_TYPE_RULES}}

## Conjugation Scope

{{CONJUGATION_SCOPE}}

## Canonical Conjugation Targets

{{CONJUGATION_TARGETS}}

## Pronunciation Policy

{{PRONUNCIATION_POLICY}}

## Pedagogy Rubric

{{PEDAGOGY_RUBRIC}}

## Generation Rules

{{GENERATION_RULES}}

## Silent Self-Audit Required

{{AUDIT_RULES}}

## Output Instructions

{{OUTPUT_INSTRUCTIONS}}
