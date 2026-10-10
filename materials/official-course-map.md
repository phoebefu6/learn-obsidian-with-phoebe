# Official course map - learn-obsidian-with-phoebe ("Obsidian & Linked Notes")

Internal build document (never linked from an audience page). Built 2026-10-09/10. Bucket `prod`,
d2, audience everyone, format project, single-track 6 x 45 min, running-project arc.
Running case: **Ines**, a FICTIONAL freelance user-research consultant (constructed; never Phoebe):
freelance, **4 active clients (Aldermoor Care, Brightwell Mutual, Dunmore District Council, Corvid
Studio), 1 part-time contractor (Theo)**. Same Ines, same facts, as learn-notion-with-phoebe (her
operations OS); here she is her research thinking: interview notes, reading notes, insights that
recur across clients. Every page says "constructed".

**Tool course: features change monthly. Re-verify the changelog before delivery.**
Obsidian help read 2026-10-09 from the official help source (repo `obsidianmd/obsidian-help`, the
Markdown that publishes help.obsidian.md, which now 301-redirects to obsidian.md/help/<slug>; last
help commit 2026-10-08). Latest release read: v1.14.4, published 2026-10-05 (GitHub
obsidianmd/obsidian-releases; obsidian.md/changelog lists 1.14.x).
Core plugins only on the core path; community plugins are self-study and never required.

## Evidence tiers

- **read** - fetched at source and the sentence or number was read there (date read 2026-10-09).
- **reported** - from a secondary page, journalism, or a summary; the primary was not read.
- **advocate** - read at source, but written by someone who teaches or sells the method. Used to
  teach the disagreement, never as proof.
- **constructed / modelled** - Ines, her vault, every bench number.

## Verified facts - Obsidian (all "read", help source, 2026-10-09)

