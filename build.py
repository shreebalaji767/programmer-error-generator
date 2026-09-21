from pathlib import Path
import json
import html


# ============================================================
# PROGRAMMER ERROR GENERATOR
# Static Site Builder
#
# Run:
#     python build.py
#
# Output:
#     index.html
#
# The generated index.html is completely standalone.
# It requires:
#     - No database
#     - No backend
#     - No LocalStorage
#     - No cookies
#     - No external JavaScript libraries
#     - No external CSS libraries
#
# Works on:
#     - GitHub Pages
#     - Render Static Site
#     - Netlify
#     - Cloudflare Pages
#     - Any normal static web server
# ============================================================


OUTPUT_FILE = Path("index.html")


# ============================================================
# SCENARIO DATABASE
# ============================================================

SCENARIOS = [

    # ========================================================
    # JAVASCRIPT
    # ========================================================

    {
        "category": "JavaScript",
        "title": "Cannot read properties of undefined",
        "error": "TypeError: Cannot read properties of undefined (reading 'name')",
        "symptom": "Your code works until a particular object is missing.",
        "cause": "The code assumes a property exists, but the object is undefined.",
        "check": "Inspect the object immediately before the failing line.",
        "fix": "Validate the object before accessing nested properties. Optional chaining may also help.",
        "example": "user.profile.name",
        "difficulty": "Beginner",
        "severity": "High",
        "joke": "JavaScript looked for your object. Your object had other plans."
    },

    {
        "category": "JavaScript",
        "title": "Variable is not defined",
        "error": "ReferenceError: x is not defined",
        "symptom": "The browser stops execution immediately.",
        "cause": "A variable name is misspelled, declared in another scope, or never declared.",
        "check": "Check spelling, declaration order, and scope.",
        "fix": "Declare the variable with let, const, or var and verify the correct scope.",
        "example": "console.log(userNmae);",
        "difficulty": "Beginner",
        "severity": "Medium",
        "joke": "The variable exists in your imagination."
    },

    {
        "category": "JavaScript",
        "title": "Undefined is not a function",
        "error": "TypeError: foo.bar is not a function",
        "symptom": "Calling a method suddenly crashes the program.",
        "cause": "The property exists but is not actually a function.",
        "check": "Use typeof before calling it.",
        "fix": "Verify the object's shape and method name.",
        "example": "user.save();",
        "difficulty": "Beginner",
        "severity": "Medium",
        "joke": "You called a function. It filed for unemployment."
    },

    {
        "category": "JavaScript",
        "title": "Async function forgot await",
        "error": "Promise { <pending> }",
        "symptom": "Instead of actual data, you receive a Promise.",
        "cause": "An asynchronous function was called without awaiting its result.",
        "check": "Look at the value returned by the function.",
        "fix": "Use await inside an async function or explicitly handle the Promise with then/catch.",
        "example": "const user = getUser();",
        "difficulty": "Intermediate",
        "severity": "High",
        "joke": "You asked for the answer before the computer finished thinking."
    },

    {
        "category": "JavaScript",
        "title": "JSON parsing failure",
        "error": "SyntaxError: Unexpected token '<', \"<!DOCTYPE...\" is not valid JSON",
        "symptom": "fetch().json() suddenly fails.",
        "cause": "The server returned HTML instead of JSON, often because an API URL is wrong.",
        "check": "Inspect the Network tab and response body.",
        "fix": "Verify the endpoint, HTTP status, and Content-Type before parsing JSON.",
        "example": "const data = await response.json();",
        "difficulty": "Intermediate",
        "severity": "High",
        "joke": "You ordered JSON. The server delivered a webpage."
    },

    {
        "category": "JavaScript",
        "title": "Fetch silently failed",
        "error": "TypeError: Failed to fetch",
        "symptom": "The request never appears to return usable data.",
        "cause": "Network failure, CORS, DNS, HTTPS mismatch, blocked request, or server outage.",
        "check": "Open DevTools Network and Console.",
        "fix": "Check the URL, CORS headers, protocol, server status, and browser security errors.",
        "example": "fetch('https://example.com/api')",
        "difficulty": "Intermediate",
        "severity": "High",
        "joke": "The network has entered witness protection."
    },

    {
        "category": "JavaScript",
        "title": "Event listener never fires",
        "error": "No exception — nothing happens",
        "symptom": "You click the button and absolutely nothing happens.",
        "cause": "Wrong selector, listener attached before the element exists, or incorrect event name.",
        "check": "Log the selected element and verify it is not null.",
        "fix": "Correct the selector and attach listeners after DOM creation.",
        "example": "document.querySelector('#submit')",
        "difficulty": "Beginner",
        "severity": "Medium",
        "joke": "The button has chosen silence."
    },

    {
        "category": "JavaScript",
        "title": "this is not what you expected",
        "error": "TypeError: Cannot read properties of undefined",
        "symptom": "A method suddenly loses access to its object.",
        "cause": "The function was passed around and lost its original this context.",
        "check": "Inspect how the function is called.",
        "fix": "Use arrow functions, bind(), or call/apply where appropriate.",
        "example": "const fn = user.sayName; fn();",
        "difficulty": "Advanced",
        "severity": "Medium",
        "joke": "JavaScript's this is apparently philosophical."
    },

    {
        "category": "JavaScript",
        "title": "Race condition",
        "error": "No consistent error",
        "symptom": "The same code sometimes works and sometimes fails.",
        "cause": "Multiple asynchronous operations finish in an unpredictable order.",
        "check": "Log timestamps and request IDs.",
        "fix": "Control concurrency, cancel stale requests, or serialize dependent operations.",
        "example": "search('a'); search('ab'); search('abc');",
        "difficulty": "Advanced",
        "severity": "Critical",
        "joke": "The bug only appears when you're trying to demonstrate that it exists."
    },

    {
        "category": "JavaScript",
        "title": "Memory leak",
        "error": "Page becomes slower over time",
        "symptom": "Memory usage increases every time a component or page section is recreated.",
        "cause": "Event listeners, timers, subscriptions, or references were never cleaned up.",
        "check": "Use browser memory profiling and inspect event listeners.",
        "fix": "Remove listeners, clear timers, unsubscribe, and release references.",
        "example": "setInterval(update, 1000);",
        "difficulty": "Advanced",
        "severity": "High",
        "joke": "The application remembers everything except why it is slow."
    },

    {
        "category": "JavaScript",
        "title": "Closure captures wrong value",
        "error": "Unexpected loop output",
        "symptom": "Every callback prints the same value.",
        "cause": "A closure captured a changing variable instead of a new per-iteration binding.",
        "check": "Inspect let/const versus var and callback creation.",
        "fix": "Use block-scoped variables or explicitly capture the value.",
        "example": "for (var i = 0; i < 3; i++) setTimeout(() => console.log(i));",
        "difficulty": "Intermediate",
        "severity": "Medium",
        "joke": "All three callbacks agreed that the answer is 3."
    },

    {
        "category": "JavaScript",
        "title": "Module import failure",
        "error": "Uncaught SyntaxError: The requested module does not provide an export named",
        "symptom": "The browser refuses to load a module.",
        "cause": "Named/default exports do not match between files.",
        "check": "Compare export and import syntax exactly.",
        "fix": "Correct the export type and imported name.",
        "example": "import { calculate } from './math.js';",
        "difficulty": "Intermediate",
        "severity": "High",
        "joke": "The module has a name. Unfortunately, it is not the name you used."
    },

    {
        "category": "JavaScript",
        "title": "Event loop surprise",
        "error": "Output order is unexpected",
        "symptom": "setTimeout appears to run before or after code you thought was synchronous.",
        "cause": "Microtasks and macrotasks execute according to the JavaScript event loop.",
        "check": "Separate synchronous code, Promise callbacks, and timers.",
        "fix": "Understand task queues and avoid relying on accidental timing.",
        "example": "console.log(1); Promise.resolve().then(() => console.log(2)); setTimeout(() => console.log(3));",
        "difficulty": "Advanced",
        "severity": "Medium",
        "joke": "The event loop is not late. Your understanding of time is."
    },


    # ========================================================
    # PYTHON
    # ========================================================

    {
        "category": "Python",
        "title": "IndentationError",
        "error": "IndentationError: unexpected indent",
        "symptom": "Python refuses to start your program.",
        "cause": "Indentation does not match Python's block structure.",
        "check": "Look for mixed tabs/spaces and inconsistent indentation.",
        "fix": "Use consistent indentation, normally four spaces.",
        "example": "if user:\\n    print(user)\\n      print('hello')",
        "difficulty": "Beginner",
        "severity": "High",
        "joke": "Python does not use braces. Python uses emotional indentation."
    },

    {
        "category": "Python",
        "title": "ModuleNotFoundError",
        "error": "ModuleNotFoundError: No module named 'flask'",
        "symptom": "An import works on one computer but not another.",
        "cause": "The dependency is not installed in the active Python environment.",
        "check": "Run python -m pip show package and verify the interpreter.",
        "fix": "Install the package in the correct virtual environment.",
        "example": "import flask",
        "difficulty": "Beginner",
        "severity": "High",
        "joke": "The package exists. Just not in this universe."
    },

    {
        "category": "Python",
        "title": "Wrong Python interpreter",
        "error": "Package installed but import still fails",
        "symptom": "pip says the package is installed, but Python cannot import it.",
        "cause": "pip and python point to different environments.",
        "check": "Compare python --version, python -m pip --version, and the IDE interpreter.",
        "fix": "Use python -m pip and select the correct virtual environment.",
        "example": "python -m pip install requests",
        "difficulty": "Beginner",
        "severity": "High",
        "joke": "You installed the package. Just not where your program lives."
    },

    {
        "category": "Python",
        "title": "KeyError",
        "error": "KeyError: 'email'",
        "symptom": "Dictionary access crashes unexpectedly.",
        "cause": "The requested key is missing.",
        "check": "Print dictionary keys before accessing the value.",
        "fix": "Use get(), validate input, or handle the missing key explicitly.",
        "example": "email = user['email']",
        "difficulty": "Beginner",
        "severity": "Medium",
        "joke": "The dictionary looked inside itself and said: never heard of email."
    },

    {
        "category": "Python",
        "title": "IndexError",
        "error": "IndexError: list index out of range",
        "symptom": "Accessing a list element crashes.",
        "cause": "The requested index does not exist.",
        "check": "Print len(list) and the index.",
        "fix": "Validate indexes and handle empty lists.",
        "example": "items[5]",
        "difficulty": "Beginner",
        "severity": "Medium",
        "joke": "You asked for item number six. The list brought five."
    },

    {
        "category": "Python",
        "title": "AttributeError",
        "error": "AttributeError: 'NoneType' object has no attribute",
        "symptom": "A method or property is missing.",
        "cause": "The object is None or is not the type you expected.",
        "check": "Inspect the object's type and value.",
        "fix": "Trace where the value became None and validate it before use.",
        "example": "user.name",
        "difficulty": "Beginner",
        "severity": "High",
        "joke": "None has arrived to personally ruin your afternoon."
    },

    {
        "category": "Python",
        "title": "Mutable default argument",
        "error": "Function remembers old values",
        "symptom": "Calling a function repeatedly unexpectedly shares data.",
        "cause": "A mutable default argument is created once when the function is defined.",
        "check": "Look for defaults such as items=[] or data={}.",
        "fix": "Use None as the default and create the object inside the function.",
        "example": "def add(x, items=[]):",
        "difficulty": "Intermediate",
        "severity": "Medium",
        "joke": "The function has a better memory than you wanted."
    },

    {
        "category": "Python",
        "title": "Circular import",
        "error": "ImportError: cannot import name",
        "symptom": "Two modules depend on each other during startup.",
        "cause": "Module A imports B while B imports A.",
        "check": "Inspect the import graph.",
        "fix": "Move shared code to another module or restructure dependencies.",
        "example": "module_a.py ↔ module_b.py",
        "difficulty": "Advanced",
        "severity": "High",
        "joke": "Module A needs Module B. Module B needs Module A. Nobody gets to work."
    },

    {
        "category": "Python",
        "title": "Encoding problem",
        "error": "UnicodeDecodeError",
        "symptom": "Reading a file works on one machine but fails on another.",
        "cause": "The file encoding and the encoding assumed by Python differ.",
        "check": "Inspect the file encoding.",
        "fix": "Specify the correct encoding explicitly, commonly UTF-8.",
        "example": "open('data.txt', encoding='utf-8')",
        "difficulty": "Intermediate",
        "severity": "Medium",
        "joke": "The text speaks UTF-8. Your program speaks ancient runes."
    },


    # ========================================================
    # HTML / CSS
    # ========================================================

    {
        "category": "HTML/CSS",
        "title": "CSS does absolutely nothing",
        "error": "No error",
        "symptom": "You change CSS and the page refuses to change.",
        "cause": "Wrong selector, stylesheet not loaded, specificity conflict, or browser cache.",
        "check": "Inspect the element in DevTools and check which rule wins.",
        "fix": "Verify the stylesheet path and selector, then inspect computed styles.",
        "example": ".button { color: red; }",
        "difficulty": "Beginner",
        "severity": "Medium",
        "joke": "CSS has acknowledged your request and chosen not to respond."
    },

    {
        "category": "HTML/CSS",
        "title": "404 for CSS file",
        "error": "GET /style.css 404",
        "symptom": "The page loads unstyled.",
        "cause": "Incorrect relative path or file name.",
        "check": "Open the CSS URL directly.",
        "fix": "Correct the path and capitalization.",
        "example": "<link rel='stylesheet' href='css/style.css'>",
        "difficulty": "Beginner",
        "severity": "High",
        "joke": "The stylesheet went out for milk."
    },

    {
        "category": "HTML/CSS",
        "title": "Mobile page is zoomed out",
        "error": "No browser error",
        "symptom": "The desktop layout appears tiny on a phone.",
        "cause": "Missing viewport meta tag.",
        "check": "Inspect the document head.",
        "fix": "Add the standard viewport meta tag.",
        "example": "<meta name='viewport' content='width=device-width, initial-scale=1.0'>",
        "difficulty": "Beginner",
        "severity": "High",
        "joke": "Your phone is showing the website from orbit."
    },

    {
        "category": "HTML/CSS",
        "title": "Z-index refuses to work",
        "error": "No error",
        "symptom": "An element stays behind another element despite a huge z-index.",
        "cause": "Stacking contexts, positioning, transforms, opacity, or parent stacking contexts.",
        "check": "Inspect parent elements and stacking contexts.",
        "fix": "Understand which stacking context each element belongs to.",
        "example": "z-index: 999999;",
        "difficulty": "Intermediate",
        "severity": "Medium",
        "joke": "You gave it z-index 999999. The parent said no."
    },

    {
        "category": "HTML/CSS",
        "title": "Flexbox child refuses to shrink",
        "error": "No error",
        "symptom": "Content overflows its container.",
        "cause": "Default min-width behavior or long unbreakable content.",
        "check": "Inspect min-width and flex properties.",
        "fix": "Try min-width: 0 and appropriate flex settings.",
        "example": ".item { min-width: 0; }",
        "difficulty": "Intermediate",
        "severity": "Medium",
        "joke": "The flex item has decided it deserves the entire screen."
    },

    {
        "category": "HTML/CSS",
        "title": "100vh mobile layout problem",
        "error": "No error",
        "symptom": "A full-screen mobile page is slightly too tall or causes scrolling.",
        "cause": "Mobile browser UI changes the effective viewport.",
        "check": "Test on actual mobile devices and inspect viewport units.",
        "fix": "Consider modern dynamic viewport units such as 100dvh.",
        "example": "height: 100vh;",
        "difficulty": "Intermediate",
        "severity": "Medium",
        "joke": "The browser toolbar has entered the calculation."
    },

    {
        "category": "HTML/CSS",
        "title": "Button works on desktop but not touch",
        "error": "No error",
        "symptom": "Touch users struggle to activate controls.",
        "cause": "Tiny hit areas, hover-only interactions, overlapping elements, or touch-action issues.",
        "check": "Test with an actual touchscreen.",
        "fix": "Use sufficiently large touch targets and avoid hover-only functionality.",
        "example": "button { min-height: 44px; }",
        "difficulty": "Intermediate",
        "severity": "High",
        "joke": "The mouse is happy. The finger has filed a complaint."
    },


    # ========================================================
    # GIT / GITHUB
    # ========================================================

    {
        "category": "Git/GitHub",
        "title": "Changes are not showing in Git",
        "error": "git status shows nothing",
        "symptom": "You edited a file but Git says the repository is clean.",
        "cause": "The file may be ignored, outside the repository, or the wrong file was edited.",
        "check": "Run git status and inspect the repository path.",
        "fix": "Verify the working directory and .gitignore.",
        "example": "git status",
        "difficulty": "Beginner",
        "severity": "High",
        "joke": "Git has reviewed your work and decided it never happened."
    },

    {
        "category": "Git/GitHub",
        "title": "Non-fast-forward push",
        "error": "rejected: non-fast-forward",
        "symptom": "GitHub refuses your push.",
        "cause": "The remote branch contains commits that your local branch does not have.",
        "check": "Fetch the remote branch and inspect the commit history.",
        "fix": "Integrate the remote changes using pull/rebase or merge, then push.",
        "example": "git push origin main",
        "difficulty": "Beginner",
        "severity": "High",
        "joke": "GitHub says someone got there first."
    },

    {
        "category": "Git/GitHub",
        "title": "Merge conflict",
        "error": "<<<<<<< HEAD",
        "symptom": "Git stops a merge because the same lines changed.",
        "cause": "Two branches modified overlapping content.",
        "check": "Open the files containing conflict markers.",
        "fix": "Choose the intended content, remove conflict markers, test, and commit.",
        "example": "<<<<<<< HEAD\\n=======\\n>>>>>>> branch",
        "difficulty": "Intermediate",
        "severity": "High",
        "joke": "Two programmers edited the same line. The line is now a battlefield."
    },

    {
        "category": "Git/GitHub",
        "title": "Detached HEAD",
        "error": "You are in 'detached HEAD' state",
        "symptom": "Commits appear disconnected from your branch.",
        "cause": "HEAD points directly to a commit rather than a branch.",
        "check": "Run git status and git branch.",
        "fix": "Create or switch to a branch before continuing important work.",
        "example": "git checkout abc1234",
        "difficulty": "Intermediate",
        "severity": "Medium",
        "joke": "HEAD has left the branch. Please remain calm."
    },

    {
        "category": "Git/GitHub",
        "title": "Accidentally committed a secret",
        "error": "No Git error",
        "symptom": "An API key or password was pushed to GitHub.",
        "cause": "Secrets were included in tracked files.",
        "check": "Review the commit and repository history.",
        "fix": "Revoke the exposed secret immediately and remove it from the repository/history as appropriate.",
        "example": "API_KEY='super-secret'",
        "difficulty": "Advanced",
        "severity": "Critical",
        "joke": "Congratulations. Your secret is now public knowledge."
    },

    {
        "category": "Git/GitHub",
        "title": "Wrong remote repository",
        "error": "Everything up-to-date",
        "symptom": "You push successfully but the expected GitHub repository does not change.",
        "cause": "The local repository points to a different remote.",
        "check": "Run git remote -v.",
        "fix": "Update the remote URL.",
        "example": "git remote -v",
        "difficulty": "Beginner",
        "severity": "High",
        "joke": "You successfully deployed to the wrong universe."
    },


    # ========================================================
    # SQL / DATABASES
    # ========================================================

    {
        "category": "SQL/Database",
        "title": "SQL syntax error",
        "error": "You have an error in your SQL syntax",
        "symptom": "The database refuses to execute the query.",
        "cause": "Invalid SQL syntax, missing comma, quote, keyword, or incorrect SQL dialect.",
        "check": "Run the smallest possible version of the query.",
        "fix": "Check syntax and the database engine's documentation.",
        "example": "SELECT name age FROM users;",
        "difficulty": "Beginner",
        "severity": "High",
        "joke": "SQL asked you to please use punctuation."
    },

    {
        "category": "SQL/Database",
        "title": "NULL comparison",
        "error": "Query returns zero rows",
        "symptom": "A query looking for NULL values finds nothing.",
        "cause": "NULL is not compared with = or !=.",
        "check": "Look at WHERE conditions involving NULL.",
        "fix": "Use IS NULL or IS NOT NULL.",
        "example": "WHERE deleted_at = NULL",
        "difficulty": "Beginner",
        "severity": "Medium",
        "joke": "NULL is not zero. NULL is not empty. NULL is NULL."
    },

    {
        "category": "SQL/Database",
        "title": "Duplicate rows after JOIN",
        "error": "No SQL error",
        "symptom": "A query returns more rows than expected.",
        "cause": "The JOIN relationship produces multiple matches.",
        "check": "Inspect cardinality and join keys.",
        "fix": "Correct the join condition or intentionally aggregate/deduplicate where appropriate.",
        "example": "SELECT * FROM users JOIN orders ON users.id = orders.user_id;",
        "difficulty": "Intermediate",
        "severity": "High",
        "joke": "The database did exactly what you asked. You just didn't mean it."
    },

    {
        "category": "SQL/Database",
        "title": "Unique constraint violation",
        "error": "duplicate key value violates unique constraint",
        "symptom": "Insert/update fails.",
        "cause": "A unique column already contains the supplied value.",
        "check": "Find the existing record.",
        "fix": "Handle duplicates according to application requirements.",
        "example": "INSERT INTO users(email) VALUES('a@example.com');",
        "difficulty": "Beginner",
        "severity": "Medium",
        "joke": "The database has already met this person."
    },

    {
        "category": "SQL/Database",
        "title": "N+1 query problem",
        "error": "No error",
        "symptom": "One page causes hundreds or thousands of database queries.",
        "cause": "Related records are queried individually inside a loop.",
        "check": "Inspect database query logs.",
        "fix": "Use joins, eager loading, batching, or carefully designed queries.",
        "example": "for user in users: load_orders(user.id)",
        "difficulty": "Advanced",
        "severity": "Critical",
        "joke": "One query became 10,001 because nobody was watching."
    },

    {
        "category": "SQL/Database",
        "title": "Database migration mismatch",
        "error": "column does not exist",
        "symptom": "Application code expects a column missing from production.",
        "cause": "Migration was not applied or environments are out of sync.",
        "check": "Compare database schema and migration history.",
        "fix": "Run the appropriate migrations and verify deployment order.",
        "example": "SELECT new_column FROM users;",
        "difficulty": "Intermediate",
        "severity": "Critical",
        "joke": "The code has moved on. The database has not."
    },


    # ========================================================
    # HTTP / API
    # ========================================================

    {
        "category": "HTTP/API",
        "title": "400 Bad Request",
        "error": "HTTP 400",
        "symptom": "The server rejects the request.",
        "cause": "Malformed request, invalid parameters, or invalid JSON.",
        "check": "Inspect the exact request body, query parameters, and headers.",
        "fix": "Send the payload in the format required by the API.",
        "example": "POST /api/users",
        "difficulty": "Beginner",
        "severity": "Medium",
        "joke": "The server understood your request well enough to reject it."
    },

    {
        "category": "HTTP/API",
        "title": "401 Unauthorized",
        "error": "HTTP 401",
        "symptom": "A protected endpoint refuses access.",
        "cause": "Missing, expired, invalid, or incorrectly formatted authentication credentials.",
        "check": "Inspect Authorization headers, cookies, and token expiration.",
        "fix": "Authenticate correctly and refresh expired credentials.",
        "example": "Authorization: Bearer TOKEN",
        "difficulty": "Intermediate",
        "severity": "High",
        "joke": "The server knows who you are. It just doesn't trust you."
    },

    {
        "category": "HTTP/API",
        "title": "403 Forbidden",
        "error": "HTTP 403",
        "symptom": "Authentication succeeds but access is denied.",
        "cause": "Insufficient permissions or server policy.",
        "check": "Inspect the authenticated user's roles and server authorization rules.",
        "fix": "Use an account with appropriate permission or correct the authorization logic.",
        "example": "GET /admin",
        "difficulty": "Intermediate",
        "severity": "High",
        "joke": "You are authenticated. Congratulations. You still can't enter."
    },

    {
        "category": "HTTP/API",
        "title": "404 Not Found",
        "error": "HTTP 404",
        "symptom": "The endpoint or resource cannot be found.",
        "cause": "Wrong URL, route, ID, base path, or deployment configuration.",
        "check": "Copy the exact URL and test it directly.",
        "fix": "Correct the route or resource identifier.",
        "example": "GET /api/usres",
        "difficulty": "Beginner",
        "severity": "Medium",
        "joke": "The server searched everywhere. It found your typo."
    },

    {
        "category": "HTTP/API",
        "title": "405 Method Not Allowed",
        "error": "HTTP 405",
        "symptom": "The endpoint exists but rejects the HTTP method.",
        "cause": "Using GET instead of POST, POST instead of PUT, etc.",
        "check": "Inspect the route's allowed methods.",
        "fix": "Use the method supported by the endpoint.",
        "example": "POST /api/users",
        "difficulty": "Beginner",
        "severity": "Medium",
        "joke": "The endpoint is real. It just doesn't accept your handshake."
    },

    {
        "category": "HTTP/API",
        "title": "429 Too Many Requests",
        "error": "HTTP 429",
        "symptom": "API calls suddenly stop working.",
        "cause": "Rate limit exceeded.",
        "check": "Inspect response headers and API documentation.",
        "fix": "Respect rate limits, add backoff, caching, batching, or request throttling.",
        "example": "GET /api/data",
        "difficulty": "Intermediate",
        "severity": "High",
        "joke": "The API has asked you to breathe."
    },

    {
        "category": "HTTP/API",
        "title": "500 Internal Server Error",
        "error": "HTTP 500",
        "symptom": "The server crashes while processing the request.",
        "cause": "Unhandled server-side exception or configuration problem.",
        "check": "Read server logs and stack traces.",
        "fix": "Fix the underlying exception rather than hiding the 500 response.",
        "example": "GET /dashboard",
        "difficulty": "Intermediate",
        "severity": "Critical",
        "joke": "The server has experienced a character-building moment."
    },

    {
        "category": "HTTP/API",
        "title": "502 Bad Gateway",
        "error": "HTTP 502",
        "symptom": "A proxy cannot obtain a valid response from the upstream server.",
        "cause": "Backend crashed, wrong port, upstream timeout, or proxy configuration.",
        "check": "Inspect proxy and backend logs.",
        "fix": "Verify backend health, port, networking, and proxy configuration.",
        "example": "Browser → proxy → application",
        "difficulty": "Advanced",
        "severity": "Critical",
        "joke": "The gateway went to ask the backend a question. The backend never answered."
    },

    {
        "category": "HTTP/API",
        "title": "CORS error",
        "error": "Blocked by CORS policy",
        "symptom": "Browser blocks a request that works with curl/Postman.",
        "cause": "The server does not permit the browser's origin or request configuration.",
        "check": "Inspect Console and Network requests, including OPTIONS.",
        "fix": "Configure appropriate server-side CORS headers.",
        "example": "Access-Control-Allow-Origin",
        "difficulty": "Intermediate",
        "severity": "High",
        "joke": "Postman gets VIP access. Your browser needs a permission slip."
    },


    # ========================================================
    # NODE / NPM
    # ========================================================

    {
        "category": "Node/npm",
        "title": "Port already in use",
        "error": "EADDRINUSE: address already in use",
        "symptom": "The Node server refuses to start.",
        "cause": "Another process is already listening on the same port.",
        "check": "Find the process using the port.",
        "fix": "Stop the old process or use another port.",
        "example": "listen(3000)",
        "difficulty": "Beginner",
        "severity": "Medium",
        "joke": "Port 3000 is occupied by your previous version of yourself."
    },

    {
        "category": "Node/npm",
        "title": "npm dependency mismatch",
        "error": "ERESOLVE unable to resolve dependency tree",
        "symptom": "npm install fails after adding or updating a package.",
        "cause": "Incompatible dependency versions or peer dependency requirements.",
        "check": "Read the dependency tree in the npm output.",
        "fix": "Choose compatible versions and update dependencies carefully.",
        "example": "npm install",
        "difficulty": "Intermediate",
        "severity": "High",
        "joke": "Your packages have entered a diplomatic dispute."
    },

    {
        "category": "Node/npm",
        "title": "node_modules missing",
        "error": "Cannot find module",
        "symptom": "The project works locally but not after cloning.",
        "cause": "node_modules is normally not committed to Git.",
        "check": "Look for package.json.",
        "fix": "Run npm install or npm ci.",
        "example": "npm ci",
        "difficulty": "Beginner",
        "severity": "High",
        "joke": "You cloned the project. You forgot to clone the universe around it."
    },

    {
        "category": "Node/npm",
        "title": "ESM/CommonJS conflict",
        "error": "ReferenceError: require is not defined in ES module scope",
        "symptom": "Node rejects import/require syntax.",
        "cause": "The project is configured for a different module system.",
        "check": "Inspect package.json and file extensions.",
        "fix": "Use a consistent module system or configure the project intentionally.",
        "example": "require('./server')",
        "difficulty": "Intermediate",
        "severity": "High",
        "joke": "CommonJS and ESM are currently refusing to speak to each other."
    },


    # ========================================================
    # LINUX / SHELL
    # ========================================================

    {
        "category": "Linux/Shell",
        "title": "Permission denied",
        "error": "bash: ./script.sh: Permission denied",
        "symptom": "A script or file cannot be executed.",
        "cause": "The execute permission is missing.",
        "check": "Run ls -l.",
        "fix": "Set appropriate permissions with chmod when appropriate.",
        "example": "chmod +x script.sh",
        "difficulty": "Beginner",
        "severity": "Medium",
        "joke": "Linux has determined that you are not worthy."
    },

    {
        "category": "Linux/Shell",
        "title": "Command not found",
        "error": "bash: command: command not found",
        "symptom": "A command works on one system but not another.",
        "cause": "Program is not installed or its directory is not in PATH.",
        "check": "Run which command and inspect PATH.",
        "fix": "Install the program or correct PATH configuration.",
        "example": "python",
        "difficulty": "Beginner",
        "severity": "Medium",
        "joke": "Linux has never heard of your command."
    },

    {
        "category": "Linux/Shell",
        "title": "Wrong working directory",
        "error": "No such file or directory",
        "symptom": "Relative paths suddenly stop working.",
        "cause": "The program is running from a different directory.",
        "check": "Run pwd and inspect the current directory.",
        "fix": "Use correct working-directory configuration or robust absolute/pathlib paths.",
        "example": "python app.py",
        "difficulty": "Beginner",
        "severity": "Medium",
        "joke": "The file exists. You are simply standing in the wrong room."
    },

    {
        "category": "Linux/Shell",
        "title": "Environment variable missing",
        "error": "KeyError / empty environment variable",
        "symptom": "Application works locally but fails on the server.",
        "cause": "Required environment variables were not configured.",
        "check": "Inspect deployment environment variables.",
        "fix": "Set required variables in the correct environment.",
        "example": "DATABASE_URL",
        "difficulty": "Intermediate",
        "severity": "Critical",
        "joke": "The application expected a secret. The server expected you to configure it."
    },

    {
        "category": "Linux/Shell",
        "title": "Disk full",
        "error": "No space left on device",
        "symptom": "Writes, builds, logs, or databases suddenly fail.",
        "cause": "Filesystem storage is exhausted.",
        "check": "Run df -h and inspect large files/logs.",
        "fix": "Free space or increase available storage.",
        "example": "df -h",
        "difficulty": "Intermediate",
        "severity": "Critical",
        "joke": "The hard drive has achieved maximum density."
    },


    # ========================================================
    # DOCKER
    # ========================================================

    {
        "category": "Docker",
        "title": "Container exits immediately",
        "error": "Exited (1)",
        "symptom": "Docker starts the container and then immediately stops it.",
        "cause": "The main process exited or crashed.",
        "check": "Run docker logs.",
        "fix": "Fix the startup command or application error.",
        "example": "docker run myapp",
        "difficulty": "Beginner",
        "severity": "Critical",
        "joke": "The container arrived, looked around, and left."
    },

    {
        "category": "Docker",
        "title": "Port mapping confusion",
        "error": "Connection refused",
        "symptom": "The application works inside Docker but cannot be reached from the host.",
        "cause": "Port was not exposed/mapped correctly or application listens on the wrong interface.",
        "check": "Inspect docker ps and application bind address.",
        "fix": "Map the correct port and listen on an accessible interface.",
        "example": "docker run -p 8080:8080 app",
        "difficulty": "Intermediate",
        "severity": "High",
        "joke": "The application is alive inside the container. Nobody outside can visit."
    },

    {
        "category": "Docker",
        "title": "localhost inside Docker",
        "error": "ECONNREFUSED 127.0.0.1",
        "symptom": "One container cannot connect to another using localhost.",
        "cause": "localhost refers to the current container.",
        "check": "Inspect container networking.",
        "fix": "Use the appropriate service/container hostname.",
        "example": "http://localhost:5000",
        "difficulty": "Intermediate",
        "severity": "High",
        "joke": "Inside Docker, localhost means 'me'. Your database is not you."
    },

    {
        "category": "Docker",
        "title": "Docker build context is huge",
        "error": "Build is extremely slow",
        "symptom": "Docker spends a long time sending files before building.",
        "cause": "Large directories such as node_modules or virtual environments are included in the build context.",
        "check": "Inspect .dockerignore.",
        "fix": "Exclude unnecessary files from the Docker build context.",
        "example": ".dockerignore",
        "difficulty": "Intermediate",
        "severity": "Medium",
        "joke": "Docker is currently uploading your entire childhood."
    },


    # ========================================================
    # DEPLOYMENT / HOSTING
    # ========================================================

    {
        "category": "Deployment",
        "title": "Build succeeds but site is blank",
        "error": "Blank page",
        "symptom": "Deployment says successful but the browser shows nothing useful.",
        "cause": "Wrong publish directory, missing index.html, broken JavaScript, or incorrect asset paths.",
        "check": "Open browser DevTools and inspect the deployed files.",
        "fix": "Verify the publish directory and generated output.",
        "example": "Publish Directory: .",
        "difficulty": "Intermediate",
        "severity": "Critical",
        "joke": "Deployment succeeded. The website decided not to participate."
    },

    {
        "category": "Deployment",
        "title": "Render build command fails",
        "error": "Build failed",
        "symptom": "Render cannot complete deployment.",
        "cause": "Build script error, missing dependency, wrong command, or incorrect project structure.",
        "check": "Read the first actual error in the Render build log.",
        "fix": "Correct the failing command or project configuration.",
        "example": "python build.py",
        "difficulty": "Intermediate",
        "severity": "Critical",
        "joke": "The deployment pipeline has discovered character development."
    },

    {
        "category": "Deployment",
        "title": "Static site expects a backend",
        "error": "404 / API request failure",
        "symptom": "Frontend deploys but backend routes do not work.",
        "cause": "A static host only serves static files and does not run Python/Node backend code.",
        "check": "Determine whether the application actually needs server-side execution.",
        "fix": "Use a suitable backend service or convert the feature to client-side logic.",
        "example": "fetch('/api/users')",
        "difficulty": "Intermediate",
        "severity": "Critical",
        "joke": "You asked a photocopier to run Python."
    },

    {
        "category": "Deployment",
        "title": "Case-sensitive filename failure",
        "error": "404 Not Found",
        "symptom": "The site works on Windows but fails after deployment.",
        "cause": "Windows often treats file names as case-insensitive while Linux hosts commonly do not.",
        "check": "Compare exact capitalization of every path.",
        "fix": "Make filenames and references match exactly.",
        "example": "Style.css vs style.css",
        "difficulty": "Beginner",
        "severity": "High",
        "joke": "Windows didn't care about capitalization. Linux absolutely does."
    },

    {
        "category": "Deployment",
        "title": "SPA route returns 404",
        "error": "404 on refresh",
        "symptom": "Navigation works inside the app but refreshing a route gives 404.",
        "cause": "The server does not know how to redirect client-side routes to index.html.",
        "check": "Refresh a non-root route directly.",
        "fix": "Configure fallback routing or use server-compatible routing.",
        "example": "/dashboard",
        "difficulty": "Intermediate",
        "severity": "High",
        "joke": "The frontend knows the route. The server has never met it."
    },


    # ========================================================
    # NETWORKING
    # ========================================================

    {
        "category": "Networking",
        "title": "Connection refused",
        "error": "ECONNREFUSED",
        "symptom": "Client cannot establish a connection.",
        "cause": "Nothing is listening on the target port, or the connection is blocked.",
        "check": "Verify the service is running and listening on the expected port.",
        "fix": "Start the service and verify host/port/firewall configuration.",
        "example": "localhost:5000",
        "difficulty": "Beginner",
        "severity": "High",
        "joke": "The server is home. It is simply not answering the door."
    },

    {
        "category": "Networking",
        "title": "DNS failure",
        "error": "ERR_NAME_NOT_RESOLVED",
        "symptom": "A domain cannot be reached.",
        "cause": "DNS record missing, incorrect, expired, or not propagated.",
        "check": "Use nslookup or dig.",
        "fix": "Correct DNS records and verify nameservers.",
        "example": "example.com",
        "difficulty": "Intermediate",
        "severity": "High",
        "joke": "The internet knows your IP. It has forgotten your name."
    },

    {
        "category": "Networking",
        "title": "HTTPS certificate problem",
        "error": "NET::ERR_CERT_COMMON_NAME_INVALID",
        "symptom": "Browser warns about the HTTPS certificate.",
        "cause": "Certificate does not match the hostname or is incorrectly configured.",
        "check": "Inspect the certificate details.",
        "fix": "Install/configure a certificate covering the correct domain.",
        "example": "https://example.com",
        "difficulty": "Intermediate",
        "severity": "Critical",
        "joke": "The certificate introduced itself. The browser did not recognize it."
    },


    # ========================================================
    # SECURITY
    # ========================================================

    {
        "category": "Security",
        "title": "API key exposed in frontend",
        "error": "No browser error",
        "symptom": "A secret appears in JavaScript or browser DevTools.",
        "cause": "Anything shipped to the browser can be inspected by users.",
        "check": "Search the built frontend for credentials.",
        "fix": "Move sensitive credentials to a trusted backend and rotate exposed secrets.",
        "example": "const API_KEY = 'secret';",
        "difficulty": "Intermediate",
        "severity": "Critical",
        "joke": "If the browser can read it, assume the user can read it too."
    },

    {
        "category": "Security",
        "title": "SQL injection",
        "error": "Unexpected database behavior",
        "symptom": "User-controlled input changes the structure of a SQL query.",
        "cause": "Untrusted input is concatenated directly into SQL.",
        "check": "Review database query construction.",
        "fix": "Use parameterized queries/prepared statements.",
        "example": "SELECT * FROM users WHERE name = '" + "USER_INPUT" + "';",
        "difficulty": "Advanced",
        "severity": "Critical",
        "joke": "The database should process data, not interpret your user's creative writing."
    },

    {
        "category": "Security",
        "title": "Cross-site scripting",
        "error": "Unexpected script execution",
        "symptom": "User-supplied content is interpreted as executable HTML/JavaScript.",
        "cause": "Untrusted content is inserted into the page without appropriate escaping/sanitization.",
        "check": "Trace how user input reaches the DOM.",
        "fix": "Use safe DOM APIs, contextual output encoding, and appropriate sanitization where needed.",
        "example": "element.innerHTML = userInput",
        "difficulty": "Advanced",
        "severity": "Critical",
        "joke": "You wanted to display text. The browser received instructions."
    },

    {
        "category": "Security",
        "title": "Password stored incorrectly",
        "error": "Security vulnerability",
        "symptom": "User passwords are stored as readable values.",
        "cause": "Passwords were stored directly or using reversible encryption instead of password hashing.",
        "check": "Inspect authentication storage.",
        "fix": "Use a modern password hashing algorithm designed for passwords.",
        "example": "password = 'secret123'",
        "difficulty": "Advanced",
        "severity": "Critical",
        "joke": "Passwords are not collectible trading cards. Do not keep the originals."
    },

    {
        "category": "Security",
        "title": "Path traversal",
        "error": "Unexpected file access",
        "symptom": "A user-controlled filename accesses files outside the intended directory.",
        "cause": "File paths are constructed from untrusted input without proper validation.",
        "check": "Review file handling and path normalization.",
        "fix": "Constrain access to an intended directory and validate/normalize paths safely.",
        "example": "../secret.txt",
        "difficulty": "Advanced",
        "severity": "Critical",
        "joke": "The user asked for one file and accidentally received a guided tour."
    },


    # ========================================================
    # TESTING
    # ========================================================

    {
        "category": "Testing",
        "title": "Flaky test",
        "error": "Test sometimes passes, sometimes fails",
        "symptom": "The same test produces different results.",
        "cause": "Timing, randomness, shared state, network dependencies, or race conditions.",
        "check": "Run the test repeatedly and isolate external dependencies.",
        "fix": "Remove nondeterminism and control test data/time/network behavior.",
        "example": "pytest test_api.py",
        "difficulty": "Advanced",
        "severity": "High",
        "joke": "The test passes when nobody is looking."
    },

    {
        "category": "Testing",
        "title": "Test passes locally but fails in CI",
        "error": "CI test failure",
        "symptom": "Local tests are green but the CI pipeline is red.",
        "cause": "Different OS, runtime, dependencies, environment variables, timezone, or test ordering.",
        "check": "Compare local and CI environments.",
        "fix": "Make environment requirements explicit and reproduce CI conditions locally.",
        "example": "pytest",
        "difficulty": "Intermediate",
        "severity": "High",
        "joke": "Your laptop and CI have different definitions of reality."
    },

    {
        "category": "Testing",
        "title": "Timezone test failure",
        "error": "Expected 10:00 but got 09:00",
        "symptom": "Date/time tests fail depending on machine or environment.",
        "cause": "Implicit local timezone assumptions.",
        "check": "Inspect timezone configuration and date handling.",
        "fix": "Use explicit timezone-aware dates and deterministic test clocks.",
        "example": "datetime.now()",
        "difficulty": "Advanced",
        "severity": "High",
        "joke": "Timezones: because apparently one clock was not complicated enough."
    },


    # ========================================================
    # PERFORMANCE
    # ========================================================

    {
        "category": "Performance",
        "title": "Page is extremely slow",
        "error": "No error",
        "symptom": "The application takes several seconds to become usable.",
        "cause": "Large JavaScript bundles, images, blocking work, slow APIs, or excessive rendering.",
        "check": "Use browser performance tools and network waterfall.",
        "fix": "Measure first, then optimize the actual bottleneck.",
        "example": "bundle.js = 12 MB",
        "difficulty": "Intermediate",
        "severity": "High",
        "joke": "The application is not slow. It is carefully considering your request."
    },

    {
        "category": "Performance",
        "title": "Huge image slows website",
        "error": "No error",
        "symptom": "Pages load slowly, especially on mobile.",
        "cause": "Images are unnecessarily large or unoptimized.",
        "check": "Inspect image sizes in Network tools.",
        "fix": "Resize, compress, modernize formats, and serve appropriately sized images.",
        "example": "hero.jpg = 8 MB",
        "difficulty": "Beginner",
        "severity": "High",
        "joke": "The hero image weighs more than the website."
    },

    {
        "category": "Performance",
        "title": "Blocking main thread",
        "error": "Long task",
        "symptom": "Scrolling and clicking become unresponsive.",
        "cause": "Expensive JavaScript blocks the browser's main thread.",
        "check": "Use the Performance panel.",
        "fix": "Break work into smaller tasks, optimize algorithms, or move suitable work off the main thread.",
        "example": "for (...) { hugeCalculation(); }",
        "difficulty": "Advanced",
        "severity": "High",
        "joke": "The browser is busy calculating the meaning of life."
    },


    # ========================================================
    # IDE / TOOLING
    # ========================================================

    {
        "category": "IDE/Tooling",
        "title": "IDE uses wrong interpreter",
        "error": "Import unresolved",
        "symptom": "The terminal works but the editor shows errors.",
        "cause": "The IDE is configured to use a different runtime or virtual environment.",
        "check": "Inspect the selected interpreter.",
        "fix": "Select the project's actual interpreter/environment.",
        "example": "Python: Select Interpreter",
        "difficulty": "Beginner",
        "severity": "Medium",
        "joke": "Your editor and terminal have broken up."
    },

    {
        "category": "IDE/Tooling",
        "title": "Formatter changes everything",
        "error": "Huge diff",
        "symptom": "A tiny edit produces hundreds of changed lines.",
        "cause": "Formatter configuration differs between environments or files were reformatted.",
        "check": "Inspect the Git diff and formatter configuration.",
        "fix": "Standardize formatting settings and avoid unrelated formatting changes.",
        "example": "prettier / black",
        "difficulty": "Beginner",
        "severity": "Medium",
        "joke": "You changed one line. The formatter took it personally."
    },


    # ========================================================
    # GENERAL DEBUGGING
    # ========================================================

    {
        "category": "Debugging",
        "title": "Works on my machine",
        "error": "No error locally",
        "symptom": "Your program works perfectly on your computer and nowhere else.",
        "cause": "Environment, dependency, OS, configuration, path, runtime, or data differences.",
        "check": "Compare versions, environment variables, dependencies, OS, and configuration.",
        "fix": "Make the environment reproducible and document dependencies.",
        "example": "python --version",
        "difficulty": "Beginner",
        "severity": "Critical",
        "joke": "The most famous production-ready sentence: Works on my machine™."
    },

    {
        "category": "Debugging",
        "title": "Console.log fixed it",
        "error": "No error after adding logging",
        "symptom": "Adding a debug statement makes the bug disappear.",
        "cause": "Timing, race condition, initialization order, or another side effect.",
        "check": "Suspect timing-sensitive behavior.",
        "fix": "Find the underlying synchronization or state-management problem.",
        "example": "console.log('here');",
        "difficulty": "Advanced",
        "severity": "High",
        "joke": "The debugger has discovered quantum mechanics."
    },

    {
        "category": "Debugging",
        "title": "Only fails in production",
        "error": "Production-only failure",
        "symptom": "Everything works locally but production fails.",
        "cause": "Configuration, environment, build mode, permissions, data, traffic, or infrastructure differences.",
        "check": "Compare production and local configuration and inspect production logs.",
        "fix": "Reproduce the production environment and add observability.",
        "example": "DEBUG=false",
        "difficulty": "Advanced",
        "severity": "Critical",
        "joke": "Production has unlocked the secret boss level."
    },

    {
        "category": "Debugging",
        "title": "Bug disappears when inspected",
        "error": "Cannot reproduce",
        "symptom": "Opening DevTools changes the behavior.",
        "cause": "Timing-sensitive race condition, debugger pause, caching, or optimization behavior.",
        "check": "Compare execution with and without debugging.",
        "fix": "Instrument the system with non-invasive structured logging and investigate timing.",
        "example": "breakpoint",
        "difficulty": "Advanced",
        "severity": "High",
        "joke": "The bug knows when you are watching."
    },

    {
        "category": "Debugging",
        "title": "Temporary fix became permanent",
        "error": "Mystery workaround",
        "symptom": "Nobody remembers why an apparently unnecessary line exists.",
        "cause": "A workaround was added during debugging and never documented or removed.",
        "check": "Search commit history and issue tracker.",
        "fix": "Document intentional workarounds and remove obsolete ones.",
        "example": "setTimeout(..., 1000)",
        "difficulty": "Intermediate",
        "severity": "Medium",
        "joke": "Temporary code has successfully obtained permanent residency."
    },

    {
        "category": "Debugging",
        "title": "One tiny CSS change breaks everything",
        "error": "Layout catastrophe",
        "symptom": "Changing one style causes unrelated elements to move.",
        "cause": "Shared selectors, flex/grid behavior, inherited styles, or cascading dependencies.",
        "check": "Inspect computed styles and layout containers.",
        "fix": "Scope styles carefully and simplify the layout structure.",
        "example": "* { box-sizing: border-box; }",
        "difficulty": "Intermediate",
        "severity": "Medium",
        "joke": "You changed padding. Civilization collapsed."
    },

    {
        "category": "Debugging",
        "title": "Restart fixed it",
        "error": "No error after restart",
        "symptom": "Restarting the application makes the issue disappear.",
        "cause": "Stale state, cache, leaked resources, corrupted temporary data, or initialization order.",
        "check": "Determine what state was reset by restarting.",
        "fix": "Identify and correct the underlying state-management problem.",
        "example": "restart server",
        "difficulty": "Intermediate",
        "severity": "Medium",
        "joke": "Have you tried turning it off and on again? Unfortunately, yes."
    },


    # ========================================================
    # FRONTEND / FRAMEWORK STYLE PROBLEMS
    # ========================================================

    {
        "category": "Frontend",
        "title": "State updated but UI did not change",
        "error": "No exception",
        "symptom": "Application state appears updated but the screen remains unchanged.",
        "cause": "Mutation happened without triggering the framework's expected update mechanism.",
        "check": "Inspect state references and component rendering.",
        "fix": "Use the framework's recommended immutable/update pattern.",
        "example": "state.items.push(item)",
        "difficulty": "Intermediate",
        "severity": "High",
        "joke": "The data changed. The UI did not receive the memo."
    },

    {
        "category": "Frontend",
        "title": "Component renders endlessly",
        "error": "Maximum update depth exceeded",
        "symptom": "CPU usage spikes and the page becomes unusable.",
        "cause": "A state update or effect continuously triggers another render.",
        "check": "Inspect render-triggering effects and dependencies.",
        "fix": "Break the render/update loop and ensure effects have correct dependencies.",
        "example": "setState() during render",
        "difficulty": "Advanced",
        "severity": "Critical",
        "joke": "The component has discovered infinite employment."
    },

    {
        "category": "Frontend",
        "title": "Stale state",
        "error": "Old value used unexpectedly",
        "symptom": "A callback sees an earlier state value.",
        "cause": "Closure captured state from an earlier render.",
        "check": "Inspect callback creation and state dependencies.",
        "fix": "Use appropriate functional updates, dependencies, or refs according to the framework.",
        "example": "setTimeout(() => console.log(count), 1000)",
        "difficulty": "Advanced",
        "severity": "High",
        "joke": "The callback is living in the past."
    },


    # ========================================================
    # DATA / FILES
    # ========================================================

    {
        "category": "Files/Data",
        "title": "File not found",
        "error": "FileNotFoundError: [Errno 2] No such file or directory",
        "symptom": "A file exists but the program cannot find it.",
        "cause": "Wrong working directory or relative path.",
        "check": "Print the current working directory and resolved path.",
        "fix": "Use reliable path handling and verify the deployment working directory.",
        "example": "open('data/report.txt')",
        "difficulty": "Beginner",
        "severity": "High",
        "joke": "The file exists. The program just has terrible navigation skills."
    },

    {
        "category": "Files/Data",
        "title": "CSV parsing problem",
        "error": "Malformed CSV",
        "symptom": "Rows or columns appear shifted.",
        "cause": "Quotes, commas, delimiters, encodings, or line endings differ from expectations.",
        "check": "Open the raw CSV and inspect problematic rows.",
        "fix": "Use a proper CSV parser and configure delimiter/encoding correctly.",
        "example": "name,address,phone",
        "difficulty": "Intermediate",
        "severity": "Medium",
        "joke": "CSV looks simple until somebody puts a comma inside an address."
    },

    {
        "category": "Files/Data",
        "title": "CRLF versus LF",
        "error": "Unexpected line endings",
        "symptom": "Scripts behave differently across operating systems.",
        "cause": "Windows and Unix-like systems commonly use different line-ending conventions.",
        "check": "Inspect file line endings.",
        "fix": "Configure consistent line-ending behavior for the project.",
        "example": "\\r\\n vs \\n",
        "difficulty": "Intermediate",
        "severity": "Medium",
        "joke": "Even the invisible newline characters are arguing."
    },


    # ========================================================
    # DATABASE CONNECTION
    # ========================================================

    {
        "category": "Database Connection",
        "title": "Database connection refused",
        "error": "connection refused",
        "symptom": "Application cannot connect to the database.",
        "cause": "Database is down, wrong host/port, network issue, or firewall restriction.",
        "check": "Verify database status and connection settings.",
        "fix": "Correct host, port, credentials, networking, and service status.",
        "example": "postgres://localhost:5432/app",
        "difficulty": "Intermediate",
        "severity": "Critical",
        "joke": "The application knocked. The database pretended nobody was home."
    },

    {
        "category": "Database Connection",
        "title": "Connection pool exhausted",
        "error": "Timeout acquiring connection",
        "symptom": "Requests become slow and eventually fail.",
        "cause": "Connections are not returned to the pool or demand exceeds configured capacity.",
        "check": "Inspect connection pool metrics and application code.",
        "fix": "Close/release connections correctly and tune the pool based on measured demand.",
        "example": "pool.acquire()",
        "difficulty": "Advanced",
        "severity": "Critical",
        "joke": "Every database connection has been invited to a meeting that never ends."
    },


    # ========================================================
    # TIME / DATE
    # ========================================================

    {
        "category": "Date/Time",
        "title": "Off-by-one-day date bug",
        "error": "Date displayed one day earlier",
        "symptom": "A date looks correct in one timezone and wrong in another.",
        "cause": "UTC/local timezone conversion changes the calendar date.",
        "check": "Inspect the exact timestamp and timezone at every conversion.",
        "fix": "Distinguish date-only values from timestamps and use explicit timezone handling.",
        "example": "new Date('2026-09-21')",
        "difficulty": "Advanced",
        "severity": "High",
        "joke": "The calendar has crossed an international border."
    },

    {
        "category": "Date/Time",
        "title": "Daylight saving surprise",
        "error": "Unexpected one-hour difference",
        "symptom": "Time calculations change around daylight-saving transitions.",
        "cause": "Local civil time is not a fixed-duration timeline.",
        "check": "Inspect timezone rules and whether calculations use local or UTC time.",
        "fix": "Use timezone-aware date/time libraries and explicit semantics.",
        "example": "2026-03-29 02:30",
        "difficulty": "Advanced",
        "severity": "High",
        "joke": "Time itself has changed the rules."
    },


    # ========================================================
    # CACHE
    # ========================================================

    {
        "category": "Caching",
        "title": "Old JavaScript is still loading",
        "error": "No error",
        "symptom": "You deployed new code but the browser appears to use the old version.",
        "cause": "Browser, CDN, service worker, or server cache.",
        "check": "Inspect Network headers and loaded script content.",
        "fix": "Use appropriate cache-control and asset versioning/cache busting.",
        "example": "app.js",
        "difficulty": "Intermediate",
        "severity": "High",
        "joke": "You deployed version 2. The browser is emotionally attached to version 1."
    },

    {
        "category": "Caching",
        "title": "Service worker serving stale content",
        "error": "Old site version appears",
        "symptom": "Refreshing does not show newly deployed files.",
        "cause": "A service worker is serving cached assets.",
        "check": "Inspect Application → Service Workers.",
        "fix": "Update cache strategy and service worker lifecycle correctly.",
        "example": "navigator.serviceWorker",
        "difficulty": "Advanced",
        "severity": "High",
        "joke": "The browser has built a time machine."
    },


    # ========================================================
    # BUILD SYSTEM
    # ========================================================

    {
        "category": "Build Tools",
        "title": "Build works locally but not in CI",
        "error": "Build failed",
        "symptom": "Local build succeeds while the hosting platform fails.",
        "cause": "Different Node/Python versions, missing environment variables, case sensitivity, or dependencies.",
        "check": "Compare build environments.",
        "fix": "Pin versions and make required configuration explicit.",
        "example": "npm run build",
        "difficulty": "Intermediate",
        "severity": "Critical",
        "joke": "Your laptop has features the server has never heard of."
    },

    {
        "category": "Build Tools",
        "title": "Environment variable missing during build",
        "error": "undefined / missing configuration",
        "symptom": "The production bundle contains incorrect configuration.",
        "cause": "Environment variables were unavailable at build time.",
        "check": "Determine whether variables are needed during build or runtime.",
        "fix": "Configure them at the correct stage without exposing secrets to public frontend code.",
        "example": "API_URL",
        "difficulty": "Intermediate",
        "severity": "High",
        "joke": "The variable was invited to production. It never received the invitation."
    },


    # ========================================================
    # RANDOM CLASSIC PROBLEMS
    # ========================================================

    {
        "category": "Classic Programmer Problems",
        "title": "Missing semicolon",
        "error": "SyntaxError",
        "symptom": "A completely unrelated line is reported as the error.",
        "cause": "A previous statement was malformed.",
        "check": "Look one or two lines above the reported location.",
        "fix": "Correct the previous expression or delimiter.",
        "example": "const x = 10\\nconst y = 20",
        "difficulty": "Beginner",
        "severity": "Low",
        "joke": "The error is on line 20 because line 19 committed the crime."
    },

    {
        "category": "Classic Programmer Problems",
        "title": "Off-by-one error",
        "error": "Unexpected first/last item",
        "symptom": "A loop processes one too many or one too few elements.",
        "cause": "Incorrect loop boundary.",
        "check": "Inspect < versus <= and starting index.",
        "fix": "Define exactly which indexes should be included.",
        "example": "for (let i = 0; i <= items.length; i++)",
        "difficulty": "Beginner",
        "severity": "Medium",
        "joke": "The program is off by exactly one. Naturally, the one that matters."
    },

    {
        "category": "Classic Programmer Problems",
        "title": "Infinite loop",
        "error": "Application freezes",
        "symptom": "CPU usage goes to 100% and the program becomes unresponsive.",
        "cause": "Loop condition never becomes false.",
        "check": "Inspect loop variables and exit conditions.",
        "fix": "Ensure loop state changes toward a terminating condition.",
        "example": "while (true) {}",
        "difficulty": "Beginner",
        "severity": "Critical",
        "joke": "The loop has discovered immortality."
    },

    {
        "category": "Classic Programmer Problems",
        "title": "Wrong variable name",
        "error": "ReferenceError / NameError",
        "symptom": "A variable appears to exist but the runtime says it does not.",
        "cause": "Typo or inconsistent naming.",
        "check": "Compare declaration and usage character by character.",
        "fix": "Rename consistently and use editor refactoring tools.",
        "example": "customerName vs custmerName",
        "difficulty": "Beginner",
        "severity": "Low",
        "joke": "One missing letter has defeated forty-five minutes of debugging."
    },

    {
        "category": "Classic Programmer Problems",
        "title": "Copy-paste bug",
        "error": "Wrong value appears",
        "symptom": "One section behaves suspiciously like another.",
        "cause": "Copied code retained an old variable, condition, endpoint, or label.",
        "check": "Compare the duplicated code with its intended context.",
        "fix": "Refactor repeated logic and rename context-specific values.",
        "example": "deleteUser(userId) accidentally calling deleteOrder(orderId)",
        "difficulty": "Beginner",
        "severity": "Medium",
        "joke": "Ctrl+C and Ctrl+V have accepted no responsibility."
    },

    {
        "category": "Classic Programmer Problems",
        "title": "Wrong environment",
        "error": "Everything looks correct but behavior differs",
        "symptom": "Development, staging, and production behave differently.",
        "cause": "Different configuration or dependencies.",
        "check": "Compare environment variables, versions, feature flags, and services.",
        "fix": "Make environments reproducible and configuration explicit.",
        "example": "development vs production",
        "difficulty": "Intermediate",
        "severity": "Critical",
        "joke": "Same code. Different universe."
    },

    {
        "category": "Classic Programmer Problems",
        "title": "Forgot to save the file",
        "error": "Old behavior",
        "symptom": "You keep testing code that contains your previous version.",
        "cause": "The latest editor changes were never saved.",
        "check": "Look at the file timestamp and editor tab.",
        "fix": "Save before testing; configure auto-save if appropriate.",
        "example": "Ctrl+S",
        "difficulty": "Beginner",
        "severity": "Low",
        "joke": "The bug was fixed 20 minutes ago. The file was not saved."
    },

    {
        "category": "Classic Programmer Problems",
        "title": "Wrong file edited",
        "error": "No error",
        "symptom": "You change code repeatedly and nothing changes.",
        "cause": "You are editing a duplicate or similarly named file.",
        "check": "Inspect the exact path of the running file.",
        "fix": "Verify the application entry point and file path.",
        "example": "index.html vs old/index.html",
        "difficulty": "Beginner",
        "severity": "Medium",
        "joke": "You fixed the bug in a file the program has never met."
    },

]


