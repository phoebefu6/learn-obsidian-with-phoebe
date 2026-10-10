#!/usr/bin/env python3
"""Build Ines's constructed research vault for the link bench (session 4).

CONSTRUCTED, end to end. Ines is a fictional freelance user-research consultant with 4 active
clients and 1 part-time contractor (Theo). No note here is a real person, client or study.

Writes assets/ob-sample.js with json.dumps (never string interpolation). Every random choice is
made HERE, once, from a fixed seed; the browser engine (assets/ob-live.js) and the Python
reference (materials/ob_reference.py) only read the file and run graph algorithms on it, so
they cannot drift apart on randomness.

    python3 materials/build_ob_vault.py            # from the repo root
"""
import json
import os
import random

SEED = 20261009
R = random.Random(SEED)
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "assets", "ob-sample.js")

# ---------------------------------------------------------------- themes (the 12 questions)
THEMES = [
    # name, three tag spellings Ines drifted between, product theme?
    ("Onboarding drop-off", ["onboarding", "onboard", "first-run"], True),
    ("Trust and credibility", ["trust", "credibility", "trust-signals"], True),
    ("Notification fatigue", ["notifications", "notifs", "alerts"], True),
    ("Accessibility barriers", ["accessibility", "a11y", "access"], True),
    ("Price perception", ["pricing", "price", "fees"], True),
    ("Recruiting participants", ["recruiting", "recruitment", "panel"], False),
    ("Interviewer bias", ["bias", "leading-questions", "interviewer-bias"], False),
    ("Jobs to be done", ["jtbd", "jobs", "jobs-to-be-done"], True),
    ("Synthesis methods", ["synthesis", "affinity", "analysis"], False),
    ("Stakeholder buy-in", ["stakeholders", "buy-in", "readouts"], False),
    ("Consent and privacy", ["consent", "privacy", "data-consent"], True),
    ("Low-connectivity use", ["offline", "low-signal", "connectivity"], True),
]
METHOD = [i for i, t in enumerate(THEMES) if not t[2]]

CLIENTS = [
    # name, folder, tag, product theme pool (weights by repetition). Names match the Notion
    # course's Ines (learn-notion-with-phoebe): same four clients, same contractor (Theo).
    ("Aldermoor Care", "Aldermoor", "aldermoor", [0, 0, 1, 1, 3, 10, 10]),
    ("Brightwell Mutual", "Brightwell", "brightwell", [1, 1, 4, 4, 10, 0]),
    ("Dunmore District Council", "Dunmore", "dunmore", [11, 11, 3, 3, 2, 1]),
    ("Corvid Studio", "Corvid", "corvid", [2, 2, 7, 7, 0, 0, 4]),
]

GENERIC = ["user", "interview", "client", "participant", "insight", "research", "feedback", "app"]

INSIGHTS = {
    0: ["Drop-off clusters at the first form that asks for an ID number",
        "People abandon set-up when the value arrives after the effort",
        "A skip button beats a progress bar for first-run screens",
        "Onboarding emails are read once, on the day they arrive"],
    1: ["Trust is borrowed from the brand people already use",
        "A named human beats a badge as a trust signal",
        "People read reviews to find the one bad case, not the average",
        "Unexplained data requests read as a threat"],
    2: ["Notification fatigue starts at the third prompt in a day",
        "People mute the whole app rather than one category",
        "A reminder tied to a person they know survives muting",
        "Badges create guilt, not action"],
    3: ["Screen-reader users judge an app in its first ten seconds",
        "Small tap targets fail first for people on the move",
        "Captions are used by far more people than those who need them",
        "Accessibility fixes found late get cut as polish"],
    4: ["People compare against the last price they paid, not the market",
        "A surprise fee at checkout reads as dishonesty",
        "Round numbers feel like estimates, odd numbers feel exact",
        "Free delivery thresholds change basket size more than discounts"],
    5: ["Screener questions leak the answer you want",
        "Recruiting through the client's list over-samples fans",
        "No-shows drop when the reminder comes from a person",
        "Incentives attract a different sample, not just a bigger one"],
    6: ["A leading question gets agreement, not information",
        "Interviewers hear the theme they came in with",
        "Silence after an answer brings out the real reason",
        "Asking about the last time beats asking about usually"],
    7: ["People hire the app for a moment, not a feature",
        "The competing job is often doing nothing",
        "A job statement names the situation before the goal",
        "Switching stories reveal the job better than wish lists"],
    8: ["Affinity walls need a question before the stickies",
        "A pattern needs three independent sources to count",
        "Quotes without context mislead the readout audience",
        "Synthesis done alone drifts toward the loudest interview"],
    9: ["Stakeholders act on one story and one number",
        "Inviting a stakeholder to one interview beats ten slides",
        "Findings that threaten a roadmap need a pre-read",
        "A readout without a decision owner changes nothing"],
    10: ["People consent to the purpose, not the form",
         "A recorded session needs consent at the start and the end",
         "Privacy worries rise when the data travels to a third party",
         "Opt-out buried in settings reads as opt-in by force"],
    11: ["Offline mode is a trust feature, not a technical one",
         "People screenshot tickets because they expect the signal to drop",
         "A spinner with no timeout reads as a broken app",
         "Sync conflicts are blamed on the user, by the user"],
}

