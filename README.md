# 🚀 RepoPulse

> **An explainable Git repository engineering analytics platform that turns repository history into actionable engineering insights.**

RepoPulse is a Python-based developer tool designed to analyze Git repositories and provide a clear, evidence-based view of how a codebase evolves.

Instead of simply displaying commit counts, RepoPulse currently analyzes development patterns such as **commit activity, contributor activity, file change frequency, code churn, and change hotspots**.

The project is being built incrementally with a strong focus on **explainability, clean architecture, testing, reproducibility, and real-world software engineering practices**.

---

## 📌 Project Status

**Current Milestone:** `v0.3.0-dev`  
**Status:** 🚧 Active Development

RepoPulse has moved beyond the initial repository-analyzer foundation and now includes several repository-history and code-change analysis capabilities.

The current focus is completing and strengthening the local Git analysis engine before introducing GitHub integration, APIs, databases, or a web dashboard.

Recent improvements include:

- Proper CLI exit codes for invalid repositories and Git-command failures
- Support for Git worktrees
- Installable CLI packaging through `pyproject.toml`
- Expanded automated test coverage

---

## 🎯 Problem Statement

Git repositories contain a large amount of information about how software is developed, but much of that information is difficult to interpret quickly.

Developers can see commits, changed files, contributors, branches, and lines added or removed. However, raw Git data does not automatically provide a convenient overview of questions such as:

- Which files change most frequently?
- Where is development activity concentrated?
- Which files have high code churn?
- How has development activity changed over time?
- Which contributors are active in the repository?
- Which files have experienced the most changes?

RepoPulse aims to transform raw repository history into **structured, measurable, and explainable engineering insights**.

---

## 💡 Project Vision

The long-term vision of RepoPulse is to become a lightweight engineering intelligence platform for Git repositories.

A future version may provide higher-level indicators such as:

```text
Repository Health
────────────────────────────

Code Stability
Commit Activity
Documentation
Contributor Distribution
Change Concentration

Engineering Insights
────────────────────────────

Evidence
Calculation
Interpretation
Limitations
```

RepoPulse will not simply produce unexplained numbers.

Every important metric should eventually provide:

- The underlying evidence
- The calculation used
- The reason for the result
- Appropriate interpretation
- Known limitations

> **Important:** High activity or high churn does not automatically mean poor engineering. RepoPulse aims to distinguish measurable repository evidence from interpretation.

---

## ✨ Current Capabilities

### 1. 🔍 Repository Detection

RepoPulse checks whether the provided path is a local Git repository before performing analysis.

It supports both normal Git repositories and Git worktrees.

### 2. 🌿 Branch Analysis

Displays the current Git branch of the repository.

### 3. 📊 Commit Count

Calculates the total number of commits in the repository.

### 4. 🧾 Commit Metadata

Displays information about:

- Commit hash
- Author
- Date
- Commit message

RepoPulse currently reports both the first and latest commits.

### 5. 📜 Commit History

Displays recent commits from the repository, including:

- Commit date
- Author
- Commit message

### 6. 📅 Commit Activity

Groups commits by date to show how frequently development activity occurred.

### 7. 👥 Contributor Activity

Counts commits associated with each contributor.

### 8. 📁 File Change Frequency

Tracks how many times individual files appear in the repository's commit history.

This provides a basic view of files that are changed frequently.

### 9. 🔄 Code Churn

Calculates the total number of lines added and deleted for files across Git history.

Binary file changes that Git reports without numeric additions and deletions are skipped.

### 10. 🔥 Change Hotspots

Combines file change frequency and code churn into a single view.

Each hotspot currently reports:

- File name
- Number of changes
- Lines added
- Lines deleted
- Total churn

This provides an early foundation for future repository-health and engineering analysis.

### 11. 🖥️ Command-Line Interface

RepoPulse provides an installable CLI command:

```bash
repopulse analyze .
```

It also supports JSON output:

```bash
repopulse analyze . --json
```

### 12. ✅ CLI Exit Codes

RepoPulse returns useful exit codes for scripts and future CI workflows:

| Exit Code | Meaning |
|---|---|
| `0` | Analysis completed successfully |
| `1` | Invalid repository or Git-command failure |
| `2` | Invalid command-line usage |

---