# ============================================================
# ADDITIONAL RANDOMIZED REAL-WORLD VARIATIONS
# ============================================================

ENVIRONMENTS = [
    "Local development",
    "Production",
    "GitHub Pages",
    "Render",
    "Docker",
    "Windows",
    "Linux",
    "macOS",
    "Android browser",
    "iPhone browser",
    "iPad browser",
    "CI/CD pipeline",
    "Staging",
    "Development server",
    "Corporate network",
]

MOODS = [
    "Everything was working five minutes ago.",
    "It worked yesterday.",
    "It only fails when someone is watching.",
    "The error disappeared after restarting.",
    "Nobody knows who changed it.",
    "The code looks completely normal.",
    "The logs contain absolutely no useful information.",
    "The application has chosen violence.",
    "Production has become experimental.",
    "The computer appears personally offended.",
]

EXTRA_JOKES = [
    "Have you tried turning it off and on again?",
    "The compiler has opinions.",
    "The server knows what you did.",
    "Git remembers everything.",
    "The bug is hiding behind a perfectly reasonable line of code.",
    "This seemed like a five-minute fix.",
    "The documentation was opened approximately 47 minutes too late.",
    "One more change and it will definitely work.",
    "The solution is probably obvious after you find it.",
    "It worked before the update. Naturally.",
    "The problem is somewhere between the keyboard and production.",
    "The computer has requested a sacrifice.",
    "You fixed one bug and unlocked three DLC bugs.",
    "This is why programmers drink coffee.",
    "The code passed review. The universe did not.",
]