| # | Fact | Help page |
|---|---|---|
| O1 | "Obsidian stores your notes as Markdown-formatted plain text files in a vault. A vault is a folder on your local file system, including any subfolders." Other editors can edit them; Obsidian refreshes on external changes | How Obsidian stores data |
| O2 | Each vault has a `.obsidian` configuration folder (hidden by default) for vault preferences; the help recommends not creating vaults within vaults because links may not be updated correctly | How Obsidian stores data |
| O3 | Obsidian keeps a local "metadata cache" that powers the Graph view and Outline; it can be rebuilt under Settings > Files and links | How Obsidian stores data |
| O4 | Link formats: Wikilink `[[Three laws of motion]]` or Markdown `[Three laws of motion](Three%20laws%20of%20motion.md)`; wikilinks are the default; disable "Use [[Wikilinks]]" for Markdown links | Internal links |
| O5 | A link to a note that does not exist yet creates the note on click; characters `# | ^ : %% [[ ]]` may not work in a link | Internal links |
| O6 | Heading links `[[Note#Heading]]`, `[[#` for same note, `[[## term` searches headings vault-wide; block links `[[Note#^37066d]]`; custom block ids "can only consist of Latin letters, numbers, and dashes"; block references "won't work outside of Obsidian" | Internal links |
| O7 | Display text `[[Example|Custom name]]`; for a reusable alternate name use an alias | Internal links, Aliases |
| O8 | Aliases go in the `aliases` property as a YAML list; linking via an alias writes `[[Artificial Intelligence|AI]]`; Backlinks finds unlinked mentions of aliases | Aliases |
| O9 | Embeds: `!` in front of an internal link; embed a note, a heading or a block (`![[Note#^id]]`); embedded content stays up to date when the source changes; images sized `|640x480` | Embed files |
| O10 | Backlinks core plugin: a backlink is a link from another note to this one; two sections, **Linked mentions** and **Unlinked mentions** (any unlinked occurrence of the note's name); options include show more context, sort, filter; "Backlink in document" shows them at the foot of the note | Backlinks |
| O11 | Outgoing links core plugin: **Links** (links in the active note) and **Unlinked mentions** (text matching the name or alias of another note); "click the button with the note's name" to make the link | Outgoing links |
| O12 | Properties: start a file with `---`; default properties `tags`, `cssclasses`, `aliases`; types Text, List, Number, Checkbox, Date, Date & time, Tags; a type assigned to a name applies vault-wide; hashtags in text properties do not create tags | Properties |
| O13 | Tags: `#tag` or `tags` property list; nested tags with `/` (`#inbox/to-read`); `tag:inbox` matches nested ones; letters, numbers, `_`, `-`, `/`; at least one non-numeric character (#1984 invalid); case-insensitive; no spaces | Tags |
| O14 | Search operators include `file:`, `path:`, `content:`, `tag:`, `line:`, `block:`, `section:`, `task:`, `task-todo:`, `task-done:`, plus `[property:value]`; `tag:#work` does not return `#myjob/work` | Search |
| O15 | Graph view: "Circles represent notes"; "Lines represent internal links"; more referencing notes make a node bigger; filters: Search files, Tags, Attachments, Existing files only, **Orphans** ("notes without any links"); groups by colour; forces (center, repel, link force, link distance); time-lapse animation by creation time | Graph view |
| O16 | Local graph: notes connected to the active note; depth slider, "Each level of depth will show notes connected to the notes revealed at the previous depth" | Graph view |
| O17 | Core plugins list (current): Audio recorder, Backlinks, Bases, Bookmarks, Canvas, Command palette, Daily notes, File explorer, File recovery, Footnotes view, Graph view, Note composer, Outgoing links, Outline, Page preview, Properties view, Publish, Quick switcher, Random note, Search, Slash commands, Slides, Sync, Tags view, Templates, Unique note creator, Web viewer, Word count (and more on the page). Some are off by default. Sync and Publish are paid services | Core plugins, Introduction to licenses and payment |
| O18 | Bases: core plugin for "database-like views of your notes"; data stays in Markdown files and their properties; a view is saved as a `.base` file or embedded in a code block; layouts Table, List, Cards, Kanban, Map (Table and Cards since app version 1.9) | Introduction to Bases, Views |
| O19 | Canvas saves `.canvas` files in the open JSON Canvas format | Canvas |
| O20 | Templates variables `{{title}}`, `{{date}}` (default YYYY-MM-DD), `{{time}}` (HH:mm), Moment.js format strings; Daily notes creates a note named after today's date, YYYY-MM-DD by default, can use a template; Unique note creator makes time-coded titles | Templates, Daily notes, Unique note creator |
| O21 | Settings > Files and links: "Automatically update internal links": "When enabled, Obsidian automatically updates internal links when you rename a file. Turn this off to be prompted to update links after renaming." New link format: Shortest path when possible / Relative path to file / Absolute path in vault | Settings, Internal links, Manage notes |
| O22 | Renaming a note (F2 or the title) inside Obsidian updates all links to it | Manage notes |
| O23 | Note composer core plugin: merge two notes or split one into two | Core plugins |
| O24 | "Obsidian is free to use and is 100% user-supported. Organizations can choose to support Obsidian by purchasing Commercial licenses." | Commercial license |
| O25 | Open a Markdown file from outside the vault: needs Obsidian 1.14 | Manage notes |
| O26 | Text and List properties can contain internal links with `[[Link]]` syntax, which "must be surrounded with quotes" (`up: "[[Notification fatigue (map)]]"`). Whether property links appear in backlinks or the graph is NOT stated on the page: pages say "check the current help" | Properties (read 2026-10-10) |

## Verified facts - Luhmann, the archive, evergreen notes

| # | Fact | Tier | Source |
|---|---|---|---|
| L1 | Luhmann calls the essay "a piece of empirical sociology" about "me and someone else, namely my slip box"; the box as a "partner of communication" | read | Luhmann, "Communicating with Slip Boxes", trans. Manfred Kuehn, luhmann.surge.sh (German original "Kommunikation mit Zettelkästen. Ein Erfahrungsbericht", 1981) |
| L2 | He decides "against the systematic ordering in accordance with topics and sub-topics" for "a firm fixed place"; "The fixed filing place needs no system"; every slip gets a number that never changes | read | same |
| L3 | Branching: slip 57/12 continues as 57/13, and is supplemented at a word by 57/12a, 57/12b, then 57/12a1 | read | same |
| L4 | Links: fixed numbers let you "add as many references to them as you may want"; record "back links in the slips that are being linked to" | read | same |
| L5 | A register of keywords, constantly updated, is needed because there is no systematic order | read | same |
| L6 | "Every note is only an element which receives its quality only from the network of links and back-links"; "A note that is not connected to this network will get lost" | read | same |
| L7 | The box "needs a number of years in order to reach critical mass. Until then, it functions as a mere container"; "Theoretical publications do therefore not result from simply copying what can already be found in the slip box"; "Some things will get lost" | read | same |
| L8 | "After more than twenty-six years" of co-operation (consistent with a box begun in the early 1950s and an essay of 1981) | read | same |
| L9 | Approximately 90,000 handwritten cards, A-6, two collections. First (about 1951-1962): about 23,000 cards in 108 subject sections, two bibliographies of about 2,000 titles, a keyword index of about 1,250 entries. Second (1963-1997): eleven top-level sections, about 100 subsections, about 67,000 cards; its keyword index grew to 3,200 entries over four versions | read | Johannes F.K. Schmidt, "Niklas Luhmann's Card Index: The Fabrication of Serendipity", Sociologica 12(1), 2018, 53-60, doi 10.6092/issn.1971-8853/8350. Schmidt is scientific coordinator of the Bielefeld project "Niklas Luhmann - A Passion for Theory" (2015-2030) |
| L10 | The keyword index listed "only one to four places" per term; the links do the rest | read | Schmidt 2018 |
| L11 | "Hubs": cards with an above-average number of links that give access to large parts of the file. "Black holes": poorly linked parts "tend to remain isolated later on and hence fade away"; some parts "seemed to be untouched since their compilation" | read | Schmidt 2018 |
| L12 | Luhmann's publication list at his death "comprised more than 500 titles" | read | Schmidt 2018 |
| L13 | The box's creativity "was not totally independent from its creator of course"; the analog design "limited the realization of its potential"; the file is the "backstage" of the theory, "Niklas Luhmann's intellectual autobiography" | read | Schmidt 2018 |
| L14 | "More than 90,000 slips" ("Mehr als 90.000 Zettel"), kept over 40 years; the archive publishes them open access | read | Union der deutschen Akademien der Wissenschaften, "90.000 Zettel" (akademienunion.de) |
| L15 | First collection about 1952-1963 and 23,000 slips in seven sections; second 1963 to early 1997 (dates differ by a year from Schmidt 2018: teach "about") | reported | Deutschlandfunk Kultur, "Niklas-Luhmann-Archiv - Der Blick in den Zettelkasten ist jetzt online" |
| L16 | Markus Krajewski (Basel): the box was the "motor" of text production; Luhmann wrote "around 50 books and 600 articles" | reported | Deutschlandfunk Kultur, same article |
| L17 | Ahrens: Luhmann published "roughly another 60 books and hundreds of articles" in 29 and a half years, framed as the box's result | advocate (read) | soenkeahrens.de/en/takesmartnotes |
| L18 | zettelkasten.de: "we fantasize about what it would mean to be as productive as Luhmann"; the method "amplifies your effectiveness" but "not with less effort per time" | advocate (read) | zettelkasten.de/introduction |
| L19 | Sonke Ahrens, How to Take Smart Notes (2017); fleeting, literature and permanent notes | reported | book not read; author page read for L17 only |
| A1 | "Evergreen notes are written and organized to evolve, contribute, and accumulate over time, across projects"; principles: atomic, concept-oriented, densely linked, associative over hierarchical | read | Andy Matuschak, notes.andymatuschak.org/Evergreen_notes |
| A2 | Atomic: notes "only about one thing - but which, as much as possible, capture the entirety of that thing"; too broad muddies links, too fragmented fragments the network; "There's no clear litmus test" | read | .../Evergreen_notes_should_be_atomic |
| A3 | Concept-oriented: factor by concept "rather than by author, book, event, project, topic" | read | .../Evergreen_notes_should_be_concept-oriented |
| A4 | Densely linked: links push you to think about how ideas relate; finding links means rereading old notes | read | .../Evergreen_notes_should_be_densely_linked |
| A5 | "Prefer associative ontologies to hierarchical taxonomies": "often items belong in many places" | read | .../Prefer_associative_ontologies_to_hierarchical_taxonomies |
| A6 | "Evergreen note titles are like APIs"; prefer complete-phrase titles | read | .../Evergreen_note_titles_are_like_APIs |
| A7 | Most people take only transient notes; "after a year ... a pile of dissociated notes"; "Most people use notes as a bucket for storage or scratch thoughts" | read | .../Most_people_take_only_transient_notes and .../Most_people_use_notes_as_a_bucket... |
| A8 | Matuschak's practice is "heavily inspired by Niklas Luhmann's Zettelkasten" but uses a different term to explore apart from that culture | read | .../Similarities_and_differences_between_evergreen_note-writing_and_Zettelkasten |
| M1 | "Map of content" (MOC) as a hub note that links notes on a theme is a term popularised by Nick Milo's Linking Your Thinking | reported | LYT pages are script-rendered; not read |

**No research was read** showing that graph views, backlinks or linked notes improve retrieval,
learning or output. The PKM sibling searched directly for a controlled study of note systems and
found none; this pass did not run a fresh systematic search (search engine unavailable). Pages say
"no controlled study was found", never "studies show".

## The disagreements to teach

1. **"The Zettelkasten made Luhmann productive."** For: Luhmann's own account (L1, L6), Krajewski's
   "motor" (L16, reported), Ahrens and zettelkasten.de (advocates, L17-18). Against or limiting:
   it is a single self-reported case (L1 calls it an empirical account of one); Luhmann says
   publications do not come from copying the box and it is "a mere container" for years (L7); the
   archive's own coordinator says its creativity was "not totally independent from its creator"
   (L13); talent, training in law and sociology, and decades of work cannot be separated from the
   box with n = 1. Even the output count differs: 50 books + 600 articles (L16), about 60 books +
   hundreds (L17), more than 500 titles (L12). Never resolve.
2. **"No hierarchy."** Luhmann says no topical system (L2), yet the first collection had 108 subject
   sections and the second eleven top-level areas (L9). Both are true: top-level areas, no
   taxonomy inside them.
3. **"The graph view is your second brain."** The help says what it draws: notes and links (O15).
   It does not say what is relevant. The bench shows a vault can look perfectly connected (0
   orphans, one component) while a 2-hop neighbourhood is mostly noise.
4. Card counts: 90,000 (L9, L14) vs older "70,000" (PKM sibling recorded both as secondary). Use
   "about 90,000"; L9 itself is approximate.

## Seams (absolute links)

- https://phoebefu6.github.io/learn-pkm-with-phoebe/ owns capture, PARA folders, review cadence,
  retrieval. PKM pages say atomic notes, permanent addresses, linking by idea = the Zettelkasten
  method = here. Honour it.
- https://phoebefu6.github.io/learn-mind-mapping-with-phoebe/ owns radial maps (a MOC is a note of
  links, not a radial drawing; Canvas is mentioned, not taught as mind mapping).
- https://phoebefu6.github.io/learn-reading-with-phoebe/ owns how to read and turn a text into a
  note by recall; here a reading note is a note type. Reading links here; link back in session 2.
- https://phoebefu6.github.io/learn-markdown-with-phoebe/ owns Markdown syntax; here only
  Obsidian-specific syntax (wikilinks, embeds, block refs, properties, tags).
- https://phoebefu6.github.io/learn-notion-with-phoebe/ holds Ines's operations (databases, the
  same four clients, Theo). Bases (O18) is mentioned as Obsidian's database-like view; databases as
  a backend are Notion's job.

