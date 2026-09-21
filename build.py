from pathlib import Path
import json
import html


# ============================================================
# PROGRAMMER ERROR GENERATOR
# Everything is contained in this build.py file.
#
# Run:
#     python build.py
#
# It generates:
#     index.html
#
# No database.
# No LocalStorage.
# No external libraries.
# No separate CSS/JS files.
# ============================================================


SCENARIOS = [

    # ========================================================
    # JAVASCRIPT
    # ========================================================

    {
        "category": "JavaScript",
        "title": "TypeError: Cannot read properties of undefined",
        "error": "TypeError: Cannot read properties of undefined (reading 'name')",
        "cause": "You assumed an object existed because your brain said it existed.",
        "fix": "Check whether the object exists before accessing its property.",
        "excuse": "The object was emotionally unavailable."
    },
    {
        "category": "JavaScript",
        "title": "ReferenceError",
        "error": "ReferenceError: x is not defined",
        "cause": "The variable was never declared, was misspelled, or lives somewhere you forgot about.",
        "fix": "Declare the variable correctly and check its spelling and scope.",
        "excuse": "The variable resigned without notice."
    },
    {
        "category": "JavaScript",
        "title": "SyntaxError",
        "error": "SyntaxError: Unexpected token",
        "cause": "JavaScript encountered something that makes absolutely no sense to it.",
        "fix": "Check brackets, commas, quotes, parentheses and the line before the reported error.",
        "excuse": "JavaScript misunderstood my creative writing."
    },
    {
        "category": "JavaScript",
        "title": "Unexpected Undefined",
        "error": "undefined",
        "cause": "Something returned nothing when you confidently expected a value.",
        "fix": "Trace the function return value and verify the object or property exists.",
        "excuse": "The value is taking a personal day."
    },
    {
        "category": "JavaScript",
        "title": "Promise Pending Forever",
        "error": "Promise { <pending> }",
        "cause": "A promise was created but never resolved or rejected.",
        "fix": "Check asynchronous control flow and make sure every code path settles the promise.",
        "excuse": "The promise is still thinking about it."
    },
    {
        "category": "JavaScript",
        "title": "Fetch Failed",
        "error": "TypeError: Failed to fetch",
        "cause": "The browser could not complete the network request.",
        "fix": "Check the URL, server, HTTPS, CORS, network connection and browser console.",
        "excuse": "The internet is temporarily unavailable due to technical reasons."
    },
    {
        "category": "JavaScript",
        "title": "JSON Parse Error",
        "error": "SyntaxError: Unexpected token < in JSON",
        "cause": "You expected JSON but the server probably returned HTML.",
        "fix": "Inspect the actual response before calling response.json().",
        "excuse": "The API decided HTML would be more artistic."
    },
    {
        "category": "JavaScript",
        "title": "Event Listener Does Nothing",
        "error": "click event fired: false",
        "cause": "The selector may be wrong, the element may not exist yet, or the listener may be attached to the wrong element.",
        "fix": "Verify the selector and attach the event listener after the DOM exists.",
        "excuse": "The button is currently ignoring me."
    },
    {
        "category": "JavaScript",
        "title": "Infinite Loop",
        "error": "Browser tab has stopped responding",
        "cause": "A loop never reaches its exit condition.",
        "fix": "Check the loop condition and make sure the controlling value changes.",
        "excuse": "I was testing infinite scalability."
    },
    {
        "category": "JavaScript",
        "title": "NaN",
        "error": "NaN",
        "cause": "A calculation received a value that cannot be converted into a valid number.",
        "fix": "Inspect the input values and validate them before calculating.",
        "excuse": "The number has entered a philosophical state."
    },
    {
        "category": "JavaScript",
        "title": "Null Is Not An Object",
        "error": "TypeError: Cannot read properties of null",
        "cause": "The code tried to access something from null.",
        "fix": "Check the value before accessing properties or methods.",
        "excuse": "Null was there five minutes ago."
    },
    {
        "category": "JavaScript",
        "title": "Wrong Array Method",
        "error": "TypeError: array.map is not a function",
        "cause": "The variable is not actually an array.",
        "fix": "Inspect the value with Array.isArray() and verify the data structure.",
        "excuse": "It looked like an array from a distance."
    },

    # ========================================================
    # PYTHON
    # ========================================================

    {
        "category": "Python",
        "title": "IndentationError",
        "error": "IndentationError: unexpected indent",
        "cause": "Python found indentation that does not match the expected structure.",
        "fix": "Check spaces, tabs and block indentation.",
        "excuse": "Python is extremely passionate about whitespace."
    },
    {
        "category": "Python",
        "title": "NameError",
        "error": "NameError: name 'variable' is not defined",
        "cause": "The variable does not exist in the current scope.",
        "fix": "Check spelling, declaration order and variable scope.",
        "excuse": "The variable entered witness protection."
    },
    {
        "category": "Python",
        "title": "ModuleNotFoundError",
        "error": "ModuleNotFoundError: No module named 'something'",
        "cause": "The package is not installed in the active Python environment.",
        "fix": "Activate the correct environment and install the required package.",
        "excuse": "The module was installed on another computer."
    },
    {
        "category": "Python",
        "title": "KeyError",
        "error": "KeyError: 'username'",
        "cause": "A dictionary key was requested that does not exist.",
        "fix": "Check the dictionary contents or use get() when appropriate.",
        "excuse": "The key exists spiritually."
    },
    {
        "category": "Python",
        "title": "IndexError",
        "error": "IndexError: list index out of range",
        "cause": "You requested an index that does not exist in the list.",
        "fix": "Check the list length and valid index range.",
        "excuse": "The list was longer in development."
    },
    {
        "category": "Python",
        "title": "AttributeError",
        "error": "AttributeError: object has no attribute",
        "cause": "The object does not have the property or method you attempted to use.",
        "fix": "Inspect the object's type and available attributes.",
        "excuse": "The object forgot its own API."
    },
    {
        "category": "Python",
        "title": "ValueError",
        "error": "ValueError: invalid literal for int()",
        "cause": "Python received a value of the wrong format.",
        "fix": "Validate or convert the input before using it.",
        "excuse": "The number looked numeric."
    },
    {
        "category": "Python",
        "title": "Pip Installed It Somewhere Else",
        "error": "Requirement already satisfied... but Python cannot import it",
        "cause": "pip and Python are using different environments.",
        "fix": "Use the correct virtual environment and check which Python and pip are active.",
        "excuse": "The package is installed. Just not here."
    },
    {
        "category": "Python",
        "title": "Circular Import",
        "error": "ImportError: cannot import name",
        "cause": "Two modules depend on each other during initialization.",
        "fix": "Refactor shared code into a separate module or change the import structure.",
        "excuse": "The modules became too dependent on each other."
    },

    # ========================================================
    # HTML
    # ========================================================

    {
        "category": "HTML",
        "title": "Mobile View Is Broken",
        "error": "Page looks fine on desktop and terrible on phone",
        "cause": "The viewport configuration or responsive CSS is missing.",
        "fix": "Use a viewport meta tag and responsive layouts with flexible dimensions.",
        "excuse": "Desktop was the original target audience."
    },
    {
        "category": "HTML",
        "title": "Wrong Element ID",
        "error": "document.getElementById(...) returned null",
        "cause": "The JavaScript ID does not match the HTML ID.",
        "fix": "Compare the HTML id attribute with the JavaScript selector character by character.",
        "excuse": "Capitalization is a matter of personal preference."
    },
    {
        "category": "HTML",
        "title": "Form Reloaded The Page",
        "error": "Page unexpectedly refreshed after submit",
        "cause": "The form's default submit behavior was not prevented.",
        "fix": "Use event.preventDefault() when handling the form with JavaScript.",
        "excuse": "The browser wanted to refresh its memory."
    },
    {
        "category": "HTML",
        "title": "Missing Closing Tag",
        "error": "Unexpected layout behavior",
        "cause": "An HTML element was opened but not correctly closed.",
        "fix": "Validate the HTML and check nested elements.",
        "excuse": "The closing tag is coming in the next sprint."
    },

    # ========================================================
    # CSS
    # ========================================================

    {
        "category": "CSS",
        "title": "Horizontal Scrollbar Appeared",
        "error": "Website is wider than the screen",
        "cause": "An element is overflowing the viewport.",
        "fix": "Inspect fixed widths, margins, transforms, grids and overflowing content.",
        "excuse": "The website needs room to breathe."
    },
    {
        "category": "CSS",
        "title": "Z-Index War",
        "error": "z-index: 9999999 still does nothing",
        "cause": "The stacking context is more complicated than the number suggests.",
        "fix": "Inspect positioning and stacking contexts instead of increasing z-index forever.",
        "excuse": "We have entered the final boss of CSS."
    },
    {
        "category": "CSS",
        "title": "Flexbox Refuses To Center",
        "error": "justify-content: center but nothing is centered",
        "cause": "The parent dimensions or flex direction are not what you expected.",
        "fix": "Inspect the parent container and verify display:flex, width, height and direction.",
        "excuse": "Centering is apparently subjective."
    },
    {
        "category": "CSS",
        "title": "Mobile Layout Exploded",
        "error": "Everything overlaps below 768px",
        "cause": "Desktop dimensions were used without responsive breakpoints.",
        "fix": "Use flexible units, wrapping, media queries and mobile-first layouts.",
        "excuse": "Phones were not part of the original requirements."
    },
    {
        "category": "CSS",
        "title": "Button Text Overflow",
        "error": "Button text escapes the button",
        "cause": "The button has fixed dimensions or text that cannot wrap.",
        "fix": "Allow flexible width, wrapping and adequate padding.",
        "excuse": "The button has big ambitions."
    },
    {
        "category": "CSS",
        "title": "Font Changed Everything",
        "error": "Changing one font broke the entire layout",
        "cause": "The new font has different metrics and dimensions.",
        "fix": "Review line-height, font size, wrapping and container dimensions.",
        "excuse": "Typography is infrastructure."
    },

    # ========================================================
    # GIT
    # ========================================================

    {
        "category": "Git",
        "title": "Detached HEAD",
        "error": "You are in 'detached HEAD' state",
        "cause": "Git checked out a commit instead of a normal branch.",
        "fix": "Create or switch to a branch if you need to continue development.",
        "excuse": "HEAD has temporarily chosen independence."
    },
    {
        "category": "Git",
        "title": "Merge Conflict",
        "error": "CONFLICT (content): Merge conflict",
        "cause": "Two changes modified overlapping parts of the same files.",
        "fix": "Open the conflicted files, resolve the markers, stage and commit the resolution.",
        "excuse": "Git is teaching us teamwork."
    },
    {
        "category": "Git",
        "title": "Push Rejected",
        "error": "Updates were rejected because the remote contains work",
        "cause": "The remote branch has commits that your local branch does not have.",
        "fix": "Fetch/pull the remote changes, resolve conflicts if necessary, then push again.",
        "excuse": "Git doesn't trust me anymore."
    },
    {
        "category": "Git",
        "title": "Wrong Branch",
        "error": "Commit landed on main",
        "cause": "You forgot to check which branch was active.",
        "fix": "Check git branch before making important changes.",
        "excuse": "Main looked exactly like my feature branch."
    },
    {
        "category": "Git",
        "title": "Secret Committed",
        "error": "API key detected in Git history",
        "cause": "A secret was accidentally committed.",
        "fix": "Revoke the exposed credential immediately and remove it from the repository history as appropriate.",
        "excuse": "It was only a tiny API key."
    },
    {
        "category": "Git",
        "title": "Forgot To Commit",
        "error": "Where did my changes go?",
        "cause": "The work exists locally but was never committed or pushed.",
        "fix": "Check git status and commit the intended changes.",
        "excuse": "The code was committed emotionally."
    },

    # ========================================================
    # NODE.JS
    # ========================================================

    {
        "category": "Node.js",
        "title": "Port Already In Use",
        "error": "Error: listen EADDRINUSE",
        "cause": "Another process is already using the requested port.",
        "fix": "Find and stop the process or configure the application to use another port.",
        "excuse": "Port 3000 has prior commitments."
    },
    {
        "category": "Node.js",
        "title": "Import/Export Disaster",
        "error": "SyntaxError: Cannot use import statement outside a module",
        "cause": "The project configuration does not match the module syntax being used.",
        "fix": "Configure ESM/CommonJS consistently and check package.json settings.",
        "excuse": "JavaScript has two personalities."
    },
    {
        "category": "Node.js",
        "title": "node_modules Is Gone",
        "error": "Cannot find module",
        "cause": "Dependencies have not been installed in the current environment.",
        "fix": "Run npm install or npm ci using the project's package configuration.",
        "excuse": "node_modules escaped to save disk space."
    },

    # ========================================================
    # HTTP
    # ========================================================

    {
        "category": "HTTP",
        "title": "400 Bad Request",
        "error": "HTTP 400 Bad Request",
        "cause": "The server could not understand the request.",
        "fix": "Check request syntax, parameters, headers and body data.",
        "excuse": "The server didn't understand my handwriting."
    },
    {
        "category": "HTTP",
        "title": "401 Unauthorized",
        "error": "HTTP 401 Unauthorized",
        "cause": "Authentication credentials are missing or invalid.",
        "fix": "Check login credentials, tokens, sessions and Authorization headers.",
        "excuse": "The server wants to see some identification."
    },
    {
        "category": "HTTP",
        "title": "403 Forbidden",
        "error": "HTTP 403 Forbidden",
        "cause": "The server understood the request but refuses access.",
        "fix": "Check permissions, authentication state and server authorization rules.",
        "excuse": "The server said no."
    },
    {
        "category": "HTTP",
        "title": "404 Not Found",
        "error": "HTTP 404 Not Found",
        "cause": "The requested resource or route could not be found.",
        "fix": "Check the URL, route configuration, filename and deployment structure.",
        "excuse": "The page moved without leaving a forwarding address."
    },
    {
        "category": "HTTP",
        "title": "429 Too Many Requests",
        "error": "HTTP 429 Too Many Requests",
        "cause": "The server or API rate limit was exceeded.",
        "fix": "Reduce request frequency and implement appropriate retry/backoff behavior.",
        "excuse": "I was just making sure the API was still alive."
    },
    {
        "category": "HTTP",
        "title": "500 Internal Server Error",
        "error": "HTTP 500 Internal Server Error",
        "cause": "The server encountered an unexpected condition.",
        "fix": "Check server logs and reproduce the failing request.",
        "excuse": "The server is having a character-building experience."
    },
    {
        "category": "HTTP",
        "title": "502 Bad Gateway",
        "error": "HTTP 502 Bad Gateway",
        "cause": "A gateway or proxy received an invalid response from an upstream server.",
        "fix": "Check the upstream service, proxy configuration and network connectivity.",
        "excuse": "The gateway misunderstood the upstream server."
    },
    {
        "category": "HTTP",
        "title": "503 Service Unavailable",
        "error": "HTTP 503 Service Unavailable",
        "cause": "The service is temporarily unable to handle the request.",
        "fix": "Check service health, deployments, capacity and dependencies.",
        "excuse": "The server is on a coffee break."
    },

    # ========================================================
    # WEB SECURITY
    # ========================================================

    {
        "category": "Web Security",
        "title": "CORS Error",
        "error": "Access to fetch has been blocked by CORS policy",
        "cause": "The server does not allow the browser's cross-origin request.",
        "fix": "Configure appropriate CORS headers on the server and avoid unsafe wildcard configurations.",
        "excuse": "The browser has trust issues."
    },
    {
        "category": "Web Security",
        "title": "Preflight Request Failed",
        "error": "Response to preflight request doesn't pass access control check",
        "cause": "The OPTIONS request or required CORS headers are not configured correctly.",
        "fix": "Check allowed origins, methods and headers on the server.",
        "excuse": "The browser wanted to ask permission first."
    },
    {
        "category": "Web Security",
        "title": "XSS Vulnerability",
        "error": "User-controlled HTML executed in the browser",
        "cause": "Untrusted input was inserted into a page without appropriate output encoding or sanitization.",
        "fix": "Treat user input as untrusted and use safe DOM APIs, output encoding and appropriate security controls.",
        "excuse": "The HTML was feeling expressive."
    },
    {
        "category": "Web Security",
        "title": "SQL Injection Risk",
        "error": "Database query contains unsanitized user input",
        "cause": "Application input was directly incorporated into SQL.",
        "fix": "Use parameterized queries or prepared statements.",
        "excuse": "The database was supposed to be friendly."
    },
    {
        "category": "Web Security",
        "title": "API Secret In Frontend",
        "error": "Secret API key visible in browser source",
        "cause": "A secret credential was included in client-side code.",
        "fix": "Move secrets to server-side configuration and rotate any exposed credential.",
        "excuse": "The frontend promised not to tell anyone."
    },

    # ========================================================
    # DATABASE
    # ========================================================

    {
        "category": "Database",
        "title": "SQL Syntax Error",
        "error": "SQL syntax error near 'FROM'",
        "cause": "The SQL statement contains invalid syntax.",
        "fix": "Inspect the generated SQL and verify keywords, commas, quotes and clauses.",
        "excuse": "SQL grammar is optional according to my development methodology."
    },
    {
        "category": "Database",
        "title": "Duplicate Entry",
        "error": "Duplicate entry violates unique constraint",
        "cause": "A value that must be unique already exists.",
        "fix": "Check existing records and decide whether to update, ignore or generate a different value.",
        "excuse": "The database liked the first one so much it wanted another."
    },
    {
        "category": "Database",
        "title": "Foreign Key Failure",
        "error": "Foreign key constraint fails",
        "cause": "A referenced record does not exist or the relationship is invalid.",
        "fix": "Verify parent records and insertion/deletion order.",
        "excuse": "The database is enforcing friendship requirements."
    },
    {
        "category": "Database",
        "title": "N+1 Query Problem",
        "error": "1 request generated 500 database queries",
        "cause": "Related data is being loaded individually instead of efficiently.",
        "fix": "Use appropriate joins, eager loading or batched queries.",
        "excuse": "I was stress-testing the database."
    },
    {
        "category": "Database",
        "title": "Connection Refused",
        "error": "Database connection refused",
        "cause": "The database server is unavailable or the connection settings are wrong.",
        "fix": "Check host, port, credentials, service status and network configuration.",
        "excuse": "The database is pretending not to be home."
    },

    # ========================================================
    # DEPLOYMENT
    # ========================================================

    {
        "category": "Deployment",
        "title": "Works On My Machine",
        "error": "Application works locally but fails in production",
        "cause": "The production environment differs from the development environment.",
        "fix": "Compare runtime versions, dependencies, environment variables, paths and configuration.",
        "excuse": "Works on my machine."
    },
    {
        "category": "Deployment",
        "title": "Missing Environment Variable",
        "error": "KeyError: DATABASE_URL",
        "cause": "A required environment variable is missing from the deployment environment.",
        "fix": "Configure the required environment variable securely in the hosting platform.",
        "excuse": "The environment forgot its variables."
    },
    {
        "category": "Deployment",
        "title": "Wrong Start Command",
        "error": "Application failed to start",
        "cause": "The hosting platform is executing the wrong command.",
        "fix": "Check the deployment start command and application entry point.",
        "excuse": "The server started the wrong application."
    },
    {
        "category": "Deployment",
        "title": "Missing index.html",
        "error": "404: index.html not found",
        "cause": "The static host cannot find the expected published file.",
        "fix": "Check the build command and publish directory.",
        "excuse": "index.html is taking the day off."
    },
    {
        "category": "Deployment",
        "title": "Filename Case Problem",
        "error": "File not found in production",
        "cause": "The development machine may use a case-insensitive filesystem while production does not.",
        "fix": "Make filename and import casing match exactly.",
        "excuse": "The file name was technically correct."
    },

    # ========================================================
    # LINUX
    # ========================================================

    {
        "category": "Linux",
        "title": "Permission Denied",
        "error": "bash: ./script.sh: Permission denied",
        "cause": "The file does not have executable permission.",
        "fix": "Check file permissions and grant execute permission when appropriate.",
        "excuse": "Linux respects boundaries."
    },
    {
        "category": "Linux",
        "title": "Command Not Found",
        "error": "bash: command: command not found",
        "cause": "The command is not installed or is not available in PATH.",
        "fix": "Check installation and PATH configuration.",
        "excuse": "The command is hiding from PATH."
    },
    {
        "category": "Linux",
        "title": "Wrong Directory",
        "error": "No such file or directory",
        "cause": "The command was executed from a directory where the expected file does not exist.",
        "fix": "Run pwd and ls, then navigate to the correct directory.",
        "excuse": "The terminal moved the folder while I wasn't looking."
    },

    # ========================================================
    # DOCKER
    # ========================================================

    {
        "category": "Docker",
        "title": "Container Exited Immediately",
        "error": "Container exited with code 1",
        "cause": "The main process inside the container terminated.",
        "fix": "Inspect container logs and verify the entry command.",
        "excuse": "The container finished its work extremely efficiently."
    },
    {
        "category": "Docker",
        "title": "Localhost Inside Container",
        "error": "Connection refused to localhost",
        "cause": "localhost inside a container refers to that container, not your host machine.",
        "fix": "Use the appropriate container/network hostname and expose services correctly.",
        "excuse": "Localhost has different definitions depending on its mood."
    },
    {
        "category": "Docker",
        "title": "Image Build Failed",
        "error": "failed to solve: process did not complete successfully",
        "cause": "A Dockerfile command failed during image creation.",
        "fix": "Read the failing build step and verify files, commands and dependencies.",
        "excuse": "Dockerfile syntax is an ancient language."
    },

    # ========================================================
    # NETWORKING
    # ========================================================

    {
        "category": "Networking",
        "title": "ECONNREFUSED",
        "error": "connect ECONNREFUSED 127.0.0.1:3000",
        "cause": "Nothing is accepting connections on the requested address and port.",
        "fix": "Check whether the server is running and listening on the expected interface and port.",
        "excuse": "The server refused to answer the door."
    },
    {
        "category": "Networking",
        "title": "DNS NXDOMAIN",
        "error": "DNS_PROBE_FINISHED_NXDOMAIN",
        "cause": "DNS could not find the requested domain.",
        "fix": "Check the domain name and DNS configuration.",
        "excuse": "DNS has never heard of that website."
    },
    {
        "category": "Networking",
        "title": "Request Timeout",
        "error": "ETIMEDOUT",
        "cause": "The connection did not complete within the configured timeout.",
        "fix": "Check network connectivity, server availability and timeout settings.",
        "excuse": "The request is almost there."
    },

    # ========================================================
    # TESTING
    # ========================================================

    {
        "category": "Testing",
        "title": "Flaky Test",
        "error": "Test passed locally. Failed in CI. Passed again.",
        "cause": "The test depends on timing, external state, randomness or another unstable factor.",
        "fix": "Make the test deterministic and isolate external dependencies.",
        "excuse": "The test has free will."
    },
    {
        "category": "Testing",
        "title": "All Tests Fail Together",
        "error": "127 tests failed",
        "cause": "A shared dependency, fixture, configuration or setup step is broken.",
        "fix": "Find the earliest meaningful failure rather than fixing every downstream error.",
        "excuse": "The tests decided to form a union."
    },
    {
        "category": "Testing",
        "title": "Test Passed By Accident",
        "error": "Test passed but nobody knows why",
        "cause": "The test may not actually assert the intended behavior.",
        "fix": "Review assertions and verify that the test fails when the feature is intentionally broken.",
        "excuse": "A passing test is a passing test."
    },

    # ========================================================
    # PERFORMANCE
    # ========================================================

    {
        "category": "Performance",
        "title": "Website Is Slow",
        "error": "Page load: 14.8 seconds",
        "cause": "Large assets, slow APIs, excessive JavaScript, database queries or rendering work may be involved.",
        "fix": "Profile the application and optimize the actual bottleneck.",
        "excuse": "Premium loading experience."
    },
    {
        "category": "Performance",
        "title": "Huge JavaScript Bundle",
        "error": "main.js: 18.7 MB",
        "cause": "Too many dependencies or unoptimized application code are shipped to the browser.",
        "fix": "Use code splitting, tree shaking, compression and dependency review.",
        "excuse": "The bundle contains important vibes."
    },
    {
        "category": "Performance",
        "title": "Memory Leak",
        "error": "Memory usage increases continuously",
        "cause": "Objects, listeners, timers or resources remain referenced after they should be released.",
        "fix": "Profile memory usage and remove unnecessary retained references.",
        "excuse": "The application is collecting memories."
    },

    # ========================================================
    # PROGRAMMER LIFE
    # ========================================================

    {
        "category": "Programmer Life",
        "title": "console.log() Fixed Everything",
        "error": "Added console.log and suddenly it works",
        "cause": "Timing, initialization order or another hidden state change may have altered behavior.",
        "fix": "Understand why the logging changed behavior before removing it.",
        "excuse": "I don't know why, but I'm afraid to touch it."
    },
    {
        "category": "Programmer Life",
        "title": "One Line Broke Everything",
        "error": "Changed one line. Entire application exploded.",
        "cause": "The changed line affected an important dependency or assumption.",
        "fix": "Use version control and trace the dependency chain to find the actual failure.",
        "excuse": "That line had too much responsibility."
    },
    {
        "category": "Programmer Life",
        "title": "Friday Deployment",
        "error": "Production error detected Friday at 5:59 PM",
        "cause": "A deployment was made immediately before the weekend.",
        "fix": "Follow deployment procedures, testing and rollback practices.",
        "excuse": "It was supposed to be a small change."
    },
    {
        "category": "Programmer Life",
        "title": "Temporary Fix Became Permanent",
        "error": "TODO: remove this workaround",
        "cause": "A temporary workaround survived long enough to become part of the system.",
        "fix": "Track technical debt and schedule the cleanup.",
        "excuse": "Temporary is a flexible concept."
    },
    {
        "category": "Programmer Life",
        "title": "It Worked Yesterday",
        "error": "Same code. Different result.",
        "cause": "Dependencies, environment, data or external services changed.",
        "fix": "Compare environment and dependency versions and inspect recent changes.",
        "excuse": "Yesterday's computer was better."
    },
    {
        "category": "Programmer Life",
        "title": "Production-Only Bug",
        "error": "Cannot reproduce locally",
        "cause": "Production has different data, configuration, traffic or environment conditions.",
        "fix": "Collect production-safe diagnostics and reproduce the relevant conditions.",
        "excuse": "The bug only respects important environments."
    },
    {
        "category": "Programmer Life",
        "title": "Copy-Paste Bug",
        "error": "Two unrelated functions contain exactly the same suspicious line",
        "cause": "Code was copied without fully adapting it to the new context.",
        "fix": "Review copied code and extract reusable logic where appropriate.",
        "excuse": "Ctrl+C/Ctrl+V is an established architecture."
    },
    {
        "category": "Programmer Life",
        "title": "Missing Comma",
        "error": "Everything failed because of one comma",
        "cause": "A small syntax error prevented parsing or changed the structure of the code.",
        "fix": "Use syntax-aware editors, formatters and linters.",
        "excuse": "The comma was optional in my imagination."
    },
    {
        "category": "Programmer Life",
        "title": "Forgot To Save",
        "error": "The fix doesn't work",
        "cause": "The edited file was never saved.",
        "fix": "Save the file and verify the running application is using the latest version.",
        "excuse": "I fixed it locally in my unsaved universe."
    },
    {
        "category": "Programmer Life",
        "title": "Wrong File Edited",
        "error": "Nothing changed",
        "cause": "You edited a duplicate or similarly named file.",
        "fix": "Verify the actual file loaded by the application.",
        "excuse": "There were too many files with the same name."
    },
    {
        "category": "Programmer Life",
        "title": "Cache Is Lying",
        "error": "Old version still appears after deployment",
        "cause": "Browser, CDN or application caching is serving an older resource.",
        "fix": "Inspect cache headers and invalidate caches when appropriate.",
        "excuse": "The browser remembers better than I do."
    },
    {
        "category": "Programmer Life",
        "title": "Rubber Duck Required",
        "error": "Bug disappeared while explaining it",
        "cause": "Explaining the problem exposed an incorrect assumption.",
        "fix": "Explain the code step by step or reproduce the issue in a minimal example.",
        "excuse": "The duck understood immediately."
    },
]