# ============================================================
# CATEGORY COLORS / ICONS
# ============================================================

CATEGORY_ICONS = {
    "JavaScript": "🟨",
    "Python": "🐍",
    "HTML/CSS": "🎨",
    "Git/GitHub": "🔀",
    "SQL/Database": "🗄️",
    "HTTP/API": "🌐",
    "Node/npm": "🟢",
    "Linux/Shell": "🐧",
    "Docker": "🐳",
    "Deployment": "🚀",
    "Networking": "📡",
    "Security": "🔐",
    "Testing": "🧪",
    "Performance": "⚡",
    "IDE/Tooling": "🛠️",
    "Debugging": "🐛",
    "Frontend": "🖥️",
    "Files/Data": "📁",
    "Database Connection": "🔌",
    "Date/Time": "🕐",
    "Caching": "💾",
    "Build Tools": "🏗️",
    "Classic Programmer Problems": "💀",
}


# ============================================================
# JSON FOR JAVASCRIPT
# ============================================================

SCENARIO_JSON = json.dumps(
    SCENARIOS,
    ensure_ascii=False,
    separators=(",", ":")
)

ENVIRONMENT_JSON = json.dumps(
    ENVIRONMENTS,
    ensure_ascii=False,
    separators=(",", ":")
)

MOOD_JSON = json.dumps(
    MOODS,
    ensure_ascii=False,
    separators=(",", ":")
)

