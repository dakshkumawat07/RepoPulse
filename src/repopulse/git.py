from pathlib import Path
import subprocess


def is_git_repository(repository_path: str) -> bool:
    """
    Check whether the given path is inside a Git working tree.

    Args:
        repository_path: Path to the directory we want to inspect.

    Returns:
        True if the path is inside a Git working tree,
        otherwise False.
    """
    path = Path(repository_path)

    if not path.exists() or not path.is_dir():
        return False

    result = subprocess.run(
        [
            "git",
            "-C",
            str(path),
            "rev-parse",
            "--is-inside-work-tree",
        ],
        capture_output=True,
        text=True,
        check=False,
    )

    return (
        result.returncode == 0
        and result.stdout.strip() == "true"
    )


def has_commits(repository_path: str) -> bool:
    """
    Check whether the given Git repository contains at least one commit.

    Args:
        repository_path: Path to the Git repository.

    Returns:
        True if the repository has at least one commit,
        otherwise False.
    """
    result = subprocess.run(
        [
            "git",
            "-C",
            repository_path,
            "rev-parse",
            "--verify",
            "HEAD",
        ],
        capture_output=True,
        text=True,
        check=False,
    )

    return result.returncode == 0


def run_git_command(repository_path: str, *arguments: str) -> str:
    """
    Run a Git command inside the given repository.

    Args:
        repository_path: Path to the Git repository.
        *arguments: Git command arguments.

    Returns:
        Command output without surrounding whitespace.

    Raises:
        RuntimeError: If the Git command fails.
    """
    command = ["git", "-C", repository_path, *arguments]

    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
        check=False,
    )

    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip())

    return result.stdout.strip()
