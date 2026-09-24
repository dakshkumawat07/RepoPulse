from collections import Counter

from .git import run_git_command


def get_file_change_frequency(repository_path: str) -> dict[str, int]:
    """
    Return how many commits have changed each file.

    Args:
        repository_path: Path to the Git repository.

    Returns:
        A dictionary mapping file paths to the number of commits
        that changed each file.
    """
    output = run_git_command(
        repository_path,
        "log",
        "--format=",
        "--name-only",
    )

    file_changes = Counter()

    for line in output.splitlines():
        file_path = line.strip()

        if file_path:
            file_changes[file_path] += 1

    return dict(
        sorted(
            file_changes.items(),
            key=lambda item: (-item[1], item[0]),
        )
    )


def get_code_churn(repository_path: str) -> dict[str, dict[str, int]]:
    """
    Return additions and deletions for each file.
    """
    output = run_git_command(
        repository_path,
        "log",
        "--numstat",
        "--format=",
    )

    churn = {}

    for line in output.splitlines():
        parts = line.split("\t")

        if len(parts) != 3:
            continue

        additions, deletions, file_path = parts

        # Git uses "-" for binary files.
        if not additions.isdigit() or not deletions.isdigit():
            continue

        if file_path not in churn:
            churn[file_path] = {
                "additions": 0,
                "deletions": 0,
            }

        churn[file_path]["additions"] += int(additions)
        churn[file_path]["deletions"] += int(deletions)

    return dict(
        sorted(
            churn.items(),
            key=lambda item: (
                -(item[1]["additions"] + item[1]["deletions"]),
                item[0],
            ),
        )
    )


def get_change_hotspots(repository_path: str) -> list[dict[str, int | str]]:
    """
    Combine file change frequency and code churn information.
    """
    file_changes = get_file_change_frequency(repository_path)
    code_churn = get_code_churn(repository_path)

    hotspots = []

    for file_path, change_count in file_changes.items():
        if file_path not in code_churn:
            continue

        additions = code_churn[file_path]["additions"]
        deletions = code_churn[file_path]["deletions"]

        hotspots.append(
            {
                "file": file_path,
                "changes": change_count,
                "additions": additions,
                "deletions": deletions,
                "churn": additions + deletions,
            }
        )

    return sorted(
        hotspots,
        key=lambda item: (-item["changes"], -item["churn"], item["file"]),
    )
