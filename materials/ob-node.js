// Node runner: loads assets/ob-sample.js + assets/ob-live.js as the browser does, prints canon JSON.
// Compare with: python3 materials/ob_reference.py --json
const path = require("path");
const repo = process.argv[2] || path.join(__dirname, "..");
const V = require(path.join(path.resolve(repo), "assets/ob-sample.js"));
const api = require(path.join(path.resolve(repo), "assets/ob-live.js"));
process.stdout.write(JSON.stringify(api.canon(V), null, 1));
