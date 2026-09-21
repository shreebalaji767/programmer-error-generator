from pathlib import Path
from html import escape
import json
import random


# ============================================================
# PROGRAMMER ERROR GENERATOR
# Static-site builder
#
# Run:
#     python build.py
#
# Output:
#     index.html
#
# Render Static Site:
#     Build Command: python build.py
#     Publish Directory: .
# ============================================================


OUTPUT_FILE = Path("index.html")


# ============================================================
# SCENARIO DATA
# ============================================================

SCENARIOS = [

    # --------------------------------------------------------
    # JAVASCRIPT
    # --------------------------------------------------------

    {
        "category": "JavaScript",
        "title": "TypeError: Cannot read properties of undefined",
        "error": "TypeError: Cannot read properties of undefined (reading 'name')",
        "cause": "You expected an object to exist. JavaScript had other plans.",
        "fix": "Check the value before accessing the property, or use optional chaining.",
        "joke": "The object went on vacation without telling you."
    },

    {
        "category": "JavaScript",
        "title": "ReferenceError",
        "error": "ReferenceError: x is not defined",
        "cause": "The variable does not exist in the current scope.",
        "fix": "Check spelling, declaration, scope, imports, and execution order.",
        "joke": "You asked JavaScript about someone JavaScript has never met."
    },

    {
        "category": "JavaScript",
        "title": "SyntaxError",
        "error": "SyntaxError: Unexpected token '}'",
        "cause": "A bracket, comma, quote, or other syntax element is wrong.",
        "fix": "Check the line and the code immediately before it.",
        "joke": "One bracket has escaped containment."
    },

    {
        "category": "JavaScript",
        "title": "undefined",
        "error": "undefined",
        "cause": "A function returned nothing, a property is missing, or a variable was never assigned.",
        "fix": "Trace where the value is created and verify every step.",
        "joke": "Congratulations. Your value is technically a value."
    },

    {
        "category": "JavaScript",
        "title": "null is not an object",
        "error": "TypeError: Cannot read properties of null",
        "cause": "Your code expected an object but received null.",
        "fix": "Check whether the object exists before using it.",
        "joke": "Null has entered the chat."
    },

    {
        "category": "JavaScript",
        "title": "Async/Await Disaster",
        "error": "Promise { <pending> }",
        "cause": "You logged or returned a Promise instead of waiting for it.",
        "fix": "Use await inside an async function or handle the Promise with .then().",
        "joke": "The data is coming. Eventually. Probably."
    },

    {
        "category": "JavaScript",
        "title": "Forgotten await",
        "error": "data.map is not a function",
        "cause": "The variable contains a Promise instead of the resolved array.",
        "fix": "Await the asynchronous function before using the result.",
        "joke": "You opened the package before the delivery arrived."
    },

    {
        "category": "JavaScript",
        "title": "this Problem",
        "error": "Cannot read properties of undefined",
        "cause": "The value of this changed because the function was called in a different context.",
        "fix": "Check how the function is invoked or use an arrow function where appropriate.",
        "joke": "this is no longer who you thought this was."
    },

    {
        "category": "JavaScript",
        "title": "Event Listener Mystery",
        "error": "Button clicked. Nothing happens.",
        "cause": "The listener was attached to the wrong element, wrong event, or before the DOM existed.",
        "fix": "Verify the selector, event name, and DOM loading order.",
        "joke": "The button has chosen silence."
    },

    {
        "category": "JavaScript",
        "title": "JSON.parse Attack",
        "error": "SyntaxError: Unexpected token '<' in JSON",
        "cause": "You expected JSON but received HTML.",
        "fix": "Inspect the actual response and HTTP status before parsing it as JSON.",
        "joke": "Your JSON endpoint returned a webpage. Surprise!"
    },

    {
        "category": "JavaScript",
        "title": "Fetch Failed",
        "error": "TypeError: Failed to fetch",
        "cause": "The browser could not complete the request.",
        "fix": "Check URL, server availability, HTTPS, CORS, network connection, and browser console.",
        "joke": "The internet has temporarily misplaced your request."
    },

    {
        "category": "JavaScript",
        "title": "Race Condition",
        "error": "Works sometimes. Fails sometimes.",
        "cause": "Multiple asynchronous operations finish in an unpredictable order.",
        "fix": "Control sequencing, cancellation, locking, or state updates.",
        "joke": "Your program is technically working. Just not in the same timeline."
    },

    {
        "category": "JavaScript",
        "title": "Memory Leak",
        "error": "Browser memory usage: 📈📈📈",
        "cause": "Event listeners, timers, DOM references, or subscriptions were never cleaned up.",
        "fix": "Remove listeners, clear timers, and release references when components are destroyed.",
        "joke": "The garbage collector has filed a complaint."
    },

    {
        "category": "JavaScript",
        "title": "Infinite Loop",
        "error": "Page stopped responding",
        "cause": "A loop condition never becomes false.",
        "fix": "Verify the loop condition and update variables.",
        "joke": "The loop has discovered immortality."
    },

    {
        "category": "JavaScript",
        "title": "Closure Confusion",
        "error": "Why does every callback use the same value?",
        "cause": "Closures captured a variable differently than expected.",
        "fix": "Understand lexical scope and how variables are captured.",
        "joke": "The callback remembered everything except what you wanted."
    },


    # --------------------------------------------------------
    # PYTHON
    # --------------------------------------------------------

    {
        "category": "Python",
        "title": "IndentationError",
        "error": "IndentationError: unexpected indent",
        "cause": "Python found indentation that does not match the expected structure.",
        "fix": "Use consistent spaces and inspect the surrounding block.",
        "joke": "Python takes indentation personally."
    },

    {
        "category": "Python",
        "title": "NameError",
        "error": "NameError: name 'username' is not defined",
        "cause": "The variable was never defined or is outside the current scope.",
        "fix": "Check spelling, scope, and execution order.",
        "joke": "Python has never heard of your username."
    },

    {
        "category": "Python",
        "title": "ModuleNotFoundError",
        "error": "ModuleNotFoundError: No module named 'flask'",
        "cause": "The package is not installed in the Python environment being used.",
        "fix": "Activate the correct virtual environment and install the dependency.",
        "joke": "You installed it. Just not where Python is looking."
    },

    {
        "category": "Python",
        "title": "KeyError",
        "error": "KeyError: 'email'",
        "cause": "You tried to access a dictionary key that does not exist.",
        "fix": "Check the dictionary contents or use .get() where appropriate.",
        "joke": "The dictionary has decided your key is not invited."
    },

    {
        "category": "Python",
        "title": "IndexError",
        "error": "IndexError: list index out of range",
        "cause": "You tried to access a list position that does not exist.",
        "fix": "Check the list length and index boundaries.",
        "joke": "You asked for item #10 in a list containing 3 items."
    },

    {
        "category": "Python",
        "title": "AttributeError",
        "error": "AttributeError: 'NoneType' object has no attribute 'id'",
        "cause": "A variable contains None instead of the expected object.",
        "fix": "Trace where the value becomes None.",
        "joke": "None has once again ruined everyone's afternoon."
    },

    {
        "category": "Python",
        "title": "ValueError",
        "error": "ValueError: invalid literal for int()",
        "cause": "Python received a value that cannot be converted into the requested type.",
        "fix": "Validate or clean the input before conversion.",
        "joke": "The string looked like a number from far away."
    },

    {
        "category": "Python",
        "title": "Mutable Default Argument",
        "error": "Why is my list remembering previous calls?",
        "cause": "A mutable object was used as a function's default argument.",
        "fix": "Use None as the default and create the mutable object inside the function.",
        "joke": "Your function has a better memory than you do."
    },

    {
        "category": "Python",
        "title": "pip vs Python",
        "error": "pip installed package, Python cannot import it",
        "cause": "pip and Python are using different environments.",
        "fix": "Use python -m pip and verify the active interpreter.",
        "joke": "Two Pythons. One package. Zero cooperation."
    },

    {
        "category": "Python",
        "title": "Virtual Environment Problem",
        "error": "ModuleNotFoundError after activating venv",
        "cause": "The wrong environment is active or the dependency was installed elsewhere.",
        "fix": "Check the interpreter path and installed packages.",
        "joke": "Your virtual environment is real. Your dependency is somewhere else."
    },


    # --------------------------------------------------------
    # HTML
    # --------------------------------------------------------

    {
        "category": "HTML",
        "title": "Missing Viewport",
        "error": "Mobile page looks like a tiny desktop website",
        "cause": "The viewport meta tag is missing or incorrect.",
        "fix": "Add the correct viewport meta tag.",
        "joke": "Congratulations. Your phone is pretending to be a 2009 laptop."
    },

    {
        "category": "HTML",
        "title": "Broken Form",
        "error": "Submit button refreshes the entire page",
        "cause": "The form's default browser submission was not prevented.",
        "fix": "Handle the submit event and call preventDefault() when appropriate.",
        "joke": "The browser submitted your hopes and dreams."
    },

    {
        "category": "HTML",
        "title": "Wrong ID",
        "error": "document.getElementById(...) returns null",
        "cause": "The element ID in JavaScript does not match the HTML.",
        "fix": "Compare the HTML id and JavaScript selector character by character.",
        "joke": "One letter is different. Therefore, they are strangers."
    },


    # --------------------------------------------------------
    # CSS
    # --------------------------------------------------------

    {
        "category": "CSS",
        "title": "Why Is This Div Not Centered?",
        "error": "margin: auto; /* still not centered */",
        "cause": "The element's parent or width constraints do not allow the expected centering.",
        "fix": "Inspect the parent layout and use the appropriate flex/grid/alignment rules.",
        "joke": "CSS has rejected your request for alignment."
    },

    {
        "category": "CSS",
        "title": "z-index War",
        "error": "z-index: 999999; /* still behind something */",
        "cause": "Stacking contexts can prevent z-index from behaving as expected.",
        "fix": "Inspect position, stacking contexts, transforms, opacity, and parent elements.",
        "joke": "You added another 9. The problem added another stacking context."
    },

    {
        "category": "CSS",
        "title": "Horizontal Scroll",
        "error": "Mobile page scrolls sideways",
        "cause": "An element is wider than the viewport.",
        "fix": "Inspect fixed widths, large margins, absolute elements, images, and long text.",
        "joke": "Your website has discovered a secret second page."
    },

    {
        "category": "CSS",
        "title": "Mobile Layout Disaster",
        "error": "Desktop: beautiful. Mobile: 💀",
        "cause": "The layout was designed for a large screen without responsive rules.",
        "fix": "Use fluid widths, responsive units, flexible layouts, and media queries.",
        "joke": "Desktop developers fear the 375px viewport."
    },

    {
        "category": "CSS",
        "title": "Flexbox Mystery",
        "error": "display: flex; /* nothing makes sense */",
        "cause": "The parent and child flex properties are interacting differently than expected.",
        "fix": "Inspect flex-direction, justify-content, align-items, flex, width, and height.",
        "joke": "Flexbox is easy. Until it isn't."
    },

    {
        "category": "CSS",
        "title": "100vh on Mobile",
        "error": "The bottom of the page disappears",
        "cause": "Mobile browser UI changes the effective viewport height.",
        "fix": "Consider modern viewport units such as svh, lvh, or dvh.",
        "joke": "100vh apparently means whatever the browser feels like today."
    },


    # --------------------------------------------------------
    # GIT / GITHUB
    # --------------------------------------------------------

    {
        "category": "Git",
        "title": "Detached HEAD",
        "error": "You are in 'detached HEAD' state.",
        "cause": "You checked out a commit instead of working on a branch.",
        "fix": "Create or switch to the intended branch before making work you want to keep.",
        "joke": "Your HEAD is detached. Please reconnect it."
    },

    {
        "category": "Git",
        "title": "Merge Conflict",
        "error": "<<<<<<< HEAD",
        "cause": "Git found conflicting changes that it cannot merge automatically.",
        "fix": "Open the conflicted files, choose the intended code, then stage and commit.",
        "joke": "Two developers touched the same line. Civilization has ended."
    },

    {
        "category": "Git",
        "title": "Push Rejected",
        "error": "rejected: non-fast-forward",
        "cause": "The remote branch contains commits your local branch does not have.",
        "fix": "Fetch/pull the remote changes, resolve conflicts if needed, then push.",
        "joke": "Git refuses to let you overwrite history without a conversation."
    },

    {
        "category": "Git",
        "title": "Wrong Branch",
        "error": "Why is production code in feature-test-please-ignore?",
        "cause": "Changes were committed on the wrong branch.",
        "fix": "Check your current branch before committing.",
        "joke": "The branch name was not a suggestion."
    },

    {
        "category": "Git",
        "title": "Forgot to Add Files",
        "error": "git commit -m \"finished\"",
        "cause": "The actual changes were never staged.",
        "fix": "Check git status before committing.",
        "joke": "You committed the concept of your changes."
    },

    {
        "category": "Git",
        "title": "Secret Accident",
        "error": "API_KEY=abcdef123456789",
        "cause": "A secret was accidentally committed to source control.",
        "fix": "Revoke/rotate the secret immediately and remove it from repository history as appropriate.",
        "joke": "Git remembers everything. Unfortunately."
    },


    # --------------------------------------------------------
    # NODE / NPM
    # --------------------------------------------------------

    {
        "category": "Node.js",
        "title": "Port Already in Use",
        "error": "Error: listen EADDRINUSE",
        "cause": "Another process is already using the requested port.",
        "fix": "Find and stop the process or use another port.",
        "joke": "Port 3000 already has a tenant."
    },

    {
        "category": "Node.js",
        "title": "npm install vs npm ci",
        "error": "Dependencies behave differently on another machine",
        "cause": "Dependency versions or lockfiles are inconsistent.",
        "fix": "Commit the lockfile and use the appropriate reproducible installation command.",
        "joke": "\"Works on my machine\" has entered the dependency tree."
    },

    {
        "category": "Node.js",
        "title": "ES Module Disaster",
        "error": "SyntaxError: Cannot use import statement outside a module",
        "cause": "Node is interpreting the file as CommonJS instead of ESM.",
        "fix": "Configure the project consistently for ESM or CommonJS.",
        "joke": "import and require are having a family dispute."
    },


    # --------------------------------------------------------
    # HTTP / API
    # --------------------------------------------------------

    {
        "category": "HTTP",
        "title": "400 Bad Request",
        "error": "HTTP 400 Bad Request",
        "cause": "The server rejected the request because the input was invalid.",
        "fix": "Inspect the request body, query parameters, headers, and required fields.",
        "joke": "The server understood your request perfectly and rejected it anyway."
    },

    {
        "category": "HTTP",
        "title": "401 Unauthorized",
        "error": "HTTP 401 Unauthorized",
        "cause": "Authentication credentials are missing, invalid, or expired.",
        "fix": "Check login state, token, API key, cookie, or authentication header.",
        "joke": "The server would like to see some identification."
    },

    {
        "category": "HTTP",
        "title": "403 Forbidden",
        "error": "HTTP 403 Forbidden",
        "cause": "The server understood the request but refuses to authorize it.",
        "fix": "Check permissions, roles, access rules, and authentication context.",
        "joke": "You are authenticated. You are still not invited."
    },

    {
        "category": "HTTP",
        "title": "404",
        "error": "HTTP 404 Not Found",
        "cause": "The requested resource or route does not exist at that URL.",
        "fix": "Check the URL, route, deployment path, filename, and capitalization.",
        "joke": "The page has achieved enlightenment and no longer exists."
    },

    {
        "category": "HTTP",
        "title": "405 Method Not Allowed",
        "error": "HTTP 405 Method Not Allowed",
        "cause": "The route exists but does not accept the HTTP method being used.",
        "fix": "Check whether the endpoint expects GET, POST, PUT, PATCH, or DELETE.",
        "joke": "Wrong method. Please try again, but with feelings."
    },

    {
        "category": "HTTP",
        "title": "429 Too Many Requests",
        "error": "HTTP 429 Too Many Requests",
        "cause": "The service has rate-limited the client.",
        "fix": "Respect rate limits, retry with backoff, and avoid unnecessary requests.",
        "joke": "You clicked refresh like it owed you money."
    },

    {
        "category": "HTTP",
        "title": "500 Internal Server Error",
        "error": "HTTP 500 Internal Server Error",
        "cause": "The server encountered an unexpected condition.",
        "fix": "Read server logs and inspect the failing code path.",
        "joke": "The server knows what happened. It refuses to tell you directly."
    },

    {
        "category": "HTTP",
        "title": "502 Bad Gateway",
        "error": "HTTP 502 Bad Gateway",
        "cause": "A gateway or proxy received an invalid response from an upstream server.",
        "fix": "Check the upstream service, proxy configuration, networking, and logs.",
        "joke": "Two servers are arguing. Neither will accept responsibility."
    },

    {
        "category": "HTTP",
        "title": "503 Service Unavailable",
        "error": "HTTP 503 Service Unavailable",
        "cause": "The service is temporarily unable to handle the request.",
        "fix": "Check service health, startup status, capacity, maintenance, and logs.",
        "joke": "The server is taking a mental health day."
    },


    # --------------------------------------------------------
    # CORS
    # --------------------------------------------------------

    {
        "category": "Web Security",
        "title": "CORS",
        "error": "Access to fetch has been blocked by CORS policy",
        "cause": "The browser blocked a cross-origin request because the server's CORS policy does not allow it.",
        "fix": "Configure the server with the appropriate CORS policy.",
        "joke": "The browser has decided two websites cannot be friends."
    },

    {
        "category": "Web Security",
        "title": "Preflight Request",
        "error": "OPTIONS request failed",
        "cause": "The browser sent a CORS preflight request that the server did not handle correctly.",
        "fix": "Check OPTIONS handling and Access-Control-Allow-* headers.",
        "joke": "The browser asked permission before asking the real question."
    },


    # --------------------------------------------------------
    # DATABASE
    # --------------------------------------------------------

    {
        "category": "Database",
        "title": "SQL Syntax Error",
        "error": "SQL syntax error near 'WHERE'",
        "cause": "The SQL statement contains invalid syntax.",
        "fix": "Check commas, quotes, keywords, parentheses, and SQL dialect.",
        "joke": "SQL has rejected your poetry."
    },

    {
        "category": "Database",
        "title": "Duplicate Entry",
        "error": "UNIQUE constraint failed",
        "cause": "A value that must be unique already exists.",
        "fix": "Check existing records before inserting or use the intended upsert behavior.",
        "joke": "The database already knows this person."
    },

    {
        "category": "Database",
        "title": "Foreign Key Error",
        "error": "FOREIGN KEY constraint failed",
        "cause": "A referenced record does not exist or cannot be deleted because it is still referenced.",
        "fix": "Check relationship order and foreign-key constraints.",
        "joke": "The database believes relationships should have consequences."
    },

    {
        "category": "Database",
        "title": "NULL Problem",
        "error": "WHERE name = NULL returned zero rows",
        "cause": "SQL uses special NULL comparison semantics.",
        "fix": "Use IS NULL or IS NOT NULL.",
        "joke": "NULL is not equal to anything. Not even itself."
    },

    {
        "category": "Database",
        "title": "N+1 Query Problem",
        "error": "One page generated 8,742 SQL queries",
        "cause": "The application is repeatedly querying related data inside a loop.",
        "fix": "Use joins, eager loading, batching, or appropriate prefetching.",
        "joke": "Your database is now doing cardio."
    },

    {
        "category": "Database",
        "title": "Migration Disaster",
        "error": "Migration works locally, fails in production",
        "cause": "Database schema or migration history differs between environments.",
        "fix": "Compare schemas, migration versions, permissions, and database engines.",
        "joke": "Production has discovered that your laptop is not production."
    },


    # --------------------------------------------------------
    # DEPLOYMENT
    # --------------------------------------------------------

    {
        "category": "Deployment",
        "title": "Works Locally",
        "error": "Works on my machine",
        "cause": "The development environment differs from the deployment environment.",
        "fix": "Compare versions, environment variables, dependencies, filesystem behavior, and configuration.",
        "joke": "The most reliable error message in software engineering."
    },

    {
        "category": "Deployment",
        "title": "Environment Variable Missing",
        "error": "KeyError: SECRET_KEY",
        "cause": "A required environment variable was not configured in the deployed environment.",
        "fix": "Add the variable to the deployment environment and restart/redeploy if required.",
        "joke": "The variable exists. Just not where the application lives."
    },

    {
        "category": "Deployment",
        "title": "Wrong Start Command",
        "error": "Application failed to start",
        "cause": "The hosting platform is launching the wrong command or entry point.",
        "fix": "Check the start command, working directory, runtime, and application entry file.",
        "joke": "The server arrived at work and nobody told it what to do."
    },

    {
        "category": "Deployment",
        "title": "Static Site Missing index.html",
        "error": "404 after successful deployment",
        "cause": "The hosting platform cannot find the published index.html at the configured publish directory.",
        "fix": "Check the build output and publish directory.",
        "joke": "The website was built. The website was also lost."
    },

    {
        "category": "Deployment",
        "title": "Case-Sensitive Path",
        "error": "Image works locally but not after deployment",
        "cause": "The deployed filesystem may be case-sensitive while the development filesystem is not.",
        "fix": "Make filenames and paths match exactly, including capitalization.",
        "joke": "Logo.png and logo.png are apparently different people."
    },

    {
        "category": "Deployment",
        "title": "Cache Problem",
        "error": "I changed the code but the old website is still showing",
        "cause": "Browser, CDN, service worker, or hosting cache may still contain an older version.",
        "fix": "Inspect caching headers and perform a controlled cache refresh.",
        "joke": "The internet remembers your old code better than you do."
    },


    # --------------------------------------------------------
    # LINUX / TERMINAL
    # --------------------------------------------------------

    {
        "category": "Linux",
        "title": "Permission Denied",
        "error": "bash: ./app: Permission denied",
        "cause": "The file does not have the required execution permissions.",
        "fix": "Check file ownership and permissions and apply the appropriate permission change.",
        "joke": "Linux has decided you are not worthy."
    },

    {
        "category": "Linux",
        "title": "Command Not Found",
        "error": "command not found",
        "cause": "The command is not installed or is not available in PATH.",
        "fix": "Check installation and PATH configuration.",
        "joke": "The terminal has never heard of your command."
    },

    {
        "category": "Linux",
        "title": "Wrong Directory",
        "error": "No such file or directory",
        "cause": "The command is being executed from the wrong working directory or the path is incorrect.",
        "fix": "Run pwd and ls, then verify the path.",
        "joke": "The file exists. You're just somewhere else."
    },


    # --------------------------------------------------------
    # DOCKER
    # --------------------------------------------------------

    {
        "category": "Docker",
        "title": "Container Exited",
        "error": "Exited (1)",
        "cause": "The main process inside the container terminated with an error.",
        "fix": "Inspect container logs and verify the entrypoint and environment.",
        "joke": "The container has left the building."
    },

    {
        "category": "Docker",
        "title": "Port Mapping Confusion",
        "error": "localhost:8000 does not work",
        "cause": "The application port and host/container port mapping are incorrect.",
        "fix": "Check EXPOSE, application bind address, and port mapping.",
        "joke": "The port exists. It just lives in another dimension."
    },

    {
        "category": "Docker",
        "title": "localhost Inside Container",
        "error": "Connection refused to localhost",
        "cause": "Inside a container, localhost refers to that container itself.",
        "fix": "Use the appropriate service/container hostname for inter-container communication.",
        "joke": "localhost has become unexpectedly local."
    },


    # --------------------------------------------------------
    # NETWORKING
    # --------------------------------------------------------

    {
        "category": "Networking",
        "title": "Connection Refused",
        "error": "ECONNREFUSED",
        "cause": "Nothing is accepting connections at the requested host and port.",
        "fix": "Check whether the service is running, listening on the correct interface, and using the correct port.",
        "joke": "The server is home. It is simply refusing visitors."
    },

    {
        "category": "Networking",
        "title": "DNS Problem",
        "error": "DNS_PROBE_FINISHED_NXDOMAIN",
        "cause": "The domain name could not be resolved.",
        "fix": "Check DNS records, nameservers, spelling, and propagation.",
        "joke": "The domain has temporarily become fictional."
    },

    {
        "category": "Networking",
        "title": "Timeout",
        "error": "ETIMEDOUT",
        "cause": "A network operation took too long to complete.",
        "fix": "Check server availability, network connectivity, firewall rules, and timeout settings.",
        "joke": "The request is still thinking about it."
    },


    # --------------------------------------------------------
    # SECURITY
    # --------------------------------------------------------

    {
        "category": "Security",
        "title": "XSS",
        "error": "User input rendered as HTML",
        "cause": "Untrusted input was inserted into a page without appropriate escaping or sanitization.",
        "fix": "Use context-appropriate output encoding and safe DOM APIs.",
        "joke": "Your input field has become a programming language."
    },

    {
        "category": "Security",
        "title": "SQL Injection",
        "error": "SELECT * FROM users WHERE name = '" + "' + userInput + '",
        "cause": "User-controlled input was concatenated into SQL.",
        "fix": "Use parameterized queries or prepared statements.",
        "joke": "The user entered data. The database received instructions."
    },

    {
        "category": "Security",
        "title": "Secret in Frontend",
        "error": "API_SECRET = 'super-secret-key'",
        "cause": "Anything shipped to browser JavaScript should be treated as publicly visible.",
        "fix": "Keep private credentials on the server and use appropriate access controls.",
        "joke": "It was a secret until you uploaded it to the internet."
    },


    # --------------------------------------------------------
    # TESTING
    # --------------------------------------------------------

    {
        "category": "Testing",
        "title": "Flaky Test",
        "error": "Test passed 8 times. Failed on CI.",
        "cause": "The test depends on timing, ordering, external state, randomness, or another unstable condition.",
        "fix": "Remove nondeterminism and isolate the test from external state.",
        "joke": "The test only fails when someone is watching."
    },

    {
        "category": "Testing",
        "title": "Works Alone, Fails Together",
        "error": "1 test passed. 847 tests failed.",
        "cause": "Tests are sharing state or depending on execution order.",
        "fix": "Reset state between tests and remove hidden dependencies.",
        "joke": "Teamwork makes the test fail."
    },


    # --------------------------------------------------------
    # PERFORMANCE
    # --------------------------------------------------------

    {
        "category": "Performance",
        "title": "Slow Page",
        "error": "First Contentful Paint: eventually",
        "cause": "The page may contain oversized assets, blocking JavaScript, excessive network requests, or expensive rendering.",
        "fix": "Profile first, then optimize the actual bottleneck.",
        "joke": "The website is loading one byte at a time out of respect."
    },

    {
        "category": "Performance",
        "title": "Huge Bundle",
        "error": "main.js: 14.8 MB",
        "cause": "Too much code or unnecessary dependencies are being shipped to the browser.",
        "fix": "Analyze the bundle, remove unused dependencies, and use code splitting where appropriate.",
        "joke": "Your button click now requires half the internet."
    },


    # --------------------------------------------------------
    # IDE / TOOLING
    # --------------------------------------------------------

    {
        "category": "Tooling",
        "title": "Wrong Python Interpreter",
        "error": "VS Code: Import could not be resolved",
        "cause": "The editor is using a different Python interpreter than your terminal.",
        "fix": "Select the correct interpreter and verify the environment.",
        "joke": "Your editor and terminal are technically on speaking terms. Barely."
    },

    {
        "category": "Tooling",
        "title": "Formatter War",
        "error": "Save file → code changes itself",
        "cause": "Multiple formatters or lint rules are fighting over the same file.",
        "fix": "Choose one formatter and configure the editor consistently.",
        "joke": "You wrote the code. The formatter rewrote your personality."
    },


    # --------------------------------------------------------
    # GENERAL PROGRAMMER LIFE
    # --------------------------------------------------------

    {
        "category": "Programmer Life",
        "title": "Console.log Fixed It",
        "error": "Added console.log → bug disappeared",
        "cause": "The extra logging changed timing or exposed an ordering issue.",
        "fix": "Investigate race conditions and timing dependencies instead of keeping random logs forever.",
        "joke": "You have discovered quantum debugging."
    },

    {
        "category": "Programmer Life",
        "title": "One-Line Change",
        "error": "Changed one line → 47 other things broke",
        "cause": "The changed code was more connected to the system than expected.",
        "fix": "Use tests, version control, and incremental changes.",
        "joke": "It was only one line. Unfortunately, it was THE line."
    },

    {
        "category": "Programmer Life",
        "title": "Friday Deployment",
        "error": "Production broke at 5:59 PM Friday",
        "cause": "Production systems do not care about your weekend.",
        "fix": "Use testing, reviews, deployment safeguards, monitoring, and rollback plans.",
        "joke": "The server has plans for your weekend."
    },

    {
        "category": "Programmer Life",
        "title": "Temporary Fix",
        "error": "// temporary fix",
        "cause": "The temporary solution has been in production for 3 years.",
        "fix": "Track technical debt and schedule proper cleanup.",
        "joke": "Nothing is more permanent than a temporary solution."
    },

    {
        "category": "Programmer Life",
        "title": "Forgot the Semicolon",
        "error": "Unexpected token",
        "cause": "A tiny syntax detail broke the entire file.",
        "fix": "Read the parser error and inspect the nearby code.",
        "joke": "One tiny punctuation mark controls your career."
    },

    {
        "category": "Programmer Life",
        "title": "It Worked Yesterday",
        "error": "Nothing changed. Everything broke.",
        "cause": "Dependencies, external services, environment state, time, caches, or hidden assumptions may have changed.",
        "fix": "Compare versions, logs, environment, recent changes, and external dependencies.",
        "joke": "Yesterday's computer is today's historical artifact."
    },

    {
        "category": "Programmer Life",
        "title": "Copy-Paste Bug",
        "error": "Why does this function call itself?",
        "cause": "Copied code was not fully adapted to its new context.",
        "fix": "Review copied code line by line instead of assuming it is correct.",
        "joke": "Ctrl+C and Ctrl+V have no quality assurance department."
    },

    {
        "category": "Programmer Life",
        "title": "Missing Comma",
        "error": "Everything looks correct",
        "cause": "One comma is missing somewhere.",
        "fix": "Use the parser error location and inspect the preceding line.",
        "joke": "The comma is hiding. You are now a detective."
    },

    {
        "category": "Programmer Life",
        "title": "The Fix",
        "error": "I don't know why it works.",
        "cause": "The code works but the programmer does not understand why.",
        "fix": "Stop and document the behavior before moving on.",
        "joke": "Never touch it again. It is now sacred."
    },

    {
        "category": "Programmer Life",
        "title": "Production Only Bug",
        "error": "Cannot reproduce locally",
        "cause": "Production has different data, configuration, timing, traffic, dependencies, or infrastructure.",
        "fix": "Compare environments and collect structured logs and diagnostics.",
        "joke": "The bug lives exclusively in production and pays no rent."
    },

]