JOKES_JSON = json.dumps(
    EXTRA_JOKES,
    ensure_ascii=False,
    separators=(",", ":")
)

CATEGORY_JSON = json.dumps(
    CATEGORY_ICONS,
    ensure_ascii=False,
    separators=(",", ":")
)


# ============================================================
# HTML
# ============================================================

HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">

<meta
    name="viewport"
    content="width=device-width, initial-scale=1.0, viewport-fit=cover"
>

<meta
    name="description"
    content="Programmer Error Generator — random real-world programming problems, errors, causes, fixes and programmer jokes."
>

<meta name="theme-color" content="#080b12">

<title>Programmer Error Generator</title>

<style>

:root {
    --bg: #080b12;
    --bg2: #0d111b;
    --panel: #111722;
    --panel2: #151c29;
    --border: #263246;
    --text: #f2f5f9;
    --muted: #9da9ba;
    --green: #61ff9a;
    --yellow: #ffd166;
    --red: #ff6577;
    --blue: #65b7ff;
    --purple: #b18cff;
    --shadow: 0 20px 60px rgba(0,0,0,.38);
}

* {
    box-sizing: border-box;
}

html {
    min-height: 100%;
    background: var(--bg);
    scroll-behavior: smooth;
}

body {
    margin: 0;
    min-height: 100vh;
    background:
        radial-gradient(circle at top left, rgba(97,255,154,.07), transparent 30%),
        radial-gradient(circle at top right, rgba(101,183,255,.07), transparent 30%),
        var(--bg);
    color: var(--text);
    font-family:
        Inter,
        ui-sans-serif,
        system-ui,
        -apple-system,
        BlinkMacSystemFont,
        "Segoe UI",
        sans-serif;
    -webkit-font-smoothing: antialiased;
}

