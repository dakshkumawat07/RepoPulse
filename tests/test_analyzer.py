from src.repopulse.analyzer import (
    get_commit_activity,
    get_commit_count,
    get_commit_history,
    get_file_change_frequency,
    get_latest_commit,
    is_git_repository,
    get_change_hotspots,
)

def test_current_directory_is_git_repository():
    assert is_git_repository(".") is True


def test_tmp_is_not_git_repository():
    assert is_git_repository("/tmp") is False


def test_commit_count_is_positive():
    commit_count = get_commit_count(".")

    assert commit_count > 0


def test_latest_commit_has_metadata():
    commit = get_latest_commit(".")

    assert len(commit.hash) == 40
    assert commit.author
    assert commit.date
    assert commit.message

def test_commit_history_returns_recent_commits():
    commits = get_commit_history(".", limit=3)

    assert len(commits) <= 3

    for commit in commits:
        assert len(commit.hash) == 40
        assert commit.author
        assert commit.date
        assert commit.message

def test_commit_activity_contains_valid_dates():
    activity = get_commit_activity(".")

    assert activity

    for date, count in activity.items():
        assert len(date) == 10
        assert count > 0



def test_file_change_frequency_contains_valid_counts():
    file_changes = get_file_change_frequency(".")

    assert file_changes

    for file_path, count in file_changes.items():
        assert file_path
        assert count > 0

def test_change_hotspots_contain_expected_fields():
    hotspots = get_change_hotspots(".")

    assert hotspots

    first_hotspot = hotspots[0]

    assert "file" in first_hotspot
    assert "changes" in first_hotspot
    assert "additions" in first_hotspot
    assert "deletions" in first_hotspot
    assert "churn" in first_hotspot

    assert first_hotspot["changes"] > 0
    assert first_hotspot["additions"] >= 0
    assert first_hotspot["deletions"] >= 0
    assert first_hotspot["churn"] == (
        first_hotspot["additions"] + first_hotspot["deletions"]
    )

