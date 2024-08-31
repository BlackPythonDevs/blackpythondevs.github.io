import os
import re
from datetime import datetime, time
from pathlib import Path
from urllib.parse import urlparse

import yaml
from github import Auth, Github
from github.Issue import Issue
from github.PaginatedList import PaginatedList

ROOT = Path(__file__).parent.parent
conferences_path = ROOT / "_data/conferences.yml"


def create_github_client():
    gh_token = os.getenv("GITHUB_TOKEN", "")
    auth = Auth.Token(gh_token)
    client = Github(auth=auth)
    return client



def get_open_issues(gh: Github) -> PaginatedList[Issue]:
    repo = gh.get_repo("BlackPythonDevs/blackpythondevs.github.io")
    issues = repo.get_issues(state="open", labels=["conference"])
    return issues


def parse_conference_details(issue_body: str) -> dict | None:
    # Extract fields from issue body
    name_match = re.search(
        r"Conference Name(?:\r\n|\n){2}(.*?)(?:\r\n|\n){2}", issue_body
    )
    url_match = re.search(r"URL(?:\r\n|\n){2}(.*?)(?:\r\n|\n){2}", issue_body)
    dates_match = re.search(
        r"Conference Dates(?:\r\n|\n){2}(.*?)(?:\r\n|\n){2}", issue_body
    )
    type_match = re.search(
        r"Conference Type(?:\r\n|\n){2}(.*?)(?:\r\n|\n){2}", issue_body
    )
    location_match = re.search(
        r"Conference Location(?:\r\n|\n){2}(.*?)(?:\r\n|\n){2}", issue_body
    )
    summary_match = re.search(
        r"Summary(?:\r\n|\n){2}(.*?)(?:\r\n|\n){2}",
        issue_body,
        re.DOTALL,
    )
    speaking_match = re.search(
        r"Speaking(?:\r\n|\n){2}(.*?)(?:\r\n|\n){2}### Code of Conduct(?:\r\n|\n){2}",
        issue_body,
        re.DOTALL,
    )

    # Set a default value of None for when the url field isn't as expected
    valid_url = normalize_url() if not url_match else normalize_url(url_match[1])

    if dates_match:
        conferenceDates = dates_match[1]
        # Parse the end date of the conference
        endDateStr = conferenceDates.split("-")[1].strip()
        endDate = datetime.strptime(endDateStr, "%d %b %Y")
        # Check if the conference end date is greater than today
        today = datetime.combine(datetime.now(), time())

        if endDate >= today:
            conference = {
                "name": name_match[1],
                "url": valid_url,
                "dates": dates_match[1],
                "type": type_match[1],
                "location": location_match[1],
                "summary": summary_match[1],
                "speaking": speaking_match[1] if speaking_match else "",
            }
            return conference
    return None


def normalize_url(url_match: str = None):
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
    with conferences_path.open("w") as f:
        yaml.dump(confs, f)


if __name__ == "__main__":
    conferences = []

    # Create Github client object
    gh_client = create_github_client()

    # Get open issues from repo
    open_issues: PaginatedList[Issue] = get_open_issues(gh_client)

    # Parse each conference issue so long as it has the "conference" label
    for issue in open_issues:
        if "conference" in [label.name for label in issue.labels]:
            parsed_conf = parse_conference_details(issue_body=issue.body)
            if parsed_conf:
                conferences.append(parsed_conf)

    write_conferences_to_file(conferences)