button,
input,
select {
    font: inherit;
}

button {
    -webkit-tap-highlight-color: transparent;
    touch-action: manipulation;
}

a {
    color: inherit;
}

.app {
    width: min(1200px, calc(100% - 28px));
    margin: 0 auto;
    padding: 22px 0 50px;
}

/* HEADER */

.header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 18px;
    margin-bottom: 22px;
}

.logo {
    display: inline-flex;
    align-items: center;
    gap: 11px;
    text-decoration: none;
    color: var(--text);
    cursor: pointer;
    user-select: none;
}

.logo-icon {
    width: 48px;
    height: 48px;
    display: grid;
    place-items: center;
    border: 1px solid var(--border);
    background: var(--panel);
    border-radius: 14px;
    font-size: 24px;
    box-shadow: var(--shadow);
}

.logo-text {
    display: flex;
    flex-direction: column;
}

.logo-title {
    font-weight: 800;
    font-size: 17px;
    letter-spacing: -.3px;
}

.logo-subtitle {
    font-size: 12px;
    color: var(--muted);
    margin-top: 2px;
}

/* HERO */

.hero {
    text-align: center;
    padding: 28px 10px 26px;
}

.badge {
    display: inline-flex;
    align-items: center;
    gap: 7px;
    border: 1px solid rgba(97,255,154,.2);
    background: rgba(97,255,154,.06);
    color: var(--green);
    border-radius: 999px;
    padding: 7px 12px;
    font-size: 12px;
    font-weight: 800;
    letter-spacing: .3px;
    text-transform: uppercase;
}