## 🖥️ Example Output

The following example shows multiple current RepoPulse analysis sections together in one continuous output block:

```text
RepoPulse
────────────────────────────────────
Repository:    .
Branch:        main
Total Commits: 12

First Commit
────────────────────────────────────
Hash:    <commit-hash>
Author:  <author>
Date:    <date>
Message: <first-commit-message>

Latest Commit
────────────────────────────────────
Hash:    <commit-hash>
Author:  <author>
Date:    <date>
Message: <latest-commit-message>

Recent Activity
────────────────────────────────────
<date> | <author> | <commit-message>

Commit Activity
────────────────────────────────────
2026-10-04 | 1 commit(s)

File Hotspots
────────────────────────────────────
src/repopulse/cli.py | 5 change(s)

Code Churn
────────────────────────────────────
src/repopulse/cli.py | +120 / -20

Change Hotspots
────────────────────────────────────
src/repopulse/cli.py | 5 change(s) | +120 / -20 | 140 churn

Contributor Activity
────────────────────────────────────
Daksh Kumawat | 12 commit(s)
```

---

## ⚙️ How It Works

RepoPulse currently follows a simple analysis pipeline:

```text
Git Repository
      │
      ▼
Git History
      │
      ▼
Repository Analyzer
      │
      ├── Commit Metadata
      ├── Commit History
      ├── Commit Activity
      ├── Contributor Activity
      ├── File Change Frequency
      ├── Code Churn
      └── Change Hotspots
      │
      ▼
CLI Report or JSON Output
```

The current implementation uses Git as the source of repository history and calculates metrics from that history.

RepoPulse currently analyzes local repositories only. It does not need a GitHub token, database, API server, or web dashboard.

---

## 🧠 Engineering Principles

### 1. Explainability

Every important metric should have a clear calculation and understandable interpretation.

### 2. Evidence Before Interpretation

Repository data should be measured first. Interpretations and recommendations should come afterward.

### 3. No Fake Intelligence

RepoPulse will not use meaningless AI-generated scores simply to make the project appear more sophisticated.

### 4. Reproducibility

Given the same repository state and analysis configuration, RepoPulse should produce consistent results.

### 5. Incremental Development

Features are introduced through controlled milestones instead of building the entire application at once.

### 6. Testability

Important analysis logic should be independently testable.

### 7. Professional Git Workflow

Development uses meaningful commits, versioned milestones, testing, documentation, and a clean Git/GitHub workflow.

### 8. Honest Metrics

A metric should never claim more than the underlying repository evidence can support.

---

## 🛠️ Technology Stack

### Core

- **Python 3.13+** — Application and analysis engine
- **Git** — Version control and repository history
- **Python Standard Library** — Core implementation
- **subprocess** — Git command execution
- **dataclasses** — Structured commit information
- **argparse** — Command-line argument parsing
- **json** — Structured JSON output

### Testing

- **Pytest** — Automated testing

### Development

- **Git**
- **GitHub**
- **Linux**
- **Python Virtual Environment**

### Planned Technologies

Future versions may introduce technologies such as:

- FastAPI
- Pydantic
- SQLite
- PostgreSQL
- GitHub API
- React / Next.js
- Data visualization libraries
- Docker
- GitHub Actions

> Technologies will be introduced only when they become necessary for the current milestone.

---

## 📚 Concepts Learned

### Python

- Functions
- Modules
- Classes
- Dataclasses
- Type hints
- Exception handling
- Data structures
- `subprocess`
- Virtual environments
- CLI development
- JSON serialization
- Package structure with `src/`
- Python packaging with `pyproject.toml`

### Git & Repository Analysis

- Git repositories
- Git worktrees
- Commit history
- Branches
- Commit metadata
- File changes
- Lines added and removed
- Code churn
- Repository history analysis

### Software Engineering

- Project architecture
- Separation of concerns
- Modular design
- Error handling
- Automated testing
- CLI application design
- Documentation
- Incremental development
- Professional Git workflow
- Meaningful exit codes
- Installable Python applications

### Data & Analytics

- Data collection
- Data transformation
- Aggregation
- Metric calculation
- Activity analysis
- Change frequency
- Code churn
- Explainable engineering metrics

---

## 📈 Project Progress