# ============================================================
# BUILD
# ============================================================

DATA = json.dumps(SCENARIOS, ensure_ascii=False)

HTML = r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">

<meta
    name="viewport"
    content="width=device-width, initial-scale=1, viewport-fit=cover"
>

<meta
    name="theme-color"
    content="#0b0d12"
>

<meta
    name="description"
    content="Programmer Error Generator — search real programmer errors and generate ridiculous excuses."
>

<title>Programmer Error Generator</title>

<style>

    /* ======================================================
       RESET
       ====================================================== */

    * {
        box-sizing: border-box;
        -webkit-tap-highlight-color: transparent;
    }

    html {
        width: 100%;
        min-height: 100%;
        background: #0b0d12;
        color-scheme: dark;
        overflow-x: hidden;
    }

    body {
        margin: 0;
        width: 100%;
        min-height: 100dvh;
        overflow-x: hidden;

        font-family:
            Inter,
            ui-sans-serif,
            system-ui,
            -apple-system,
            BlinkMacSystemFont,
            "Segoe UI",
            sans-serif;

        background:
            radial-gradient(
                circle at 15% 10%,
                rgba(108, 92, 231, 0.16),
                transparent 30%
            ),
            radial-gradient(
                circle at 85% 15%,
                rgba(0, 220, 255, 0.10),
                transparent 30%
            ),
            #0b0d12;

        color: #f5f7fb;
    }

    button,
    input {
        font: inherit;
    }

    button {
        cursor: pointer;
    }

    ::selection {
        background: rgba(120, 100, 255, 0.45);
        color: white;
    }


    /* ======================================================
       PAGE
       ====================================================== */

    .page {
        width: min(1180px, 100%);
        margin: 0 auto;

        min-height: 100dvh;

        padding:
            max(18px, env(safe-area-inset-top))
            max(16px, env(safe-area-inset-right))
            max(24px, env(safe-area-inset-bottom))
            max(16px, env(safe-area-inset-left));
    }


    /* ======================================================
       HEADER
       ====================================================== */

    header {
        padding: 28px 0 22px;
        text-align: center;
    }

    .logo {
        display: inline-flex;
        align-items: center;
        justify-content: center;

        width: 74px;
        height: 74px;

        border-radius: 22px;

        font-size: 36px;

        background:
            linear-gradient(
                135deg,
                rgba(126, 99, 255, 0.24),
                rgba(0, 220, 255, 0.13)
            );

        border: 1px solid rgba(255,255,255,0.10);

        box-shadow:
            0 15px 50px rgba(0,0,0,0.30),
            inset 0 1px rgba(255,255,255,0.08);
    }

    h1 {
        margin: 15px 0 7px;

        font-size: clamp(30px, 6vw, 58px);
        line-height: 1.02;
        letter-spacing: -0.045em;
    }

    .subtitle {
        max-width: 760px;
        margin: 0 auto;

        color: #9da5b5;

        font-size: clamp(14px, 2vw, 18px);
        line-height: 1.55;
    }


    /* ======================================================
       SEARCH
       ====================================================== */

    .search-panel {
        position: relative;

        margin: 12px auto 24px;

        width: min(900px, 100%);
    }

    .search-box {
        display: flex;
        gap: 10px;

        width: 100%;

        padding: 9px;

        border: 1px solid rgba(255,255,255,0.10);
        border-radius: 18px;

        background: rgba(18, 21, 29, 0.88);

        box-shadow:
            0 18px 55px rgba(0,0,0,0.22),
            inset 0 1px rgba(255,255,255,0.04);

        backdrop-filter: blur(18px);
        -webkit-backdrop-filter: blur(18px);
    }

    .search-input {
        flex: 1;
        min-width: 0;

        height: 54px;

        border: 0;
        outline: 0;

        border-radius: 12px;

        padding: 0 15px;

        background: #0d1016;
        color: #fff;

        font-size: 16px;

        border: 1px solid rgba(255,255,255,0.06);
    }

    .search-input::placeholder {
        color: #687181;
    }

    .search-input:focus {
        border-color: rgba(125, 104, 255, 0.65);
        box-shadow: 0 0 0 3px rgba(125,104,255,0.10);
    }

    .search-button {
        flex: 0 0 auto;

        min-width: 120px;
        min-height: 54px;

        padding: 0 18px;

        border: 0;
        border-radius: 12px;

        color: white;
        font-weight: 800;

        background:
            linear-gradient(
                135deg,
                #6f5cff,
                #4b7cff
            );

        box-shadow:
            0 8px 25px rgba(91,83,255,0.25);
    }

    .search-button:active {
        transform: translateY(1px) scale(0.99);
    }


    /* ======================================================
       SEARCH RESULTS
       ====================================================== */

    .results {
        position: absolute;

        z-index: 100;

        left: 0;
        right: 0;
        top: calc(100% + 8px);

        display: none;

        max-height: min(60vh, 480px);

        overflow-y: auto;
        overflow-x: hidden;

        padding: 7px;

        border-radius: 16px;

        border: 1px solid rgba(255,255,255,0.10);

        background: rgba(16, 19, 26, 0.97);

        box-shadow:
            0 25px 70px rgba(0,0,0,0.55);

        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
    }

    .results.visible {
        display: block;
    }

    .result-item {
        width: 100%;

        padding: 14px;

        margin-bottom: 5px;

        text-align: left;

        border: 0;
        border-radius: 12px;

        color: white;

        background: transparent;
    }

    .result-item:last-child {
        margin-bottom: 0;
    }

    .result-item:hover,
    .result-item:focus-visible {
        background: rgba(255,255,255,0.07);
        outline: none;
    }

    .result-title {
        font-weight: 800;
        margin-bottom: 5px;
    }

    .result-meta {
        color: #8f98aa;
        font-size: 12px;
        line-height: 1.4;
    }

    .no-results {
        padding: 18px;
        text-align: center;
        color: #8f98aa;
    }


    /* ======================================================
       MAIN GRID
       ====================================================== */

    .main-grid {
        display: grid;

        grid-template-columns:
            minmax(0, 1fr)
            minmax(270px, 0.34fr);

        gap: 18px;

        align-items: start;
    }


    /* ======================================================
       CARDS
       ====================================================== */

    .card {
        min-width: 0;

        border-radius: 22px;

        border: 1px solid rgba(255,255,255,0.09);

        background:
            linear-gradient(
                180deg,
                rgba(22, 25, 34, 0.94),
                rgba(14, 17, 23, 0.94)
            );

        box-shadow:
            0 25px 80px rgba(0,0,0,0.22),
            inset 0 1px rgba(255,255,255,0.035);
    }

    .error-card {
        overflow: hidden;
    }

    .card-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 12px;

        padding: 18px 20px;

        border-bottom: 1px solid rgba(255,255,255,0.07);
    }

    .category {
        display: inline-flex;
        align-items: center;

        min-height: 32px;

        padding: 6px 11px;

        border-radius: 999px;

        background: rgba(111,92,255,0.13);

        border: 1px solid rgba(111,92,255,0.24);

        color: #c6c0ff;

        font-size: 12px;
        font-weight: 800;
        letter-spacing: 0.02em;
    }

    .error-number {
        color: #697284;
        font-size: 12px;
        white-space: nowrap;
    }


    /* ======================================================
       ERROR CONTENT
       ====================================================== */

    .error-content {
        padding: clamp(20px, 4vw, 34px);
    }

    .error-title {
        margin: 0 0 18px;

        font-size: clamp(24px, 4vw, 39px);

        line-height: 1.12;

        letter-spacing: -0.03em;
    }

    .terminal {
        position: relative;

        width: 100%;

        padding: 20px;

        border-radius: 16px;

        overflow: hidden;

        background: #07090d;

        border: 1px solid rgba(255,255,255,0.07);

        box-shadow:
            inset 0 0 35px rgba(0,0,0,0.4);
    }

    .terminal-bar {
        display: flex;
        gap: 6px;

        margin-bottom: 16px;
    }

    .dot {
        width: 9px;
        height: 9px;

        border-radius: 50%;

        background: #434957;
    }

    .terminal-text {
        margin: 0;

        color: #ff6b8a;

        font-family:
            "SFMono-Regular",
            Consolas,
            "Liberation Mono",
            monospace;

        font-size: clamp(13px, 2vw, 15px);

        line-height: 1.65;

        white-space: pre-wrap;
        overflow-wrap: anywhere;
        word-break: break-word;
    }


    /* ======================================================
       INFO SECTIONS
       ====================================================== */

    .info-grid {
        display: grid;

        grid-template-columns:
            repeat(2, minmax(0, 1fr));

        gap: 13px;

        margin-top: 18px;
    }

    .info {
        min-width: 0;

        padding: 17px;

        border-radius: 15px;

        background: rgba(255,255,255,0.025);

        border: 1px solid rgba(255,255,255,0.055);
    }

    .info.full {
        grid-column: 1 / -1;
    }

    .info-label {
        margin-bottom: 7px;

        color: #747d8e;

        font-size: 11px;
        font-weight: 900;

        text-transform: uppercase;
        letter-spacing: 0.09em;
    }

    .info-text {
        margin: 0;

        color: #dce1ea;

        font-size: 14px;
        line-height: 1.65;

        overflow-wrap: anywhere;
    }

    .excuse {
        color: #ddd8ff;

        font-size: clamp(17px, 2.5vw, 22px);

        line-height: 1.45;

        font-weight: 800;
    }


    /* ======================================================
       BUTTONS
       ====================================================== */

    .actions {
        display: grid;

        grid-template-columns:
            minmax(0, 1fr)
            minmax(0, 1fr)
            auto;

        gap: 10px;

        margin-top: 20px;
    }

    .btn {
        min-width: 0;
        min-height: 54px;

        padding: 0 17px;

        border-radius: 13px;

        border: 1px solid rgba(255,255,255,0.09);

        color: #f5f7fb;

        background: #171b24;

        font-weight: 800;

        transition:
            transform .15s ease,
            background .15s ease,
            border-color .15s ease;
    }

    .btn:hover {
        background: #1e2430;
        border-color: rgba(255,255,255,0.16);
    }

    .btn:active {
        transform: scale(0.985);
    }

    .btn.primary {
        border: 0;

        background:
            linear-gradient(
                135deg,
                #705cff,
                #4d7fff
            );

        box-shadow:
            0 10px 30px rgba(84,82,255,0.22);
    }

    .btn.copy {
        min-width: 110px;
    }


    /* ======================================================
       SIDE PANEL
       ====================================================== */

    .side-card {
        padding: 20px;
    }

    .side-title {
        margin: 0 0 10px;

        font-size: 18px;
    }

    .side-description {
        margin: 0 0 17px;

        color: #858e9f;

        font-size: 13px;
        line-height: 1.6;
    }

    .tips {
        display: grid;
        gap: 9px;
    }

    .tip {
        padding: 12px 13px;

        border-radius: 12px;

        background: rgba(255,255,255,0.025);

        border: 1px solid rgba(255,255,255,0.05);

        color: #adb5c4;

        font-size: 13px;
        line-height: 1.5;
    }

    .tip strong {
        color: #e6e9ef;
    }


    /* ======================================================
       FOOTER
       ====================================================== */

    footer {
        padding: 25px 0 5px;

        text-align: center;

        color: #596273;

        font-size: 12px;

        line-height: 1.6;
    }


    /* ======================================================
       TOAST
       ====================================================== */

    .toast {
        position: fixed;

        z-index: 9999;

        left: 50%;

        bottom:
            max(18px, env(safe-area-inset-bottom));

        transform:
            translate(-50%, 20px);

        width: max-content;
        max-width: calc(100vw - 30px);

        padding: 12px 16px;

        border-radius: 999px;

        background: rgba(30,34,44,0.96);

        border: 1px solid rgba(255,255,255,0.10);

        box-shadow: 0 15px 45px rgba(0,0,0,0.35);

        color: white;

        font-size: 13px;
        font-weight: 700;

        opacity: 0;
        pointer-events: none;

        transition:
            opacity .2s ease,
            transform .2s ease;
    }

    .toast.show {
        opacity: 1;

        transform:
            translate(-50%, 0);
    }


    /* ======================================================
       TABLETS
       ====================================================== */

    @media (max-width: 900px) {

        .main-grid {
            grid-template-columns: 1fr;
        }

        .side-card {
            order: 2;
        }

    }


    /* ======================================================
       PHONES
       ====================================================== */

    @media (max-width: 680px) {

        .page {
            padding-left: max(12px, env(safe-area-inset-left));
            padding-right: max(12px, env(safe-area-inset-right));
        }

        header {
            padding-top: 20px;
        }

        .logo {
            width: 62px;
            height: 62px;

            border-radius: 18px;

            font-size: 30px;
        }

        .search-box {
            flex-direction: column;
        }

        .search-input {
            width: 100%;
        }

        .search-button {
            width: 100%;
        }

        .main-grid {
            gap: 12px;
        }

        .card {
            border-radius: 18px;
        }

        .card-header {
            padding: 14px 15px;
        }

        .error-content {
            padding: 17px;
        }

        .info-grid {
            grid-template-columns: 1fr;
        }

        .info.full {
            grid-column: auto;
        }

        .actions {
            grid-template-columns: 1fr;
        }

        .btn,
        .btn.copy {
            width: 100%;
        }

        .results {
            max-height: 55vh;
        }

    }


    /* ======================================================
       SMALL PHONES
       ====================================================== */

    @media (max-width: 380px) {

        h1 {
            font-size: 29px;
        }

        .subtitle {
            font-size: 13px;
        }

        .terminal {
            padding: 14px;
        }

        .error-title {
            font-size: 23px;
        }

        .info {
            padding: 14px;
        }

    }


    /* ======================================================
       LANDSCAPE PHONE
       ====================================================== */

    @media (max-height: 500px) and (orientation: landscape) {

        header {
            padding-top: 12px;
            padding-bottom: 12px;
        }

        .logo {
            width: 48px;
            height: 48px;
            font-size: 24px;
        }

        h1 {
            margin-top: 8px;
            font-size: 28px;
        }

        .subtitle {
            display: none;
        }

        .search-panel {
            margin-bottom: 12px;
        }

    }


    /* ======================================================
       TOUCH DEVICES
       ====================================================== */

    @media (pointer: coarse) {

        button,
        input {
            touch-action: manipulation;
        }

        button {
            min-height: 54px;
        }

        .result-item {
            min-height: 64px;
        }

    }


    /* ======================================================
       REDUCED MOTION
       ====================================================== */

    @media (prefers-reduced-motion: reduce) {

        *,
        *::before,
        *::after {
            scroll-behavior: auto !important;
            transition: none !important;
            animation: none !important;
        }

    }

