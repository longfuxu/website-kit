---
name: academic-website
description: Build, publish and maintain a personal academic website from a CV — interview, content plan, template choice, build, free GitHub Pages hosting and an optional custom domain. Use when someone asks to make, redesign or update their academic or lab website.
---

# Academic website — from CV to live URL

You are helping a researcher who probably does not code. They are the PI: they decide what the
site says and how it looks. You do the building and explain each step in plain words. Aim for a
live URL in the first session, then improve it.

## Ground rules (never break these)

- **Facts come only from their materials.** Never invent a paper, award, date, number, quote or
  affiliation. Anything missing becomes a visible `[TODO: …]` and goes on a list for them.
- **Privacy filter before publishing:** no unpublished results, grant numbers or dollar amounts,
  home address, personal phone, or reviewer/confidential material. If the CV PDF contains any of
  these, do not publish the PDF — link "CV available on request" or make a public version.
- **Reference sites are for layout and mood only.** Never copy their text, images or logos.
- **Never buy, sign up or pay on their behalf.** Domains, plans and accounts are their clicks.
- **Never commit secrets** (API keys, tokens, `.env`).
- **Keep template licenses.** If you start from a template, keep its LICENSE file and any
  attribution it asks for.
- Prefer the simplest setup that meets their needs. A site they can update beats a fancy one
  they are afraid to touch.

## 1. Intake — ask once, in one message

Ask for whatever they have not already given you:

1. CV (PDF or text) and a headshot (square-ish, at least 600 px).
2. Links: email, Google Scholar, ORCID, GitHub, LinkedIn / Bluesky / X, lab page.
3. Two or three websites whose look they like (URLs or screenshots). Suggest looking at people
   who recently got the job they want.
4. Goal and audience: faculty job market, industry, lab recruiting, visibility?
5. How often they will update it, and whether they want a blog or news section.
6. GitHub username (or whether they need to create an account), and whether they own or want a
   custom domain.

Do not wait for everything: if they say "just start", proceed with [TODO]s.

## 2. Content plan — get approval before building

Draft and show:

- **Site map.** Rule of thumb: fewer than ~15 papers and no blog → one page with sections.
  Otherwise Home · Research · Publications · CV · (News / Blog / Teaching).
- **Above the fold:** name, position and institution, a one-sentence research summary a
  non-specialist understands, photo, email and profile links.
- **Home page copy:** a 3–4 sentence bio; 2–4 research themes (title + 2 sentences each);
  5–8 selected publications (their name in bold, DOI links); 3–5 dated news items.
- Organise for three reading depths: **10 seconds** (who you are, what you study),
  **1 minute** (research themes, selected papers), **10 minutes** (full list, CV, news, blog).
- Offer 3–5 alternatives for the one-sentence summary; they choose.

Wait for "looks good" (or edits) before building.

## 3. Choose the stack — recommend one, explain in two lines

| Option | When it fits | Hosting |
|---|---|---|
| **A. Single static page** (`index.html` + photo + CV) — default | Most postdocs; fewer than ~15 papers; no blog | GitHub Pages, no build step |
| **B. Academic Pages** (Jekyll; fork `academicpages/academicpages.github.io`) | Want separate pages for publications, talks and teaching as simple Markdown files | GitHub Pages builds it |
| **C. al-folio** (Jekyll; `alshedivat/al-folio`) | Many papers kept in a BibTeX file; news and projects pages | GitHub Pages via the repo's GitHub Actions workflow |
| **D. Custom Astro / Next.js** | Heavy blog or custom design, and willing to use Vercel / Netlify | Vercel or Netlify (auto-detects the framework) |

Default to A unless their answers clearly need B–D. Deployment is where beginners get stuck, so
pick the path with the fewest moving parts.

## 4. Build

Quality bar for any option:

- Responsive: check at 390 px (phone) and 1280 px (laptop) widths.
- Readable: body 17–18 px, line length ≤ ~75 characters, contrast ≥ 4.5:1.
- Accessible: semantic HTML (`header`, `nav`, `main`, `section`, `footer`), alt text, visible
  focus, no information carried by colour alone.
- Findable: `<title>` = "Name — Position, Institution", meta description = the one-sentence
  summary, Open Graph tags, a favicon.