## Sessions (titles locked after a sibling grep, 2026-10-10)

1. `01-a-note-that-knows-its-neighbours.html` A note that knows its neighbours (green). O1-O5,
   O10, O11, O15 intro. Local files, vault, wikilinks, backlinks, unlinked mentions. Build: Ines's
   vault, first five notes, first links, read the backlinks panel.
2. `02-atomic-notes-and-their-address.html` Atomic notes and the address they keep (yellow). L1-L8,
   A1-A8, O6, O7, O8, O9, O20. Luhmann's fixed numbers vs titles as addresses; atomic, concept-
   oriented, complete-phrase titles; reading note vs interview note vs insight note; block refs and
   embeds; aliases; templates. Disagreement 1 (taught here). Build: split one fat interview note into
   three insight notes.
3. `03-maps-of-content-not-folders.html` Maps of content, not folders (yellow). L9-L11, A5, M1,
   O12, O13, O14, O18, disagreement 2. Folders vs tags vs links vs MOCs; Luhmann's keyword index and
   hubs; properties and tags; search operators; Bases as a view. Build: one MOC for one theme.
4. `04-the-link-bench.html` The link bench (orange). Bench canon below.
5. `05-what-the-graph-view-is-telling-you.html` What the graph view is (and is not) telling you
   (orange). O15, O16, L11, disagreement 3. Global vs local graph, depth, filters, groups, orphans;
   what node size means; the anti-lever as the cautionary tale. Build: a local graph read for one
   insight, groups by folder.
