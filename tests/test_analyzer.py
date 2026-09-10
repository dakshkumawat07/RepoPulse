from src.repopulse.analyzer import (
    get_commit_count,
    get_latest_commit,
    is_git_repository,
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
