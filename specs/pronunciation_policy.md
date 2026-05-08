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
- `TenseParadigmIPA` for the tense paradigm reference

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

Call out liaison when it helps production, and say whether it is required, optional, or blocked.

Required or expected liaison in careful standard speech:

- `nous avons` → /nuz‿avɔ̃/
- `vous avez` → /vuz‿ave/
- `ils ont` → /ilz‿ɔ̃/
- `elles ont` → /ɛlz‿ɔ̃/
- `nous avons eu` → /nuz‿avɔ̃z‿y/
- `vous avez eu` → /vuz‿avez‿y/
- `ils ont eu` → /ilz‿ɔ̃t‿y/

These are required or strongly expected because subject pronouns and many clitic-like function words link to a following vowel-initial verb in careful speech.

Optional liaison:

- often appears in careful/formal speech after short adverbs or prepositions, but may be absent in ordinary speech
- should be marked as optional if the learner can safely omit it in normal conversation

Forbidden or blocked liaison:

- no liaison after `et`
- no liaison before h aspiré
- avoid liaison across a strong syntactic break

Do not invent liaison where standard French would not normally make one.

## Good Note Style

- `Elide je before ai.`
- `Required liaison: nous avons links /z/ before vowel.`
- `Required liaison from avez into eu.`
- `Optional liaison in careful speech; often omitted casually.`
- `Final t in eut is normally silent.`
- `Watch the nasal vowel /ɔ̃/.`
- `Watch /y/ in eu.`
- `No liaison before h aspiré.`

## Bad Note Style

- Long explanations of French phonology.
- Notes that merely repeat the IPA.
- Notes unrelated to producing the answer aloud.
