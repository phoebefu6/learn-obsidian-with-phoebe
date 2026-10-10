# Agent brief - shared by every fan-out page of learn-obsidian-with-phoebe

Filled from course-builder/references/agent-brief.template.md on 2026-10-10. Internal build
document: never link it from an audience page.

You are writing ONE static HTML session page. No servers, no npm. **If your target file already
exists on disk, do not write it; report that and stop.** Write the file, return its path and one
line of coverage. No HTML in your reply.

## Read first, in this order

1. The template page. Copy its structure, classes, SVG grammar and quiz markup EXACTLY, including
   how many options each question has (FOUR, "A · ..." to "D · ..."):
   `/Users/phoebe.fu/Documents/claude_work/github_repo/learn-obsidian-with-phoebe/courses/01-a-note-that-knows-its-neighbours.html`
   For rhythm you may also skim the bench page
   `/Users/phoebe.fu/Documents/claude_work/github_repo/learn-obsidian-with-phoebe/courses/04-the-link-bench.html`
2. The source map: every verified number, its evidence tier, per-session coverage, the seams, the
   bench canon. Use ONLY its numbers; never invent a statistic; if a fact is missing, teach the
   uncertainty.
   `/Users/phoebe.fu/Documents/claude_work/github_repo/learn-obsidian-with-phoebe/materials/official-course-map.md`
3. The stylesheet `:root` block (first 27 lines) for the palette tokens:
   `/Users/phoebe.fu/Documents/claude_work/github_repo/learn-obsidian-with-phoebe/assets/style.css`

## Page skeleton (keep every component)

toolbar (crumb EXACTLY `<a href="../index.html">learn-obsidian-with-phoebe</a> / Session N of 6`,
#toggle-all, #zoom-toggle) · masthead (eyebrow "Learn Obsidian with Phoebe · Session N of 6", h1
with one `<span class="accent">`, .sub, .chip-row with the level chip (🟡 Core for sessions 2 and 3,
🟠 Deeper for 5, 🔴 Advanced for 6), two .chip.audience chips and .chip.time "45 min", .agenda a1-a4 with flex
weights as in the template) · main.wrap · section#intro (Part 0 "Where we start": kicker, .lede,
.legend pills copied from the template, .callout.win "★ What you walk out with tonight.") · 3 Parts,
each `section.section#part-N` with section-kicker (klabel "Part N · covers ...", h2,
`.tag.concept "5 min live"`), a `.lede`, ONE figure, `details.card` accordions (summary:
`.mode.live` or `.mode.self`, title, `.mini`, `.caret ▶`), at least one `.callout.example` with
`span.ex-pill` "Real world" on the page · section#demo-1 Build-along (kicker klabel "Build-along",
h2, `.tag.demo "★ 22 min · everyone builds"`, .lede, ONE figure, `.steps > .step`, each step a `p`
then a `.prompt-box.good` carrying a `span.label` "★ Step N · ..."; 5 or 6 steps done in the learner's own
Obsidian vault, with Ines's notes as the worked example; show exact note text, front matter or
search strings in the boxes; any count from a vault says "your numbers will differ") · section#exercise Homework (ol, 4 items, tag
"30 min") · section#quiz (3 x `.quiz-q data-answer="0-based"`, `p.qtext`, FOUR `button.qopt`
"A · ..." to "D · ...", `p.qwhy`; one `p.quiz-score` after the last; vary the correct letter) ·
section#official, h2 EXACTLY "What this session teaches, and where it came from",
`.covered > .covered-row` (pill solid ✓ / light ◐ + name + note), then the `.mono` line EXACTLY
"Every fact on this page, and its verification tier, is recorded in the course's source map." ·
section.cheat#cheatsheet (h3 "Session N cheat sheet <span>· pin this</span>", .grid-2 of six
.cheat-item) · `.callout.next` with `.nx-pill` "Next session" (session 6: "Where next" pointing to
the course home and the hub) · footer.pagefoot · `<script src="../assets/app.js?v=2"></script>`.

Head: the template's social meta block with this page's own title/description/url (og:image stays
`https://phoebefu6.github.io/learn-obsidian-with-phoebe/assets/og-cover.png`);
`<title>Session N · <Title> - learn obsidian with phoebe</title>`;
`<link rel="stylesheet" href="../assets/style.css?v=2">`. Nothing else external.