</style>
</head>


<body>

<div class="page">

    <header>

        <div class="logo" aria-hidden="true">
            🧑‍💻
        </div>

        <h1>Programmer Error Generator</h1>

        <p class="subtitle">
            Search an error. Discover the cause. Find the fix.
            Then generate a completely professional excuse.
        </p>

    </header>


    <!-- =====================================================
         SEARCH
         ===================================================== -->

    <section class="search-panel">

        <div class="search-box">

            <input
                id="searchInput"
                class="search-input"
                type="search"
                autocomplete="off"
                spellcheck="false"
                placeholder="Search an error... e.g. 404, TypeError, CORS, Python, Git"
                aria-label="Search programmer errors"
            >

            <button
                id="searchButton"
                class="search-button"
                type="button"
            >
                🔎 Search
            </button>

        </div>


        <div
            id="results"
            class="results"
            aria-live="polite"
        ></div>

    </section>


    <!-- =====================================================
         MAIN
         ===================================================== -->

    <main class="main-grid">


        <!-- =================================================
             ERROR CARD
             ================================================= -->

        <section class="card error-card">

            <div class="card-header">

                <span
                    id="category"
                    class="category"
                >
                    JavaScript
                </span>

                <span
                    id="errorNumber"
                    class="error-number"
                >
                    ERROR #001
                </span>

            </div>


            <div class="error-content">

                <h2
                    id="errorTitle"
                    class="error-title"
                >
                    Loading error...
                </h2>


                <div class="terminal">

                    <div class="terminal-bar">
                        <span class="dot"></span>
                        <span class="dot"></span>
                        <span class="dot"></span>
                    </div>

                    <p
                        id="errorText"
                        class="terminal-text"
                    ></p>

                </div>


                <div class="info-grid">

                    <div class="info">

                        <div class="info-label">
                            What happened?
                        </div>

                        <p
                            id="cause"
                            class="info-text"
                        ></p>

                    </div>


                    <div class="info">

                        <div class="info-label">
                            Suggested fix
                        </div>

                        <p
                            id="fix"
                            class="info-text"
                        ></p>

                    </div>


                    <div class="info full">

                        <div class="info-label">
                            🧑‍💻 Official Programmer Excuse
                        </div>

                        <p
                            id="excuse"
                            class="info-text excuse"
                        ></p>

                    </div>

                </div>


                <div class="actions">

                    <button
                        id="generateButton"
                        class="btn primary"
                        type="button"
                    >
                        🎲 Generate New Error
                    </button>

                    <button
                        id="randomButton"
                        class="btn"
                        type="button"
                    >
                        🔀 Random Error
                    </button>

                    <button
                        id="copyButton"
                        class="btn copy"
                        type="button"
                    >
                        📋 Copy
                    </button>

                </div>

            </div>

        </section>


        <!-- =================================================
             SIDE INFORMATION
             ================================================= -->

        <aside class="card side-card">

            <h3 class="side-title">
                🔎 Search → Excuse
            </h3>

            <p class="side-description">
                Type almost anything related to a programming
                problem. The generator searches the error,
                cause, fix and excuse database.
            </p>


            <div class="tips">

                <div class="tip">
                    <strong>Try:</strong>
                    <br>
                    404
                </div>

                <div class="tip">
                    <strong>Try:</strong>
                    <br>
                    TypeError
                </div>

                <div class="tip">
                    <strong>Try:</strong>
                    <br>
                    CORS
                </div>

                <div class="tip">
                    <strong>Try:</strong>
                    <br>
                    Python
                </div>

                <div class="tip">
                    <strong>Try:</strong>
                    <br>
                    Git merge conflict
                </div>

                <div class="tip">
                    <strong>Try:</strong>
                    <br>
                    database
                </div>

                <div class="tip">
                    <strong>Try:</strong>
                    <br>
                    permission
                </div>

                <div class="tip">
                    <strong>Try:</strong>
                    <br>
                    deployment
                </div>

            </div>

        </aside>

    </main>


    <footer>

        Programmer Error Generator •
        Static website •
        No database •
        No LocalStorage •
        No tracking

        <br>

        Press <strong>/</strong> to search •
        Press <strong>Esc</strong> to close results

    </footer>