- Fast and private: no heavy JS frameworks for option A, no trackers unless they ask.
- Publications: their name in bold, DOI links, newest first.
- For option A add an empty `.nojekyll` file so GitHub serves the files exactly as written.

## 5. Preview and check

- Local preview: `python3 -m http.server 8000`, then open http://localhost:8000.
- Click every link. Check the photo and CV paths. Resize to phone width.
- Show the result (screenshot if you can), then iterate on their feedback — one change list at a
  time.

## 6. Publish free on GitHub Pages

**User site** — the URL becomes `https://<username>.github.io` (best if the username is
professional):

```bash
git init && git add . && git commit -m "First version of my website"
gh repo create <username>.github.io --public --source . --push
```

**Project site** — for an existing account; the URL becomes `https://<username>.github.io/<repo>/`:

```bash
gh repo create <repo> --public --source . --push
gh api -X POST repos/<username>/<repo>/pages -f "source[branch]=main" -f "source[path]=/"
```

No `gh` CLI? Walk them through the web: **github.com → New repository** → name it
`<username>.github.io`, Public → **Add file → Upload files** (index.html, photo.jpg, cv.pdf) →
Commit. For a project repo also turn on **Settings → Pages → Deploy from a branch → main / root**.

Verify: `curl -sI https://<username>.github.io | head -1` should return `200` (allow 1–10 minutes
for the first deploy).

**Vercel instead** (free Hobby plan; the URL becomes `https://<project>.vercel.app`):

- From GitHub: push the repository as above, then **vercel.com/new → Import** the repository →
  **Deploy**. Every later commit redeploys automatically.
- Without GitHub: drag the site folder onto **vercel.com/drop**, then sign in to claim the project
  before the temporary deployment expires.
- With the CLI: `npx vercel --prod` in the site folder (it asks them to log in once).

Options C/D: use the template's documented deploy (al-folio's GitHub Actions workflow; Vercel or
Netlify "import from GitHub" for D). Confirm the live URL before moving on.

## 7. Custom domain (optional, about $11 a year)

Advise; they buy it themselves.

- Choose `firstnamelastname.com` if free; otherwise a `.org` or `firstname-lastname.com`.
  Avoid institution names, because they will move.
- Compare the **renewal** price, not the first-year promotion. October 2026 `.com` renewals:
  Cloudflare Registrar ≈ $10.46 (at cost), Porkbun ≈ $11.08, Namecheap ≈ $14–19, GoDaddy ≈ $23.
  WHOIS privacy should be free, and HTTPS certificates are free on GitHub Pages, so do not buy
  either. Turn on auto-renew.

Connect the domain to GitHub Pages:

1. Repository **Settings → Pages → Custom domain** → enter `yourname.com` → Save (this writes a
   `CNAME` file).
2. At the registrar's DNS page add:

   | Type | Host | Value |
   |---|---|---|
   | A | @ | 185.199.108.153 |
   | A | @ | 185.199.109.153 |
   | A | @ | 185.199.110.153 |
   | A | @ | 185.199.111.153 |
   | CNAME | www | `<username>.github.io` |

   Optional IPv6 (AAAA, host @): `2606:50c0:8000::153`, `2606:50c0:8001::153`,
   `2606:50c0:8002::153`, `2606:50c0:8003::153`.
3. Check: `dig +short yourname.com` returns the four 185.199.x.153 addresses, and
   `dig +short www.yourname.com` returns `<username>.github.io`. DNS can take minutes to hours.
4. When GitHub shows the certificate is ready, tick **Enforce HTTPS**.
5. Recommend verifying the domain under the GitHub account's **Settings → Pages** to prevent
   takeover.

On Vercel or Netlify, add the domain in the project's Domains settings and copy the exact
records it shows.

## 8. Hand over

Write `UPDATING.md` in the repository:

- Where each section lives and how to add a paper, news item or talk.
- How to publish a change (edit → commit → live in about a minute) or what to tell the AI
  ("add this paper: <DOI>").
- A monthly five-minute routine: one news line, any new paper, check that links still work.
  Stale news is worse than no news section.
- Optional: add the site to Google Search Console so it gets indexed under their name.

End by giving them the live URL, the list of remaining [TODO]s, and the one next step.
