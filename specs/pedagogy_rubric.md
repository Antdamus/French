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