</div>


<!-- =========================================================
     TOAST
     ========================================================= -->

<div
    id="toast"
    class="toast"
    role="status"
    aria-live="polite"
></div>


<script>

    /* ========================================================
       DATA
       ======================================================== */

    const SCENARIOS = __SCENARIOS__;


    /* ========================================================
       ELEMENTS
       ======================================================== */

    const searchInput =
        document.getElementById("searchInput");

    const searchButton =
        document.getElementById("searchButton");

    const results =
        document.getElementById("results");

    const category =
        document.getElementById("category");

    const errorNumber =
        document.getElementById("errorNumber");

    const errorTitle =
        document.getElementById("errorTitle");

    const errorText =
        document.getElementById("errorText");

    const cause =
        document.getElementById("cause");

    const fix =
        document.getElementById("fix");

    const excuse =
        document.getElementById("excuse");

    const generateButton =
        document.getElementById("generateButton");

    const randomButton =
        document.getElementById("randomButton");

    const copyButton =
        document.getElementById("copyButton");

    const toast =
        document.getElementById("toast");


    /* ========================================================
       STATE
       ======================================================== */

    let currentIndex = -1;

    let lastRandomIndex = -1;

    let toastTimer = null;


    /* ========================================================
       HELPERS
       ======================================================== */

    function escapeHtml(value) {

        return String(value)
            .replaceAll("&", "&amp;")
            .replaceAll("<", "&lt;")
            .replaceAll(">", "&gt;")
            .replaceAll('"', "&quot;")
            .replaceAll("'", "&#039;");

    }


    function showToast(message) {

        toast.textContent = message;

        toast.classList.add("show");

        clearTimeout(toastTimer);

        toastTimer = setTimeout(() => {

            toast.classList.remove("show");

        }, 1800);

    }


    /* ========================================================
       DISPLAY ERROR
       ======================================================== */

    function displayScenario(index) {

        if (!SCENARIOS.length) {
            return;
        }

        currentIndex = index;

        const item = SCENARIOS[index];

        category.textContent =
            item.category;

        errorNumber.textContent =
            "ERROR #" +
            String(index + 1).padStart(3, "0");

        errorTitle.textContent =
            item.title;

        errorText.textContent =
            item.error;

        cause.textContent =
            item.cause;

        fix.textContent =
            item.fix;

        excuse.textContent =
            item.excuse;

        document.title =
            item.title +
            " • Programmer Error Generator";

    }


    /* ========================================================
       RANDOM ERROR
       ======================================================== */

    function randomScenario() {

        if (SCENARIOS.length === 1) {

            lastRandomIndex = 0;

            displayScenario(0);

            return;
        }


        let index;

        do {

            index =
                Math.floor(
                    Math.random() *
                    SCENARIOS.length
                );

        } while (
            index === lastRandomIndex
        );


        lastRandomIndex = index;

        displayScenario(index);

        results.classList.remove("visible");

    }


    /* ========================================================
       SEARCH SCORE
       ======================================================== */

    function scoreScenario(item, query) {

        const q =
            query.toLowerCase().trim();

        if (!q) {
            return 0;
        }


        const fields = [

            {
                value: item.category,
                weight: 8
            },

            {
                value: item.title,
                weight: 10
            },

            {
                value: item.error,
                weight: 9
            },

            {
                value: item.cause,
                weight: 4
            },

            {
                value: item.fix,
                weight: 3
            },

            {
                value: item.excuse,
                weight: 2
            }

        ];


        let score = 0;


        for (const field of fields) {

            const value =
                field.value.toLowerCase();


            if (value === q) {

                score +=
                    field.weight * 10;

                continue;

            }


            if (value.includes(q)) {

                score +=
                    field.weight;

            }


            const words =
                q.split(/\s+/)
                    .filter(Boolean);


            for (const word of words) {

                if (word.length < 2) {
                    continue;
                }

                if (value.includes(word)) {

                    score +=
                        field.weight * 0.7;

                }

            }

        }


        return score;

    }


    /* ========================================================
       SEARCH
       ======================================================== */

    function searchErrors(query) {

        const q =
            query.trim();


        if (!q) {

            results.innerHTML = "";

            results.classList.remove("visible");

            return;

        }


        const matches =
            SCENARIOS
                .map((item, index) => ({

                    item,
                    index,
                    score:
                        scoreScenario(
                            item,
                            q
                        )

                }))
                .filter(
                    result =>
                        result.score > 0
                )
                .sort(
                    (a, b) =>
                        b.score - a.score
                )
                .slice(0, 12);


        if (!matches.length) {

            results.innerHTML = `
                <div class="no-results">
                    No programmer error found for
                    "<strong>${escapeHtml(q)}</strong>".
                    <br><br>
                    Try <strong>404</strong>,
                    <strong>TypeError</strong>,
                    <strong>CORS</strong>,
                    <strong>Python</strong>,
                    <strong>Git</strong> or
                    <strong>database</strong>.
                </div>
            `;

            results.classList.add("visible");

            return;

        }


        results.innerHTML =
            matches.map(result => {

                const item =
                    result.item;

                return `
                    <button
                        class="result-item"
                        type="button"
                        data-index="${result.index}"
                    >

                        <div class="result-title">
                            ${escapeHtml(item.title)}
                        </div>

                        <div class="result-meta">
                            ${escapeHtml(item.category)}
                            •
                            ${escapeHtml(item.error)}
                        </div>

                    </button>
                `;

            }).join("");


        results.classList.add("visible");


        results
            .querySelectorAll(".result-item")
            .forEach(button => {

                button.addEventListener(
                    "click",
                    () => {

                        const index =
                            Number(
                                button.dataset.index
                            );

                        displayScenario(index);

                        results.classList.remove(
                            "visible"
                        );

                        searchInput.blur();

                        showToast(
                            "Error found — excuse generated."
                        );

                    }
                );

            });

    }


    /* ========================================================
       SEARCH BUTTON
       ======================================================== */

    searchButton.addEventListener(
        "click",
        () => {

            searchErrors(
                searchInput.value
            );

        }
    );


    /* ========================================================
       LIVE SEARCH
       ======================================================== */

    searchInput.addEventListener(
        "input",
        () => {

            searchErrors(
                searchInput.value
            );

        }
    );


    /* ========================================================
       ENTER SEARCH
       ======================================================== */

    searchInput.addEventListener(
        "keydown",
        event => {

            if (event.key === "Enter") {

                event.preventDefault();

                searchErrors(
                    searchInput.value
                );

            }

            if (event.key === "Escape") {

                results.classList.remove(
                    "visible"
                );

                searchInput.blur();

            }

        }
    );


    /* ========================================================
       GENERATE BUTTON
       ======================================================== */

    generateButton.addEventListener(
        "click",
        () => {

            randomScenario();

            showToast(
                "New programmer disaster generated."
            );

        }
    );


    /* ========================================================
       RANDOM BUTTON
       ======================================================== */

    randomButton.addEventListener(
        "click",
        () => {

            randomScenario();

            showToast(
                "Random error generated."
            );

        }
    );


    /* ========================================================
       COPY
       ======================================================== */

    async function copyError() {

        if (currentIndex < 0) {
            return;
        }


        const item =
            SCENARIOS[currentIndex];


        const text =
`PROGRAMMER ERROR

Category: ${item.category}

Error: ${item.error}

What happened:
${item.cause}

Suggested fix:
${item.fix}

Official Programmer Excuse:
${item.excuse}`;


        try {

            await navigator.clipboard.writeText(
                text
            );

            showToast(
                "Error + excuse copied."
            );

        } catch {

            const textarea =
                document.createElement("textarea");

            textarea.value =
                text;

            textarea.style.position =
                "fixed";

            textarea.style.opacity =
                "0";

            document.body.appendChild(
                textarea
            );

            textarea.select();

            try {

                document.execCommand(
                    "copy"
                );

                showToast(
                    "Copied."
                );

            } catch {

                showToast(
                    "Copy failed — select the text manually."
                );

            }

            textarea.remove();

        }

    }


    copyButton.addEventListener(
        "click",
        copyError
    );


    /* ========================================================
       KEYBOARD SHORTCUTS
       ======================================================== */

    document.addEventListener(
        "keydown",
        event => {

            if (
                event.key === "/" &&
                document.activeElement !== searchInput
            ) {

                event.preventDefault();

                searchInput.focus();

            }


            if (
                event.key === "Escape"
            ) {

                results.classList.remove(
                    "visible"
                );

            }

        }
    );


    /* ========================================================
       CLICK OUTSIDE SEARCH
       ======================================================== */

    document.addEventListener(
        "click",
        event => {

            if (
                !event.target.closest(
                    ".search-panel"
                )
            ) {

                results.classList.remove(
                    "visible"
                );

            }

        }
    );


    /* ========================================================
       NEW ERROR WHEN PAGE BECOMES VISIBLE
       ======================================================== */

    let pageWasHidden = false;


    document.addEventListener(
        "visibilitychange",
        () => {

            if (
                document.hidden
            ) {

                pageWasHidden = true;

                return;

            }


            if (
                pageWasHidden &&
                document.visibilityState === "visible"
            ) {

                pageWasHidden = false;


                if (
                    document.activeElement !== searchInput &&
                    !searchInput.value.trim()
                ) {

                    randomScenario();

                }

            }

        }
    );


    /* ========================================================
       INITIAL ERROR
       ======================================================== */

    randomScenario();

</script>

</body>
</html>
'''


# Replace the data placeholder with the complete scenario database.
HTML = HTML.replace(
    "__SCENARIOS__",
    DATA
)


# Write the generated website.
output = Path("index.html")

output.write_text(
    HTML,
    encoding="utf-8"
)


print()
print("=" * 60)
print("PROGRAMMER ERROR GENERATOR BUILD COMPLETE")
print("=" * 60)
print()
print(f"Generated: {output.resolve()}")
print(f"Errors included: {len(SCENARIOS)}")
print()
print("Everything is contained inside build.py.")
print("index.html is generated automatically.")
print()
print("Run locally:")
print("    python build.py")
print()
print("Then open:")
print("    index.html")
print()
print("=" * 60)