# ============================================================
# BUILD DATA
# ============================================================

DATA_JSON = json.dumps(SCENARIOS, ensure_ascii=False)


# ============================================================
# COMPLETE HTML
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
    content="Programmer Error Generator - real programming errors, bugs, deployment problems and programmer life disasters."
>

<meta name="theme-color" content="#080b12">

<title>Programmer Error Generator</title>

<style>

:root {
    --bg: #080b12;
    --panel: #101620;
    --panel-2: #151d29;
    --border: #263244;
    --text: #f3f7ff;
    --muted: #98a6ba;
    --accent: #00e5ff;
    --accent-2: #7c4dff;
    --danger: #ff4d6d;
    --success: #39ff88;

    --radius: 20px;

    --page-width: 1100px;
}

/* =========================================================
   RESET
========================================================= */

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

html {
    min-height: 100%;
    background: var(--bg);
    scroll-behavior: smooth;
    -webkit-text-size-adjust: 100%;
}

body {
    min-height: 100vh;
    min-height: 100dvh;

    background:
        radial-gradient(
            circle at top,
            rgba(0, 229, 255, 0.09),
            transparent 35%
        ),
        radial-gradient(
            circle at bottom right,
            rgba(124, 77, 255, 0.08),
            transparent 35%
        ),
        var(--bg);

    color: var(--text);

    font-family:
        Inter,
        system-ui,
        -apple-system,
        BlinkMacSystemFont,
        "Segoe UI",
        Roboto,
        Arial,
        sans-serif;

    line-height: 1.5;

    overflow-x: hidden;

    -webkit-font-smoothing: antialiased;
    text-rendering: optimizeLegibility;
}

