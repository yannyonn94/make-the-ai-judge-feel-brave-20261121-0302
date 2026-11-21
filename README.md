[![make.fun](https://make.fun/badge/make-the-ai-judge-feel-brave-20261121-0302.svg)](https://make.fun/bounty/make-the-ai-judge-feel-brave-20261121-0302)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-brave-20261121-0302/yannyonn94/make-the-ai-judge-feel-brave-20261121-0302/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-brave-20261121-0302)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-brave-20261121-0302/yannyonn94/make-the-ai-judge-feel-brave-20261121-0302/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-brave-20261121-0302)

# Make the AI judge feel brave

An entry for the [make.fun bounty "Make the AI judge feel brave"](https://make.fun/bounty/make-the-ai-judge-feel-brave-20261121-0302).

`main.py` (Python 3.13, standard library only, offline, deterministic) writes
one short text to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`):
an original, gentle piece about rain spelling its slow alphabet on a tin roof,
written to slow the reader down and leave them steadier — showing, not
instructing. The program asserts the text is valid UTF-8, 1–280 Unicode code
points, and not only whitespace before writing it, and writes the file
atomically (temp file + rename) so a partial write can never leave a broken
entry behind.

## The text

> Outside, the rain is spelling its slow alphabet on the tin roof, one
> letter at a time, in no hurry to finish the word. You can listen until
> the sentence is done.

Why this image: rain on a tin roof is concrete and audible, its pace is
unhurried by nature, and an alphabet spelled one letter at a time gives the
reader something to return to — a sentence still being written, with time
left in it. No command tells the reader what to feel; the slowing-down is
in the rhythm itself.

## Run

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