.hero h1 {
    margin: 15px 0 10px;
    font-size: clamp(34px, 7vw, 70px);
    line-height: .98;
    letter-spacing: -3px;
}

.hero h1 span {
    color: var(--green);
}

.hero p {
    margin: 0 auto;
    max-width: 720px;
    color: var(--muted);
    font-size: clamp(14px, 2vw, 17px);
    line-height: 1.7;
}

/* CONTROLS */

.controls {
    display: grid;
    grid-template-columns: 1fr 230px auto;
    gap: 10px;
    margin-bottom: 18px;
}

.control {
    min-height: 50px;
    border: 1px solid var(--border);
    border-radius: 13px;
    background: rgba(17,23,34,.9);
    color: var(--text);
    padding: 0 15px;
    outline: none;
}

.control:focus {
    border-color: var(--green);
    box-shadow: 0 0 0 3px rgba(97,255,154,.08);
}

select.control {
    cursor: pointer;
}

.search-wrap {
    position: relative;
}

.search-wrap input {
    width: 100%;
    padding-left: 42px;
}

.search-icon {
    position: absolute;
    left: 15px;
    top: 50%;
    transform: translateY(-50%);
    color: var(--muted);
    pointer-events: none;
}

.button {
    min-height: 50px;
    padding: 0 20px;
    border-radius: 13px;
    border: 1px solid var(--border);
    background: var(--panel);
    color: var(--text);
    cursor: pointer;
    font-weight: 800;
    transition:
        transform .12s ease,
        border-color .12s ease,
        background .12s ease;
}