READING_TOPICS = {
    0: ["Article on progressive onboarding", "Paper on first-session retention", "Talk notes on empty states"],
    1: ["Book chapter on trust in interfaces", "Article on review reading behaviour", "Paper on credibility cues"],
    2: ["Article on notification permission prompts", "Paper on interruption cost", "Talk notes on digest emails"],
    3: ["Guide to screen-reader testing", "Article on touch target sizes", "Paper on captions in everyday use"],
    4: ["Article on reference prices", "Paper on drip pricing", "Talk notes on fee transparency"],
    5: ["Guide to writing screeners", "Article on participant incentives", "Paper on panel bias"],
    6: ["Article on leading questions", "Book chapter on interview technique"],
    7: ["Article on job statements", "Talk notes on switching interviews"],
    8: ["Guide to affinity mapping", "Article on thematic analysis"],
    9: ["Article on research readouts", "Talk notes on stakeholder interviews"],
    10: ["Guide to informed consent in research", "Article on dark patterns in consent"],
    11: ["Article on offline-first design", "Paper on mobile use in low-signal areas"],
}


def tag_for(theme, when):
    """Tag spelling drift: early notes use spelling 0, later notes spelling 1, some spelling 2."""
    spellings = THEMES[theme][1]
    x = R.random()
    if x < 0.15:
        return spellings[2]
    return spellings[0] if when < 0.5 else spellings[1]


notes = []


def add(title, folder, kind, themes, client=None):
    n = {"id": len(notes), "title": title, "folder": folder, "kind": kind,
         "themes": sorted(set(themes)), "client": client, "tags": [], "links": [], "up": [],
         "mentions": []}
    notes.append(n)
    return n


# ---------------------------------------------------------------- content notes
# Interviews: 4 clients x 18, dated through Jan-Sep 2026
for ci, (cname, cfold, ctag, pool) in enumerate(CLIENTS):
    for k in range(18):
        month = 1 + (k * 9) // 18
        day = 1 + R.randrange(27)
        t = [R.choice(pool)]
        if R.random() < 0.35:
            t.append(R.choice(pool) if R.random() < 0.5 else R.choice(METHOD))
        n = add("2026-%02d-%02d %s interview P%02d" % (month, day, cfold, k + 1),
                "Clients/%s/Interviews" % cfold, "interview", t, ci)
        n["when"] = k / 18.0

# Projects: 3 per client
for ci, (cname, cfold, ctag, pool) in enumerate(CLIENTS):
    prod = sorted(set(pool), key=lambda x: -pool.count(x))
    add("%s - research brief" % cfold, "Clients/%s" % cfold, "project", [5, prod[0]], ci)
    add("%s - findings readout" % cfold, "Clients/%s" % cfold, "project", [8, prod[0], prod[1]], ci)
    add("%s - stakeholder workshop" % cfold, "Clients/%s" % cfold, "project", [9, prod[1]], ci)

# Readings: 30
for t, titles in READING_TOPICS.items():
    for title in titles:
        th = [t]
        if R.random() < 0.2:
            th.append(R.randrange(len(THEMES)))
        add("Reading - " + title.lower(), "Reading", "reading", th)

# Insights (evergreen, atomic): 48, titled as claims
for t, titles in INSIGHTS.items():
    for title in titles:
        th = [t]
        if R.random() < 0.15:
            th.append(R.randrange(len(THEMES)))
        add(title, "Insights", "insight", th)