/* Prevent ugly tap highlights while keeping usability */
button,
a {
    -webkit-tap-highlight-color: transparent;
}

/* =========================================================
   PAGE
========================================================= */

.page {
    width: min(100%, var(--page-width));
    margin: 0 auto;

    padding:
        max(18px, env(safe-area-inset-top))
        max(16px, env(safe-area-inset-right))
        max(30px, env(safe-area-inset-bottom))
        max(16px, env(safe-area-inset-left));
}

/* =========================================================
   HEADER
========================================================= */

header {
    text-align: center;

    padding:
        clamp(28px, 7vw, 70px)
        0
        clamp(22px, 5vw, 45px);
}

.logo {
    display: inline-flex;

    align-items: center;
    justify-content: center;

    width: clamp(62px, 12vw, 90px);
    height: clamp(62px, 12vw, 90px);

    margin-bottom: 18px;

    border:
        1px solid
        rgba(0, 229, 255, 0.3);

    border-radius: 24px;

    background:
        linear-gradient(
            135deg,
            rgba(0, 229, 255, 0.12),
            rgba(124, 77, 255, 0.16)
        );

    font-size: clamp(30px, 7vw, 48px);

    box-shadow:
        0 0 45px rgba(0, 229, 255, 0.08);

    user-select: none;
}

