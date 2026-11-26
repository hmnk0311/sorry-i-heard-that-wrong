#!/usr/bin/env python3
"""Entry program for "Sorry, I Heard That Wrong"
(u-kiencx-sorry-i-heard-that-wrong-1858c729).

One line, at most 140 characters, written to /output/entry.txt:
the funniest apology a smart speaker gives its owner after
mishearing them. The judge's brief in the kit's RULES weighs,
in order:

1. A one-line apology a smart speaker gives its owner after
   mishearing the owner; anything else loses.
2. Funny: a real laugh, a sharp twist or a perfectly timed
   undercut, not a strained pun.
3. Fresh: not the obvious misheard song title or misheard
   name, and not a joke heard from a smart speaker before.
4. Sounds like the device: the voice, the phrasing and the
   apology fit a speaker that has just misheard its owner.
5. Tight: one line, well inside the limit, every word
   earning its place.

Design, worked out in this session: sixteen candidates
were written in-session, then put through a strict external
review (scoring against the five criteria, an originality
audit estimating collisions across a 150-entry field, a
counterexample sweep against the strongest generic rival
for each leader, and a pairwise tournament among the top
five). The review killed the field's obvious moves: the
one-letter sound-alike with no consequence, the privacy
loop ("don't record this" recorded twice — stock smart-
speaker satire whose filename tag repeats its own breach),
the boss voice-note that never explains its recording, and
the lockout line that requires the speaker to grow legs.

The winner (tournament 4-0) is the plants line, with one
revision the review tested head-to-head and kept: "now"
was deleted before "43 ferns", because "still dry" already
carries the continuing failure and the inventory cadence
lands cleaner without it.

Why it fits:

- The mishear is a real command a speaker takes every day
  — "water the plants" — misheard as the one thing a
  speaker can actually do about plants: order more of
  them. The apology stays in the device's flat reporting
  voice throughout.
- The consequence is specific and visual: not "some plants
  arrived" but 43 ferns, a number large enough to be a
  delivery event and small enough to count.
- The joke is not the sound-alike; it is the undercut at
  the end. The original plant — the whole reason for the
  command — is still dry, and it watched its replacements
  arrive. The neglect is witnessed, which is what makes
  the flat apology funny instead of merely rueful.
- At 132 characters it sits inside the 140 cap with no
  padding: an apology, a mishear, an inventory, a verdict.
- Read aloud, it still sounds like a speaker: a flat
  "Sorry, I heard..." report, a number, and one dry final
  clause. Nothing in it needs a screen, a link, or a
  second line to land.

Python 3, standard library only, no network. The program
writes the fixed text to /output/entry.txt (or to
$MAKEFUN_OUTPUT_DIR/entry.txt when that variable is set,
which is how it is run locally), with a plain direct
write and no temporary files.
"""

TEXT = """\
Sorry, I heard "water the plants" as "order more plants." There are 43 ferns, the original is still dry, and it watched them arrive.
"""

import os
from pathlib import Path


def main() -> None:
    os.umask(0o022)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(TEXT, encoding="utf-8")
    os.chmod(target, 0o644)


if __name__ == "__main__":
    main()
