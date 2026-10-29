import json
import subprocess
import src.repopulse.git as git_module

from src.repopulse.cli import create_parser

from src.repopulse.commits import (
    get_commit_activity,
    get_commit_count,
    get_commit_history,
    get_current_branch,
    get_latest_commit,
)
from src.repopulse.git import is_git_repository
from src.repopulse.hotspots import (
    get_change_hotspots,
    get_file_change_frequency,
)

def create_test_repository(tmp_path):
    repository = tmp_path / "test-repo"
    repository.mkdir()

    subprocess.run(
        ["git", "init", "-q", "-b", "main", str(repository)],
        check=True,
    )

    subprocess.run(
        ["git", "-C", str(repository), "config", "user.name", "Test User"],
        check=True,
    )

    subprocess.run(
        [
            "git",
            "-C",
            str(repository),
            "config",
            "user.email",
            "test@example.com",
        ],
        check=True,
    )

    return repository


def make_commit(repository, filename, content, message):
    file_path = repository / filename
    file_path.write_text(content)

    subprocess.run(
        ["git", "-C", str(repository), "add", filename],
        check=True,
    )

    subprocess.run(
        ["git", "-C", str(repository), "commit", "-m", message],
        check=True,
        capture_output=True,
        text=True,
    )


def test_tmp_is_not_git_repository(tmp_path):
    assert is_git_repository(str(tmp_path)) is False


def test_commit_count(tmp_path):
    repository = create_test_repository(tmp_path)

    make_commit(repository, "file.txt", "first version", "first commit")
    make_commit(repository, "file.txt", "second version", "second commit")

    assert get_commit_count(str(repository)) == 2


def test_latest_commit_has_metadata(tmp_path):
    repository = create_test_repository(tmp_path)

    make_commit(repository, "file.txt", "hello", "add file")

    commit = get_latest_commit(str(repository))

    assert len(commit.hash) == 40
    assert commit.author == "Test User"
    assert commit.date
    assert commit.message == "add file"


def test_commit_history_returns_recent_commits(tmp_path):
    repository = create_test_repository(tmp_path)

    make_commit(repository, "file.txt", "one", "first commit")
    make_commit(repository, "file.txt", "two", "second commit")
    make_commit(repository, "file.txt", "three", "third commit")

    commits = get_commit_history(str(repository), limit=2)

    assert len(commits) == 2
    assert commits[0].message == "third commit"
    assert commits[1].message == "second commit"


def test_commit_activity_contains_valid_dates(tmp_path):
    repository = create_test_repository(tmp_path)

    make_commit(repository, "file.txt", "one", "first commit")
    make_commit(repository, "file.txt", "two", "second commit")

    activity = get_commit_activity(str(repository))

    assert activity
    assert sum(activity.values()) == 2

    for date, count in activity.items():
        assert len(date) == 10
        assert count > 0


def test_file_change_frequency_contains_valid_counts(tmp_path):
    repository = create_test_repository(tmp_path)

    make_commit(repository, "file.txt", "one", "first commit")
    make_commit(repository, "file.txt", "two", "second commit")
    make_commit(repository, "other.txt", "hello", "third commit")

    file_changes = get_file_change_frequency(str(repository))

    assert file_changes["file.txt"] == 2
    assert file_changes["other.txt"] == 1


def test_change_hotspots_contain_expected_fields(tmp_path):
    repository = create_test_repository(tmp_path)

    make_commit(repository, "file.txt", "one", "first commit")
    make_commit(repository, "file.txt", "one\ntwo\nthree", "second commit")
    make_commit(repository, "other.txt", "hello", "third commit")

    hotspots = get_change_hotspots(str(repository))

    assert hotspots

    first_hotspot = hotspots[0]

    assert first_hotspot["file"] == "file.txt"
    assert first_hotspot["changes"] == 2
    assert first_hotspot["additions"] >= 0
    assert first_hotspot["deletions"] >= 0
    assert first_hotspot["churn"] == (
        first_hotspot["additions"] + first_hotspot["deletions"]
    )