# Daily notes: 26, not about any theme
for k in range(26):
    add("2026-%02d-%02d" % (1 + k // 3, 3 + 9 * (k % 3)), "Daily", "daily", [])

# Admin: 4
for title in ["Theo - contractor onboarding", "Transcription checklist", "Client list", "Vault conventions"]:
    add(title, "Admin", "admin", [])

CONTENT = len(notes)
by_kind = lambda k: [n for n in notes if n["kind"] == k]
with_theme = lambda kind, t: [n for n in notes if n["kind"] == kind and t in n["themes"]]

# ---------------------------------------------------------------- tags (rung 2)
for n in notes:
    when = n.get("when", R.random())
    if n["kind"] in ("interview", "project"):
        n["tags"].append(CLIENTS[n["client"]][2])
    p = {"interview": 0.65, "project": 0.8, "reading": 0.8, "insight": 0.7}.get(n["kind"], 0)
    for t in n["themes"]:
        if R.random() < p:
            n["tags"].append(tag_for(t, when))
    if n["kind"] == "reading" and R.random() < 0.5:
        n["tags"].append("to-process")
    if n["kind"] == "daily":
        n["tags"].append("daily")
    if n["kind"] == "admin":
        n["tags"].append("admin")
    n["tags"] = sorted(set(n["tags"]))


# ---------------------------------------------------------------- sparse idea links (rung 3)
def link(a, b):
    if a["id"] != b["id"] and b["id"] not in a["links"]:
        a["links"].append(b["id"])


for n in by_kind("interview"):
    if R.random() < 0.12:
        continue  # never processed: no links out
    for t in n["themes"]:
        pool = with_theme("insight", t)
        if pool and R.random() < 0.75:
            for b in R.sample(pool, 1 if R.random() < 0.6 else 2):
                link(n, b)
    if R.random() < 0.2:
        same = [m for m in by_kind("interview") if m["client"] == n["client"] and m["id"] != n["id"]]
        link(n, R.choice(same))

for n in by_kind("insight"):
    t = n["themes"][0]
    if R.random() < 0.7:
        pool = [m for m in with_theme("insight", t) if m["id"] != n["id"]]
        link(n, R.choice(pool))
    if R.random() < 0.3:
        link(n, R.choice([m for m in by_kind("insight") if t not in m["themes"]]))
    if R.random() < 0.5:
        pool = with_theme("reading", t)
        if pool:
            link(n, R.choice(pool))

for n in by_kind("reading"):
    if R.random() < 0.6:
        link(n, R.choice(with_theme("insight", n["themes"][0])))

for n in by_kind("project"):
    kind = n["title"].split(" - ")[1]
    if kind == "findings readout":
        pool = [m for t in n["themes"] if t != 8 for m in with_theme("insight", t)]
        for b in R.sample(pool, 3):
            link(n, b)
    elif kind == "research brief":
        link(n, R.choice(with_theme("reading", 5)))
    else:
        link(n, [m for m in by_kind("project") if m["client"] == n["client"] and "findings" in m["title"]][0])

interviews = by_kind("interview")
for n in by_kind("daily"):
    if R.random() < 0.8:
        for b in R.sample(interviews, 1 if R.random() < 0.5 else 2):
            link(n, b)

admin = {n["title"]: n for n in by_kind("admin")}
link(admin["Theo - contractor onboarding"], R.choice(with_theme("reading", 5)))
link(admin["Client list"], [m for m in by_kind("project") if "brief" in m["title"]][0])

# ---------------------------------------------------------------- maps of content (rung 4)
maps = []
for t, (name, _, _) in enumerate(THEMES):
    m = {"id": len(notes) + t, "title": name + " (map)", "folder": "Maps", "kind": "map",
         "themes": [t], "client": None, "tags": [], "links": [], "up": [], "mentions": []}
    maps.append(m)
for m in maps:
    t = m["themes"][0]
    members = with_theme("insight", t) + with_theme("reading", t) + \
        [n for n in with_theme("project", t) if "findings" in n["title"]]
    m["links"] = sorted(n["id"] for n in members)
for n in notes:
    if n["kind"] in ("insight", "reading"):
        n["up"].append(maps[n["themes"][0]]["id"])
    elif n["kind"] == "project":
        n["up"] = [maps[t]["id"] for t in n["themes"]]
    elif n["kind"] == "interview":
        n["up"] = [maps[t]["id"] for t in n["themes"] if R.random() < 0.7]

# ---------------------------------------------------------------- mentions (anti-lever)
for n in notes:
    k = 3 + R.randrange(3)
    n["mentions"] = sorted(R.sample(GENERIC, k)) + sorted(THEMES[t][1][0] for t in n["themes"])

# ---------------------------------------------------------------- questions + break set
questions = []
for t, (name, _, product) in enumerate(THEMES):
    if product:
        start = [n for n in interviews if t in n["themes"]][-1]   # the latest interview on it
    else:
        cands = [n for n in by_kind("project") if t in n["themes"]] or with_theme("reading", t)
        start = cands[-1]
    questions.append({"theme": t, "q": "Find everything about " + name.lower(), "start": start["id"]})

linked_targets = sorted({b for n in notes for b in n["links"]})
renamed = sorted(R.sample(linked_targets, 20))

for n in notes:
    n.pop("when", None)
    n["links"] = sorted(n["links"])
    n["up"] = sorted(n["up"])

data = {
    "about": "Ines's research vault, CONSTRUCTED for learn-obsidian-with-phoebe. Fictional notes, seeded.",
    "seed": SEED,
    "themes": [t[0] for t in THEMES],
    "notes": [[n["title"], n["folder"], n["kind"], n["themes"], n["tags"], n["links"], n["up"],
               n["mentions"]] for n in notes + maps],
    "fields": ["title", "folder", "kind", "themes", "tags", "links", "up", "mentions"],
    "content": CONTENT,
    "questions": questions,
    "renamed": renamed,
}
with open(OUT, "w") as f:
    f.write("/* ob-sample.js - Ines's research vault, CONSTRUCTED (fictional notes, seed %d).\n"
            "   Generated by materials/build_ob_vault.py with json.dumps. Do not edit by hand. */\n" % SEED)
    f.write("(function (root) { var V = ")
    f.write(json.dumps(data, separators=(",", ":"), ensure_ascii=True))
    f.write(";\n  if (typeof module === \"object\" && module.exports) module.exports = V; else root.OB_VAULT = V;\n"
            "})(typeof self !== \"undefined\" ? self : this);\n")
print("notes", len(notes), "maps", len(maps), "bytes", os.path.getsize(OUT))