First `details.card` in the FIRST Part is `open`; no other. Sentence case headings. Warm
practitioner voice, concrete, never dry. Inside prompt-boxes escape `&` `<` `>`. 450 to 650 lines
is guidance about depth, never a target: never collapse whitespace, dissolve a list into a
paragraph, or drop a component to fit.

## Hard rules (a violation is rework)

- NEVER an em dash or en dash, anywhere (prose, code, aria-labels, comments). Hyphen only.
- No meta text: never "this course", "in this course", "the course teaches", "banned here". State
  the professional norm directly with its reason. The two exact estate phrases above are the only
  self-references; "session 4" cross-references are fine.
- Attribution "by Phoebe Fu". Never "built with" a tool.
- Every number comes from the map or is labelled constructed. For constructed data print "your
  numbers will differ", never invented outputs as if run. Bench numbers are quoted only from the
  map's canon table and are always called "modelled".
- Contested or missing evidence: teach the disagreement; never resolve what the literature has not.
- Citations in the exact form of the map's appendix; anything marked reported is "reported" on the
  page; anything vendor is "a vendor's claim".
- NEVER "lottery" or "lotteries"; say the mechanism.
- Default to the English word. No Chinese terms are needed.
- Titles, widget ids and class names must not collide with siblings. Banned titles: "A system you
  keep", "The one-page marketing plan", "Is it worth the time?", "Where your week actually goes".
  Do not add new CSS classes or ids beyond those in the template; figure classes use your prefix.
- Tool facts: name ONLY Obsidian features listed in the map's O table (read at source 2026-10-09).
  Core plugins only on the core path; a community plugin may appear once as self-study, never as a
  required step. Say "check the current help" where a menu name matters; features change monthly.
- Obsidian-specific syntax only (wikilinks, embeds, block refs, properties/YAML, tags, search
  operators); general Markdown syntax links to the Markdown course instead of being taught.
- Seams, said out loud with absolute links where the page touches them:
  capture/PARA/review cadence -> https://phoebefu6.github.io/learn-pkm-with-phoebe/ ;
  reading technique, turning a text into notes by recall -> https://phoebefu6.github.io/learn-reading-with-phoebe/ ;
  radial mind maps -> https://phoebefu6.github.io/learn-mind-mapping-with-phoebe/ ;
  Markdown syntax -> https://phoebefu6.github.io/learn-markdown-with-phoebe/ ;
  databases for clients/projects/invoices -> https://phoebefu6.github.io/learn-notion-with-phoebe/ .
  Link format: `<a href="URL">Name ↗</a>`.

## Figure grammar (hand-drawn, every figure)

Palette, ONLY these hexes (no invented greys): ink `#3A3A46` · muted `#62616F` · violet primary
`#6741C4` · violet deep `#45288A` · violet mid `#5634A8` · violet soft `#DCD2F4` · violet 50 `#F5F1FD`
· faint `#D4D2DE` · hairline `#ECEAF3` · amber contrast `#A15C07` · amber ink `#6B3D04` · amber 50
`#FDF3E3` · `#FFFFFF` · universal reds `#991B1B` `#FEF2F2` `#FCA5A5` only for a wrong-way panel.

- `<figure class="zoomable">` > `<svg viewBox="0 0 880 H" xmlns="http://www.w3.org/2000/svg"
  role="img" aria-label="the data, not the shape">` > `<defs>` + `<style>` + content, then
  `<figcaption>🔍 Click to zoom - takeaway</figcaption>`. Grow H, never W.
- Prefix unique per figure, used for every class and id: `o<session><letter>`, e.g. o2a, o2b, o2c,
  o2d (build-along figure is d). Never reuse o1* or o4*.
