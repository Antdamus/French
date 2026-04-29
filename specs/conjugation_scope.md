# Conjugation Scope

The deck is for active production. If a form is included, it is included so the learner can actively produce it, not merely recognize it.

## Scope Labels

### full

The full default scope includes all supported spoken, educated written, and literary production forms:

Indicatif:

- présent
- imparfait
- passé composé
- plus-que-parfait
- passé simple
- passé antérieur
- futur simple
- futur antérieur

Conditionnel:

- présent
- passé

Subjonctif:

- présent
- passé
- imparfait
- plus-que-parfait

Impératif:

- présent
- passé

Infinitif:

- présent
- passé

Participe:

- présent
- passé

Gérondif:

- présent
- passé

### modern

Modern scope targets spoken French and standard written high-value forms. It should emphasize forms that are useful in conversation, contemporary media, school/professional writing, and ordinary educated prose.

Modern scope should normally include:

- indicatif présent, imparfait, passé composé, plus-que-parfait, futur simple, futur antérieur
- conditionnel présent and passé
- subjonctif présent and passé
- impératif présent
- infinitif présent and passé
- participe présent and passé
- gérondif présent

It should usually exclude or sharply limit literary-only forms such as passé simple, passé antérieur, subjonctif imparfait, subjonctif plus-que-parfait, impératif passé, and gérondif passé unless the verb or requested use case strongly justifies them.

### literary

Literary scope is literary-heavy. It still treats forms as active-production targets, but emphasizes forms needed to read and actively produce educated or literary prose, including forms useful for authors in the range of Camus and Sartre.

Literary scope should include the modern high-value forms plus literary forms such as:

- passé simple
- passé antérieur
- subjonctif imparfait
- subjonctif plus-que-parfait
- other marked written or literary forms from the full scope when useful

## Subject Policy

Default behavior is split subjects.

For finite non-imperative forms, generate separate target rows for:

- `je`
- `tu`
- `il`
- `elle`
- `on`
- `nous`
- `vous`
- `ils`
- `elles`

Use `j’` before a vowel or mute h where appropriate.

## Merged-Subject Option

The prompt generator supports `--subjects merged`. In merged mode, the downstream model may combine forms only when the surface verb form and production behavior are genuinely identical and pedagogically safe to merge.

Merged mode must not hide important agreement, liaison, spelling, subject, register, or pronunciation differences. When unsure, split the subjects.

When subjects are merged, use slash-separated subject labels in `Person` and `SubjectFR`, such as `il/elle/on` or `ils/elles`. Do not merge subjects with different surface forms or important pronunciation behavior.

## Imperative

Imperative rows use only:

- `tu`
- `nous`
- `vous`

## Non-Finite Forms

For infinitive, participle, and gerund rows:

- `Person` = `N/A`
- `SubjectFR` = `—`

Non-finite rows should still contain production prompts and natural French answers or phrases that practice the target form actively.
