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
- `FormPronunciationNote` for isolated forms

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

Call out liaison when it helps production, especially in common verb forms:

- `nous avons` → /nuz‿avɔ̃/
- `vous avez` → /vuz‿ave/
- `ils ont` → /ilz‿ɔ̃/
- `elles ont` → /ɛlz‿ɔ̃/
- `nous avons eu` → /nuz‿avɔ̃z‿y/
- `vous avez eu` → /vuz‿avez‿y/
- `ils ont eu` → /ilz‿ɔ̃t‿y/

Do not invent liaison where standard French would not normally make one. Note h aspiré when it blocks elision or liaison.

## Good Note Style

- `Elide je before ai.`
- `Liaison in nous avons.`
- `Liaison from avez into eu.`
- `Final t in eut is normally silent.`
- `Watch the nasal vowel /ɔ̃/.`
- `Watch /y/ in eu.`
- `No liaison before h aspiré.`

## Bad Note Style

- Long explanations of French phonology.
- Notes that merely repeat the IPA.
- Notes unrelated to producing the answer aloud.
