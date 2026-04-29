# Review Prompt for FrenchCards: avoir

You are reviewing TSV generated for my existing Anki note type `FrenchCards`.

Target verb: `avoir`
Scope: `full`
Subject policy: `split subjects; finite non-imperative rows should separate je, tu, il, elle, on, nous, vous, ils, and elles.`

Your job is to audit the TSV for structure, conjugation accuracy, broad Parisian IPA quality, naturalness, register, and pedagogy. Do not rewrite the whole TSV unless explicitly asked. Find problems precisely.

## Canonical Field Order

1. Verb
2. VerbIPA
3. Meaning
4. Regularity
5. VerbGroup
6. PatternRule
7. StemChangeNote
8. IrregularityNote
9. Auxiliary
10. PastParticiple
11. AgreementNote
12. Register
13. FrequencyTier
14. Mood
15. Tense
16. Person
17. SubjectFR
18. CorePromptEN
19. CoreAnswerFR
20. CoreAnswerIPA
21. CorePronunciationNote
22. AlternateAcceptedAnswers
23. IdiomPromptEN
24. IdiomAnswerFR
25. IdiomAnswerIPA
26. IdiomPronunciationNote
27. FormPrompt
28. FormAnswerFR
29. FormAnswerIPA
30. FormPronunciationNote
31. UsageNote
32. AudioFR

## Field Summary

- `Verb` (required): Infinitive of the target French verb.
- `VerbIPA` (required): Broad modern Parisian / standard metropolitan French IPA for the infinitive.
- `Meaning` (required): Compact core English meaning.
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
- `Person` (required): Grammatical person label, or N/A for non-finite forms.
- `SubjectFR` (required): Exact surface French subject, such as je, j’, tu, il, elle, on, nous, vous, ils, elles, or —.
- `CorePromptEN` (required): Main natural English production prompt.
- `CoreAnswerFR` (required): Main French answer as a natural sentence or phrase that realizes the exact target form.
- `CoreAnswerIPA` (required): Broad Parisian IPA for the entire CoreAnswerFR.
- `CorePronunciationNote` (optional): Short practical pronunciation note.
- `AlternateAcceptedAnswers` (optional): Optional semicolon-separated alternate accepted answers; empty if none.
- `IdiomPromptEN` (optional): Optional English prompt for a genuine high-value idiom or chunk.
- `IdiomAnswerFR` (optional): Optional French answer for the idiom production card.
- `IdiomAnswerIPA` (optional): Optional broad Parisian IPA for IdiomAnswerFR.
- `IdiomPronunciationNote` (optional): Optional short practical pronunciation note for the idiom answer.
- `FormPrompt` (optional): Optional repair prompt for an irregular, confusable, or otherwise high-value isolated form.
- `FormAnswerFR` (optional): Optional isolated French form answer.
- `FormAnswerIPA` (optional): Optional broad Parisian IPA for FormAnswerFR.
- `FormPronunciationNote` (optional): Optional short practical pronunciation note for the isolated form.
- `UsageNote` (optional): Short note about use, nuance, style, or literary status.
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

Focus on:

- liaison
- elision
- nasal vowels
- silent final consonants
- semivowels
- important standard metropolitan pronunciation points

Avoid:

- long phonetics essays
- dialect surveys
- ultra-narrow allophones
- repeating obvious information in every row

## Good Note Style

- `Elide je before ai.`
- `Liaison in nous avons.`
- `Final t is silent before a consonant.`
- `Watch the nasal vowel /ɔ̃/.`

## Bad Note Style

- Long explanations of French phonology.
- Notes that merely repeat the IPA.
- Notes unrelated to producing the answer aloud.

## Pedagogy Rubric

# Pedagogy Rubric

FrenchCards is an active-production system. A strong row helps the learner produce one exact form in a natural context.

## High-Value Rows

A good row:

- targets one exact verb form
- uses a natural English production prompt
- gives a concise, idiomatic French answer
- avoids translationese
- uses a prompt that differs meaningfully from nearby rows
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

Variation should serve production. Do not make prompts strange just to be different.

## Literary Forms

Literary forms are active-production targets when included. Label them clearly and use contexts where they naturally belong, especially narration, formal prose, or literary style.

Do not mix literary forms into casual spoken prompts unless the contrast is intentional and explained in `UsageNote`.

## Idiom Discipline

Fill idiom fields only for genuine high-value idioms, expressions, or reusable chunks. A weak phrase is worse than a blank optional card.

## Form Repair Discipline

Fill form repair fields only when the isolated form deserves extra attention because it is irregular, confusable, pronunciation-sensitive, or especially common.

## Review Standard

When reviewing TSV, prefer fewer excellent cards over many mediocre cards. Flag rows that are structurally valid but pedagogically weak.

## Review Checklist

Check:

1. Structure
- no header row
- every row has exactly 32 fields
- field order matches `FrenchCards`
- required fields are not blank
- optional blanks are represented by empty cells
- no tabs or line breaks inside cell content

2. Conjugation
- `CoreAnswerFR` contains the exact target form for `Verb`, `Mood`, `Tense`, `Person`, and `SubjectFR`
- imperative rows use only `tu`, `nous`, and `vous`
- non-finite rows use `Person = N/A` and `SubjectFR = —`
- subject labels match the French answer, including `j’` before vowels or mute h
- merged subject rows, when allowed, use slash-separated labels and do not hide important production differences
- literary forms are correct and labeled accurately

3. IPA
- IPA is broad modern Parisian / standard metropolitan French
- IPA covers the full answer, not only the target form
- liaison, elision, nasal vowels, semivowels, and silent final consonants are handled correctly where relevant
- pronunciation notes are short and practical

4. Naturalness And Pedagogy
- English prompts are natural and varied
- French answers are concise, idiomatic, and useful
- rows avoid awkward literal translation
- optional idiom fields are genuinely high-value
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
avoir	/a.vwaʁ/	to have	irregular	irregular family	Highly irregular common auxiliary.		Present stem alternates ai-/av-/ont.	avoir	eu	With avoir, past participle agrees with a preceding direct object when required.	spoken	high	indicatif	présent	je	j’	I have three questions.	J’ai trois questions.	/ʒe tʁwa kɛs.tjɔ̃/	Elide je before ai.		I feel like continuing.	J’ai envie de continuer.	/ʒe ɑ̃.vi də kɔ̃.ti.nɥe/	Enchaînement in j’ai envie.					Common high-frequency auxiliary; also used in many expressions.	
avoir	/a.vwaʁ/	to have	irregular	irregular family	Highly irregular common auxiliary.		Present stem alternates ai-/av-/ont.	avoir	eu	With avoir, past participle agrees with a preceding direct object when required.	standard written	high	indicatif	présent	nous	nous	We have enough time.	Nous avons assez de temps.	/nu.za.vɔ̃ a.se də tɑ̃/	Liaison in nous avons.						avoir — présent — nous	nous avons	/nu.za.vɔ̃/	Liaison from nous to avons.	Common high-frequency auxiliary; present nous form is a useful repair target.	
avoir	/a.vwaʁ/	to have	irregular	irregular family	Highly irregular common auxiliary.		Compound tenses use avoir eu.	avoir	eu	With avoir, past participle agrees with a preceding direct object when required.	literary	literary	indicatif	passé simple	il	il	He had a sudden doubt.	Il eut un doute soudain.	/il y œ̃ dut su.dɛ̃/	Final t in eut is normally silent before consonant.										Literary narrative form; active-production target for formal prose.
```
