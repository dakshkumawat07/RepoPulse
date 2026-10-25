import argparse
import json
from dataclasses import asdict
from . import __version__

from .commits import (
    get_commit_activity,
    get_commit_count,
    get_commit_history,
    get_current_branch,
    get_first_commit,
    get_latest_commit,
)
from .contributors import get_contributor_activity
from .git import (
    get_repository_root,
    has_commits,
    is_git_repository,
)
from .hotspots import (
    get_change_hotspots,
    get_code_churn,
    get_file_change_frequency,
)


def positive_int(value: str) -> int:
    """Return a positive integer for command-line arguments."""
    try:
        number = int(value)
    except ValueError as error:
        raise argparse.ArgumentTypeError(
            "must be a positive integer"
        ) from error

    if number < 1:
        raise argparse.ArgumentTypeError(
            "must be a positive integer"
        )

    return number



def create_parser() -> argparse.ArgumentParser:
    """Create the RepoPulse command-line argument parser."""
    parser = argparse.ArgumentParser(
        prog="repopulse",
        description="Analyze Git repositories and generate engineering insights.",
    )

    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )

    subparsers = parser.add_subparsers(dest="command")

    analyze_parser = subparsers.add_parser(
        "analyze",
        help="Analyze a Git repository.",
    )


    analyze_parser.add_argument(
        "repository",
        nargs="?",
        default=".",
        help="Path to the Git repository (default: current directory).",
    )


    analyze_parser.add_argument(
        "--json",
        action="store_true",
        help="Output analysis results as JSON.",
    )

    analyze_parser.add_argument(
        "--limit",
        type=positive_int,
        default=5,
        help="Number of recent commits to display (default: 5).",
    )

    return parser


def main() -> int:
    """Run the RepoPulse command-line interface."""
    parser = create_parser()
    args = parser.parse_args()

    if args.command != "analyze":
        parser.print_help()
        return 0

    if not is_git_repository(args.repository):
        print(
            f"Error: '{args.repository}' is not a Git repository."
        )
        return 1

    if not has_commits(args.repository):
        print(f"Error: '{args.repository}' has no commits.")
        return 1

    try:
        repository_root = get_repository_root(args.repository)
        branch = get_current_branch(args.repository)
        commit_count = get_commit_count(args.repository)
        first_commit = get_first_commit(args.repository)
        latest_commit = get_latest_commit(args.repository)
        commit_history = get_commit_history(
            args.repository,
            limit=args.limit,
        )
        commit_activity = get_commit_activity(args.repository)
        contributor_activity = get_contributor_activity(args.repository)
        file_changes = get_file_change_frequency(args.repository)
        change_hotspots = get_change_hotspots(args.repository)

        code_churn = get_code_churn(args.repository)

        if args.json:
            result = {
                "version": __version__,
                "repository": args.repository,
                "repository_root": repository_root,
                "branch": branch,
                "total_commits": commit_count,
                "first_commit": asdict(first_commit),
                "latest_commit": asdict(latest_commit),
                "commit_history": [
                    asdict(commit) for commit in commit_history
                ],
                "commit_activity": commit_activity,
                "contributors": contributor_activity,
                "file_hotspots": file_changes,
                "code_churn": code_churn,
                "change_hotspots": change_hotspots,
            }

            print(json.dumps(result, indent=2))
            return 0
      

        print()
        print("RepoPulse")
        print("────────────────────────────────────")
        print(f"Repository:    {args.repository}")
        print(f"Repository Root: {repository_root}")
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
        print("Recent Activity")
        print("────────────────────────────────────")

        for commit in commit_history:
            print(f"{commit.date} | {commit.author} | {commit.message}")

        print()


        print("Commit Activity")
        print("────────────────────────────────────")

        for date, count in commit_activity.items():
            print(f"{date} | {count} commit(s)")

        print() 

        print("File Hotspots")
        print("────────────────────────────────────")

        for file_path, count in list(file_changes.items())[:10]:
            print(f"{file_path} | {count} change(s)")

        print()
        print("Code Churn")
        print("────────────────────────────────────")

        churn = code_churn

        for file_path, changes in list(churn.items())[:10]:
            print(
                f"{file_path} | "
                f"+{changes['additions']} / -{changes['deletions']}"
            )

        print()
        print("Change Hotspots")
        print("────────────────────────────────────")

        for hotspot in change_hotspots[:10]:
            print(
                f"{hotspot['file']} | "
                f"{hotspot['changes']} change(s) | "
                f"+{hotspot['additions']} / -{hotspot['deletions']} | "
                f"{hotspot['churn']} churn"
            )

        print()

        print("Contributor Activity")
        print("────────────────────────────────────")

        for author, count in contributor_activity.items():
            print(f"{author} | {count} commit(s)")

        print()

        return 0

    except RuntimeError as error:
        print(f"Error: {error}")
        return 1
