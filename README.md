# 🧑‍💻 Programmer Error Generator

A humorous, random **Programmer Error Generator** that produces realistic programming problems, bugs, error messages, symptoms, causes, fixes, environments, and programmer jokes.

It is designed as a **fully static website** that can be hosted on **GitHub Pages, Render Static Site, or any static web hosting service**.

---

## 🚀 Live Concept

Every time the website is opened or refreshed, it generates a new random programming problem.

Examples:

> `TypeError: Cannot read properties of undefined`

> "Works perfectly on my machine."

> **Problem:** Everything worked until you deployed it.

> **Environment:** Production

> **Likely Cause:** Environment variables are missing.

> **Fix:** Check the production environment configuration.

---

# ✨ Features

## 🎲 Random Error Generation

The site automatically generates a new scenario when:

- The page is opened
- The page is refreshed
- The user clicks **Generate New Error**

No previous scenario needs to be stored.

---

## 🧑‍💻 Real Programming Problems

The generator contains realistic programming situations covering areas such as:

### JavaScript

- `TypeError`
- `ReferenceError`
- `SyntaxError`
- `undefined`
- `null`
- `NaN`
- Promise errors
- `async/await`
- Event loop problems
- Race conditions
- `this` problems
- Closures
- Hoisting
- Module/import problems
- `fetch()` failures
- JSON parsing
- DOM errors
- Event listener problems
- Memory leaks
- Timers
- Form handling
- Browser compatibility

---

### Python

- `NameError`
- `TypeError`
- `ValueError`
- `KeyError`
- `IndexError`
- `AttributeError`
- `ImportError`
- `ModuleNotFoundError`
- `SyntaxError`
- `IndentationError`
- Virtual environment problems
- `pip` problems
- Dependency conflicts
- Python version conflicts
- File handling errors
- Mutable default arguments
- Async problems
- Encoding problems
- Flask/Django problems

---

### HTML & CSS

- Broken layouts
- Flexbox problems
- Grid problems
- Overflow
- `z-index`
- Positioning
- Responsive design
- Mobile layout problems
- Missing viewport configuration
- Font problems
- Image sizing
- CSS specificity
- Unexpected margins
- Fixed/sticky positioning
- Touchscreen issues
- Button problems
- Form problems

---

### Git & GitHub

- Merge conflicts
- Rebase conflicts
- Detached HEAD
- Wrong branch
- Wrong remote
- Push rejected
- Non-fast-forward errors
- Untracked files
- `.gitignore` problems
- Accidentally committed secrets
- Authentication failures
- Force push disasters
- Stash problems
- Cherry-pick conflicts
- Case-sensitive filename problems

---

### APIs & HTTP

- HTTP 400
- HTTP 401
- HTTP 403
- HTTP 404
- HTTP 405
- HTTP 409
- HTTP 422
- HTTP 429
- HTTP 500
- HTTP 502
- HTTP 503
- HTTP 504
- CORS errors
- Authentication failures
- Invalid JSON
- Wrong Content-Type
- Timeout errors
- Rate limiting
- Pagination problems
- Token problems
- Cookie problems
- CSRF problems
- API contract mismatches

---

### SQL & Databases

- SQL syntax errors
- `NULL` problems
- Duplicate rows
- Incorrect JOINs
- Missing indexes
- Slow queries
- Unique constraint failures
- Foreign key failures
- Transaction problems
- Deadlocks
- Connection problems
- Migration failures
- Encoding problems
- N+1 queries
- Connection pool problems

---

### Node.js & npm

- `npm install` problems
- `npm ci` problems
- Dependency conflicts
- `package-lock.json` problems
- Node version problems
- ESM/CommonJS conflicts
- Missing packages
- `node_modules` problems
- Environment variable problems
- Port already in use
- Startup failures
- Dependency vulnerabilities

---

### Linux & Command Line

- `Permission denied`
- `command not found`
- Incorrect `PATH`
- Wrong working directory
- Port conflicts
- Process problems
- File permissions
- `chmod`
- `chown`
- Disk full
- DNS problems
- Environment variables
- CRLF/LF problems

---

### Docker

- Container exits immediately
- Port already allocated
- Incorrect Dockerfile
- Wrong build context
- Environment variables missing
- Volume problems
- Container networking
- `localhost` confusion
- Image size problems
- Docker cache problems
- Architecture mismatch
- Health check failures

---

### Deployment

- Production works differently from development
- Missing environment variables
- Wrong build command
- Wrong start command
- Wrong Node/Python version
- Missing files
- Incorrect publish directory
- Static vs server deployment confusion
- Build failures
- Runtime failures
- Health-check failures
- Deployment configuration problems

---

### GitHub Pages & Static Hosting

The generator also includes problems such as:

- Missing `index.html`
- Incorrect paths
- Case-sensitive filenames
- Missing static files
- Incorrect publish directory
- SPA routing problems
- Relative path problems
- Browser caching
- Build configuration problems

---

### Render

Common Render deployment problems include:

- Incorrect build command
- Incorrect publish directory
- Using Web Service instead of Static Site
- Python build failures
- Missing generated `index.html`
- Incorrect repository configuration
- Incorrect branch
- Missing environment variables
- Build output problems

---

### 🔐 Security

Security-related programming scenarios include:

- XSS
- SQL injection
- CSRF
- Command injection
- Path traversal
- Exposed API keys
- Exposed secrets
- Insecure password storage
- Authentication problems
- Session problems
- CORS misconfiguration
- Unsafe file uploads
- Missing rate limiting
- Dependency supply-chain risks

---

### 🧪 Testing & Debugging

Examples include:

- Tests passing locally but failing in CI
- Flaky tests
- Race conditions
- Incorrect mocks
- Wrong test environment
- Timezone problems
- Hidden test failures
- Snapshot problems
- Browser-specific bugs
- Mobile-only bugs
- Production-only bugs

---

# 😂 Programmer Humor

The generator also produces programmer jokes and situations.

Examples:

- "Works on my machine™"
- "It worked yesterday."
- "Don't touch that code."
- "One small CSS change."
- "The production server has chosen violence."
- "Just restart it."
- "Have you tried turning it off and on again?"
- "It was working before I cleaned up the code."
- "The bug disappeared when I added `console.log()`."
- "Temporary fix from 2023 is now production architecture."
- "Nobody knows why it works. Nobody is allowed to touch it."
- "The compiler knows what you did."
- "There are no bugs. There are undocumented features."

---

# 🧠 How It Works

The project uses a very simple architecture.

```text
build.py
   │
   │ generates
   ▼
index.html
   │
   │ contains
   ├── HTML
   ├── CSS
   ├── JavaScript
   └── Error/Scenario Data
   │
   ▼
Static Website
