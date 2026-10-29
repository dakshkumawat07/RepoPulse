from pathlib import Path


README_FILENAMES = {
    "readme",
    "readme.md",
    "readme.rst",
    "readme.txt",
}


def has_readme(repository_root: str) -> bool:
    """
    Check whether the repository root contains a README file.

    Args:
        repository_root: Absolute path to the repository root.

    Returns:
        True if a supported README file exists, otherwise False.
    """
    root = Path(repository_root)

    return any(
        path.is_file()
        and path.name.lower() in README_FILENAMES
        for path in root.iterdir()
    )
