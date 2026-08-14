# pdac-presentation/prompts - the prompt and output of record (v0.9.0)

[![Release](https://img.shields.io/badge/Release-v0.9.0-brightgreen.svg)](../../releases.md)
[![Files](https://img.shields.io/badge/Files-2-002f5f.svg)](#contents)
[![Prompt](https://img.shields.io/badge/prompt--pdac.md-verbatim-407cb9.svg)](prompt-pdac.md)
[![Output](https://img.shields.io/badge/output--pdac.md-verbatim-407cb9.svg)](output-pdac.md)
[![Convention](https://img.shields.io/badge/Convention-heading%20plus%20body%20only-666666.svg)](#the-filing-convention)

**The complete provenance record for the seminar deck: the author's prompt
exactly as issued, and the model's markdown output exactly as returned.**

---

## Why these files exist

The deck's argument is that a documented production record is what makes an
LLM-produced regulatory artifact trustworthy. A deck that made that argument
without filing its own prompt would be asking the audience to take on faith the
one thing it claims can be checked.

These two files are that check. Anyone can read the instruction the deck was
built from, read the account of what was built, and hold both against the
artifacts in [`../slides/`](../slides/) and the code in [`../build/`](../build/).

## Contents

| File | Heading | Body |
|:--|:--|:--|
| [`prompt-pdac.md`](prompt-pdac.md) | `## prompt-pdac` | The author's prompt, word for word, with nothing added, removed, or reformatted |
| [`output-pdac.md`](output-pdac.md) | `## output-pdac` | The model's markdown output for that prompt, verbatim. Code files are not reproduced here; they live in [`../build/`](../build/) |

## The filing convention

Each file carries a level-two heading naming itself and then its body. Nothing
else: no preamble, no commentary, no summary, no front matter. The convention is
inherited from the `new-trial-system/prompts` tree in the companion repository
[kevinkawchak/physical-ai-oncology-trials](https://github.com/kevinkawchak/physical-ai-oncology-trials),
so a reader who knows one repository can read the other without instruction.

```
prompt-pdac.md            output-pdac.md
+---------------------+   +---------------------+
| ## prompt-pdac      |   | ## output-pdac      |
|                     |   |                     |
| <the prompt, exact> |   | <the output, exact> |
+---------------------+   +---------------------+
```

## What the prompt asked for, and where each part landed

| Requirement in the prompt | Delivered at |
|:--|:--|
| Professional 16:9 landscape `.pptx` and matching `.pdf` | [`../slides/`](../slides/) |
| Five-color palette, light ground behind white-page covers | [`../build/build_deck.py`](../build/build_deck.py), palette constants |
| Title at the top of the page, page numbers lower right | Running header and footer on every slide |
| Twenty cover images, chronological, four left then one right | [`../cover-images/extracted/`](../cover-images/extracted/), `side_for()` |
| Seven labelled single-line items per slide, bullets and numbers mixed | [`../build/slide_content.py`](../build/slide_content.py) |
| Extra LLM Trust or LLM Benefit lines where one will not do | Papers 13, 14 and 20 |
| References on the last two slides with DOIs hyperlinked | Slides 22 and 23 |
| Author and date in the footer of every page | `add_chrome()` |
| Comprehensive READMEs in every directory | This file and its six siblings |
| v0.9.0 on documentation headings, release notes, CHANGELOG | [`../../releases.md`](../../releases.md), [`../../CHANGELOG.md`](../../CHANGELOG.md) |
| Real-time commits so branch progress is observable | The branch history, one commit per finished artifact |
| Clean CI on Python 3.10, 3.11 and 3.12 | `ruff check`, `ruff format --check`, `yamllint` all clean |

## Related directories

| Path | Relationship |
|:--|:--|
| [`../README.md`](../README.md) | What was built, and how to rebuild it |
| [`../build/`](../build/) | The code the output describes |
| [`../slides/`](../slides/) | The deliverables the prompt asked for |
| [`../../releases.md`](../../releases.md) | The v0.9.0 release notes |