| Version | Milestone | Status |
|---|---|---|
| v0.1.0 | Project foundation and local repository analyzer | ✅ Completed |
| v0.2.0 | Commit intelligence | ✅ Completed |
| v0.3.0 | Code change and hotspot analysis | 🚧 In Development |
| v0.4.0 | Engineering health model | ⏳ Planned |
| v0.5.0 | GitHub integration | ⏳ Planned |
| v0.6.0 | REST API | ⏳ Planned |
| v0.7.0 | Web dashboard | ⏳ Planned |
| v1.0.0 | Production-ready portfolio release | 🎯 Planned |

---

## 🗺️ Development Roadmap

### Phase 1 — Repository Analyzer ✅

Build a command-line tool capable of analyzing a local Git repository.

Implemented:

- Repository detection
- Current branch
- Commit count
- First commit
- Latest commit
- Commit metadata
- Initial CLI

---

### Phase 2 — Commit Intelligence ✅

Analyze repository development activity.

Implemented:

- Recent commit history
- Commit activity by date
- Contributor activity
- Commit metadata

---

### Phase 3 — Code Change Analysis 🚧

Analyze how files change throughout repository history.

Implemented:

- File change frequency
- Code churn
- Change hotspots
- JSON output
- Installable CLI command
- CLI error exit codes
- Git worktree support

Current focus:

- Better edge-case handling
- Additional tests
- More robust analysis
- Cleaner analysis abstractions
- Improved documentation
- Packaging and release readiness

---

### Phase 4 — Engineering Health Model 📋

Develop an explainable engineering-health model based on multiple repository signals.

The model should clearly document:

- Inputs
- Calculations
- Assumptions
- Interpretation
- Limitations

---

### Phase 5 — GitHub Integration 📋

Allow RepoPulse to analyze GitHub repositories using GitHub APIs.

Potential capabilities:

- GitHub repository analysis
- Repository metadata
- Contributor information
- Pull request analysis
- Issue activity analysis

---

### Phase 6 — REST API 📋

Introduce a FastAPI backend for programmatic repository analysis.

Potential capabilities:

- Analysis endpoints
- Structured JSON responses
- Input validation
- Error handling
- Analysis services

---

### Phase 7 — Dashboard 📋

Build a professional web interface for exploring repository analytics.

Potential capabilities:

- Repository overview
- Commit activity visualization
- Contributor analytics
- File hotspot visualization
- Code churn visualization
- Historical trends
- Exportable reports

---

### Phase 8 — v1.0 Release 🎯

The long-term goal is a polished release containing:

- CLI
- Repository analysis engine
- GitHub integration
- REST API
- Dashboard
- Automated tests
- Documentation
- Deployment support

---

## 📂 Project Structure

Current structure:

```text
RepoPulse/
├── src/
│   └── repopulse/
│       ├── __init__.py
│       ├── __main__.py
│       ├── cli.py
│       ├── commits.py
│       ├── contributors.py
│       ├── git.py
│       └── hotspots.py
├── tests/
│   └── test_analyzer.py
├── .gitignore
├── pyproject.toml
├── pytest.ini
└── README.md
```

### Important Files

**`src/repopulse/git.py`**

Contains Git repository detection and the shared helper used to run Git commands.

**`src/repopulse/commits.py`**

Contains current-branch analysis, commit counting, commit metadata, commit history, and commit activity analysis.

**`src/repopulse/contributors.py`**

Contains contributor activity analysis.

**`src/repopulse/hotspots.py`**

Contains file change frequency, code churn, and change hotspot analysis.

**`src/repopulse/cli.py`**

Handles command-line arguments and displays analysis results in text or JSON format.

**`src/repopulse/__main__.py`**

Allows RepoPulse to be executed using Python module syntax.

**`tests/test_analyzer.py`**

Contains automated tests that use isolated temporary Git repositories.

**`pyproject.toml`**

Contains package metadata and defines the installable `repopulse` CLI command.

**`pytest.ini`**

Contains the current pytest configuration.

---

## 🚀 How to Use

### Prerequisite

RepoPulse requires:

- Python 3.13 or later
- Git installed and available on your system

Check your versions:

```bash
python --version
git --version
```

### 1. Clone the Repository

