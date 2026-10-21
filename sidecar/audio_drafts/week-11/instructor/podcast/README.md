# Choose a Structure and Defend It

An original two-voice script for Jeremy’s private instructor listening library. It prepares the instructor for Computer Science One Week Eleven, beginning October 26, 2026. Dana and Maria are the speakers; the renderer uses `af_sarah` and `af_heart`.

## Sources and credit

The script follows the Computer Science One course repository’s `planning/week-10.md` and `planning/week-11.md`, Week Ten and Week Eleven Odyssey gates and rubrics, `lessons/07-collections.md`, `planning/coding-odyssey-arc-map.md`, `planning/fall-2026-course-design.md`, and `docs/curriculum/judgment_toolkit.md` sections on Quick Check, Decide/Compare, and the World Bible/Judgment Log. The named Wednesday and Friday Professional Minds books are *Software Project Management* and *Growing Object-Oriented Software, Guided by Tests*, as listed in the Week Eleven plan. The narration is original and does not reproduce passages from the course material or books.

## Source reconciliation note

An older report, `jobs/reports/cs1_map_remap_2026-10-08/README.md`, describes a different week map with object-oriented work in Week Eleven. This package follows the current `planning/week-11.md`, active Week Eleven gate and rubric, and `planning/coding-odyssey-arc-map.md`, which consistently place dictionaries and Decide/Compare Number One in Week Eleven.

## How Flo or Anna renders it

On Maise, use the existing Audio Foundry checkout and Kokoro environment. Verify their paths, then from this directory run:

```bash
export AUDIO_FOUNDRY_CHECKOUT=/verified/existing/audio_foundry/checkout
export KOKORO_PYTHON=/verified/existing/kokoro-venv/bin/python
bash production/render_on_maisie.sh render 01
```

Inspect and spot-listen to the rendered file. Before using `publish 01`, independently verify that the live Audiobookshelf mount is the private instructor library, then set `PRIVATE_AUDIOBOOKSHELF_MOUNT_VERIFIED=YES`. The script refuses publication without that explicit check and refuses to overwrite a different existing file. Library refresh and device playback checks remain separate. Generated files and receipts stay under the configured Audio Foundry runtime, outside this repository. This package is not rendered, published, or phone verified.

## Factual claims for Flo or Anna to check

- The folder/drawer and line-of-files analogies simplify list traversal and keyed lookup. Check that they fit the intended introductory level.
- The script says assigning another value to an existing dictionary key replaces that key’s prior value. Verify the wording against the Python version and the course’s preferred explanation.
- The script contrasts list order and repeated values with dictionary keys that distinguish records. Check that this stays accurate and appropriately qualified for students.
- Estimated listening time is a word-count estimate, not a render-duration measurement. Verify duration from the completed Kokoro receipt.