h1 {
    font-size:
        clamp(2rem, 7vw, 4.8rem);

    line-height: 1.03;

    letter-spacing: -0.05em;

    font-weight: 900;

    overflow-wrap: anywhere;
}

.subtitle {
    max-width: 720px;

    margin: 16px auto 0;

    color: var(--muted);

    font-size:
        clamp(0.95rem, 2.4vw, 1.2rem);
}

/* =========================================================
   GENERATOR CARD
========================================================= */

.generator {
    width: 100%;

    border: 1px solid var(--border);

    border-radius: var(--radius);

    background:
        linear-gradient(
            145deg,
            rgba(255,255,255,0.035),
            rgba(255,255,255,0.015)
        );

    box-shadow:
        0 25px 80px rgba(0,0,0,0.35);

    overflow: hidden;
}

.card-top {
    padding: clamp(16px, 4vw, 30px);

    border-bottom: 1px solid var(--border);

    display: flex;

    align-items: center;

    justify-content: space-between;

    gap: 12px;

    flex-wrap: wrap;
}

.category {
    display: inline-flex;

    align-items: center;

    min-height: 36px;

    padding: 7px 13px;

    border-radius: 999px;

    background:
        rgba(0, 229, 255, 0.09);

    border:
        1px solid
        rgba(0, 229, 255, 0.2);

    color: var(--accent);

    font-size: 0.8rem;

    font-weight: 800;

    letter-spacing: 0.08em;

    text-transform: uppercase;
}

