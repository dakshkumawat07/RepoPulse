# 🚀 RepoPulse

> **An explainable Git repository engineering analytics platform that turns repository history into actionable engineering insights.**

RepoPulse is a Python-based developer tool designed to analyze Git repositories and provide a clear, evidence-based view of how a codebase evolves.

Instead of simply displaying commit counts, RepoPulse currently analyzes development patterns such as **commit activity, contributor activity, file change frequency, code churn, and change hotspots**.

The project is being built incrementally with a strong focus on **explainability, clean architecture, testing, reproducibility, and real-world software engineering practices**.

---

## 📌 Project Status

**Current Milestone:** `v0.3.0-dev`  
**Status:** 🚧 Active Development

RepoPulse has moved beyond the initial repository-analyzer foundation and now includes several repository history and code-change analysis capabilities.

The current focus is strengthening the local Git analysis engine before introducing GitHub integration, APIs, databases, or a web dashboard.

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

This provides an early foundation for future repository health and engineering analysis.

---

## 🖥️ Example Output

The following example shows multiple current RepoPulse analysis sections together in **one continuous output block**:

```text
RepoPulse
────────────────────────────────────
Repository:    .
Branch:        main
Total Commits: 9

First Commit
────────────────────────────────────
Hash:    8d5bd64c63b35c5af7fdc2dcb072bbfe02cf5e27
Author:  Daksh Kumawat
Date:    2026-09-05 06:43:09 -0400
Message: chore: initialize RepoPulse project

Latest Commit
────────────────────────────────────
Hash:    aa88edc29579da294e55fa711d78d83e052dff1b
Author:  Daksh Kumawat
Date:    2026-09-15 06:14:41 -0400
Message: feat: add code churn analysis

Recent Activity
────────────────────────────────────
2026-09-15 06:14:41 -0400 | Daksh Kumawat | feat: add code churn analysis
2026-09-14 05:12:10 -0400 | Daksh Kumawat | feat: add file hotspot analysis
2026-09-13 11:35:08 -0400 | Daksh Kumawat | feat: add contributor activity analysis
2026-09-12 04:54:55 -0400 | Daksh Kumawat | feat: add commit activity analysis
2026-09-11 04:54:25 -0400 | Daksh Kumawat | feat: add commit history analysis

Commit Activity
────────────────────────────────────
2026-09-15 | 1 commit(s)
2026-09-14 | 1 commit(s)
2026-09-13 | 1 commit(s)
2026-09-12 | 1 commit(s)
2026-09-11 | 1 commit(s)
2026-09-10 | 1 commit(s)
2026-09-09 | 2 commit(s)
2026-09-05 | 1 commit(s)

File Hotspots
────────────────────────────────────
src/repopulse/analyzer.py | 7 change(s)
src/repopulse/cli.py | 7 change(s)
tests/test_analyzer.py | 3 change(s)
README.md | 2 change(s)
.gitignore | 1 change(s)
pytest.ini | 1 change(s)

Code Churn
────────────────────────────────────
README.md | +799 / -258
src/repopulse/analyzer.py | +313 / -11
src/repopulse/cli.py | +160 / -25
tests/test_analyzer.py | +67 / -8

Change Hotspots
────────────────────────────────────
src/repopulse/analyzer.py | 7 change(s) | +313 / -11 | 324 churn
src/repopulse/cli.py | 7 change(s) | +160 / -25 | 185 churn
tests/test_analyzer.py | 3 change(s) | +67 / -8 | 75 churn
README.md | 2 change(s) | +799 / -258 | 1057 churn

Contributor Activity
────────────────────────────────────
Daksh Kumawat | 9 commit(s)
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
CLI Report
```

The current implementation uses Git as the source of repository history and calculates metrics from that history.

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

- **Python 3** — Application and analysis engine
- **Git** — Version control and repository history
- **Python Standard Library** — Core implementation
- **subprocess** — Git command execution
- **dataclasses** — Structured commit information

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

### Git & Repository Analysis

- Git repositories
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
| v0.1.0 | Project foundation & local repository analyzer | ✅ Completed |
| v0.2.0 | Commit intelligence | ✅ Completed |
| v0.3.0 | Code change and hotspot analysis | 🔄 In Development |
| v0.4.0 | Engineering health model | ⏳ Planned |
| v0.5.0 | GitHub integration | ⏳ Planned |
| v0.6.0 | REST API | ⏳ Planned |
| v0.7.0 | Web dashboard | ⏳ Planned |
| v1.0.0 | Production-ready portfolio release | ⏳ Planned |

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

### Phase 3 — Code Change Analysis 🔄

Analyze how files change throughout repository history.

Implemented:

- File change frequency
- Code churn
- Change hotspots

Planned improvements:

- Better edge-case handling
- Additional tests
- More robust analysis
- Cleaner analysis abstractions

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

Allow RepoPulse to analyze repositories using GitHub repositories and APIs.

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
│       ├── analyzer.py
│       └── cli.py
├── tests/
│   └── test_analyzer.py
├── .gitignore
├── pytest.ini
└── README.md
```

### Important Files

**`src/repopulse/analyzer.py`**

Contains the core Git repository analysis logic.

**`src/repopulse/cli.py`**

Handles command-line arguments and displays analysis results.

**`src/repopulse/__main__.py`**

Allows RepoPulse to be executed using Python's module syntax.

**`tests/test_analyzer.py`**

Contains automated tests for repository analysis functionality.

**`pytest.ini`**

Contains the current pytest configuration.

---

## 🚀 How to Use

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

On Windows:

```powershell
.venv\Scripts\activate
```

### 4. Install Testing Dependency

```bash
pip install pytest
```

### 5. Analyze a Repository

Analyze the current repository:

```bash
python -m src.repopulse analyze .
```

Or provide another local Git repository:

```bash
python -m src.repopulse analyze /path/to/repository
```

### 6. Run Tests

```bash
pytest
```

---

## 🧪 Testing

RepoPulse currently uses **pytest** for automated testing.

The current test suite covers areas including:

- Git repository detection
- Commit count
- Commit metadata
- Recent commit history
- Commit activity
- File change frequency
- Change hotspot structure

Current development state:

```text
8 tests passed
```

The test suite will continue to grow as new analysis capabilities are introduced.

Future testing improvements may include:

- Temporary test repositories
- More edge cases
- Invalid repository handling
- Multiple repository scenarios
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

The project prioritizes **engineering depth, transparency, and practical usefulness** over simply increasing the number of features.

---

## 👨‍💻 Author

**Daksh Kumawat**

Computer Science & Engineering Student

GitHub: [@dakshkumawat07](https://github.com/dakshkumawat07)

---

## 📌 Future Vision

RepoPulse started with a simple question:

> **Can Git history tell us something meaningful about the engineering evolution of a codebase?**

The long-term vision is to turn that question into a practical developer tool that makes repository evolution easier to understand.

```text
Measure the evidence.
Explain the pattern.
Improve the engineering.
```

---

## 📄 License

License will be added before the first stable release.