```bash
git clone https://github.com/dakshkumawat07/RepoPulse.git
cd RepoPulse
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment

On Linux/macOS:

```bash
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install RepoPulse

```bash
python -m pip install -e .
```

### 5. Install the Testing Dependency

```bash
python -m pip install pytest
```

### 6. Analyze a Repository

Analyze the current repository:

```bash
repopulse analyze .
```

Or provide another local Git repository:

```bash
repopulse analyze /path/to/repository
```

### 7. Generate JSON Output

```bash
repopulse analyze . --json
```

### 8. Use Module Syntax

RepoPulse can also be run through Python after installation:

```bash
python -m repopulse analyze .
```

### 9. Run Tests

```bash
pytest -q
```

---

## 🧪 Testing

RepoPulse currently uses pytest for automated testing.

The current test suite covers:

- Git repository detection
- Git worktree detection
- Commit count
- Commit metadata
- Recent commit history
- Commit activity
- File change frequency
- Change hotspot structure
- JSON CLI output
- Invalid repository CLI errors
- Git-command failure CLI errors

Current development state:

```text
11 passed
```

The test suite will continue to grow as new analysis capabilities are introduced.

Future testing improvements may include:

- Temporary test repositories with multiple branches
- Empty repository handling
- Detached HEAD handling
- Multiple repository scenarios
- Large repository performance tests
- Integration tests
- API tests when the REST API is introduced

---

## 🔐 Security Considerations

RepoPulse may eventually analyze repositories containing sensitive source code.

The project will therefore consider:

- Secure handling of repository data
- Environment variables for secrets
- No hardcoded API credentials
- Safe GitHub API authentication
- Input validation
- Temporary repository cleanup
- Appropriate logging practices

The current version analyzes local Git repositories only and does not upload repository contents to an external service.

Sensitive repository contents should never be unnecessarily transmitted or stored.

---

## 🏗️ Future Architecture

The long-term architecture is expected to evolve toward:

```text
User / CLI
     │
     ▼
Repository Analyzer
     │
     ├───────────────┬───────────────┐
     ▼               ▼               ▼
 Git Data        Code Changes     Metadata
     │               │               │
     └───────────────┼───────────────┘
                     ▼
             Metrics & Analytics
                     │
                     ▼
             Explainable Insights
                     │
                ┌────┴────┐
                ▼         ▼
            REST API   Dashboard
```

> This is a long-term architectural direction. Components will be introduced incrementally.

---

## 🌱 Planned Improvements

Future improvements may include:

- Better handling of detached HEAD repositories
- Support for more Git repository layouts
- Better handling of repositories with multiple root commits
- Configurable history limits
- More robust test repositories
- Repository comparison
- Historical development trends
- Advanced hotspot detection
- Configurable engineering metrics
- Pull request analysis
- Issue activity analysis
- Release analysis
- Exportable reports
- Performance optimization
- GitHub integration
- GitHub Actions CI workflow
- PyPI release support

---

## 🎓 Learning Goal

The primary learning goal of RepoPulse is to move beyond writing isolated Python programs and gain practical experience building a real software engineering system.

Through the project, I am working with:

- Python application development
- Git and repository analysis
- Data processing
- Software architecture
- CLI development
- Automated testing
- Linux development
- GitHub workflows
- REST APIs
- Databases
- Docker
- CI/CD
- GitHub APIs
- Production-oriented development practices

The project is intentionally developed feature-by-feature so that each stage can be understood, tested, and improved.

---

## 🏆 Portfolio Goal

RepoPulse is intended to become a substantial Computer Science portfolio project demonstrating the ability to:

> **Identify a real developer problem → design a solution → implement it incrementally → test it → document it → improve it.**

The project prioritizes engineering depth, transparency, and practical usefulness over simply increasing the number of features.

---

## 👨‍💻 Author

**Daksh Kumawat**

Computer Science & Engineering Student

GitHub: [@dakshkumawat07](https://github.com/dakshkumawat07)

---

## 📌 Future Vision

RepoPulse started with a simple question:

> Can Git history tell us something meaningful about the engineering evolution of a codebase?

The long-term vision is to turn that question into a practical developer tool that makes repository evolution easier to understand.

```text
Measure the evidence.
Explain the pattern.
Improve the engineering.
```

---

## 📄 License

A license will be added before the first stable release.
