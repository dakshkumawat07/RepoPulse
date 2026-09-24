from pathlib import Path
import subprocess


def is_git_repository(repository_path: str) -> bool:
    """
    Check whether the given path is a Git repository.

    Args:
        repository_path: Path to the directory we want to inspect.

    Returns:
        True if the directory contains a .git directory,
        otherwise False.
    """
    path = Path(repository_path)

    if not path.exists():
        return False

    if not path.is_dir():
        return False

    return (path / ".git").is_dir()


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
