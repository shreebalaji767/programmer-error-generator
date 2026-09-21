from pathlib import Path
import json

categories = {
    "JavaScript": [
        ("Why is this variable undefined?", "You probably accessed it before it was initialized, used the wrong scope, or misspelled the variable."),
        ("Why does == work but === fail?", "Because == performs type coercion while === requires both value and type to match."),
        ("Why does setTimeout run later?", "JavaScript schedules it through the event loop instead of executing it immediately."),
        ("Why does my array look empty in console?", "The console may display the object's later state. Log a copied value when debugging."),
        ("Why does this work locally but fail in production?", "Check environment variables, build configuration, API URLs, case sensitivity, and production-only behavior."),
        ("Why is my click handler firing twice?", "You may have registered the same event listener more than once."),
        ("Why does this lose the correct this value?", "Regular functions and arrow functions handle this differently."),
        ("Why isn't my async function returning the data?", "You probably forgot to await the Promise or return it."),
        ("Why does map return undefined?", "Your callback probably uses braces without an explicit return."),
        ("Why does my Promise never finish?", "A Promise may never resolve or reject because one execution path leaves it pending.")
    ],

    "Python": [
        ("Why is my Python list changing unexpectedly?", "You may have accidentally created multiple references to the same mutable list."),
        ("Why does Python say ModuleNotFoundError?", "The package may not be installed in the active environment, the wrong interpreter may be selected, or the import name may differ."),
        ("Why does my function return None?", "A function without an explicit return statement returns None."),
        ("Why does my code work in one terminal but not another?", "The terminals may be using different Python installations or virtual environments."),
        ("Why is my dictionary KeyError happening?", "The requested key does not exist. Use get(), check membership, or correct the key."),
        ("Why does pip install succeed but Python cannot import it?", "pip and python may point to different environments."),
        ("Why does my Flask app work locally but not on hosting?", "Check the host/port binding, start command, dependencies, environment variables, and deployment configuration."),
        ("Why does Python say indentation error?", "Python uses indentation as syntax. Mixed tabs/spaces or inconsistent indentation can cause this."),
        ("Why does my file say PermissionError?", "The process does not have sufficient permission to access the requested file or directory."),
        ("Why did changing one list change another list?", "Both variables may reference the same mutable object.")
    ],

    "HTML/CSS": [
        ("Why is my div not centered?", "Check the parent layout. Flexbox or Grid with appropriate alignment is usually simpler than manual positioning."),
        ("Why is my CSS not applying?", "Check selector specificity, stylesheet loading, syntax errors, and whether another rule overrides it."),
        ("Why does my page overflow horizontally on mobile?", "Look for fixed widths, oversized elements, long unbreakable text, margins, and viewport issues."),
        ("Why does z-index not work?", "z-index depends on stacking contexts and positioning; a larger number does not always cross stacking contexts."),
        ("Why does height: 100% not work?", "Percentage height requires a defined height on the containing block."),
        ("Why does position: fixed behave strangely?", "Transforms or certain containing contexts can affect how fixed positioning behaves."),
        ("Why does my button move when text changes?", "Its dimensions may depend on content. Set appropriate sizing, padding, or layout constraints."),
        ("Why does the site look fine on desktop but terrible on mobile?", "The layout probably lacks responsive rules, flexible sizing, and mobile-specific breakpoints."),
        ("Why is text overflowing its container?", "The content may be too long or unbreakable. Check overflow, word breaking, width and white-space."),
        ("Why does my image stretch?", "Use responsive sizing such as max-width:100% and appropriate object-fit behavior.")
    ],

    "Git": [
        ("Why does Git say my branch has diverged?", "Your local and remote branches contain different commits. You need to integrate the histories."),
        ("Why did my commit disappear?", "It may still exist in Git history or reflog even if the branch reference moved."),
        ("Why is Git asking for a username/password?", "Your remote authentication configuration may require a token, SSH key, or credential manager."),
        ("Why does .gitignore not work?", "Already tracked files are not automatically removed from Git just because they were added to .gitignore."),
        ("Why does git push get rejected?", "The remote may contain commits your local branch does not have, or branch protection/authentication may be involved."),
        ("Why did I accidentally commit a secret?", "Remove the secret from the repository and rotate/revoke the credential immediately. Removing it from the latest commit alone may not remove it from history."),
        ("Why does Git say nothing to commit?", "Git sees no changes relative to the current index and working tree."),
        ("Why did merge create conflicts?", "Git could not automatically reconcile incompatible changes in the same parts of files."),
        ("Why is my file renamed only by capitalization?", "Case sensitivity differs between operating systems and filesystems.")
    ],

    "SQL": [
        ("Why is my SQL query returning duplicate rows?", "A JOIN can multiply rows when the relationship is one-to-many or many-to-many."),
        ("Why does WHERE fail with NULL?", "NULL represents an unknown value. Use IS NULL or IS NOT NULL rather than = NULL."),
        ("Why is my query extremely slow?", "Check indexes, query plans, joins, filtering, data volume, and unnecessary operations."),
        ("Why does GROUP BY complain?", "Selected non-aggregated columns generally need to appear in the GROUP BY depending on the database."),
        ("Why did my JOIN remove records?", "An INNER JOIN only keeps matching rows. Use an appropriate OUTER JOIN when unmatched rows must remain."),
        ("Why did DELETE remove more rows than expected?", "The WHERE condition may have been too broad or missing."),
        ("Why does my database connection fail?", "Check credentials, hostname, port, database availability, firewall rules, and connection configuration."),
        ("Why is an index not helping?", "The query planner may determine another strategy is cheaper, or the indexed column may not be selective/useful for the query.")
    ],

    "APIs": [
        ("Why am I getting HTTP 404?", "The server was reached but the requested route/resource was not found."),
        ("Why am I getting HTTP 401?", "Authentication is missing or invalid."),
        ("Why am I getting HTTP 403?", "The server understood the request but is refusing access."),
        ("Why am I getting HTTP 500?", "The server encountered an internal error. Check server logs and the failing request path."),
        ("Why does my API work in Postman but not the browser?", "Browser security policies such as CORS, request headers, cookies, or preflight behavior may differ."),
        ("Why is my API returning JSON but my frontend cannot read it?", "Check response headers, CORS, JSON validity, request handling, and frontend parsing."),
        ("Why does POST work but PUT fail?", "Check the route, HTTP method, server implementation, authentication, payload, and content type."),
        ("Why is my API suddenly rate limited?", "The server may enforce request quotas or detect too many requests in a short period.")
    ],

    "Deployment": [
        ("Why does Render build successfully but the site does not start?", "Check whether the service type, start command, listening port, and application binding match the deployment environment."),
        ("Why does my static site show a blank page?", "Check the published root directory, index.html location, JavaScript errors, and asset paths."),
        ("Why do CSS files work locally but not after deployment?", "Check relative paths, filename capitalization, and whether the files were committed."),
        ("Why does GitHub Pages show 404?", "Check the Pages source, branch/folder configuration, repository path, and presence of index.html."),
        ("Why does my deployment fail because a package is missing?", "The dependency may not be declared in the project's dependency file."),
        ("Why does production use an old version?", "Caching, deployment configuration, build artifacts, or an unchanged commit may be responsible."),
        ("Why does an environment variable work locally but not online?", "Local .env files are not automatically available to the hosting environment."),
        ("Why does my server listen on localhost in production?", "A hosted server generally needs to bind to the platform-provided interface/port rather than only localhost.")
    ],

    "Linux": [
        ("Why does Linux say Permission denied?", "The current user may lack the required file permissions, ownership, or execution permission."),
        ("Why does chmod not fix everything?", "Permissions are only one part of access; ownership, parent directory permissions, ACLs, mounts, and security policies can matter."),
        ("Why is my process using 100% CPU?", "Inspect the process, stack/logs, workload, loops, concurrency, and system metrics."),
        ("Why can't I connect to a port?", "Check whether the service is listening, firewall rules, network binding, and routing."),
        ("Why does a command work with sudo but not normally?", "The normal user may lack permissions or environment configuration required by the command.")
    ],

    "Docker": [
        ("Why does it work outside Docker but not inside?", "The container has a different filesystem, network, environment, dependencies, and runtime configuration."),
        ("Why can't my container reach localhost on the host?", "Inside a container, localhost refers to the container itself, not automatically the host."),
        ("Why is my Docker image huge?", "Large base images, package caches, build artifacts, and unnecessary files may be included."),
        ("Why does Docker say port is already allocated?", "Another process or container is already using the host port."),
        ("Why are my container changes gone after restart?", "Container filesystem changes are ephemeral unless persisted appropriately.")
    ],

    "Security": [
        ("Why should I never put API secrets in frontend JavaScript?", "Anything delivered to the browser can be inspected by users. Sensitive credentials belong on trusted server-side systems."),
        ("Why is SQL string concatenation dangerous?", "Untrusted input can alter the intended query. Parameterized queries are the standard defense."),
        ("Why should passwords not be stored as plain text?", "A database compromise would expose every stored password directly. Passwords should be securely hashed with an appropriate password-hashing algorithm."),
        ("Why is user input validation important?", "Input can be malformed or malicious. Validation reduces unexpected behavior and attack surface."),
        ("Why is HTTPS important?", "It protects data in transit against interception and tampering between client and server.")
    ],

    "Debugging": [
        ("The code worked yesterday. What changed?", "Check recent commits, dependency updates, configuration changes, environment differences, external services, and data."),
        ("Why does restarting the app magically fix it?", "Restarting can clear memory state, connections, caches, temporary files, or stuck processes—but it may only hide the underlying bug."),
        ("Why does adding console.log fix the bug?", "It probably changes timing or execution enough to expose a race condition or other timing-sensitive behavior."),
        ("Why can't I reproduce the bug?", "Differences in environment, input data, timing, browser, device, configuration, or deployment may be involved."),
        ("Why does the bug only happen sometimes?", "Intermittent failures often involve race conditions, timing, concurrency, network behavior, resource limits, or non-deterministic data.")
    ]
}

