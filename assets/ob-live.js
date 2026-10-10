/* ob-live.js - the link bench for learn-obsidian-with-phoebe (session 4)
 *
 * CONSTRUCTED vault, REAL graph algorithms. Ines is a fictional user-research consultant; her
 * 192 notes (and 12 maps of content) are seeded and generated once by materials/build_ob_vault.py
 * into assets/ob-sample.js. Nothing random happens here: the page builds a navigation graph for
 * the chosen rung and runs breadth-first search, degree counts and connected components on it.
 * materials/ob_reference.py runs the same algorithms in Python and must print identical numbers.
 *
 * Rungs (what a reader can follow from the note they have open):
 *   1 Folders only   - a folder listing is one hop: open the folder, open a note.
 *   2 Tags only      - a tag's search page is one hop: click the tag, open a note.
 *   3 Idea links     - wikilinks Ines wrote by idea; backlinks make every link walkable both ways.
 *   4 + Maps of content - rung 3 plus 12 map notes (map lists members; members link "up").
 * Maps and tag or folder pages are signposts: they cost a hop but are never counted as found.
 * Anti-lever "link every mention of every term": every term a note mentions becomes a link to a
 *   term note ([[user]], [[interview]] ...). Reach and recall go up; precision collapses.
 * Break "rename 20 notes outside Obsidian": the 20 fixed notes in V.renamed are renamed where no
 *   link gets updated (Finder, another editor, a sync script). Links pointing AT them break; their
 *   own outgoing links still work, so a backlink still leads to them from the other side.
 * Questions: 12 x "find everything about <theme>", each from a fixed start note. Relevant = every
 *   content note labelled with that theme. A question counts as answered at recall >= 75%.
 */
