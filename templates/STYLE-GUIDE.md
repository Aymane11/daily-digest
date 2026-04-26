# DAILY DIGEST — Editorial Style Guide

> Style C · **Swiss Editorial Zine** · grid-driven, numbered sections, mono metadata,
> ink-black + paper-cream + red accent + yellow highlight + teal/navy/ochre/slate accents.

This guide explains how to **respect the design**, **pick the right story
template**, and **populate** every section. Read the **Design DNA**
section first — it is the rulebook everything else inherits from.

---

## 1 · DESIGN DNA — the non-negotiables

### 1.1 Color
Use ONLY these tokens. No new colors. No gradients.

| Token       | Hex       | Use                                                   |
|-------------|-----------|-------------------------------------------------------|
| `--paper`   | `#f5f0e8` | Page background — warm white. Never use as text color. |
| `--card`    | `#fffdf7` | Card / surface background.                            |
| `--ink`     | `#111111` | All text + rules + dark surfaces.                     |
| `--ink-2`   | `#5a5a5a` | Muted metadata only (never headlines or body).        |
| `--accent`  | `#d62828` | Vivid red — section numbers (01/02/...), kickers, "today" markers. Never body copy. |
| `--hi`      | `#f5c842` | Bright gold — highlight blocks (Quote of the Day, stat slabs, voice card #1). |
| `--teal`    | `#0d7377` | Vivid teal — source links, archive links, HL2 border/stamp, voice card 2 accent. |
| `--navy`    | `#14213d` | Deep navy — HL1 stamp tags, secondary dark accent.   |
| `--ochre`   | `#e07b39` | Vivid ochre — HL3 border/stamp, voice card 3 accent, warm stories. |
| `--slate`   | `#3d5a80` | Vivid slate — HL4 border/stamp, cool secondary stamps. |
| `--sage`    | `#2d6a4f` | Vivid sage — tool visit links on dark backgrounds.   |
| `--purple`  | `#7b2d8b` | Purple — extra stamp color option.                   |

**Color use principles:**
- The four headline cards each get a distinct accent (accent/navy/teal/ochre/slate) for their left border and tag stamp.
- The three voice cards in Template C use yellow (voice 1), teal (voice 2), ochre (voice 3) as accent borders and quote glyphs — this makes perspectives visually distinct.
- Takeaways 01/02/03 in the "What it means" module use accent/teal/ochre for their left borders.
- Colors are for orientation, not decoration — each color should map to a consistent meaning.
- Do not mix colors randomly. Use them in the established role mapping.

**Inversion rule.** Black surfaces (Tools module, hero on data-first, opener
on modules) always pair with paper for body and yellow for kickers + numbers.
Never put red text on a black surface — it fails contrast and dilutes the accent.

### 1.2 Type
- **Display + body:** `Lora` — serif, weights 400/600/700, italic available. Base body size 18px, line-height 1.6–1.65.
- **Mono / metadata:** `IBM Plex Serif` — *only* for kickers, tags, captions,
  timestamps, author lines, breadcrumbs, "BY THE NUMBERS" labels. ALWAYS in
  UPPERCASE with `letter-spacing: 1.5–3px`; font-weight 500–600.
- **Script accent:** `Playfair Display` — italic, *only* for the deck-line on the dark hero
  (story-page) and the giant `"` quote glyph. Sparingly.

### 1.3 Hierarchy & scale
| Level                          | Desktop    | Mobile     | Notes                                |
|--------------------------------|------------|------------|--------------------------------------|
| Mega stat (story page)         | 64–96 px   | 44–56 px   | Always paired with mono label.       |
| Lead headline (homepage 01)    | 46 px      | 32 px      | Max 3 lines.                         |
| Story headline (story page)    | 46–60 px   | 28–36 px   | Max 3 lines, `text-wrap: balance`.   |
| Section / module title         | 18–24 px   | 18 px      | Always preceded by red `01/02/...`.  |
| Body copy                      | 18 px      | 16–17 px   | `line-height: 1.6–1.65`.            |
| Kicker / mono labels           | 11–13 px   | 10–11 px   | UPPERCASE, letter-spaced.            |

### 1.4 Grid
- 12-column grid, **24 px gutter**, 32 px page padding (14 px on mobile).
- Every multi-column grid must carry the responsive class: `sk-homepage-grid`, `sk-grid-dossier`, `sk-grid-data`, `sk-grid-brief`, `sk-grid-tool`, `sk-grid-modules`, `sk-grid-headlines`.
- Mobile (≤640px): all grids collapse to single column.
- Module headers ALWAYS show `<accent number>` + `<mono title>` left, +
  optional mono right-meta. Followed by a thin rule.
- Every module is wrapped in `.sk-box` (1.5 px ink border) — borders are the
  visual scaffolding. Don't replace with shadows.

### 1.5 Numbering ritual
Every page is structured as numbered modules:
- **Homepage:** `01 LEAD`, `02 TOP HEADLINES`, `03 QUICK BRIEFS`, `04 TOOLS`.
- **Story page:** modules `01`–`05` (Modules layout) or `¶ 01`–`¶ 03` (Dossier
  / Data-first paragraph markers).
- Headlines on the homepage get sub-refs: `02.1`, `02.2`, `02.3`, `02.4`.
  Briefs get `03.1`–`03.6`. Tools get `04.1`–`04.4`. **These IDs become the
  story-page `FILE_REF` value** — wire them up.

### 1.6 Stamp tags
Use `.sk-stamp` with a color modifier class instead of plain border boxes for all story and headline tags.

```html
<span class="sk-stamp sk-stamp--red">AI · MODELS</span>
<span class="sk-stamp sk-stamp--navy">OPEN SOURCE</span>
<span class="sk-stamp sk-stamp--teal">RESEARCH</span>
<span class="sk-stamp sk-stamp--ochre">SECURITY</span>
<span class="sk-stamp sk-stamp--slate">INFRA</span>
<span class="sk-stamp sk-stamp--hi">TOOL</span>   ← on dark backgrounds only
<span class="sk-stamp sk-stamp--ink">PAPER</span>
```

Stamps are slightly rotated (`rotate(-1deg)`) — this is intentional and part of the editorial handmade feel.
**Each headline card and stamp should use a consistent color:** HL1 → navy, HL2 → teal, HL3 → ochre, HL4 → slate.

### 1.7 Source attribution — always visible
Every story page must show the original source as a **clickable, styled link**:
- In the header metadata line: `SOURCE · {{SOURCE_LABEL}} ↗` (color: `--teal` or `--sage` on dark bg)
- In a dedicated source bar at the bottom of the article body
- Use class `.sk-src-link` or inline the teal color + underline style

For Hacker News stories, show **both**:
1. Link to the original article: `SOURCE · {DOMAIN} ↗`
2. Link to HN discussion: `HN DISCUSSION · {POINTS} PTS ↗`

Format: `SOURCE · SIMONWILLISON.NET ↗` (all caps, `IBM Plex Serif`, teal color, underlined)

### 1.8 Archive access
Every page must have an archive link:
- **Masthead (homepage):** `ARCHIVE ↗` link inside the nav bar (color: `--sage`)
- **Breadcrumb (story pages):** `ARCHIVE ↗` on the right end of the nav row (color: `--teal`)
- **Colophon (homepage footer):** `← ALL ISSUES · ARCHIVE` link (color: `--teal`)
- Archive page path: `../../archive.html` from issues/{NNN}/, `../../../archive.html` from stories/

### 1.9 The 5 things you may NEVER do
1. **No emoji.** Use mono symbols (`★`, `→`, `↗`, `←`, `¶`, `·`) only.
2. **No drop shadows or rounded corners > 0**. The aesthetic is flat and ruled.
3. **No new fonts** outside Lora / IBM Plex Serif / Playfair Display.
4. **No body text in `--accent`** — red is reserved for numbers + kickers + accent markers.
5. **No image placeholder (`.sk-img`)** in the lead section of homepage or the hero slots of story templates — these have been removed. Keep `.sk-img` only if you are explicitly adding an image somewhere.

---

## 2 · TEMPLATE FILES

| File                              | Purpose                                              |
|-----------------------------------|------------------------------------------------------|
| `daily-digest.css`                | Shared styles + tokens. Link from every page.        |
| `01-homepage.html`                | Issue homepage. One per issue.                       |
| `02-story-dossier.html`           | Story type **A** — research dossier                  |
| `03-story-data-first.html`        | Story type **B** — data-first feature                |
| `04-story-modules.html`           | Story type **C** — numbered modules deck             |
| `05-story-brief.html`             | Story type **D** — quick brief (compact summary)     |
| `06-story-tool.html`              | Story type **E** — tool/resource (hands-on summary)  |

All six files share the same CSS file. Editing tokens in
`daily-digest.css` propagates everywhere.

---

## 3 · WHICH STORY TEMPLATE TO USE

The story templates aren't stylistic alternatives — they're
**different shapes for different stories**. Pick by content type, not vibe.

### A · Dossier — `02-story-dossier.html`
**Use for:** funding rounds, M&A, company / product launches, anything where
the reader wants the **facts in a glance + a deeper read alongside**.

**Picks itself when you can answer ALL of these:**
- Is there a single dominant entity (company / product / model)?
- Are there ≥ 3 hard numbers worth surfacing (valuation, multiples, %)?
- Are there ≥ 2 named players (companies / investors / people)?
- Will most readers want the facts, not the narrative?

**Example beats:** *"$2.4B Series C for Anthropic"*, *"OpenAI acquires Rockset"*,
*"Claude 5 launches with 200B params"*.

### B · Data-first — `03-story-data-first.html`
**Use for:** stories where **the numbers ARE the news**. Benchmarks, market
shifts, survey results, performance reports.

**Picks itself when:**
- The headline is meaningless without numbers (e.g. *"GPT-X scores 92% on..."*).
- You have 3 strong, comparable stats that share a common unit / category.
- The supporting narrative is short — readers came for the data.

**Example beats:** *"AI coding benchmarks H1 2026"*, *"VC funding hits record"*,
*"Inference costs drop 40% YoY"*.

### C · Modules — `04-story-modules.html`
**Use for:** **explainers, analysis pieces, deep dives**. Stories with a
beginning-middle-end shape and multiple angles.

**Picks itself when:**
- The story has ≥ 4 distinct facets (history, players, debate, implications).
- You have multiple voices (≥ 3 quotes from different perspectives).
- There's a timeline worth drawing.
- You want to give the reader chunked, scannable progress.

**Example beats:** *"How the EU AI Act rewrites Big Tech"*, *"The fight over
synthetic data"*, *"What the chip ban means for 2026"*.

### D · Brief — `05-story-brief.html`
**Use for:** every Quick Brief (03.N) story. Compact 2-section layout: summary + why it matters.
Replaces external links — readers get the essentials without leaving the digest.
Stats sidebar optional — include if 1–2 hard numbers exist.

### E · Tool — `06-story-tool.html`
**Use for:** every Tool / Resource (04.N) story. Hands-on focused with step-by-step try-it instructions,
quick facts sidebar, direct tool link. Every tool entry gets its own dedicated page.

### Decision flowchart
```
Is this a Quick Brief (03.N)? ─→ D (Brief)
Is this a Tool/Resource (04.N)? ─→ E (Tool)
Is the story PRIMARILY a number / benchmark / report? ─→ B (Data-first)
Is the story about ONE entity with hard facts to surface? ─→ A (Dossier)
Otherwise (analysis, debate, multi-angle) ─→ C (Modules)
```

---

## 4 · POPULATING THE HOMEPAGE — `01-homepage.html`

The homepage is the table-of-contents for one issue. **One file per day.**
Replace every `{{TOKEN}}`. Drop a placeholder where you don't have data —
**do not delete the wrapping module.** Empty modules break the grid rhythm.

### 4.1 Masthead
| Token             | Format / rule                                    |
|-------------------|--------------------------------------------------|
| `ISSUE_NUMBER`    | Zero-padded 3-digit. `042`, `043`, `100`.        |
| `YEAR`            | `2026`.                                          |
| `ISO_DATE`        | `YYYY · MM · DD` with mid-dots.                  |
| `TOPICS`          | 1–3 short tags joined by ` · ` — e.g. `AI · TECH`. |
| `WEEKDAY`         | 3-letter UPPER — `MON`, `SAT`.                   |
| `DATE_SHORT`      | `MM · DD` — `04 · 25`.                           |
| `PUBLISH_TIME`    | `HH:MM UTC` — `06:00 UTC`.                       |
| `STORY_COUNT`     | Total stories in the issue. Integer.             |
| `NEXT_DATE`       | Tomorrow in `MM · DD` form.                      |

### 4.2 Module 01 — Lead (no image placeholder)
The biggest single-story slot. Pick the most important story of the day.
| Token                  | Rule                                                                  |
|------------------------|-----------------------------------------------------------------------|
| `LEAD_TAG_1`           | Primary topic stamp — e.g. `AI · MODELS`. Renders as `.sk-stamp--red`.|
| `LEAD_TAG_2`           | Secondary topic stamp. Renders as `.sk-stamp--navy`.                  |
| `LEAD_HEADLINE`        | 6–12 words, max 3 lines. Sentence case. **No clickbait.**             |
| `LEAD_DECK`            | One sentence (≤ 18 words) explaining the angle, in mono.              |
| `LEAD_BODY_PARAGRAPH`  | 2–3 sentences. The hook + the proof.                                  |
| `LEAD_AUTHOR`          | First-name LASTNAME. UPPERCASE in render.                             |
| `LEAD_READ_TIME`       | `N MIN`.                                                              |
| `LEAD_HREF`            | Relative path to the story file (e.g. `stories/02-1-anthropic.html`). |

### 4.3 Module 01 RAIL — Quote of the Day + Stats
| Token                                        | Rule                                                |
|----------------------------------------------|-----------------------------------------------------|
| `QUOTE_TEXT`                                 | 12–22 words, declarative, present tense.            |
| `QUOTE_SOURCE`                               | `FIRSTNAME LASTNAME · TITLE · COMPANY`.             |
| `STAT_N_VALUE` / `STAT_N_LABEL` (×3)         | Compact: `$ ##B`, `##×`, `##%`. Label ≤ 3 words.    |

### 4.4 Module 02 — Top Headlines (×4)
**Always exactly four.** If you have 5 stories, demote one to a brief.
For each `HL{n}` (n = 1..4):
- `HL{n}_TAG`: 1-2 word category — `AI · MODELS`, `STARTUPS · FUNDING`. Rendered as stamp.
- `HL{n}_HEADLINE`: 4–8 words, max 2 lines.
- `HL{n}_DEK`: One sentence, supporting the headline.
- `HL{n}_READ_TIME`: `N MIN`.
- `HL{n}_HREF`: Story file relative path.

Tag color mapping: HL1 → navy, HL2 → teal, HL3 → ochre, HL4 → slate. (Border color matches.)

### 4.5 Module 03 — Quick Briefs (×6)
Six items. Each brief links to its own **internal story page** (Template D).
Also provide `BRIEF{n}_SRC_HREF` for the clickable external source link shown inline.
- `BRIEF{n}_TEXT`: One declarative sentence (8–14 words). No headline case.
- `BRIEF{n}_META`: `SOURCE · TAG · N MIN`.
- `BRIEF{n}_HREF`: Internal story page path (e.g. `stories/03-1-gpt55.html`).
- `BRIEF{n}_SRC_HREF`: External source URL (shown as "SOURCE ↗" inline).

### 4.6 Module 04 — Tools / Resources (×4)
**Inverted (black) module.** Each tool links to its own **internal story page** (Template E).
Also provide `TOOL{n}_SRC_HREF` for the direct "VISIT SITE ↗" link.
- `TOOL{n}_NAME`: Product name.
- `TOOL{n}_CATEGORY`: 1-word category — `IDE`, `MODEL`, `EVAL`, `CLI`, `LIBRARY`, `FRAMEWORK`.
- `TOOL{n}_DESCRIPTION`: One sentence (≤ 14 words) explaining what it does.
- `TOOL{n}_HREF`: Internal story page path (e.g. `stories/04-1-deepseek-v4.html`).
- `TOOL{n}_SRC_HREF`: Direct tool URL.

---

## 5 · POPULATING STORY PAGES — shared tokens

These tokens appear in all story templates:

| Token             | Rule                                                                |
|-------------------|---------------------------------------------------------------------|
| `ISSUE_NUMBER`    | Same `042`-style as homepage.                                       |
| `FILE_REF`        | `02.1`, `02.2`… — **must match** the homepage headline ref.         |
| `TOPIC`           | Single-line topic — e.g. `AI / MODELS`.                             |
| `HEADLINE`        | 6–14 words, max 3 lines. Don't add a period.                        |
| `DECK`            | The angle in one sentence (≤ 22 words). Reads as italic/script.     |
| `AUTHOR`          | `FIRSTNAME LASTNAME` — render forces UPPER.                         |
| `DATE_LONG`       | `APR 25 · 2026 · 06:00 UTC`.                                        |
| `LOCATION`        | Optional dateline — `SF`, `LONDON`, `BERLIN`.                       |
| `READ_TIME`       | `N MIN`.                                                            |
| `SOURCE_HREF`     | URL of the original source article. Always required.                |
| `SOURCE_LABEL`    | Domain in CAPS — `SIMONWILLISON.NET`, `ARXIV.ORG`, `HN · 342 PTS`. |
| `TAG_1..3`        | Filing tags — rendered as `.sk-stamp` elements.                     |
| `PREV_HREF` / `PREV_REF` / `NEXT_HREF` / `NEXT_REF` | Cross-issue navigation.       |

**For Hacker News stories only** — add both source links:
- `SOURCE_HREF`: URL to the original article (not HN).
- `HN_HREF`: URL to the HN discussion page.
- `HN_POINTS`: Score at time of selection (integer).

### 5.1 Dossier-only tokens — `02-story-dossier.html`
- `TLDR_1..3`: Three bullets, each one sentence. Together they tell the
  whole story to a reader who reads nothing else.
- `BIG_STAT_1..3_VALUE` / `_LABEL`: 64-px numbers + mono label. Stat 1 should
  be the **most punchy** (shown in red). Stats 2 and 3 in ink.
- `PLAYER_1..2_NAME` / `_ROLE`: Named entity + their role in the story.
- `TAG_1..3`: Filing tags — use `.sk-stamp` with distinct colors.
- `STANDFIRST`: One paragraph (2 sentences) — the story's thesis.
- `BODY_PARAGRAPH_1..3`: Three short paragraphs (3-5 sentences each) under
  the `¶ 01 WHAT HAPPENED`, `¶ 02 WHY IT MATTERS`, `¶ 03 WHAT TO WATCH`
  headers. **Don't rename the headers — they're a fixed ritual.**
- `INLINE_STAT_VALUE` / `_LABEL`: A single dramatic number in a black band.
- `PULL_QUOTE` / `PULL_QUOTE_SOURCE`: Quote from a voice other than the main player.

### 5.2 Data-first-only tokens — `03-story-data-first.html`
- `BIG_STAT_1..3_VALUE` / `_LABEL` / `_CONTEXT`: Three matching stats.
  The `_CONTEXT` field is one short sentence explaining what the number means.
- `STATS_SOURCE`: e.g. `COMPANY FILING + INTERNAL DATA`, `MMLU LEADERBOARD`.
- `LEAD_PARAGRAPH`: One large-typeset paragraph that opens the body.
- `BODY_PARAGRAPH_1..3`: Same as Dossier.
- `T1..T4_YEAR` / `T1..T4_LABEL`: Compact 4-event timeline. T4 is "today".
- `PLAYER_1..2_NAME` / `_ROLE`: Same as Dossier.
- `PULL_QUOTE` / `PULL_QUOTE_SOURCE`: Set in the big yellow band.

### 5.3 Modules-only tokens — `04-story-modules.html`
- `STAT_1..4_VALUE` / `_LABEL` / `_NOTE`: Four stats on yellow slab.
- `T1..T4_YEAR` / `_LABEL` / `_DETAIL`: Visual horizontal timeline. T4 red = today.
- `VOICE_1..3_QUOTE` / `_TAG` / `_NAME`: Three quotes from different perspectives.
  Voice 1 on yellow, Voice 2 teal-accented, Voice 3 ochre-accented.
- `TAKEAWAY_1..3_HEAD` / `_BODY`: 3 implications. Takeaway 1 red, 2 teal, 3 ochre.
- `LINK_1..3_LABEL` / `_HREF`: 3 outbound links in FURTHER READING sidebar.

### 5.4 Brief-only tokens — `05-story-brief.html`
- `SUMMARY_PARAGRAPH`: 3–5 sentences. The complete story, no teasing.
- `WHY_IT_MATTERS`: 2–3 sentences. Implication + context.
- `WHAT_TO_WATCH`: 2–3 sentences. Forward-looking.
- `BRIEF_STAT_1..2_VALUE` / `_LABEL`: 1–2 stats for the sidebar (optional — omit box if no data).
- `SOURCE_META`: e.g. `HN · 342 PTS · APR 26 2026` or `PUBLISHED APR 26 2026`.

### 5.5 Tool-only tokens — `06-story-tool.html`
- `TOOL_NAME`: Product name.
- `TOOL_TAGLINE`: One punchy sentence (≤ 12 words) — what it does.
- `TOOL_CATEGORY`: Category stamp — `MODEL`, `CLI`, `LIBRARY`, `FRAMEWORK`, `EVAL`.
- `TOOL_AUTHOR`: Creator / company.
- `TOOL_LICENSE`: e.g. `MIT`, `APACHE 2.0`, `PROPRIETARY`.
- `TOOL_PREREQS`: What you need to run it (e.g. `Python 3.10+, API key`).
- `TOOL_URL`: Direct URL to the tool.
- `TOOL_URL_LABEL`: Short label for the URL — e.g. `GITHUB.COM/TOOL`.
- `TOOL_DOCS_URL`: Documentation URL.
- `TOOL_RELEASE_DATE`: e.g. `RELEASED APR 26 2026`.
- `WHAT_IT_IS`: 2–4 sentences. Clear, concrete, no hype.
- `WHY_IT_MATTERS`: 2–3 sentences. Context + implication.
- `STEP_1..N`: Numbered try-it steps. Copy-paste ready where applicable.
- `WHAT_TO_OBSERVE`: What success looks like; what to pay attention to.
- `THE_QUESTION`: One open question to answer through the experiment.
- `TRY_TIME`: Estimated minutes to try it (e.g. `20`).

---

## 6 · CONTENT VOICE

The deck-line, brief, and dek copy all live in this voice:
- **Smart but conversational.** Stratechery / Platformer / Morning Brew.
- Sentence case — never headline case.
- Active verbs. Present tense. No marketing speak ("revolutionary",
  "game-changing", "powerful" are banned).
- Numbers in copy: spell out one-through-nine, numerals from 10. Currency:
  `$2.4B`, `$200M`, never `2.4 billion`.
- Acronyms: introduce on first use, then OK to abbreviate.

---

## 7 · QUICK CHECKLIST — before you publish an issue

- [ ] One `01-homepage.html` per issue, in `issues/{ISSUE_NUMBER}/`.
- [ ] Each headline `02.N` links to a story file (Templates A, B, or C).
- [ ] Each brief `03.N` links to its own story file (Template D).
- [ ] Each tool `04.N` links to its own story file (Template E).
- [ ] Story `FILE_REF` matches its homepage anchor.
- [ ] Lead, Top Headlines (4), Quick Briefs (6), Tools (4) all populated.
- [ ] Every story page has a visible, clickable SOURCE link.
- [ ] HN stories show BOTH original article link AND HN discussion link.
- [ ] Archive link present in every masthead and story breadcrumb.
- [ ] Stamp tags used on all story pages and headline cards.
- [ ] No new fonts, no new colors, no emoji, no rounded corners.
- [ ] Mono labels are UPPERCASE with letter-spacing.
- [ ] Numbers are big. Labels are small. **Always.**
- [ ] No image placeholder (`.sk-img`) in lead or story hero slots.

— end of guide —
