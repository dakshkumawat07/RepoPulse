import argparse

from .analyzer import (
    get_commit_count,
    get_current_branch,
    get_first_commit,
    get_latest_commit,
    is_git_repository,
)


def create_parser() -> argparse.ArgumentParser:
    """Create the RepoPulse command-line argument parser."""
    parser = argparse.ArgumentParser(
        prog="repopulse",
        description="Analyze Git repositories and generate engineering insights.",
    )

    subparsers = parser.add_subparsers(dest="command")

    analyze_parser = subparsers.add_parser(
        "analyze",
        help="Analyze a Git repository.",
    )

    analyze_parser.add_argument(
        "repository",
        help="Path to the Git repository.",
    )

    return parser


def main() -> None:
    """Run the RepoPulse command-line interface."""
    parser = create_parser()
    args = parser.parse_args()

    if args.command != "analyze":
        parser.print_help()
        return

    if not is_git_repository(args.repository):
        print(
            f"Error: '{args.repository}' is not a Git repository."
        )
        return

    try:
        branch = get_current_branch(args.repository)
        commit_count = get_commit_count(args.repository)
        first_commit = get_first_commit(args.repository)
        latest_commit = get_latest_commit(args.repository)

        print()
        print("RepoPulse")
        print("────────────────────────────────────")
        print(f"Repository:    {args.repository}")
        print(f"Branch:        {branch}")
        print(f"Total Commits: {commit_count}")

        print()
        print("First Commit")
        print("────────────────────────────────────")
        print(f"Hash:    {first_commit.hash}")
        print(f"Author:  {first_commit.author}")
        print(f"Date:    {first_commit.date}")
        print(f"Message: {first_commit.message}")

        print()
        print("Latest Commit")
        print("────────────────────────────────────")
        print(f"Hash:    {latest_commit.hash}")
        print(f"Author:  {latest_commit.author}")
        print(f"Date:    {latest_commit.date}")
        print(f"Message: {latest_commit.message}")
        print()

    except RuntimeError as error:
        print(f"Error: {error}")
