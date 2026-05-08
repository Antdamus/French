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