jokes = [
    "Have you tried turning it off and on again?",
    "The bug has officially entered production and requested a promotion.",
    "Works on my machine™.",
    "Congratulations. You have discovered a new undocumented feature.",
    "The compiler is not angry. It is disappointed.",
    "Your code is valid. Your assumptions are not.",
    "It passed all tests because apparently nobody tested THAT.",
    "The missing semicolon has hired a lawyer.",
    "The API returned 500 because it too needs emotional support.",
    "One small CSS change. Three hours later: complete architectural redesign.",
    "Git remembers everything. Unfortunately.",
    "The production server has chosen violence.",
    "This is not a bug. It is a surprise requirement.",
    "You fixed the error. Now there are two errors.",
    "The dependency was updated. Nobody knows why.",
    "Congratulations: your temporary workaround is now legacy infrastructure.",
    "The documentation says it is simple. The documentation is lying.",
    "You don't have technical debt. You have an investment portfolio."
]

html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#111827">
<title>Programmer Error Generator</title>

<style>
* {{
    box-sizing:border-box;
}}

html,body {{
    margin:0;
    min-height:100%;
    font-family:system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
    background:#0b1020;
    color:#f8fafc;
}}

body {{
    min-height:100vh;
    padding:20px;
}}

button {{
    font:inherit;
    touch-action:manipulation;
    -webkit-tap-highlight-color:transparent;
}}

