#!/usr/bin/env python3
"""Python reference for the link bench (assets/ob-live.js). Same graph, same algorithms, written
independently; `python3 materials/ob_reference.py --json` must equal `node materials/ob-node.js`.
CONSTRUCTED vault (Ines is fictional). Reads assets/ob-sample.js."""
import json, math, os, sys
from collections import deque

HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, "..", "assets", "ob-sample.js")).read()
V = json.loads(src[src.index("var V = ") + 8: src.index(";\n  if (typeof module")])
DEPTH, PASS = 2, 0.75


def pct(x):
    return math.floor(x * 1000 + 0.5) / 10


def build(rung, anti, brk):
    notes, C = V["notes"], V["content"]
    M = len(notes)
    renamed = set(V["renamed"]) if brk else set()
    adj = {i: set() for i in range(M)}
    links, broken = [], 0

    def edge(a, b):
        adj.setdefault(a, set()).add(b)
        adj.setdefault(b, set()).add(a)

    def dlink(a, b):
        nonlocal broken
        if b in renamed:
            broken += 1
            return
        links.append((a, b))
        edge(a, b)

    for i in range(C):
        title, folder, kind, themes, tags, out, up, mentions = notes[i]
        if rung == 1:
            edge(i, ("f", folder))
        if rung == 2:
            for t in tags:
                edge(i, ("t", t))
        if rung >= 3:
            for b in out:
                dlink(i, b)
        if rung == 4:
            for b in up:
                dlink(i, b)
        if anti:
            for m in mentions:
                links.append((i, ("m", m)))
                edge(i, ("m", m))
    if rung == 4:
        for i in range(C, M):
            for b in notes[i][5]:
                dlink(i, b)
    return adj, links, broken


def run(rung, anti, brk):
    adj, links, broken = build(rung, anti, brk)
    notes, C = V["notes"], V["content"]
    sumR = sumP = 0.0
    sumReach = answered = 0
    qs = []
    for Q in V["questions"]:
        t, s = Q["theme"], Q["start"]
        dist = {s: 0}
        dq = deque([s])
        while dq:
            u = dq.popleft()
            if dist[u] == DEPTH:
                continue
            for v in adj[u]:
                if v not in dist:
                    dist[v] = dist[u] + 1
                    dq.append(v)
        got = [v for v in dist if v != s and isinstance(v, int) and v < C]
        reach = len(got)
        found = sum(1 for v in got if t in notes[v][3])
        rel = sum(1 for i in range(C) if i != s and t in notes[i][3])
        rec = found / rel
        prec = found / reach if reach else 0
        sumR += rec; sumP += prec; sumReach += reach
        answered += rec >= PASS
        qs.append({"theme": t, "q": Q["q"], "start": notes[s][0], "reach": reach, "found": found,
                   "relevant": rel, "recall": pct(rec), "precision": pct(prec), "pass": rec >= PASS})
    linked = set()
    for a, b in links:
        linked.add(a); linked.add(b)
    orphans = sum(1 for i in range(C) if i not in linked)
    seen, best = set(), 0
    for i in range(C):
        if i in seen:
            continue
        stack, size = [i], 0
        seen.add(i)
        while stack:
            u = stack.pop()
            if isinstance(u, int) and u < C:
                size += 1
            for v in adj[u]:
                if v not in seen:
                    seen.add(v); stack.append(v)
        best = max(best, size)
    nq = len(V["questions"])
    return {"rung": rung, "anti": anti, "brk": brk, "recall": pct(sumR / nq), "precision": pct(sumP / nq),
            "reach": math.floor(sumReach * 10 / nq + 0.5) / 10, "answered": answered, "orphans": orphans,
            "largest": pct(best / C), "largestNotes": best, "links": len(links), "broken": broken,
            "questions": qs}


def canon():
    return [run(r, a, b) for a in (False, True) for b in (False, True) for r in (1, 2, 3, 4)]


if __name__ == "__main__":
    c = canon()
    if "--json" in sys.argv:
        sys.stdout.write(json.dumps(c, indent=1))
    else:
        for x in c:
            print(x["rung"], "anti" if x["anti"] else "    ", "brk" if x["brk"] else "   ",
                  "recall", x["recall"], "prec", x["precision"], "reach", x["reach"], "ans", x["answered"],
                  "orph", x["orphans"], "comp", x["largest"], "links", x["links"], "broken", x["broken"])
