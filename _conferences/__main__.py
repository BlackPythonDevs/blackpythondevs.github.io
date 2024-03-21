import os
import re
from datetime import datetime, time
from pathlib import Path

import yaml
from github import Auth, Github

TOKEN = os.getenv("GITHUB_TOKEN", "")
ROOT = Path(__file__).parent.parent
conferences_path = ROOT / "_data/conferences.yml"

auth = Auth.Token(TOKEN)
g = Github(auth=auth)

repo = g.get_repo("BlackPythonDevs/blackpythondevs.github.io")
open_issues = repo.get_issues(state="open", labels=["conference"])
conferences = []
today = datetime.combine(datetime.now(), time())

for issue in open_issues:
    if "conference" in [label.name for label in issue.labels]:
        # Extract fields from issue body
        name_match = re.search(
            r"Conference Name(?:\r\n|\n){2}(.*?)(?:\r\n|\n){2}", issue.body
        )
        url_match = re.search(r"URL(?:\r\n|\n){2}(.*?)(?:\r\n|\n){2}", issue.body)
        dates_match = re.search(
            r"Conference Dates(?:\r\n|\n){2}(.*?)(?:\r\n|\n){2}", issue.body
        )
        type_match = re.search(
            r"Conference Type(?:\r\n|\n){2}(.*?)(?:\r\n|\n){2}", issue.body
        )
        location_match = re.search(
            r"Conference Location(?:\r\n|\n){2}(.*?)(?:\r\n|\n){2}", issue.body
        )
        summary_match = re.search(
            r"Summary(?:\r\n|\n){2}(.*?)(?:\r\n|\n){2}",
            issue.body,
            re.DOTALL,
        )
        speaking_match = re.search(
            r"Speaking(?:\r\n|\n){2}(.*?)(?:\r\n|\n){2}### Code of Conduct(?:\r\n|\n){2}",
            issue.body,
            re.DOTALL,
        )

        if dates_match:
            conferenceDates = dates_match[1]
            # Parse the end date of the conference
            endDateStr = conferenceDates.split("-")[1].strip()
            endDate = datetime.strptime(endDateStr, "%d %b %Y")
            # Check if the conference end date is greater than today
            if endDate >= today:
                conference = {
                    "name": name_match[1],
                    "url": url_match[1],
                    "dates": dates_match[1],
                    "type": type_match[1],
                    "location": location_match[1],
                    "summary": summary_match[1],
                    "speaking": speaking_match[1] if speaking_match else "",
                }
                conferences.append(conference)

# Write the conferences to the _data/conferences.yml file
with conferences_path.open("w") as f:
    yaml.dump(conferences, f)