.button:hover {
    border-color: #41516a;
    background: var(--panel2);
}

.button:active {
    transform: scale(.97);
}

.button.primary {
    background: var(--green);
    color: #061009;
    border-color: var(--green);
}

.button.primary:hover {
    background: #7bffac;
}

/* MAIN CARD */

.card {
    border: 1px solid var(--border);
    border-radius: 22px;
    background:
        linear-gradient(
            145deg,
            rgba(21,28,41,.96),
            rgba(13,17,27,.96)
        );
    box-shadow: var(--shadow);
    overflow: hidden;
}

.card-top {
    padding: 18px 20px;
    border-bottom: 1px solid var(--border);
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 15px;
}

.category {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    color: var(--green);
    font-size: 13px;
    font-weight: 800;
}

.number {
    color: var(--muted);
    font-size: 12px;
    font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
}

.card-body {
    padding: clamp(20px, 5vw, 38px);
}

.title-row {
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    gap: 20px;
}

.title {
    margin: 0;
    font-size: clamp(27px, 5vw, 46px);
    line-height: 1.08;
    letter-spacing: -1.8px;
}

.tags {
    display: flex;
    flex-wrap: wrap;
    gap: 7px;
    justify-content: flex-end;
}

.tag {
    display: inline-flex;
    align-items: center;
    min-height: 28px;
    border-radius: 999px;
    padding: 4px 9px;
    border: 1px solid var(--border);
    color: var(--muted);
    font-size: 11px;
    font-weight: 800;
    white-space: nowrap;
}

.tag.high,
.tag.critical {
    color: var(--red);
    border-color: rgba(255,101,119,.25);
    background: rgba(255,101,119,.06);
}

.tag.beginner {
    color: var(--green);
    border-color: rgba(97,255,154,.25);
    background: rgba(97,255,154,.05);
}

.tag.intermediate {
    color: var(--yellow);
    border-color: rgba(255,209,102,.25);
    background: rgba(255,209,102,.05);
}

.tag.advanced {
    color: var(--purple);
    border-color: rgba(177,140,255,.25);
    background: rgba(177,140,255,.05);
}

.error-box {
    margin: 25px 0;
    padding: 18px;
    border: 1px solid rgba(255,101,119,.2);
    background: rgba(255,101,119,.045);
    border-radius: 14px;
}

.error-label {
    color: var(--red);
    font-size: 11px;
    font-weight: 900;
    letter-spacing: .8px;
    text-transform: uppercase;
    margin-bottom: 9px;
}

.error-text {
    color: #ffd8dd;
    font-family:
        ui-monospace,
        SFMono-Regular,
        Menlo,
        Monaco,
        Consolas,
        monospace;
    font-size: 14px;
    line-height: 1.65;
    white-space: pre-wrap;
    overflow-wrap: anywhere;
}

.grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 12px;
}

.info {
    padding: 17px;
    border: 1px solid var(--border);
    border-radius: 14px;
    background: rgba(8,11,18,.35);
}

.info-label {
    color: var(--muted);
    font-size: 11px;
    font-weight: 900;
    letter-spacing: .7px;
    text-transform: uppercase;
    margin-bottom: 7px;
}

.info-text {
    font-size: 14px;
    line-height: 1.65;
}

.code-box {
    margin-top: 12px;
    padding: 16px;
    border-radius: 14px;
    background: #070a0f;
    border: 1px solid #202938;
    overflow-x: auto;
}

.code-label {
    color: var(--blue);
    font-size: 11px;
    font-weight: 900;
    text-transform: uppercase;
    margin-bottom: 8px;
}

pre {
    margin: 0;
    color: #d8e1ed;
    font-family:
        ui-monospace,
        SFMono-Regular,
        Menlo,
        Monaco,
        Consolas,
        monospace;
    font-size: 13px;
    line-height: 1.65;
    white-space: pre-wrap;
    overflow-wrap: anywhere;
}

.fix {
    margin-top: 12px;
    border-color: rgba(97,255,154,.18);
    background: rgba(97,255,154,.035);
}

.fix .info-label {
    color: var(--green);
}

.meta-row {
    margin-top: 18px;
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    align-items: center;
}

.environment {
    color: var(--blue);
    font-size: 12px;
    font-weight: 800;
}

.mood {
    color: var(--muted);
    font-size: 12px;
}

/* JOKE */

.joke {
    margin-top: 20px;
    padding: 19px;
    border: 1px dashed #344156;
    border-radius: 14px;
    color: #cfd8e5;
    background: rgba(255,255,255,.018);
    font-size: 14px;
    line-height: 1.6;
}

.joke strong {
    color: var(--yellow);
}

/* ACTIONS */

.actions {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
    margin-top: 22px;
}

.actions .button {
    flex: 1 1 180px;
}

/* STATS */

.stats {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 10px;
    margin-top: 18px;
}

.stat {
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 15px;
    background: rgba(17,23,34,.65);
}

.stat-number {
    font-size: 23px;
    font-weight: 900;
}

.stat-label {
    color: var(--muted);
    font-size: 11px;
    margin-top: 3px;
}

/* FOOTER */

.footer {
    text-align: center;
    padding: 30px 0 10px;
    color: var(--muted);
    font-size: 12px;
    line-height: 1.7;
}

.footer strong {
    color: var(--text);
}

/* MOBILE */

@media (max-width: 820px) {

    .controls {
        grid-template-columns: 1fr 1fr;
    }

    .controls .button {
        grid-column: 1 / -1;
    }

    .title-row {
        flex-direction: column;
    }

    .tags {
        justify-content: flex-start;
    }

    .stats {
        grid-template-columns: repeat(2, 1fr);
    }
}

@media (max-width: 600px) {

    .app {
        width: min(100% - 18px, 1200px);
        padding-top: 10px;
    }

    .header {
        margin-bottom: 5px;
    }

    .logo-icon {
        width: 42px;
        height: 42px;
        border-radius: 12px;
    }

    .logo-title {
        font-size: 15px;
    }

    .hero {
        padding: 25px 4px 22px;
    }

    .hero h1 {
        font-size: clamp(35px, 13vw, 58px);
        letter-spacing: -2.2px;
    }

    .controls {
        grid-template-columns: 1fr;
    }

    .controls .button {
        grid-column: auto;
    }

    .control,
    .button {
        min-height: 54px;
    }

    .card {
        border-radius: 18px;
    }

    .card-top {
        padding: 15px;
    }

    .card-body {
        padding: 18px;
    }

    .grid {
        grid-template-columns: 1fr;
    }

    .actions {
        flex-direction: column;
    }

    .actions .button {
        width: 100%;
        flex-basis: auto;
    }

    .stats {
        grid-template-columns: 1fr 1fr;
    }

    .title {
        font-size: 30px;
    }
}

/* VERY SMALL DEVICES */

@media (max-width: 380px) {

    .app {
        width: calc(100% - 12px);
    }

    .hero h1 {
        font-size: 34px;
    }

    .card-body {
        padding: 14px;
    }

    .stats {
        gap: 7px;
    }

    .stat {
        padding: 12px;
    }
}

/* REDUCED MOTION */

@media (prefers-reduced-motion: reduce) {
    html {
        scroll-behavior: auto;
    }

    *,
    *::before,
    *::after {
        transition: none !important;
        animation: none !important;
    }
}

</style>
</head>

<body>

<div class="app">

    <header class="header">

        <a
            href="./"
            class="logo"
            id="logo"
            aria-label="Refresh Programmer Error Generator"
        >

            <div class="logo-icon">🐛</div>

            <div class="logo-text">
                <div class="logo-title">
                    Programmer Error Generator
                </div>

                <div class="logo-subtitle">
                    Because bugs are forever.
                </div>
            </div>

        </a>

    </header>


    <section class="hero">

        <div class="badge">
            ⚠️ REAL-WORLD PROGRAMMER PROBLEMS
        </div>

        <h1>
            What broke <span>now?</span>
        </h1>

        <p>
            Generate realistic programming errors, symptoms, causes,
            debugging clues, fixes and the occasional emotional damage.
        </p>

    </section>


    <section class="controls">

        <div class="search-wrap">

            <span class="search-icon">⌕</span>

            <input
                id="search"
                class="control"
                type="search"
                placeholder="Search errors, technologies, symptoms..."
                autocomplete="off"
                spellcheck="false"
            >

        </div>

        <select
            id="category"
            class="control"
            aria-label="Filter by category"
        >
            <option value="all">All Categories</option>
        </select>

        <button
            id="randomButton"
            class="button primary"
            type="button"
        >
            🎲 New Error
        </button>

    </section>


    <main id="main">

        <article class="card">

            <div class="card-top">

                <div id="categoryDisplay" class="category">
                    🐛 Debugging
                </div>

                <div id="number" class="number">
                    ERROR #001
                </div>

            </div>


            <div class="card-body">

                <div class="title-row">

                    <h2 id="title" class="title">
                        Loading...
                    </h2>

                    <div id="tags" class="tags"></div>

                </div>


                <div class="error-box">

                    <div class="error-label">
                        Error / Symptom
                    </div>

                    <div id="error" class="error-text">
                        Loading...
                    </div>

                </div>


                <div class="grid">

                    <section class="info">

                        <div class="info-label">
                            What happened?
                        </div>

                        <div id="symptom" class="info-text">
                            Loading...
                        </div>

                    </section>


                    <section class="info">

                        <div class="info-label">
                            Likely cause
                        </div>

                        <div id="cause" class="info-text">
                            Loading...
                        </div>

                    </section>


                    <section class="info">

                        <div class="info-label">
                            Check first
                        </div>

                        <div id="check" class="info-text">
                            Loading...
                        </div>

                    </section>


                    <section class="info fix">

                        <div class="info-label">
                            Possible fix
                        </div>

                        <div id="fix" class="info-text">
                            Loading...
                        </div>

                    </section>

                </div>


                <div class="code-box">

                    <div class="code-label">
                        Example
                    </div>

                    <pre id="example"></pre>

                </div>


                <div class="meta-row">

                    <span id="environment" class="environment">
                        Environment
                    </span>

                    <span>•</span>

                    <span id="mood" class="mood">
                        Everything was working five minutes ago.
                    </span>

                </div>


                <div class="joke">

                    <strong>💀 Programmer wisdom:</strong>

                    <span id="joke">
                        Loading...
                    </span>

                </div>


                <div class="actions">

                    <button
                        id="anotherButton"
                        class="button primary"
                        type="button"
                    >
                        🎲 Generate Another
                    </button>

                    <button
                        id="copyButton"
                        class="button"
                        type="button"
                    >
                        📋 Copy Error
                    </button>

                </div>

            </div>

        </article>


        <section class="stats">

            <div class="stat">
                <div id="scenarioCount" class="stat-number">0</div>
                <div class="stat-label">Real scenarios</div>
            </div>

            <div class="stat">
                <div id="categoryCount" class="stat-number">0</div>
                <div class="stat-label">Categories</div>
            </div>

            <div class="stat">
                <div id="shownCount" class="stat-number">0</div>
                <div class="stat-label">Matching scenarios</div>
            </div>

            <div class="stat">
                <div id="generatedCount" class="stat-number">0</div>
                <div class="stat-label">Generated this visit</div>
            </div>

        </section>

    </main>


    <footer class="footer">

        <strong>Programmer Error Generator</strong>

        <br>

        No database • No account • No LocalStorage • No tracking

        <br>

        Refresh the page and suffer a completely different problem.

    </footer>

