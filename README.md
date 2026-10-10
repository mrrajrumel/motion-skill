# Motion Skill: AI B-Roll Generator & Video Object Separation (SAM 2) for Agentic IDEs 🎬✨

[![Created by Rumel Ahmed](https://img.shields.io/badge/Creator-Rumel%20Ahmed-FF5A1F?style=for-the-badge&logo=github&logoColor=white)](https://github.com/mrrajrumel)
[![GitHub Repository](https://img.shields.io/badge/Repository-mrrajrumel%2Fmotion--skill-0B0B0B?style=for-the-badge&logo=github)](https://github.com/mrrajrumel/motion-skill)
[![Agent Skills](https://img.shields.io/badge/Agentic%20IDEs-Antigravity%20%7C%20Claude-7C3AED?style=for-the-badge&logo=anthropic&logoColor=white)](https://github.com/mrrajrumel/motion-skill)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](LICENSE)

> **Motion** is an AI agent skill that turns a talking-head video into **motion graphics B-roll** timed to the speaker's words, generates **standalone 60fps motion graphic explainer videos**, and **isolates any subject** (person, product, hand) from a video background using **Meta's SAM 2** — all running locally on your machine.

Works with agentic coding tools such as **Google Antigravity**, **Claude Code**, **Claude.ai** (Web Projects & Artifacts), and any agent that can read a `SKILL.md` file and run shell commands.

Created by **[Rumel Ahmed](https://github.com/mrrajrumel)** · [https://github.com/mrrajrumel/motion-skill](https://github.com/mrrajrumel/motion-skill)

---

**Keywords:** AI B-roll generator, motion graphics automation, standalone explainer video, video object segmentation, SAM 2 video masking, rotoscoping with AI, automatic video cutaways, animated overlays, talking-head video editing, YouTube video editing automation, Antigravity skills, Claude.ai skills, Claude Code skills, agent skills, SKILL.md.

---

## Table of Contents

- [What can you do with the Motion skill?](#what-can-you-do-with-the-motion-skill)
- [Workflow 1: AI B-Roll & Motion Graphics](#workflow-1-ai-b-roll--motion-graphics)
- [Workflow 2: Video Object Separation (Rotoscoping with SAM 2)](#workflow-2-video-object-separation-rotoscoping-with-sam-2)
- [Requirements](#requirements)
- [Installation Guide](#installation-guide)
  - [Installation in Google Antigravity](#installation-in-google-antigravity)
  - [Installation in Claude.ai (Web Projects)](#installation-in-claudeai-web-projects)
  - [Installation in Claude Code (Terminal CLI)](#installation-in-claude-code-terminal-cli)
- [How to command the skill (Prompt Examples)](#how-to-command-the-skill-prompt-examples)
- [Project structure](#project-structure)
- [Output files](#output-files)
- [FAQ](#faq)
- [License & credits](#license--credits)
- [Suggested GitHub repository settings (for SEO)](#suggested-github-repository-settings-for-seo)

---

## What can you do with the Motion skill?

| You want to... | Workflow | Result |
|---|---|---|
| Create standalone 60fps explainer, SaaS UI demo, or promotional motion videos from a script | **Standalone Motion Video** | Continuous single-shape morphing animation clips rendered with 4x subframe motion blur |
| Add animated cutaways, overlays or panels to a talking-head video | **B-roll** | Motion-graphic clips timed to spoken words, plus a preview video and comparison page |
| Cut a person, product or hand out of a video background | **Object separation** | Green-highlighted video plus a lossless mask PNG for every single frame |
| Separate a product, then build B-roll around it | **Both** | Separation runs first; B-roll reuses the saved masks without rerunning |

---

## Workflow 1: AI B-Roll & Motion Graphics

Generate **continuous, one-shape motion-graphic clips** for a creator's video. Each clip is a single shape that never cuts: it morphs its size, corners and colour between states while its content swaps with a short blur. A cursor drives the changes with real clicks and drags, and every change lands on a spoken word.

### Two Supported Modes:
1. **Video B-Roll Mode**: Synchronized to an existing talking-head video (`source.mp4`) and transcript (`transcript.srt`). Produces full-frame cutaways or transparent ProRes 4444 (`.mov`) overlay panels for Picture-in-Picture layouts.
2. **Standalone Motion Video Mode**: Generates a complete 60fps motion graphic explainer (product highlights, kinetic UI cards, terminal demos) directly from your prompt or script without needing raw footage!

### How it works:
1. **Setup** – Checks Node, Python 3 and ffmpeg; installs Playwright + Chromium locally into `motion/node_modules`.
2. **Interview** – Asks for your video, transcript (SRT/VTT), density (light / medium / heavy) and look (default palette or your brand).
3. **Inspect footage** – Reads resolution, fps and layout (full-frame speaker or picture-in-picture).
4. **Plan** – Shows a clip-by-clip table (timing, covered line, treatment, reason). **Nothing is built until you approve it.**
5. **Build** – Writes each clip as self-contained HTML following `reference/engine-api.md`.
6. **Check** – Renders still frames on key words with `engine/beats.js` and fixes layout problems.
7. **Render** – Frame-by-frame 4x subframe render with motion blur to MP4 (or ProRes 4444 `.mov` with alpha for transparent panels).
8. **Deliver** – Clips, `TIMING.md`, `preview.mp4`, `viewer.html`, `compare.html`.

**Design defaults:** Warm gray canvas `#E9E7E2`, ink `#0B0B0B`, one orange accent `#FF5A1F`, Geist and Geist Mono fonts. Your brand colours and fonts override these. No invented numbers, quotes or results.

---

## Workflow 2: Video Object Separation (Rotoscoping with SAM 2)

Isolate one subject from the background of a video using **SAM 2.1 (Segment Anything Model 2)**. Everything runs on your computer and nothing is uploaded to external clouds.

The skill scans your hardware and picks the right model automatically:

| Machine | Model | Download size |
|---|---|---|
| NVIDIA GPU with 12 GB+ VRAM | `sam2.1-hiera-large` | ~898 MB |
| NVIDIA GPU under 12 GB, or Apple Silicon | `sam2.1-hiera-base-plus` | ~323 MB |
| CPU only | `sam2.1-hiera-tiny` | ~156 MB |

> CPU-only runs work but are slow (about 5 seconds per frame). For long clips without a GPU, separate only the section you need.

**Output:** `work/separated.mp4` (subject highlighted in green edge glow) and `work/masks/subject/` (one mask per frame, white = subject).

---

## Requirements

- **Python 3.10+** (with `numpy`)
- **ffmpeg** (with `prores_ks` encoder if you want transparent panel clips)
- **Node.js 18+** (for Playwright rendering engine)
- Internet only for the first run (model and Playwright downloads)
- *Optional:* NVIDIA GPU (CUDA) or Apple Silicon (MPS) for accelerated SAM 2 object separation

---

## Installation Guide

### Installation in Google Antigravity

1. Clone this repository so the folder is named `motion` and contains `SKILL.md` at its top level:
   ```bash
   # Clone the repository
   git clone https://github.com/mrrajrumel/motion-skill.git motion
   ```

2. Place the folder in your Antigravity skills directory:
   - **Workspace (this project only):**
     ```bash
     mkdir -p .agent/skills
     cp -r motion .agent/skills/motion
     ```
   - **Global (all projects):** Copy into your Antigravity global configuration skills directory:
     - Windows: `C:\Users\<user>\.gemini\config\skills\motion\`
     - macOS/Linux: `~/.gemini/config/skills/motion/`
3. Refresh or start your agent session so Antigravity loads the skill.
4. Put your video (and transcript) in your project folder, or prompt the agent to create standalone motion graphics.

---

### Installation in Claude.ai (Web Projects)

You can upload this skill directly into [Claude.ai](https://claude.ai) Projects:

1. **Package the Skill Bundle**:
   ```bash
   python scripts/package_skill.py
   ```
   This generates `motion-skill-claude.zip`.
2. **Create a Claude.ai Project**:
   - Go to [Claude.ai](https://claude.ai) → **Projects** → **Create Project**.
   - Name it: `Motion Graphics Studio`.
3. **Upload Knowledge**:
   - Upload `motion-skill-claude.zip` (or upload `SKILL.md`, `workflows/`, and `reference/engine-api.md`).
4. **Set Custom Instructions**:
   - Paste the following prompt into the Project Instructions box:
     ```text
     You are a Motion Graphics Producer using the Motion Skill created by Rumel Ahmed (https://github.com/mrrajrumel).
     Follow SKILL.md strictly. You support standalone motion graphics (/motion), B-roll cutaways (/broll), transparent PiP panels (/panel), and SAM 2 rotoscoping (/separate). Produce pure single-shape morphing clips using Geist typography and warm studio palettes. Output interactive HTML artifacts for live browser preview.
     ```
5. **Use Commands in Chat**:
   - Type `/motion` or `/broll` with your idea or transcript! Claude renders live interactive previews inside Claude Artifacts.

---

### Installation in Claude Code (Terminal CLI)

Install as a native Claude agent skill:

```bash
# Global installation:
git clone https://github.com/mrrajrumel/motion-skill.git ~/.claude/skills/motion

# Or project-specific installation:
git clone https://github.com/mrrajrumel/motion-skill.git .claude/skills/motion
```

Run one-time setup:
```bash
# macOS / Linux:
bash ~/.claude/skills/motion/scripts/setup.sh ./motion

# Windows (PowerShell):
powershell -ExecutionPolicy Bypass -File ~/.claude/skills/motion/scripts/setup.ps1 ./motion
```

Then run `claude` and command the skill directly in the terminal!

---

## How to command the skill (prompt examples)

You do not run scripts manually. Describe what you want in plain English or use slash commands, and the agent follows the skill:

### Standalone Motion Videos

```
/motion Create a 20-second 60fps standalone motion graphic video explaining our new developer API:
- Scene 1: An API key pill morphs into an interactive authorization card.
- Scene 2: Terminal typing showing curl request and instant JSON response.
- Scene 3: Analytics latency bar springing down from 250ms to 8ms.
```

```
Use the motion skill to create a standalone product changelog video for version 2.0. No source video needed. Use 16:9 1920x1080 resolution.
```

### B-roll and motion graphics

```
Use the motion skill to make B-roll for my video at ./videos/intro.mp4.
The transcript is ./videos/intro.srt. Use medium density and my brand
colours: background #101010, accent #00C2FF.
```

```
/broll Add animated cutaways to my YouTube video. Light density,
only the strongest moments. Keep the first 5 seconds on my face.
```

```
Use motion to create a transparent panel overlay for the picture-in-picture
section of my video, from 0:20 to 0:45.
```

### Object separation

```
Use the motion skill to separate the product in clip.mp4 from the background.
Frames 0 to 89. The product is in the centre of the frame.
```

```
Isolate the hand holding the phone in demo.mp4 and give me the masks.
```

### Combined

```
Separate the bottle from the background in ad.mp4, then build B-roll
around it using the saved masks.
```

### Tips for better results:
- Always provide a **transcript (SRT or VTT)** for B-roll. Word timing drives the animation.
- State the **density** (light, medium, heavy) and your **brand colours** upfront to skip questions.
- Tell the agent which lines to **keep on your face** or which **real numbers** to show.
- For object separation, say what to **include and exclude** (for example, "leave out my fingers").
- Review the **plan table** before approving. This is the best moment to change the edit.

---

## Project structure

```text
motion/
├── SKILL.md                 # Entry point: routes the request to a workflow
├── README.md                # Full documentation & setup guide
├── LICENSE                  # MIT License
├── workflows/
│   ├── broll.md             # Motion graphics B-roll & standalone video workflow
│   └── object-separation.md # SAM 2 object separation workflow
├── engine/                  # Motion engine, base.css, build.py, render.js, beats.js, fonts (Geist, OFL)
├── scripts/                 # setup.sh, setup.ps1, package_skill.py, inspect_video, words, composite, make_pages
├── templates/               # viewer.html and compare.html
├── reference/
│   └── engine-api.md        # Complete window.M engine API reference
└── examples/
    └── opus-aoe2/           # Six finished example clips (quality reference)
```

---

## Output files

All deliverables are written to `motion/out/`:

| File | Purpose |
|---|---|
| `NN-name_XmYsZZ.mp4` / `.mov` | Individual clips named by timeline in-point |
| `TIMING.md` | File, in/out time, covered line, treatment, what is illustrative |
| `preview.mp4` | Your video with the clips cut in (for review) |
| `viewer.html` | Step through the clips one by one in your browser |
| `compare.html` | Original vs preview synced comparison (side-by-side, stacked, or wipe) |

> `preview.mp4` is for review. For the final edit, drop the clips into your own video editor to adjust timing, add transitions and mix audio.

---

## FAQ

**What is the Motion skill?**  
An agent skill (`SKILL.md` plus scripts) that automates motion-graphics videos, B-roll for talking-head videos, and AI-powered video object separation.

**Can I create standalone motion videos without a source video?**  
Yes! Use the standalone motion video mode (`/motion`) to generate complete 60fps explainer and promotional videos from any script or prompt.

**Does it upload my video anywhere?**  
No. B-roll rendering and SAM 2 separation both run 100% locally on your machine.

**Which editors can I use the clips in?**  
Any editor that imports MP4 or ProRes `.mov`: Premiere Pro, DaVinci Resolve, Final Cut Pro, CapCut and others.

**Do I need a GPU?**  
Not for B-roll or motion graphics. For object separation a GPU is much faster, but CPU works with the small model.

**Can I use my own brand colours and fonts?**  
Yes. Share colours, a logo or screenshots and the skill uses them instead of the defaults.

**Does it invent statistics?**  
No. It uses placeholders and labels from your transcript unless you provide real figures.

**How do I remove the object-separation setup?**  
Delete the `.object-separation` virtual environment folder and the cached models in `~/.cache/huggingface/hub/models--facebook--sam2.1-hiera-*`.

---

## License & credits

- **Creator**: Developed by **[Rumel Ahmed](https://github.com/mrrajrumel)** ([https://github.com/mrrajrumel/motion-skill](https://github.com/mrrajrumel/motion-skill)).
- **License**: [MIT License](LICENSE).
- **Fonts**: **Geist** and **Geist Mono** (SIL Open Font License, included in `engine/fonts/`).
- **Object separation**: Uses **SAM 2.1** from Meta AI via Hugging Face Transformers.
- **Rendering**: Uses **Playwright (Chromium)** and **ffmpeg**.

---

### Suggested GitHub repository settings (for SEO)

- **Repository name:** `motion-skill`
- **Description:** `AI agent skill: motion graphics B-roll generator and SAM 2 video object separation. Works with Google Antigravity & Claude.`
- **Topics:** `ai-agent`, `agent-skills`, `antigravity`, `claude-code`, `claude-ai`, `b-roll`, `motion-graphics`, `video-editing`, `sam2`, `segment-anything`, `rotoscoping`, `video-segmentation`, `youtube`, `automation`, `playwright`, `ffmpeg`