.scenario-number {
    color: var(--muted);

    font-size: 0.8rem;

    font-family:
        ui-monospace,
        SFMono-Regular,
        Menlo,
        Monaco,
        Consolas,
        monospace;
}

/* =========================================================
   ERROR CONTENT
========================================================= */

.error-content {
    padding: clamp(20px, 5vw, 45px);
}

.error-title {
    font-size:
        clamp(1.55rem, 5vw, 2.6rem);

    line-height: 1.15;

    font-weight: 850;

    margin-bottom: 20px;

    overflow-wrap: anywhere;
}

.error-box {
    width: 100%;

    padding:
        clamp(16px, 4vw, 25px);

    margin-bottom: 28px;

    border:
        1px solid
        rgba(255, 77, 109, 0.28);

    border-left:
        4px solid
        var(--danger);

    border-radius: 14px;

    background:
        rgba(255, 77, 109, 0.055);

    overflow-x: auto;

    -webkit-overflow-scrolling: touch;
}

.error-message {
    color: #ff9db0;

    font-family:
        ui-monospace,
        SFMono-Regular,
        Menlo,
        Monaco,
        Consolas,
        monospace;

    font-size:
        clamp(0.82rem, 2.2vw, 1rem);

    line-height: 1.65;

    white-space: pre-wrap;

    overflow-wrap: anywhere;

    word-break: break-word;
}