def test_cli_json_output(tmp_path):
    repository = create_test_repository(tmp_path)

    make_commit(repository, "file.txt", "hello", "add file")

    result = subprocess.run(
        [
            "python",
            "-m",
            "src.repopulse",
            "analyze",
            str(repository),
            "--json",
        ],
        capture_output=True,
        text=True,
        check=True,
    )

    data = json.loads(result.stdout)

    assert data["version"] == "0.1.0"
    assert data["repository"] == str(repository)
    assert data["branch"] == "main"
    assert data["total_commits"] == 1
    assert data["latest_commit"]["message"] == "add file"
    assert data["latest_commit"]["author"] == "Test User"


def test_cli_returns_error_for_non_git_repository(tmp_path):
    result = subprocess.run(
        [
            "python",
            "-m",
            "src.repopulse",
            "analyze",
            str(tmp_path),
        ],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 1
    assert "is not a Git repository" in result.stdout


def test_cli_returns_error_when_git_command_fails(tmp_path):
    repository = create_test_repository(tmp_path)

    (repository / ".git" / "HEAD").unlink()

    result = subprocess.run(
        [
            "python",
            "-m",
            "src.repopulse",
            "analyze",
            str(repository),
        ],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 1
    assert result.stdout.startswith("Error:")


def test_git_worktree_is_recognized_as_repository(tmp_path):
    repository = create_test_repository(tmp_path)

    make_commit(repository, "file.txt", "hello", "initial commit")

    worktree = tmp_path / "linked-worktree"

    subprocess.run(
        [
            "git",
            "-C",
            str(repository),
            "worktree",
            "add",
            "-q",
            "-b",
            "test-worktree-branch",
            str(worktree),
        ],
        check=True,
    )

    assert is_git_repository(str(worktree)) is True

def test_cli_version_output():
    result = subprocess.run(
        [
            "python",
            "-m",
            "src.repopulse",
            "--version",
        ],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert result.stdout == "repopulse 0.1.0\n"
    assert result.stderr == ""


def test_cli_returns_error_for_empty_repository(tmp_path):
    repository = create_test_repository(tmp_path)

    result = subprocess.run(
        [
            "python",
            "-m",
            "src.repopulse",
            "analyze",
            str(repository),
        ],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 1
    assert "has no commits" in result.stdout


def test_current_branch_identifies_detached_head(tmp_path):
    repository = create_test_repository(tmp_path)

    make_commit(repository, "file.txt", "hello", "initial commit")

    subprocess.run(
        [
            "git",
            "-C",
            str(repository),
            "checkout",
            "--detach",
        ],
        check=True,
        capture_output=True,
        text=True,
    )

    assert get_current_branch(str(repository)) == "(detached HEAD)"


def test_analyze_defaults_to_current_directory():
    parser = create_parser()

    arguments = parser.parse_args(["analyze"])

    assert arguments.repository == "."



def test_cli_limits_recent_commit_history(tmp_path):
    repository = create_test_repository(tmp_path)

    for number in range(1, 7):
        make_commit(
            repository,
            "file.txt",
            f"content {number}",
            f"commit {number}",
        )

    result = subprocess.run(
        [
            "python",
            "-m",
            "src.repopulse",
            "analyze",
            str(repository),
            "--limit",
            "2",
        ],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert "commit 6" in result.stdout
    assert "commit 5" in result.stdout
    assert "commit 4" not in result.stdout


def test_get_repository_root(tmp_path):
    repository = create_test_repository(tmp_path)

    make_commit(repository, "file.txt", "hello", "initial commit")

    assert git_module.get_repository_root(
        str(repository)
    ) == str(repository)


def test_working_tree_clean_status(tmp_path):
    repository = create_test_repository(tmp_path)

    make_commit(repository, "file.txt", "original content", "initial commit")

    assert git_module.is_working_tree_clean(
        str(repository)
    ) is True

    (repository / "file.txt").write_text("changed content")

    assert git_module.is_working_tree_clean(
        str(repository)
    ) is False

def test_cli_json_output_reports_readme_presence(tmp_path):
    repository = create_test_repository(tmp_path)

    make_commit(repository, "file.txt", "hello", "initial commit")
    make_commit(repository, "README.md", "# Test Repository\n", "add readme")

    result = subprocess.run(
        [
            "python",
            "-m",
            "src.repopulse",
            "analyze",
            str(repository),
            "--json",
        ],
        capture_output=True,
        text=True,
    )

    data = json.loads(result.stdout)

    assert data["readme_present"] is True
