from collections import Counter
from dataclasses import dataclass
from datetime import datetime

from .git import run_git_command


@dataclass
class CommitInfo:
    """Store useful information about a Git commit."""

    hash: str
    author: str
    date: str
    message: str


def get_current_branch(repository_path: str) -> str:
    """Return the current Git branch name."""
    return run_git_command(
        repository_path,
        "branch",
        "--show-current",
    )


def get_commit_count(repository_path: str) -> int:
    """Return the total number of commits in the repository."""
    output = run_git_command(
        repository_path,
        "rev-list",
        "--count",
        "HEAD",
    )

    return int(output)


def get_commit(repository_path: str, revision: str) -> CommitInfo:
    """
    Return structured information about a Git commit.

    Args:
        repository_path: Path to the Git repository.
        revision: Git revision such as HEAD or a commit hash.

    Returns:
        CommitInfo containing hash, author, date, and message.
    """
    output = run_git_command(
        repository_path,
        "show",
        "-s",
        "--format=%H%x1f%an%x1f%ad%x1f%s",
        "--date=iso",
        revision,
    )

    commit_hash, author, date, message = output.split("\x1f")

    return CommitInfo(
        hash=commit_hash,
        author=author,
        date=date,
        message=message,
    )


def get_first_commit(repository_path: str) -> CommitInfo:
    """Return information about the first commit."""
    first_commit_hash = run_git_command(
        repository_path,
        "rev-list",
        "--max-parents=0",
        "HEAD",
    )

    return get_commit(repository_path, first_commit_hash)


def get_latest_commit(repository_path: str) -> CommitInfo:
    """Return information about the latest commit."""
    return get_commit(repository_path, "HEAD")


def get_commit_history(
    repository_path: str,
    limit: int = 10,
) -> list[CommitInfo]:
    """
    Return the most recent commits from the repository.

    Args:
        repository_path: Path to the Git repository.
        limit: Maximum number of commits to return.

    Returns:
        A list of CommitInfo objects, newest commit first.
    """
    output = run_git_command(
        repository_path,
        "log",
        f"-{limit}",
        "--format=%H%x1f%an%x1f%ad%x1f%s",
        "--date=iso",
    )

    if not output:
        return []

    commits = []

    for line in output.splitlines():
        commit_hash, author, date, message = line.split("\x1f")

        commits.append(
            CommitInfo(
                hash=commit_hash,
                author=author,
                date=date,
                message=message,
            )
        )

    return commits


def get_commit_activity(repository_path: str) -> dict[str, int]:
    """
    Return the number of commits made on each date.

    Args:
        repository_path: Path to the Git repository.

    Returns:
        A dictionary mapping dates to commit counts.
    """
    commits = get_commit_history(
        repository_path,
        limit=1000,
    )

    activity = Counter()

    for commit in commits:
        commit_date = datetime.fromisoformat(commit.date).date()
        activity[commit_date.isoformat()] += 1

    return dict(sorted(activity.items(), reverse=True))
