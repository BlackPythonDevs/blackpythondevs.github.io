import datetime
import pathlib
from urllib.parse import urlparse
from typing import Iterator

import json
import gh_issues


def get_conference_issues() -> Iterator[gh_issues.Issue]:
    query = "repo:blackpythondevs/blackpythondevs.github.io type:issue label:conference"
    issues = gh_issues.issues_by_query(query)
    return issues


def normalize_url(url_match: str = str):
    valid_url = None
    # Ensure the url field is not blank and the url matches the regex
    if url_match is not None and url_match.strip() != "":
        # Parse the url and see if a scheme (`https`) is included in it
        # If not, then prepend `https` to the url from the issue body
        # This guards against the website thinking the passed in url is another page on https://blackpythondevs.com/
        parsed_url = urlparse(url_match)

        if "http" not in parsed_url.scheme.casefold():
            valid_url = f"https://{url_match}"
        else:
            valid_url = url_match

    return valid_url


def write_conferences_to_file(confs: list[dict]):
    # Write the conferences to the _data/conferences.yml file
    conferences_path.write_text(json.dumps(confs))


def __to_conference_date(conference_date: str) -> datetime.date:
    return datetime.date.fromisoformat(conference_date)


if __name__ == "__main__":
    KEYS = [
        "conference_name",
        "url",
        "conference_start_date",
        "conference_end_date",
        "conference_type",
        "conference_location",
        "summary",
        "speaking",
    ]

    conferences = []
    for _issue in get_conference_issues():
        if not hasattr(_issue, "conference_end_date"):
            continue

        if __to_conference_date(_issue.conference_end_date) >= datetime.date.today():
            conferences.append({k: getattr(_issue, k, None) for k in KEYS})

    ROOT = pathlib.Path(__file__).parent.parent
    conferences_path = ROOT.joinpath("_data/conferences.json")
    conferences_path.write_text(
        json.dumps(
            list(
                sorted(
                    conferences,
                    key=lambda x: __to_conference_date(x["conference_start_date"]),
                )
            ),
            indent=2,
        )
    )