/* =========================================================
   INFO GRID
========================================================= */

.info-grid {
    display: grid;

    grid-template-columns:
        repeat(3, minmax(0, 1fr));

    gap: 14px;

    margin-bottom: 30px;
}

.info {
    min-width: 0;

    padding: 18px;

    border:
        1px solid
        var(--border);

    border-radius: 15px;

    background:
        rgba(255,255,255,0.025);
}

.info-label {
    margin-bottom: 8px;

    color: var(--muted);

    font-size: 0.72rem;

    font-weight: 800;

    letter-spacing: 0.1em;

    text-transform: uppercase;
}

.info-text {
    color: #e5ebf5;

    font-size:
        clamp(0.9rem, 2vw, 1rem);

    overflow-wrap: anywhere;
}

/* =========================================================
   JOKE
========================================================= */

.joke {
    margin-bottom: 30px;

    padding:
        clamp(17px, 4vw, 25px);

    border:
        1px solid
        rgba(124, 77, 255, 0.3);

    border-radius: 15px;

    background:
        linear-gradient(
            135deg,
            rgba(124, 77, 255, 0.08),
            rgba(0, 229, 255, 0.04)
        );
}

.joke-label {
    color: #bdaeff;

    font-size: 0.72rem;

    font-weight: 900;

    letter-spacing: 0.1em;

    text-transform: uppercase;

    margin-bottom: 7px;
}