6. `06-growing-the-vault-without-losing-the-thread.html` Growing the vault without losing the
   thread (red). O2, O3, O17, O19, O21-O25, L7, L11. Renaming safely (inside Obsidian vs outside),
   link format settings, unlinked mentions as a weekly sweep, note composer merge/split, Canvas,
   daily notes, sync options (paid Sync vs any folder sync), local-first exit. Build: Ines's
   monthly vault maintenance pass.

## Not covered (honest)

Community plugins (Dataview, Templater, Excalidraw...) beyond a self-study mention; Obsidian
Publish and Sync set-up; themes and CSS snippets; the plugin API; mobile specifics; Bases formulas
and functions in depth; Markdown syntax (sibling); reading technique (sibling); PARA and review
cadence (sibling); radial mind maps (sibling); any claim that linked notes improve learning (no
study read); the Luhmann-Archiv's own site (script-rendered, not read; Schmidt 2018 and the
Akademienunion page stand in).

## Bench canon (session 4) - CONSTRUCTED

Vault `assets/ob-sample.js` (33 KB), generated once by `materials/build_ob_vault.py`, seed 20261009:
192 content notes (72 interviews, 12 project notes, 30 reading notes, 48 insight notes, 26 daily
notes, 4 admin notes) + 12 maps of content (rung 4 only). 162 notes carry 1-2 theme labels.
Engine `assets/ob-live.js`; reference `materials/ob_reference.py`; runner `materials/ob-node.js`.
**Python and node outputs are IDENTICAL** (all 16 configurations, every per-question value),
checked 2026-10-10. Depth 2 hops; a folder listing, tag page or map costs a hop and is never
counted as found; backlinks make links walkable both ways. Answered = recall >= 75%.

