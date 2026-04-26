# DAILY DIGEST — Editorial Style Guide

> Style C · **Swiss Editorial Zine** · grid-driven, numbered sections, mono metadata,
> ink-black + paper-cream + red accent + yellow highlight.

This guide explains how to **respect the design**, **pick the right story
template**, and **populate** every section. Read the **Design DNA**
section first — it is the rulebook everything else inherits from.

---

## 1 · DESIGN DNA — the non-negotiables

### 1.1 Color
Use ONLY these four. No new colors. No gradients.

| Token       | Hex       | Use                                                   |
|-------------|-----------|-------------------------------------------------------|
| `--paper`   | `#ece7dc` | Page background. Never use as text color.             |
| `--card`    | `#faf7f0` | Card / surface background.                            |
| `--ink`     | `#0d0d0d` | All text + rules + dark surfaces.                     |
| `--ink-2`   | `#6a6a6a` | Muted metadata only (never headlines or body).        |
| `--accent`  | `#c0392b` | Section numbers (01/02/...), kickers, "today" markers, accent links. **No accent text larger than ~64px** and never used for body copy. |
| `--hi`      | `#ffe89a` | Highlight blocks (Quote of the Day, stat slabs on yellow, voice card #1). |

**Inversion rule.** Black surfaces (Tools module, hero on data-first, opener
on modules) always pair with paper for body and yellow for kickers + numbers.
Never put red text on a black surface — it fails contrast and dilutes the
accent.

### 1.2 Type
- **Display + body:** `Kalam` — used for everything readable, weights 400/700.
- **Mono / metadata:** `Special Elite` — *only* for kickers, tags, captions,
  timestamps, author lines, breadcrumbs, "BY THE NUMBERS" labels. ALWAYS in
  UPPERCASE with `letter-spacing: 1.5–3px`.
- **Script accent:** `Caveat` — *only* for the deck-line on the dark hero
  (story-page) and the giant `"` quote glyph. Sparingly.

### 1.3 Hierarchy & scale
| Level                          | Size       | Notes                                  |
|--------------------------------|------------|----------------------------------------|
| Mega stat (story page)         | 64–96 px   | Always paired with mono label.         |
| Lead headline (homepage 01)    | 36 px      | Max 3 lines.                           |
| Story headline (story page)    | 44–56 px   | Max 3 lines, `text-wrap: balance`.     |
| Section / module title         | 18–24 px   | Always preceded by red `01/02/...`.    |
| Body copy                      | 14–15 px   | `line-height: 1.5–1.6`.                |
| Kicker / mono labels           | 10–11 px   | UPPERCASE, letter-spaced.              |

### 1.4 Grid
- 12-column grid, **24 px gutter**, 28 px page padding.
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

### 1.6 The 5 things you may NEVER do
1. **No emoji.** Use mono symbols (`★`, `→`, `↗`, `←`, `¶`, `·`) only.
2. **No drop shadows or rounded corners > 0**. The aesthetic is flat and ruled.
3. **No new fonts** outside Kalam / Special Elite / Caveat.
4. **No body text in `--accent`** — red is reserved for numbers + kickers + accent markers.
5. **No image without a `FIG · NN · caption` line in mono below it.**

---

## 2 · TEMPLATE FILES

| File                              | Purpose                                              |
|-----------------------------------|------------------------------------------------------|
| `daily-digest.css`                | Shared styles + tokens. Link from every page.        |
| `01-homepage.html`                | Issue homepage. One per issue.                       |
| `02-story-dossier.html`           | Story type **A** — research dossier                  |
| `03-story-data-first.html`        | Story type **B** — data-first feature                |
| `04-story-modules.html`           | Story type **C** — numbered modules deck             |

All four files share the same CSS file. Editing tokens in
`daily-digest.css` propagates everywhere.

---

## 3 · WHICH STORY TEMPLATE TO USE

The three story templates aren't stylistic alternatives — they're
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

### Decision flowchart
```
Is the story PRIMARILY a number / benchmark / report? ─→ B (Data-first)
              │ no
              ▼
Is the story about ONE entity with hard facts to surface? ─→ A (Dossier)
              │ no
              ▼
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
| `PUBLISH_TIME`    | `HH:MM PT` — `06:00 PT`.                         |
| `STORY_COUNT`     | Total stories in the issue. Integer.             |
| `NEXT_DATE`       | Tomorrow in `MM · DD` form.                      |

### 4.2 Module 01 — Lead
The biggest single-story slot. Pick the most important story of the day.
| Token                  | Rule                                                                  |
|------------------------|-----------------------------------------------------------------------|
| `LEAD_HEADLINE`        | 6–12 words, max 3 lines. Sentence case. **No clickbait.**             |
| `LEAD_DECK`            | One sentence (≤ 18 words) explaining the angle, in mono.              |
| `LEAD_BODY_PARAGRAPH`  | 2–3 sentences. The hook + the proof.                                  |
| `LEAD_AUTHOR`          | First-name LASTNAME. UPPERCASE in render.                             |
| `LEAD_READ_TIME`       | `N MIN`.                                                              |
| `LEAD_HREF`            | Relative path to the story file (e.g. `stories/02-1-anthropic.html`). |
| `LEAD_CAPTION`         | Mono caption sentence — what the photo shows.                         |

### 4.3 Module 01 RAIL — Quote of the Day + Stats
| Token                                        | Rule                                                |
|----------------------------------------------|-----------------------------------------------------|
| `QUOTE_TEXT`                                 | 12–22 words, declarative, present tense.            |
| `QUOTE_SOURCE`                               | `FIRSTNAME LASTNAME · TITLE · COMPANY`.             |
| `STAT_N_VALUE` / `STAT_N_LABEL` (×3)         | Compact: `$ ##B`, `##×`, `##%`. Label ≤ 3 words.    |

### 4.4 Module 02 — Top Headlines (×4)
**Always exactly four.** If you have 5 stories, demote one to a brief.
For each `HL{n}` (n = 1..4):
- `HL{n}_TAG`: 1-2 word category — `AI · MODELS`, `STARTUPS · FUNDING`.
- `HL{n}_HEADLINE`: 4–8 words, max 2 lines.
- `HL{n}_DEK`: One sentence, supporting the headline.
- `HL{n}_READ_TIME`: `N MIN`.
- `HL{n}_HREF`: Story file relative path.

### 4.5 Module 03 — Quick Briefs (×6)
Six one-liners. **The template only includes one row** — duplicate the
`<a class="row gap-3">…</a>` block 5 more times for `03.2`–`03.6`.
- `BRIEF{n}_TEXT`: One declarative sentence (8–14 words). No headline case.
- `BRIEF{n}_META`: `SOURCE · TAG · N MIN`.
- `BRIEF{n}_HREF`: External or internal link.

### 4.6 Module 04 — Tools / Resources (×4)
**Inverted (black) module.** Same — duplicate the row block 3 more times.
- `TOOL{n}_NAME`: Product name.
- `TOOL{n}_CATEGORY`: 1-word category — `IDE`, `MODEL`, `EVAL`.
- `TOOL{n}_DESCRIPTION`: One sentence (≤ 14 words) explaining what it does.

---

## 5 · POPULATING STORY PAGES — shared tokens

These tokens appear in all three story templates:

| Token             | Rule                                                                |
|-------------------|---------------------------------------------------------------------|
| `ISSUE_NUMBER`    | Same `042`-style as homepage.                                       |
| `FILE_REF`        | `02.1`, `02.2`… — **must match** the homepage headline ref.         |
| `TOPIC`           | Single-line topic — e.g. `AI / MODELS`.                             |
| `HEADLINE`        | 6–14 words, max 3 lines. Don't add a period.                        |
| `DECK`            | The angle in one sentence (≤ 22 words). Reads as italic/script.     |
| `AUTHOR`          | `FIRSTNAME LASTNAME` — render forces UPPER.                         |
| `DATE_LONG`       | `APR 25 · 2026 · 06:00 PT`.                                         |
| `LOCATION`        | Optional dateline — `SF`, `LONDON`, `BERLIN`.                       |
| `READ_TIME`       | `N MIN`.                                                            |
| `HERO_CAPTION`    | One mono sentence describing the photo.                             |
| `PREV_HREF` / `PREV_REF` / `NEXT_HREF` / `NEXT_REF` | Cross-issue navigation.       |

### 5.1 Dossier-only tokens — `02-story-dossier.html`
- `TLDR_1..3`: Three bullets, each one sentence. Together they tell the
  whole story to a reader who reads nothing else.
- `BIG_STAT_1..3_VALUE` / `_LABEL`: 64-px numbers + mono label. Stat 1 should
  be the **most punchy** (shown in red). Stats 2 and 3 in ink.
- `PLAYER_1..2_NAME` / `_ROLE`: Named entity + their role in the story.
- `TAG_1..3`: 1-word filing tags.
- `STANDFIRST`: One paragraph (2 sentences) — the story's thesis. Treated as
  pull-quote sized text with a left red bar.
- `BODY_PARAGRAPH_1..3`: Three short paragraphs (3-5 sentences each) under
  the `¶ 01 WHAT HAPPENED`, `¶ 02 WHY IT MATTERS`, `¶ 03 WHAT TO WATCH`
  headers. **Don't rename the headers — they're a fixed ritual.**
- `INLINE_STAT_VALUE` / `_LABEL`: A single dramatic number that sits between
  ¶ 01 and ¶ 02 in a black band. Pick the most quotable number.
- `PULL_QUOTE` / `PULL_QUOTE_SOURCE`: A second quote from a different source
  than the inline stat.

### 5.2 Data-first-only tokens — `03-story-data-first.html`
- `BIG_STAT_1..3_VALUE` / `_LABEL` / `_CONTEXT`: Three matching stats — same
  unit family if possible (all $, all %, all ×). The `_CONTEXT` field is one
  short sentence explaining what the number means.
- `STATS_SOURCE`: e.g. `COMPANY FILING + INTERNAL DATA`, `MMLU LEADERBOARD`.
- `LEAD_PARAGRAPH`: One large-typeset paragraph that opens the body.
- `BODY_PARAGRAPH_1..3`: Same as Dossier.
- `T1..T4_YEAR` / `T1..T4_LABEL`: Compact 4-event timeline. T4 is "today".
- `PLAYER_1..2_NAME` / `_ROLE`: Same as Dossier.
- `PULL_QUOTE` / `PULL_QUOTE_SOURCE`: Set in the big yellow band.

### 5.3 Modules-only tokens — `04-story-modules.html`
- `STAT_1..4_VALUE` / `_LABEL` / `_NOTE`: **Four** stats (vs. three) — fits
  the wider yellow grid. Notes are one short sentence.
- `T1..T4_YEAR` / `_LABEL` / `_DETAIL`: Visual horizontal timeline. T4 is
  rendered in red.
- `VOICE_1..3_QUOTE` / `_TAG` / `_NAME`: Three short (≤ 16 word) quotes from
  different perspectives. `_TAG` is the role (`BUILDER`, `INVESTOR`,
  `CRITIC`); `_NAME` is the human + company. **Voice 1 sits on yellow.**
- `TAKEAWAY_1..3_HEAD` / `_BODY`: 3 implications. Head is one bold line,
  body is one explanatory sentence.
- `LINK_1..3_LABEL` / `_HREF`: 3 outbound links — *the paper, the filing,
  prior coverage* are good defaults.

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
- [ ] Each headline `02.N` links to a story file using template A, B, or C.
- [ ] Story `FILE_REF` matches its homepage anchor.
- [ ] Lead, Top Headlines (4), Quick Briefs (6), Tools (4) all populated —
      no empty modules.
- [ ] All images have a `FIG · NN · caption` mono line.
- [ ] No new fonts, no new colors, no emoji, no rounded corners.
- [ ] Mono labels are UPPERCASE with letter-spacing.
- [ ] Numbers are big. Labels are small. **Always.**

— end of guide —