.joke-text {
    color: #f0ebff;

    font-size:
        clamp(0.95rem, 2.3vw, 1.1rem);

    font-weight: 600;
}

/* =========================================================
   BUTTON AREA
========================================================= */

.actions {
    display: flex;

    gap: 12px;

    flex-wrap: wrap;
}

button {
    appearance: none;

    border: 0;

    font: inherit;

    cursor: pointer;

    touch-action: manipulation;

    user-select: none;

    min-height: 52px;

    padding:
        13px
        clamp(18px, 4vw, 27px);

    border-radius: 13px;

    font-weight: 850;

    transition:
        transform 0.15s ease,
        box-shadow 0.15s ease,
        background 0.15s ease;

    display: inline-flex;

    align-items: center;

    justify-content: center;

    gap: 9px;
}

.primary {
    color: #001015;

    background:
        linear-gradient(
            135deg,
            var(--accent),
            #65f4ff
        );

    box-shadow:
        0 10px 30px
        rgba(0, 229, 255, 0.14);
}

.secondary {
    color: var(--text);

    border:
        1px solid var(--border);

    background:
        rgba(255,255,255,0.045);
}

button:hover {
    transform: translateY(-2px);
}

button:active {
    transform: translateY(1px) scale(0.98);
}

button:focus-visible {
    outline:
        3px solid
        rgba(0, 229, 255, 0.45);

    outline-offset: 3px;
}

/* =========================================================
   FOOTER
========================================================= */

footer {
    text-align: center;

    padding:
        28px 0 8px;

    color: var(--muted);

    font-size: 0.82rem;
}

footer strong {
    color: #dce5f2;
}

/* =========================================================
   TABLETS
========================================================= */

@media (max-width: 850px) {

    .info-grid {
        grid-template-columns:
            repeat(2, minmax(0, 1fr));
    }

}


/* =========================================================
   MOBILE
========================================================= */

@media (max-width: 600px) {

    .page {
        width: 100%;

        padding-left:
            max(12px, env(safe-area-inset-left));

        padding-right:
            max(12px, env(safe-area-inset-right));
    }

    header {
        padding-top: 30px;
    }

    .logo {
        border-radius: 19px;
    }

    .card-top {
        align-items: flex-start;

        flex-direction: column;
    }

    .error-content {
        padding: 18px 15px 20px;
    }

    .info-grid {
        grid-template-columns: 1fr;

        gap: 10px;
    }

    .info {
        padding: 15px;
    }

    .actions {
        display: grid;

        grid-template-columns: 1fr;

        width: 100%;
    }

    button {
        width: 100%;

        min-height: 54px;
    }

}


/* =========================================================
   VERY SMALL PHONES
========================================================= */

@media (max-width: 360px) {

    .page {
        padding-left: 10px;
        padding-right: 10px;
    }

    .error-content {
        padding-left: 12px;
        padding-right: 12px;
    }

    .error-box {
        padding: 13px;
    }

    .info {
        padding: 13px;
    }

}


/* =========================================================
   LANDSCAPE PHONES
========================================================= */

@media (
    max-height: 520px
) and (
    orientation: landscape
) {

    header {
        padding-top: 18px;
        padding-bottom: 18px;
    }

    .logo {
        width: 52px;
        height: 52px;

        margin-bottom: 10px;

        border-radius: 14px;

        font-size: 26px;
    }

}


/* =========================================================
   TOUCHSCREENS
========================================================= */

@media (pointer: coarse) {

    button {
        min-height: 54px;

        padding-top: 14px;
        padding-bottom: 14px;
    }

}


/* =========================================================
   DEVICES THAT SUPPORT HOVER
========================================================= */

@media (hover: hover) {

    .primary:hover {
        box-shadow:
            0 14px 38px
            rgba(0, 229, 255, 0.22);
    }

    .secondary:hover {
        background:
            rgba(255,255,255,0.08);
    }

}


/* =========================================================
   REDUCED MOTION
========================================================= */

@media (prefers-reduced-motion: reduce) {

    html {
        scroll-behavior: auto;
    }

    * {
        transition: none !important;
        animation: none !important;
    }

}


/* =========================================================
   PRINT
========================================================= */

@media print {

    body {
        background: white;

        color: black;
    }

    .actions {
        display: none;
    }

    .generator {
        box-shadow: none;

        border: 1px solid #ddd;
    }

}

</style>
</head>


<body>

<main class="page">

    <header>

        <div
            class="logo"
            aria-hidden="true"
        >
            &lt;/&gt;
        </div>

        <h1>
            Programmer Error Generator
        </h1>

        <p class="subtitle">
            Real bugs. Real errors. Real programmer suffering.
            Generate another disaster whenever you need one.
        </p>

    </header>


    <section
        class="generator"
        aria-live="polite"
    >

        <div class="card-top">

            <span
                id="category"
                class="category"
            >
                Loading...
            </span>

            <span
                id="scenarioNumber"
                class="scenario-number"
            >
                ERROR #---
            </span>

        </div>


        <div class="error-content">

            <h2
                id="title"
                class="error-title"
            >
                Loading programmer disaster...
            </h2>


            <div class="error-box">

                <div
                    id="error"
                    class="error-message"
                >
                    Loading...
                </div>

            </div>


            <div class="info-grid">

                <article class="info">

                    <div class="info-label">
                        What happened?
                    </div>

                    <div
                        id="cause"
                        class="info-text"
                    >
                        Loading...
                    </div>

                </article>


                <article class="info">

                    <div class="info-label">
                        Possible fix
                    </div>

                    <div
                        id="fix"
                        class="info-text"
                    >
                        Loading...
                    </div>

                </article>


                <article class="info">

                    <div class="info-label">
                        Developer status
                    </div>

                    <div
                        class="info-text"
                    >
                        Searching Stack Overflow...
                    </div>

                </article>

            </div>


            <div class="joke">

                <div class="joke-label">
                    Programmer's official response
                </div>

                <div
                    id="joke"
                    class="joke-text"
                >
                    Loading...
                </div>

            </div>


            <div class="actions">

                <button
                    id="generateButton"
                    class="primary"
                    type="button"
                >
                    ⚡ Generate New Error
                </button>

                <button
                    id="copyButton"
                    class="secondary"
                    type="button"
                >
                    📋 Copy Error
                </button>

            </div>

        </div>

    </section>


    <footer>

        <strong>Programmer Error Generator</strong>
        <br>

        No database · No LocalStorage · No backend ·
        Just bugs

    </footer>

