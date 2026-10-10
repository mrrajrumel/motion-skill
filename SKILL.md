---
name: motion
description: Professional motion-graphics & video toolkit for Claude. Three core capabilities: (1) Standalone Motion Graphic Videos - generate continuous one-shape morphing explainer, product, and UI demo videos from a prompt or script. (2) Video B-roll - turn a talking-head video and transcript into continuous single-shape motion-graphic cutaways and transparent PiP overlay panels timed to the speaker's words. (3) Local Object Separation - isolate a person, product or hand locally with SAM 2, outputting a green-highlight preview video and lossless per-frame alpha masks. Supports commands like /motion, /broll, /separate.
---

# Motion

Created by **[Rumel Ahmed](https://github.com/mrrajrumel)** · [GitHub Repository](https://github.com/mrrajrumel/motion-skill)

Professional motion graphics and video editing skill for Claude.ai and Claude Code. `$SKILL` refers to this skill's root folder.

## Quick Command Dispatch

| Command / User Intent | Description | Workflow File |
|---|---|---|
| `/motion` or "Make motion video" | Create standalone 60fps motion graphic videos (explainers, SaaS UI demos, product highlights) from a script or prompt | `$SKILL/workflows/broll.md` (Standalone mode) |
| `/broll` or "Add B-roll to video" | Generate motion-graphic cutaways or transparent overlay panels synchronized to a talking-head video & transcript | `$SKILL/workflows/broll.md` (B-roll mode) |
| `/separate` or "Rotoscope / isolate subject" | Locally isolate a person, hand, or product with SAM 2 (GPU/CPU auto-detected, 100% private) | `$SKILL/workflows/object-separation.md` |

If the request combines workflows (for example, isolate a product with SAM 2, then build motion B-roll around it), run object separation first. Its per-frame alpha masks stay in `work/masks/subject/` so the motion engine can use them directly.

## Direct Use on Claude.ai & Claude Code

- **On Claude.ai (Web / Projects)**:
  - Upload this folder or project files (`SKILL.md`, `workflows/`, `reference/`) into your Project Knowledge.
  - Ask Claude: `/motion create a 20s explainer for our new feature` or `/broll here is my transcript.srt`.
  - Claude generates interactive HTML fragments in **Claude Artifacts** so you can preview them directly in your browser.
  - Run the local render scripts (`python engine/build.py`, `node engine/render.js`) to export final 60fps MP4 or ProRes 4444 `.mov` clips.

- **On Claude Code (Terminal CLI)**:
  - Clone or install into `~/.claude/skills/motion` or `.claude/skills/motion`.
  - Claude executes inspection, planning, fragment creation, beats checks, and video rendering autonomously.

## Folder Map

- `workflows/`: Step-by-step instructions for B-roll, standalone motion graphics, and SAM 2 rotoscoping.
- `engine/`: Core spring physics (`motion.js`), styles (`base.css`), compiler (`build.py`), subframe renderer (`render.js`), contact sheet generator (`beats.js`), and embedded Geist fonts.
- `scripts/`: Platform setup (`setup.sh`, `setup.ps1`), video inspection (`inspect_video.py`), transcript timing parser (`words.py`), composite generator (`composite.py`), and review page generator (`make_pages.py`).
- `reference/`: Complete `window.M` engine API documentation (`engine-api.md`). Read before authoring clips.
- `templates/`: Synchronized review player (`viewer.html`) and before/after comparison tool (`compare.html`).
- `examples/`: Full reference implementation (`examples/opus-aoe2/`).

All paths written as `$SKILL/...` resolve relative to this directory.
