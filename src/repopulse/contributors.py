from collections import Counter

from .commits import get_commit_history


def get_contributor_activity(repository_path: str) -> dict[str, int]:
    """
    Return the number of commits made by each contributor.

    Args:
        repository_path: Path to the Git repository.

    Returns:
        A dictionary mapping contributor names to commit counts.
    """
    commits = get_commit_history(
        repository_path,
        limit=1000,
    )

    contributors = Counter()

    for commit in commits:
        contributors[commit.author] += 1

    return dict(
        sorted(
            contributors.items(),
            key=lambda item: item[1],
            reverse=True,
        )
    )