.app {{
    width:min(1100px,100%);
    margin:auto;
}}

header {{
    text-align:center;
    padding:25px 10px 20px;
}}

.logo {{
    font-size:clamp(2rem,7vw,4.5rem);
    font-weight:900;
    letter-spacing:-.06em;
}}

.subtitle {{
    color:#94a3b8;
    margin-top:8px;
    font-size:clamp(.9rem,2vw,1.1rem);
}}

.card {{
    background:#111827;
    border:1px solid #263247;
    border-radius:24px;
    padding:clamp(18px,4vw,35px);
    box-shadow:0 20px 60px rgba(0,0,0,.3);
}}

.meta {{
    display:flex;
    flex-wrap:wrap;
    gap:8px;
    margin-bottom:20px;
}}

.badge {{
    border:1px solid #334155;
    border-radius:999px;
    padding:7px 12px;
    color:#cbd5e1;
    font-size:.85rem;
}}

.problem {{
    font-size:clamp(1.5rem,4vw,2.8rem);
    line-height:1.15;
    font-weight:850;
    margin:10px 0 28px;
}}

.section {{
    background:#0b1220;
    border:1px solid #263247;
    border-radius:16px;
    padding:18px;
    margin-top:15px;
}}

.label {{
    font-size:.75rem;
    text-transform:uppercase;
    letter-spacing:.12em;
    color:#94a3b8;
    font-weight:800;
    margin-bottom:8px;
}}

