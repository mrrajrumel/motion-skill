# Motion Skill for Claude 🎬✨

[![Created by Rumel Ahmed](https://img.shields.io/badge/Creator-Rumel%20Ahmed-FF5A1F?style=for-the-badge&logo=github&logoColor=white)](https://github.com/mrrajrumel)
[![GitHub Repository](https://img.shields.io/badge/Repository-mrrajrumel%2Fmotion--skill-0B0B0B?style=for-the-badge&logo=github)](https://github.com/mrrajrumel/motion-skill)
[![Claude Skill](https://img.shields.io/badge/Claude-Agent%20Skill-7C3AED?style=for-the-badge&logo=anthropic&logoColor=white)](https://claude.ai)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](LICENSE)

An intelligent, production-grade motion graphics video toolkit designed for **Claude.ai** and **Claude Code**. 

Turn talking-head videos and transcripts into continuous, single-shape motion-graphic B-roll timed to the speaker's words, and perform 100% local subject rotoscoping/object separation with SAM 2.

Created by **[Rumel Ahmed](https://github.com/mrrajrumel)**.

---

## 🌟 Key Highlights

- **One Shape That Never Cuts**: Instead of jarring transitions, a single shape morphs size, corner radius, and color from state to state while content swaps with a soft motion blur.
- **Natural Cursor Dynamics**: Realistic cursor movement with easing curves, clicks, and drags that directly drives interface changes.
- **Spoken Word Sync**: Every beat, morph, and indicator lands precisely on spoken words from your SRT transcript.
- **Cinematic Motion Blur**: 4 subframes per frame across a 180° shutter rendered via Playwright and blended with `ffmpeg tmix`.
- **ProRes 4444 Alpha Panels**: Render transparent overlay panels (`.mov`) that float in the empty space beside the speaker (e.g., Picture-in-Picture).
- **Local SAM 2 Object Separation**: Isolate products, people, or hands using Meta's Segment Anything Model 2 locally on your GPU/CPU with zero cloud uploads.

---

## 📂 Repository Structure

```text
motion-skill/
├── SKILL.md                     # Claude agent skill definition & workflow router
├── README.md                    # Documentation & Claude.ai setup guide
├── workflows/
│   ├── broll.md                 # Step-by-step motion graphics B-roll workflow
│   └── object-separation.md     # Local SAM 2 video rotoscoping workflow
├── engine/
│   ├── base.css                 # Base stylesheet with embedded Geist fonts
│   ├── motion.js                # Core spring physics and motion engine (window.M)
│   ├── build.py                 # Fragment compiler (clip fragment → standalone HTML)
│   ├── render.js                # Playwright + ffmpeg 4x subframe video renderer
│   ├── beats.js                 # Contact sheet generator for keyframe validation
│   └── fonts/                   # Geist & Geist Mono embedded fonts (OFL)
├── scripts/
│   ├── setup.sh                 # Unix/macOS one-line environment setup
│   ├── setup.ps1                # Windows PowerShell environment setup
│   ├── inspect_video.py         # Video inspector (PiP detection, aspect ratio, fps)
│   ├── words.py                 # SRT transcript parser with word-level timestamps
│   ├── composite.py             # Automatic preview composite generator
│   └── make_pages.py            # Generates interactive viewer.html and compare.html
├── templates/
│   ├── viewer.html              # Interactive clip-by-clip review player
│   └── compare.html             # Synced side-by-side / wipe / stacked comparison
├── examples/
│   └── opus-aoe2/               # Complete reference project (6 clips + plan.json)
└── reference/
    └── engine-api.md            # Complete window.M engine API reference
```

---

## 🚀 How to Use on Claude.ai

You can use this skill on **Claude.ai** (Web Projects) or via **Claude Code** (Anthropic's terminal CLI agent).

---

### Method 1: Using Claude.ai Projects (Web Interface)

Claude Projects allows you to supply custom knowledge and instructions to Claude so it acts as your personal motion designer.

#### Step 1: Create a Project
1. Log in to [Claude.ai](https://claude.ai).
2. Click **Projects** in the left sidebar and click **Create Project**.
3. Name it: `Motion Graphics Producer` (or `Video B-Roll Skill`).

#### Step 2: Add Project Knowledge
Upload the following files from this repository into the **Project Knowledge** section:
- `SKILL.md`
- `workflows/broll.md`
- `workflows/object-separation.md`
- `reference/engine-api.md`
- `examples/opus-aoe2/plan.json` *(optional, for quality reference)*

#### Step 3: Set Custom Instructions
Paste the following into the **Project Instructions** box:

```text
You are an expert motion graphics director and developer using the Motion Skill toolkit created by Rumel Ahmed (https://github.com/mrrajrumel/motion-skill).

Follow the instructions in SKILL.md and workflows/broll.md strictly:
1. When given a transcript or video description, conduct a concise one-round interview (density, brand look, cutaway vs panel).
2. Propose a clip plan table with timestamps, lines covered, and shape interactions before writing code.
3. Once approved, write complete HTML clip fragments following reference/engine-api.md and output them as downloadable Claude Artifacts.
4. Adhere strictly to the design principles: one shape that never cuts, spring physics, Geist typography, warm gray palette (#E9E7E2), no generic transitions, and realistic cursor timing.
```

#### Step 4: Chat & Generate Motion Graphics
1. Start a new chat inside your project.
2. Provide your transcript (e.g., an `.srt` file or pasted text with timestamps) and describe your video.
3. Claude will:
   - Interview you about visual density and brand palette.
   - Propose an approved **Clip Plan Table**.
   - Generate the self-contained HTML fragments for each clip inside Claude Artifacts.
4. Download the generated `.html` fragments and place them in your local `motion/clips/` directory.

#### Step 5: Render Locally on Your Computer
Because browser sandboxes cannot execute `ffmpeg` or `playwright` directly, run the rendering step locally on your machine:

```bash
# 1. Compile fragments into self-contained HTML
python engine/build.py motion/dist motion/clips/*.html

# 2. Render each clip to 60fps MP4 with motion blur
NODE_PATH=./motion/node_modules node engine/render.js motion/dist/01-clip.html motion/out/01-clip.mp4 60

# 3. Create the review composite and comparison pages
python scripts/composite.py motion/plan.json motion/out/preview.mp4
python scripts/make_pages.py motion/plan.json motion/out/preview.mp4
```

Open `motion/out/compare.html` in any browser to review the synced side-by-side comparison with your original footage!

---

### Method 2: Using Claude Code (Terminal CLI)

If you use **Claude Code**, Claude can execute the Python and Node rendering scripts directly:

#### Step 1: Install the Skill
Clone this repository into your Claude skills directory:

```bash
# Global skills directory:
git clone https://github.com/mrrajrumel/motion-skill.git ~/.claude/skills/motion

# Or as a project-specific skill inside your video folder:
git clone https://github.com/mrrajrumel/motion-skill.git .claude/skills/motion
```

#### Step 2: Run Setup in Your Project
In your video project root:

```bash
# On macOS / Linux:
bash ~/.claude/skills/motion/scripts/setup.sh ./motion

# On Windows PowerShell:
powershell -ExecutionPolicy Bypass -File ~/.claude/skills/motion/scripts/setup.ps1 ./motion
```

#### Step 3: Run Claude Code
Place your video in `motion/work/source.mp4` and your transcript in `transcript.srt`. Then run:

```bash
claude
```

Prompt Claude:
> *"I have a talking-head video at `motion/work/source.mp4` and transcript at `transcript.srt`. Use the motion skill to create motion graphics B-roll for it."*

Claude will autonomously inspect the footage, present the plan, code the clips, inspect contact sheets, render the MP4s/MOVs, and generate the review pages.

---

## 🎨 The Two Core Workflows

### 1. Motion B-Roll (`workflows/broll.md`)

Turn talking-head footage into rich, animated visual demonstrations:

| Step | Action | Command / Output |
|---|---|---|
| **1. Setup** | Install Playwright & Chromium | `setup.sh` or `setup.ps1` |
| **2. Interview** | Determine density & branding | Ask user for palette, fonts, key points |
| **3. Inspection** | Detect PiP / speaker box & timings | `python scripts/inspect_video.py` |
| **4. Planning** | Map lines to UI interactions | Output approval table |
| **5. Building** | Write single-shape morph HTML | `python engine/build.py` |
| **6. Verification** | Contact sheet of still frames | `node engine/beats.js` |
| **7. Rendering** | Frame-by-frame 4x subframe blur | `node engine/render.js` (MP4 / ProRes MOV) |
| **8. Delivery** | Cut preview, synced comparison | `composite.py` + `make_pages.py` |

#### Visual Design Tokens:
- **Canvas**: `#E9E7E2` (warm studio gray)
- **Ink**: `#0B0B0B` (crisp dark contrast)
- **Accent**: `#FF5A1F` (energetic safety orange)
- **Panel Shapes**: `#F4F2EE` (for dark footage overlays)
- **Typography**: Geist (UI text) & Geist Mono (code, data, counters)

---

### 2. Local Object Separation (`workflows/object-separation.md`)

Isolate a subject (person, product, phone, hands) using **Meta SAM 2** without uploading any video to external servers:

1. **Hardware Auto-Detection**:
   - NVIDIA GPU (12GB+): `facebook/sam2.1-hiera-large`
   - Apple Silicon / NVIDIA (<12GB): `facebook/sam2.1-hiera-base-plus`
   - CPU-only fallback: `facebook/sam2.1-hiera-tiny`
2. **Coordinate Grid Selection**: Generates an initial frame overlay with coordinate grids so you or Claude can pick click points (`PTS = [[x, y]]`, `LBL = [1, 0]`).
3. **Chunked Memory Propagation**: Tracks subjects in 60-frame chunks for rock-solid stability even on modest hardware.
4. **Deliverables**:
   - `work/separated.mp4`: Video with green silhouette edge-glow overlay for instant validation.
   - `work/masks/subject/*.png`: Lossless per-frame alpha masks ready for your NLE editor (Premiere, DaVinci Resolve, Final Cut).

---

## 🛠️ Requirements & Prerequisites

- **Node.js**: v18.0 or newer
- **Python**: 3.10 or newer (with `numpy`)
- **FFmpeg**: Installed and available in PATH (with `prores_ks` support for ProRes 4444 transparent renders)
- **Playwright**: Installed via `setup.sh` / `setup.ps1` (`npx playwright install chromium`)
- **GPU (Optional)**: CUDA-enabled NVIDIA GPU or Apple Silicon for fast SAM 2 rotoscoping.

---

## 👨‍💻 Creator & Author

**Rumel Ahmed**
- GitHub: [@mrrajrumel](https://github.com/mrrajrumel)
- Repository: [https://github.com/mrrajrumel/motion-skill](https://github.com/mrrajrumel/motion-skill)

Feel free to open issues, submit pull requests, or share videos produced with this toolkit!

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
Embedded Geist fonts are licensed under the [SIL Open Font License 1.1](engine/fonts/OFL-Geist.txt).