(function (root) {
  "use strict";

  var DEPTH = 2, PASS = 0.75;
  var RUNGS = [
    { id: 1, label: "Folders only" },
    { id: 2, label: "Tags only" },
    { id: 3, label: "Idea links" },
    { id: 4, label: "Idea links + maps of content" }
  ];

  function pct(x) { return Math.floor(x * 1000 + 0.5) / 10; }

  function build(V, rung, anti, brk) {
    var N = V.notes, C = V.content, M = N.length;
    var renamed = {}, i, j;
    if (brk) for (i = 0; i < V.renamed.length; i++) renamed[V.renamed[i]] = true;
    var adj = [], hubs = {}, nNodes = M, links = [], broken = 0;
    for (i = 0; i < M; i++) adj.push([]);
    function hub(key) {
      if (!(key in hubs)) { hubs[key] = nNodes++; adj.push([]); }
      return hubs[key];
    }
    function edge(a, b) { adj[a].push(b); adj[b].push(a); }
    function dlink(a, b) {               /* a directed wikilink a -> b */
      if (renamed[b]) { broken++; return; }
      links.push([a, b]); edge(a, b);
    }
    for (i = 0; i < C; i++) {
      var n = N[i];
      if (rung === 1) edge(i, hub("f:" + n[1]));
      if (rung === 2) for (j = 0; j < n[4].length; j++) edge(i, hub("t:" + n[4][j]));
      if (rung >= 3) for (j = 0; j < n[5].length; j++) dlink(i, n[5][j]);
      if (rung === 4) for (j = 0; j < n[6].length; j++) dlink(i, n[6][j]);
      if (anti) for (j = 0; j < n[7].length; j++) {
        var h = hub("m:" + n[7][j]); links.push([i, h]); edge(i, h);
      }
    }
    if (rung === 4) for (i = C; i < M; i++) for (j = 0; j < N[i][5].length; j++) dlink(i, N[i][5][j]);
    return { adj: adj, nNodes: nNodes, links: links, broken: broken, active: rung === 4 ? M : C };
  }

  function bfs(adj, s, depth) {
    var dist = {}, q = [s], out = [];
    dist[s] = 0;
    for (var h = 0; h < q.length; h++) {
      var u = q[h];
      if (dist[u] === depth) continue;
      for (var k = 0; k < adj[u].length; k++) {
        var v = adj[u][k];
        if (!(v in dist)) { dist[v] = dist[u] + 1; q.push(v); out.push(v); }
      }
    }
    return out;
  }

  function run(V, rung, anti, brk) {
    var G = build(V, rung, anti, brk), C = V.content, N = V.notes, i;
    var qs = [], sumR = 0, sumP = 0, sumReach = 0, answered = 0;
    for (var qi = 0; qi < V.questions.length; qi++) {
      var Q = V.questions[qi], t = Q.theme, s = Q.start;
      var got = bfs(G.adj, s, DEPTH), reach = 0, found = 0, rel = 0;
      for (i = 0; i < got.length; i++) if (got[i] < C) {
        reach++; if (N[got[i]][3].indexOf(t) >= 0) found++;
      }
      for (i = 0; i < C; i++) if (i !== s && N[i][3].indexOf(t) >= 0) rel++;
      var rec = found / rel, prec = reach ? found / reach : 0;
      sumR += rec; sumP += prec; sumReach += reach;
      if (rec >= PASS) answered++;
      qs.push({ theme: t, q: Q.q, start: N[s][0], reach: reach, found: found, relevant: rel,
        recall: pct(rec), precision: pct(prec), pass: rec >= PASS });
    }
    /* orphans: content notes with no working link in or out */
    var linked = {};
    for (i = 0; i < G.links.length; i++) { linked[G.links[i][0]] = 1; linked[G.links[i][1]] = 1; }
    var orphans = 0;
    for (i = 0; i < C; i++) if (!linked[i]) orphans++;
    /* largest connected component, counted in content notes */
    var comp = new Array(G.nNodes), best = 0;
    for (i = 0; i < G.nNodes; i++) comp[i] = -1;
    for (i = 0; i < C; i++) if (comp[i] < 0) {
      var stack = [i], size = 0; comp[i] = i;
      while (stack.length) {
        var u = stack.pop(); if (u < C) size++;
        for (var k = 0; k < G.adj[u].length; k++) {
          var v = G.adj[u][k]; if (comp[v] < 0) { comp[v] = i; stack.push(v); }
        }
      }
      if (size > best) best = size;
    }
    var nq = V.questions.length;
    return {
      rung: rung, anti: !!anti, brk: !!brk,
      recall: pct(sumR / nq), precision: pct(sumP / nq), reach: Math.floor(sumReach * 10 / nq + 0.5) / 10,
      answered: answered, orphans: orphans, largest: pct(best / C), largestNotes: best,
      links: G.links.length, broken: G.broken, questions: qs
    };
  }

  function canon(V) {
    var out = [];
    [false, true].forEach(function (anti) {
      [false, true].forEach(function (brk) {
        for (var r = 1; r <= 4; r++) out.push(run(V, r, anti, brk));
      });
    });
    return out;
  }

  var api = { RUNGS: RUNGS, DEPTH: DEPTH, PASS: PASS, run: run, canon: canon };
  if (typeof module === "object" && module.exports) { module.exports = api; return; }
  root.OBLive = api;

  /* ---------------------------------------------------------------- widget */
  function el(tag, cls, txt) {
    var e = document.createElement(tag); if (cls) e.className = cls;
    if (txt !== undefined) e.textContent = txt; return e;
  }
  function mount() {
    var box = document.getElementById("link-bench");
    if (!box || !root.OB_VAULT) return;
    var V = root.OB_VAULT, state = { rung: 1, anti: false, brk: false };
    var ctl = box.querySelector(".lb-controls"), out = box.querySelector(".lb-out");
    var rungBtns = [];
    RUNGS.forEach(function (R) {
      var b = el("button", "lb-rung", R.id + " · " + R.label);
      b.type = "button"; b.setAttribute("data-rung", R.id);
      b.addEventListener("click", function () { state.rung = R.id; render(); });
      ctl.querySelector(".lb-rungs").appendChild(b); rungBtns.push(b);
    });
    var antiBtn = ctl.querySelector("[data-lb='anti']"), brkBtn = ctl.querySelector("[data-lb='break']");
    antiBtn.addEventListener("click", function () { state.anti = !state.anti; render(); });
    brkBtn.addEventListener("click", function () { state.brk = !state.brk; render(); });

    function f1(x) { return x.toFixed(1); }
    function stat(label, value, note) {
      var d = el("div", "lb-stat"); d.appendChild(el("b", null, value));
      d.appendChild(el("span", null, label)); if (note) d.appendChild(el("i", null, note));
      return d;
    }
    function render() {
      rungBtns.forEach(function (b) { b.classList.toggle("on", +b.getAttribute("data-rung") === state.rung); });
      antiBtn.classList.toggle("on", state.anti); antiBtn.setAttribute("aria-pressed", state.anti);
      brkBtn.classList.toggle("on", state.brk); brkBtn.setAttribute("aria-pressed", state.brk);
      var r = run(V, state.rung, state.anti, state.brk);
      var base = state.brk ? run(V, state.rung, state.anti, false) : null;
      out.innerHTML = "";
      var g = el("div", "lb-stats");
      g.appendChild(stat("mean recall", f1(r.recall) + "%", "of the relevant notes, found within 2 hops"));
      g.appendChild(stat("mean precision", f1(r.precision) + "%", "of what you reach, relevant"));
      g.appendChild(stat("notes reached", f1(r.reach), "per question, mean, of 192"));
      g.appendChild(stat("questions answered", r.answered + " / 12", "recall 75% or more"));
      g.appendChild(stat("orphans", String(r.orphans), "notes with no working link, of " + r.links.toLocaleString("en-US") + " links"));
      g.appendChild(stat("largest component", f1(r.largest) + "%", r.largestNotes + " of 192 notes"));
      out.appendChild(g);
      if (state.brk) {
        var lost = [];
        r.questions.forEach(function (q, k) { if (base.questions[k].pass && !q.pass) lost.push(q.q); });
        var p = el("p", "lb-break");
        p.textContent = r.broken + " broken links after renaming 20 notes outside Obsidian. " +
          (lost.length ? "Questions that now fail: " + lost.join("; ") + "." :
            "No question changes pass or fail on this rung" +
            (r.broken ? " (recall still drops: " + f1(base.recall) + "% to " + f1(r.recall) + "%)." : ": folders and tags do not care about names."));
        out.appendChild(p);
      }
      var tbl = el("table", "clean lb-table"), hd = el("tr");
      ["Question", "Reached", "Found / relevant", "Recall", "Precision"].forEach(function (h) { hd.appendChild(el("th", null, h)); });
      var th = el("thead"); th.appendChild(hd); tbl.appendChild(th);
      var tb = el("tbody");
      r.questions.forEach(function (q) {
        var tr = el("tr", q.pass ? "is-pass" : "is-miss");
        tr.appendChild(el("td", null, q.q));
        tr.appendChild(el("td", null, String(q.reach)));
        tr.appendChild(el("td", null, q.found + " / " + q.relevant));
        tr.appendChild(el("td", null, f1(q.recall) + "%"));
        tr.appendChild(el("td", null, f1(q.precision) + "%"));
        tb.appendChild(tr);
      });
      tbl.appendChild(tb);
      var wrap = el("div", "lb-tablewrap"); wrap.appendChild(tbl); out.appendChild(wrap);
    }
    render();
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", mount); else mount();
})(typeof self !== "undefined" ? self : this);