.answer {{
    line-height:1.65;
    color:#dbeafe;
}}

.joke {{
    font-size:1.05rem;
    line-height:1.5;
    color:#fde68a;
}}

.controls {{
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:12px;
    margin-top:18px;
}}

.btn {{
    min-height:56px;
    border:0;
    border-radius:15px;
    cursor:pointer;
    padding:14px 18px;
    font-weight:800;
    color:white;
    background:#2563eb;
}}

.btn.secondary {{
    background:#1e293b;
    border:1px solid #334155;
}}

.btn:active {{
    transform:scale(.98);
}}

.tip {{
    text-align:center;
    color:#64748b;
    font-size:.8rem;
    margin-top:15px;
}}

footer {{
    text-align:center;
    color:#475569;
    font-size:.8rem;
    padding:25px 0;
}}

@media(max-width:600px) {{
    body {{
        padding:10px;
    }}

    .card {{
        border-radius:18px;
        padding:16px;
    }}

    .controls {{
        grid-template-columns:1fr;
    }}

    .btn {{
        min-height:58px;
    }}
}}

@media(pointer:coarse) {{
    .btn {{
        min-height:64px;
        padding:16px;
    }}
}}
</style>
</head>

<body>
<div class="app">

<header>
    <div class="logo">🧑‍💻 ERROR GENERATOR</div>
    <div class="subtitle">
        Real programming problems. Automatic explanations. Completely unnecessary jokes.
    </div>
</header>

<main class="card">

    <div class="meta">
        <span class="badge" id="category"></span>
        <span class="badge" id="difficulty"></span>
        <span class="badge" id="number"></span>
    </div>

    <div class="problem" id="problem"></div>

    <div class="section">
        <div class="label">🤖 Diagnosis</div>
        <div class="answer" id="answer"></div>
    </div>

    <div class="section">
        <div class="label">😂 Programmer's Reality</div>
        <div class="joke" id="joke"></div>
    </div>

    <div class="controls">
        <button class="btn" onclick="generate()">🎲 NEXT ERROR</button>
        <button class="btn secondary" onclick="location.reload()">🔄 REFRESH PAGE</button>
    </div>

    <div class="tip">
        No database • No LocalStorage • No cookies • No backend
    </div>

</main>

<footer>
    Programmer Error Generator • Static HTML • Built with Python
</footer>

</div>

<script>
const DATA = {json.dumps(categories, ensure_ascii=False)};
const JOKES = {json.dumps(jokes, ensure_ascii=False)};

let counter = 0;

function randomItem(array) {{
    return array[Math.floor(Math.random() * array.length)];
}}

function generate() {{
    const category = randomItem(Object.keys(DATA));
    const item = randomItem(DATA[category]);

    const difficulties = [
        "Easy",
        "Medium",
        "Hard",
        "Production",
        "Why Is This Happening?"
    ];

    document.getElementById("category").textContent = "💻 " + category;
    document.getElementById("difficulty").textContent =
        "🔥 " + randomItem(difficulties);

    document.getElementById("number").textContent =
        "#"+(++counter);

    document.getElementById("problem").textContent = item[0];
    document.getElementById("answer").textContent = item[1];
    document.getElementById("joke").textContent = randomItem(JOKES);
}}

generate();
</script>

</body>
</html>
'''

Path("index.html").write_text(html, encoding="utf-8")

print("Created index.html")
print("Ready for GitHub Pages or Render Static Site.")
