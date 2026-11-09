# CV → website: an AI starter kit for academics

Hands-on material from the QB3 Postdoc Seminar (UC Berkeley, 9 November 2026). It turns a CV into a live academic website: an AI agent fills the al-folio template from your CV and publishes it free on GitHub Pages and Vercel. No coding needed. Live page: https://longfuxu.github.io/website-kit/

- **`index.html`**: the talk and the follow-along protocol in one page: ten slides (arrow keys to present) with a Copy button on every prompt and setting.
- **`agent-prompt.txt`**: the one prompt to paste into Claude Code or Codex (template + CV + photo → `name.github.io` and `name.vercel.app`).
- **`academic-website/SKILL.md`**: a skill for AI agents (Claude Code, Codex, the Claude app, or paste it into any agent) that interviews you, builds, deploys to GitHub Pages and connects a custom domain.

## Install the skill

| Tool | Put `SKILL.md` here |
|---|---|
| Claude Code | `~/.claude/skills/academic-website/SKILL.md` |
| OpenAI Codex | `~/.codex/skills/academic-website/SKILL.md` |
| Claude app (paid plans) | zip the `academic-website` folder and upload it under Settings → Skills |
| Anything else | paste it as your first message, or save it as `AGENTS.md` |

Then, in a folder with your CV and photo: *"Use the academic-website skill to build my site from cv.pdf."*

## Rebuild the page

`index.html` is generated: edit `src/site.src.html`, `agent-prompt.txt` or `academic-website/SKILL.md`, then run `python3 src/build.py`.

Prices and service details were checked in October–November 2026; confirm them before buying anything.

Prepared by Longfu Xu (Bustamante Lab, UC Berkeley) · longfuxu.com