</main>


<script>

"use strict";


/* =========================================================
   DATA
========================================================= */

const scenarios = __SCENARIOS__;


/* =========================================================
   ELEMENTS
========================================================= */

const categoryElement =
    document.getElementById("category");

const scenarioNumberElement =
    document.getElementById("scenarioNumber");

const titleElement =
    document.getElementById("title");

const errorElement =
    document.getElementById("error");

const causeElement =
    document.getElementById("cause");

const fixElement =
    document.getElementById("fix");

const jokeElement =
    document.getElementById("joke");

const generateButton =
    document.getElementById("generateButton");

const copyButton =
    document.getElementById("copyButton");


/* =========================================================
   RANDOM SCENARIO
========================================================= */

let currentScenario = null;


function getRandomScenario() {

    if (scenarios.length === 0) {
        return null;
    }

    if (scenarios.length === 1) {
        return scenarios[0];
    }

    let next;

    do {
        next =
            scenarios[
                Math.floor(
                    Math.random() * scenarios.length
                )
            ];
    }
    while (
        currentScenario &&
        next === currentScenario
    );

    return next;
}


/* =========================================================
   DISPLAY
========================================================= */

function showScenario() {

    const scenario =
        getRandomScenario();

    if (!scenario) {
        return;
    }

    currentScenario =
        scenario;

    const number =
        scenarios.indexOf(scenario) + 1;


    categoryElement.textContent =
        scenario.category;

    scenarioNumberElement.textContent =
        `ERROR #${String(number).padStart(3, "0")}`;

    titleElement.textContent =
        scenario.title;

    errorElement.textContent =
        scenario.error;

    causeElement.textContent =
        scenario.cause;

    fixElement.textContent =
        scenario.fix;

    jokeElement.textContent =
        scenario.joke;
}


/* =========================================================
   COPY ERROR
========================================================= */

async function copyError() {

    if (!currentScenario) {
        return;
    }

    const text =
`${currentScenario.title}

${currentScenario.error}

What happened:
${currentScenario.cause}

Possible fix:
${currentScenario.fix}

Programmer's official response:
${currentScenario.joke}`;


    try {

        await navigator.clipboard.writeText(text);

        const original =
            copyButton.textContent;

        copyButton.textContent =
            "✓ Copied";

        setTimeout(() => {

            copyButton.textContent =
                original;

        }, 1400);

    } catch (error) {

        /*
         * Clipboard may be unavailable
         * on some browsers or insecure contexts.
         */

        const textarea =
            document.createElement("textarea");

        textarea.value = text;

        textarea.style.position =
            "fixed";

        textarea.style.opacity =
            "0";

        document.body.appendChild(textarea);

        textarea.select();

        try {
            document.execCommand("copy");
        } catch (_) {
            // Clipboard unavailable.
        }

        textarea.remove();

        const original =
            copyButton.textContent;

        copyButton.textContent =
            "✓ Copied";

        setTimeout(() => {

            copyButton.textContent =
                original;

        }, 1400);
    }
}


/* =========================================================
   BUTTONS
========================================================= */

generateButton.addEventListener(
    "click",
    showScenario
);

copyButton.addEventListener(
    "click",
    copyError
);


/* =========================================================
   KEYBOARD
========================================================= */

document.addEventListener(
    "keydown",
    event => {

        /*
         * Space / Enter generates
         * another scenario unless the user
         * is interacting with a form control.
         */

        if (
            event.key === " " ||
            event.key === "Enter"
        ) {

            const active =
                document.activeElement;

            const tag =
                active?.tagName;

            if (
                tag !== "BUTTON" &&
                tag !== "INPUT" &&
                tag !== "TEXTAREA" &&
                tag !== "SELECT"
            ) {

                showScenario();
            }
        }

        /*
         * Press C to copy.
         */

        if (
            event.key.toLowerCase() === "c" &&
            !event.ctrlKey &&
            !event.metaKey &&
            !event.altKey
        ) {

            const active =
                document.activeElement;

            const tag =
                active?.tagName;

            if (
                tag !== "INPUT" &&
                tag !== "TEXTAREA"
            ) {

                copyError();
            }
        }

    }
);


/* =========================================================
   INITIAL LOAD
========================================================= */

/*
 * Every page load gets a fresh random scenario.
 *
 * No:
 * - LocalStorage
 * - SessionStorage
 * - Cookies
 * - Database
 * - Backend
 */

showScenario();


/* =========================================================
   OPTIONAL PAGE VISIBILITY REFRESH
========================================================= */

/*
 * If the user leaves the tab and later returns,
 * generate another error.
 *
 * This does NOT store anything.
 */

document.addEventListener(
    "visibilitychange",
    () => {

        if (
            document.visibilityState === "visible"
        ) {

            showScenario();
        }

    }
);

</script>

</body>
</html>
"""


# ============================================================
# INSERT SCENARIO DATA
# ============================================================

HTML = HTML.replace(
    "__SCENARIOS__",
    DATA_JSON
)


# ============================================================
# WRITE FILE
# ============================================================

OUTPUT_FILE.write_text(
    HTML,
    encoding="utf-8"
)


print("=" * 60)
print("PROGRAMMER ERROR GENERATOR")
print("=" * 60)
print(f"Scenarios: {len(SCENARIOS)}")
print(f"Generated: {OUTPUT_FILE.resolve()}")
print()
print("Static site ready.")
print()
print("Render:")
print("  Service Type: Static Site")
print("  Build Command: python build.py")
print("  Publish Directory: .")
print("=" * 60)
