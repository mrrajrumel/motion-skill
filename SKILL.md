---
name: motion
description: Motion-graphics toolkit for video. Two workflows. (1) B-roll - turn a talking-head video and transcript into continuous one-shape motion-graphic clips timed to the speaker's words (cutaways, overlays, panels). (2) Object separation - isolate a person, product or hand from the background in a video locally with SAM 2, outputting a green-highlighted video and per-frame masks. Use when someone gives a video and asks for motion graphics, B-roll, animated cutaways or overlays, or asks to separate, isolate, cut out or rotoscope a subject.
---

# Motion

One skill, two workflows. `$SKILL` means this skill's folder. Pick the workflow from the request, read its file fully, then follow it.

| The user wants... | Read |
|---|---|
| Motion graphics, B-roll, animated cutaways or overlays for a video | `$SKILL/workflows/broll.md` |
| To separate / isolate / cut out / rotoscope a subject in a video | `$SKILL/workflows/object-separation.md` |

If the request needs both (for example, separate a product, then build B-roll around it), run object separation first. Its masks stay in `work/masks/subject/`, so B-roll can start from them without separating again.

If it is unclear which one the user means, ask one short question.

## Folder map

- `workflows/`: the step-by-step instructions for each workflow.
- `engine/`, `scripts/`, `templates/`, `examples/`, `reference/`: used by the B-roll workflow. Read `reference/engine-api.md` before writing the first clip.

All paths written as `$SKILL/...` inside the workflow files resolve against this folder.