</div>


<script>

const SCENARIOS = __SCENARIOS__;
const ENVIRONMENTS = __ENVIRONMENTS__;
const MOODS = __MOODS__;
const EXTRA_JOKES = __JOKES__;
const CATEGORY_ICONS = __CATEGORIES__;


const $ = (id) => document.getElementById(id);


let currentScenario = null;
let generatedCount = 0;
let lastIndex = -1;


/* ----------------------------------------------------------
   RANDOM
---------------------------------------------------------- */

function randomInt(max) {

    if (max <= 0) {
        return 0;
    }

    if (
        window.crypto &&
        window.crypto.getRandomValues
    ) {

        const array = new Uint32Array(1);

        window.crypto.getRandomValues(array);

        return array[0] % max;
    }

    return Math.floor(Math.random() * max);
}


function randomItem(array) {

    if (!array || !array.length) {
        return "";
    }

    return array[randomInt(array.length)];
}


function getDifferentIndex(length, oldIndex) {

    if (length <= 1) {
        return 0;
    }

    let index = randomInt(length);

    while (index === oldIndex) {
        index = randomInt(length);
    }

    return index;
}


/* ----------------------------------------------------------
   ESCAPE HTML
---------------------------------------------------------- */

function escapeHTML(value) {

    return String(value ?? "")
        .replaceAll("&", "&amp;")
        .replaceAll("<", "&lt;")
        .replaceAll(">", "&gt;")
        .replaceAll('"', "&quot;")
        .replaceAll("'", "&#039;");
}


/* ----------------------------------------------------------
   SEARCH
---------------------------------------------------------- */

function scenarioMatches(scenario, query) {

    if (!query) {
        return true;
    }

    const haystack = [
        scenario.category,
        scenario.title,
        scenario.error,
        scenario.symptom,
        scenario.cause,
        scenario.check,
        scenario.fix,
        scenario.example,
        scenario.difficulty,
        scenario.severity,
        scenario.joke
    ]
    .join(" ")
    .toLowerCase();

    return haystack.includes(query.toLowerCase());
}


function getFilteredScenarios() {

    const query = $("search").value.trim();

    const category = $("category").value;

    return SCENARIOS.filter((scenario) => {

        const categoryOK =
            category === "all" ||
            scenario.category === category;

        const searchOK =
            scenarioMatches(scenario, query);

        return categoryOK && searchOK;
    });
}


/* ----------------------------------------------------------
   RENDER
---------------------------------------------------------- */

function renderScenario(scenario, index) {

    currentScenario = scenario;

    $("categoryDisplay").textContent =
        `${CATEGORY_ICONS[scenario.category] || "🐛"} ${scenario.category}`;

    $("number").textContent =
        `ERROR #${String(index + 1).padStart(3, "0")}`;

    $("title").textContent = scenario.title;

    $("error").textContent = scenario.error;

    $("symptom").textContent = scenario.symptom;

    $("cause").textContent = scenario.cause;

    $("check").textContent = scenario.check;

    $("fix").textContent = scenario.fix;

    $("example").textContent = scenario.example;

    $("environment").textContent =
        `📍 ${randomItem(ENVIRONMENTS)}`;

    $("mood").textContent =
        randomItem(MOODS);

    let joke = scenario.joke;

    if (randomInt(4) === 0) {
        joke += " " + randomItem(EXTRA_JOKES);
    }

    $("joke").textContent = joke;


    $("tags").innerHTML = `
        <span class="tag ${scenario.difficulty.toLowerCase()}">
            ${escapeHTML(scenario.difficulty)}
        </span>

        <span class="tag ${scenario.severity.toLowerCase()}">
            ${escapeHTML(scenario.severity)}
        </span>
    `;


    generatedCount++;

    $("generatedCount").textContent = generatedCount;
}


/* ----------------------------------------------------------
   GENERATE
---------------------------------------------------------- */

function generateScenario() {

    const filtered = getFilteredScenarios();

    updateCounts(filtered.length);

    if (!filtered.length) {

        currentScenario = null;

        $("title").textContent = "No matching error";

        $("categoryDisplay").textContent = "🔎 Search";

        $("number").textContent = "NO RESULT";

        $("error").textContent =
            "Try another search or category.";

        $("symptom").textContent =
            "Nothing in the current scenario database matches your search.";

        $("cause").textContent =
            "The search may be too specific.";

        $("check").textContent =
            "Clear the search field or select All Categories.";

        $("fix").textContent =
            "Broaden your search.";

        $("example").textContent =
            "Try: JavaScript, Git, Python, API, Docker, CSS";

        $("environment").textContent = "";

        $("mood").textContent = "";

        $("joke").textContent =
            "Even the error generator cannot find this bug.";

        $("tags").innerHTML = "";

        return;
    }


    const index =
        getDifferentIndex(filtered.length, lastIndex);

    lastIndex = index;

    renderScenario(filtered[index], index);
}


/* ----------------------------------------------------------
   COUNTS
---------------------------------------------------------- */

function updateCounts(matchingCount) {

    $("scenarioCount").textContent =
        SCENARIOS.length;

    $("categoryCount").textContent =
        Object.keys(CATEGORY_ICONS).length;

    $("shownCount").textContent =
        matchingCount;
}


/* ----------------------------------------------------------
   CATEGORY MENU
---------------------------------------------------------- */

function buildCategoryMenu() {

    const select = $("category");

    const categories =
        Object.keys(CATEGORY_ICONS)
            .sort((a, b) => a.localeCompare(b));

    for (const category of categories) {

        const option =
            document.createElement("option");

        option.value = category;

        option.textContent =
            `${CATEGORY_ICONS[category]} ${category}`;

        select.appendChild(option);
    }
}


/* ----------------------------------------------------------
   COPY
---------------------------------------------------------- */

async function copyCurrentScenario() {

    if (!currentScenario) {
        return;
    }

    const text = [
        `PROGRAMMER ERROR: ${currentScenario.title}`,
        ``,
        `Category: ${currentScenario.category}`,
        `Error: ${currentScenario.error}`,
        `Symptom: ${currentScenario.symptom}`,
        `Cause: ${currentScenario.cause}`,
        `Check: ${currentScenario.check}`,
        `Possible Fix: ${currentScenario.fix}`,
        `Example: ${currentScenario.example}`,
        `Difficulty: ${currentScenario.difficulty}`,
        `Severity: ${currentScenario.severity}`,
        `Joke: ${currentScenario.joke}`
    ].join("\n");


    try {

        await navigator.clipboard.writeText(text);

        const button = $("copyButton");

        const oldText = button.textContent;

        button.textContent = "✅ Copied";

        setTimeout(() => {
            button.textContent = oldText;
        }, 1200);

    } catch (error) {

        const textarea =
            document.createElement("textarea");

        textarea.value = text;

        textarea.style.position = "fixed";
        textarea.style.opacity = "0";

        document.body.appendChild(textarea);

        textarea.select();

        try {
            document.execCommand("copy");
        } catch (_) {}

        textarea.remove();
    }
}


/* ----------------------------------------------------------
   EVENTS
---------------------------------------------------------- */

$("randomButton").addEventListener(
    "click",
    generateScenario
);


$("anotherButton").addEventListener(
    "click",
    generateScenario
);


$("copyButton").addEventListener(
    "click",
    copyCurrentScenario
);


$("category").addEventListener(
    "change",
    () => {

        lastIndex = -1;

        generateScenario();
    }
);


$("search").addEventListener(
    "input",
    () => {

        lastIndex = -1;

        generateScenario();
    }
);


/* ----------------------------------------------------------
   LOGO / HOME
   Clicking logo refreshes the site.
---------------------------------------------------------- */

$("logo").addEventListener(
    "click",
    function(event) {

        event.preventDefault();

        window.location.reload();
    }
);


/* ----------------------------------------------------------
   KEYBOARD
---------------------------------------------------------- */

document.addEventListener(
    "keydown",
    function(event) {

        if (
            event.target.tagName === "INPUT" ||
            event.target.tagName === "SELECT" ||
            event.target.tagName === "TEXTAREA"
        ) {
            return;
        }

        if (event.code === "Space" || event.key === "n") {

            event.preventDefault();

            generateScenario();
        }

        if (event.key === "/") {

            event.preventDefault();

            $("search").focus();
        }
    }
);


/* ----------------------------------------------------------
   START
---------------------------------------------------------- */

buildCategoryMenu();

updateCounts(SCENARIOS.length);

generateScenario();

</script>

</body>
</html>
"""


# ============================================================
# INSERT DATA
# ============================================================

HTML = HTML.replace(
    "__SCENARIOS__",
    SCENARIO_JSON
)

HTML = HTML.replace(
    "__ENVIRONMENTS__",
    ENVIRONMENT_JSON
)

HTML = HTML.replace(
    "__MOODS__",
    MOOD_JSON
)

HTML = HTML.replace(
    "__JOKES__",
    JOKES_JSON
)

HTML = HTML.replace(
    "__CATEGORIES__",
    CATEGORY_JSON
)


# ============================================================
# WRITE INDEX.HTML
# ============================================================

OUTPUT_FILE.write_text(
    HTML,
    encoding="utf-8"
)


print()
print("=" * 64)
print(" PROGRAMMER ERROR GENERATOR")
print("=" * 64)
print()
print(f"Generated: {OUTPUT_FILE.resolve()}")
print(f"Scenarios: {len(SCENARIOS)}")
print(f"Categories: {len(CATEGORY_ICONS)}")
print()
print("The generated site is completely static.")
print()
print("No database")
print("No LocalStorage")
print("No cookies")
print("No backend")
print("No external libraries")
print()
print("Ready for GitHub Pages or Render Static Site.")
print()
print("Render settings:")
print("  Build Command: python build.py")
print("  Publish Directory: .")
print()
print("=" * 64)
