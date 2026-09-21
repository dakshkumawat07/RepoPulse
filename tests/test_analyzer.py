import subprocess

from src.repopulse.analyzer import (
    get_change_hotspots,
    get_commit_activity,
    get_commit_count,
    get_commit_history,
    get_file_change_frequency,
    get_latest_commit,
    is_git_repository,
)


def create_test_repository(tmp_path):
    repository = tmp_path / "test-repo"
    repository.mkdir()

    subprocess.run(
        ["git", "init", "-q", str(repository)],
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
