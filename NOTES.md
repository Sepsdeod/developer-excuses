# NOTES — Developer Excuses

## Chosen line (76 characters)

> It worked on my machine because my machine has never had a single real user.

## Why it wins against the judge brief

The judge weighs, in order: (1) a funny single-line dev excuse about code
breaking in production; (2) a twist a developer recognises, revealing what
really happened; (3) sounds like something a developer would actually say,
jargon used right; (4) lands fast, every word earning its place; (5) feels
fresh, turning a worn excuse in a way nobody has before.

- **On brief (1):** it is exactly one excuse for production breaking, in one
  line, in a developer's voice.
- **Twist (2):** the classic defence "it works on my machine" is flipped —
  the machine is not proof the code is good, it is proof the code was never
  truly tested. The reveal (no real user ever touched it) is what really
  happened: the code only ever ran against its author's happy path.
- **Voice (3):** "it worked on my machine" is the most-quoted sentence in
  incident post-mortems; the rest of the line is plain spoken English, no
  forced jargon.
- **Fast (4):** 76 characters, one clause of setup and one punch. Nothing to
  trim — every word carries the joke.
- **Fresh (5):** it does not just repeat the worn excuse; it turns it against
  the person saying it. The excuse indicts the speaker, which is the part
  nobody has said before.

## Alternatives considered and rejected

1. "The code was fine — production just has commitment issues."
   Rejected: the "commitment issues" gag is a generic relationship joke
   pasted onto production; it reveals nothing a developer recognises about
   what actually went wrong, so it loses on criterion 2.

2. "I didn't push a bug to production; I pushed a feature only production was brave enough to run."
   Rejected: lands slower (over 100 characters, two clauses of setup for a
   thin punch), and "brave enough to run" is vague where the judge wants a
   concrete twist. Loses on criteria 4 and 2.