| Rung | Mean recall | Mean precision | Notes reached (mean) | Answered of 12 | Orphans | Largest component |
|---|---|---|---|---|---|---|
| 1 Folders only | 19.1% | 17.7% | 14.3 | 0 | 192 | 25.0% (48) |
| 2 Tags only | 38.3% | 32.1% | 22.4 | 0 | 192 | 77.1% |
| 3 Idea links (226 links) | 11.5% | 34.5% | 4.8 | 0 | 20 | 79.2% |
| 4 + maps of content (498 links) | 84.4% | 66.6% | 23.0 | 11 | 5 | 96.4% |

Honest finding the pages must keep: **sparse idea links alone do WORSE than tags or folders**
(recall 11.5%, 4.8 notes reached); links pay off once hub notes exist (rung 4). This matches
Schmidt's "hubs" (L11) and Luhmann's keyword index entering at "one to four places" (L10).
Rung 4 unanswered question: trust and credibility (26.9%), because its start interview was never
processed (no up-link to the map) - the 30% of interviews Ines did not process.
Orphans and components for rungs 1-2 count links only: folders and tags are not links (O15).

**Anti-lever, "link every mention of every term"** (on any rung): recall 100.0%, answered 12/12,
orphans 0, largest component 100.0%, notes reached about 182 of 192 (rung 4: 181.8), precision
9.1% on rungs 3-4 (9.0% on 1-2), roughly the share of the vault on any one theme (mean relevant
set 16.5 of 191, about 8.6%). Links on rung 4: 498 -> 1,488. The graph looks perfect and the
neighbourhood is noise.