- `<defs>` holds with prefix P: a wobble filter `id="PSk"` (`feTurbulence type="fractalNoise"
  baseFrequency="0.02" numOctaves="2" seed="<int>"` + `feDisplacementMap scale="2.4"
  xChannelSelector="R" yChannelSelector="G"`, `x="-3%" y="-3%" width="106%" height="106%"`), a
  hachure pattern `id="PHc"` (7x7 userSpaceOnUse, rotate(-38), one `#6741C4` line, opacity .5), an
  open arrowhead `id="PAr"` (path `M1 1 L9 5 L1 9`, fill none, stroke `#3A3A46` 1.6). ALL shapes sit
  inside ONE `<g filter="url(#PSk)" fill="none" stroke="#3A3A46" stroke-width="2"
  stroke-linecap="round" stroke-linejoin="round">`; rects carry a tiny rotation (-4 to 4 degrees for
  hand-placed items, under 1 for panels). Fills: white, `#F5F1FD`, the hachure for "the pile" or
  "the data", and amber (`#FDF3E3` fill, `#A15C07` stroke) ONLY for the one thing the figure is
  about. One doodle anchor per figure, simple strokes, never a mascot.
- Text classes, copy the template's `<style>` block: `.PH` 800 12px ink heading · `.PL` 600 12px
  ink label · `.PS` 400 11px muted · `.PB` 800 11px `#6B3D04` · `.PV` 800 13-18px `#45288A` value ·
  `.PA` 700 11px `#6741C4` axis caption · `.PN` 400 12px muted note. White text only on `#6741C4`
  or darker, via `style="fill:#FFFFFF"`.
- ALL `<text>` outside the filtered group, sans stack, never below 10.5px.
- Fit: max chars ≈ (box width - 20) / 7 at 12px, 6.4px/char at 11px; full-width note under 110
  chars; 40px between neighbouring point labels; bottom note 22px below the last row, H clears it by
  8px. No line, arrow or curve may cross a label (the gate flags line-through-text and
  text-out-of-box); hand-stacked rects must not overlap as painted rects. When in doubt, shorten.
- Floor: one figure per Part plus one in the build-along (4 figures). Draw the MECHANISM (what the
  outline names for each figure), never a metaphor literally, never decoration.

## Voice and honesty

Every Part gets a story; the "Real world" callout is a generic, recognisable pattern ("a familiar
pattern: a researcher who..."), never a named real person's private case and never Phoebe. Ines is
constructed: freelance user-research consultant, 4 active clients (Aldermoor Care, Brightwell
Mutual, Dunmore District Council, Corvid Studio), 1 part-time contractor (Theo). Say "constructed".
Use her note titles from the bench vault where useful (see session 1 and 4 pages: e.g.
"2026-09-15 Corvid interview P18", "Drop-off clusters at the first form that asks for an ID number",
"Notification fatigue", maps named "<Theme> (map)").
Luhmann facts only from the map's L table, with their tiers: Luhmann's essay and Schmidt 2018 are
"read"; Deutschlandfunk/Krajewski are "reported"; Ahrens and zettelkasten.de are "advocates";
Ahrens's book is "reported". Matuschak (A table) is read at source. "Map of content" origin (Nick
Milo) is "reported". Contested: "the slip box made Luhmann productive" and "the graph view is
your second brain": teach the disagreement as the map's section lays it out; never resolve. Never
say studies show linked notes help; say no controlled study was found. Bench numbers only from the
map's canon section, called "computed on a constructed vault".

## Footer chain and session titles

Footer left: `Session N of 6 · learn-obsidian-with-phoebe · by Phoebe Fu &nbsp;·&nbsp; 📚 <a href="https://phoebefu6.github.io/learn-with-phoebe/">Learn with Phoebe ↗</a>`
Footer right: `<a href="PREV">← Prev: <title></a> &nbsp;·&nbsp; <a href="NEXT">Next: <title> →</a>` (session 6: `← Prev` and `<a href="../index.html">Course home →</a>`).

Session titles (exact, sentence case, one accent span in h1) and files:
1 `01-a-note-that-knows-its-neighbours.html` A note that knows its neighbours ·
2 `02-atomic-notes-and-their-address.html` Atomic notes and the address they keep ·
3 `03-maps-of-content-not-folders.html` Maps of content, not folders ·
4 `04-the-link-bench.html` The link bench ·
5 `05-what-the-graph-view-is-telling-you.html` What the graph view is (and is not) telling you ·
6 `06-growing-the-vault-without-losing-the-thread.html` Growing the vault without losing the thread