**Break, "rename 20 notes outside Obsidian"** (fixed set: 4 Brightwell interviews, Corvid findings
readout, 5 reading notes, 10 insight notes; no link updated): rung 4: 72 broken links, recall
84.4% -> 80.1%, precision 66.6% -> 62.9%, answered 11 -> 10 ("interviewer bias" 90.0% -> 70.0%
now fails; "trust and credibility" 26.9% -> 3.8%), orphans 5 -> 8, largest component 96.4% ->
93.8%. Rung 3: 51 broken links, recall 11.5% -> 6.5%, orphans 20 -> 41. Rungs 1-2: 0 broken,
nothing changes (folders and tags do not care about names). Inside Obsidian a rename updates
links by default (O21, O22); with the setting off it prompts. The break models a rename where no
update can happen.

Correction to the course block: the block said "rename 20 notes with link updating off". Per the
help (O21) turning the setting off makes Obsidian PROMPT, it does not silently break links. The
break is relabelled "rename 20 notes outside Obsidian (Finder, another editor, a sync script)".
Second correction: the contractor is Theo and the four clients are Aldermoor Care, Brightwell
Mutual, Dunmore District Council, Corvid Studio, matching learn-notion-with-phoebe.

## Citation appendix

- Obsidian Help, help.obsidian.md (now obsidian.md/help), pages named in the O table, read 2026-10-09 from github.com/obsidianmd/obsidian-help (en/).
- Obsidian releases, github.com/obsidianmd/obsidian-releases, v1.14.4, 2026-10-05.
- Niklas Luhmann, "Communicating with Slip Boxes: An Empirical Account", trans. Manfred Kuehn, http://luhmann.surge.sh/communicating-with-slip-boxes (orig. 1981).
- Johannes F.K. Schmidt (2018), "Niklas Luhmann's Card Index: The Fabrication of Serendipity", Sociologica 12(1): 53-60.
- Union der deutschen Akademien der Wissenschaften, "90.000 Zettel", akademienunion.de/akademienforschung/90000-zettel.
- Deutschlandfunk Kultur, "Niklas-Luhmann-Archiv - Der Blick in den Zettelkasten ist jetzt online" (reported).
- Sonke Ahrens, How to Take Smart Notes (2017) (reported); author page soenkeahrens.de/en/takesmartnotes (advocate).
- zettelkasten.de/introduction (advocate).
- Andy Matuschak, notes.andymatuschak.org (pages named in A1-A8).
- Nick Milo, Linking Your Thinking (reported).
