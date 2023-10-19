import os
import re
from datetime import datetime
from pathlib import Path

from github import Auth, Github

TOKEN = os.getenv("GITHUB_TOKEN", "")
ROOT = Path(__file__).parent.parent
conferences_path = ROOT / "conferences.md"

auth = Auth.Token(TOKEN)
g = Github(auth=auth)

repo = g.get_repo("oleksis/blackpythondevs.com")
open_issues = repo.get_issues(state="open", labels=["conference"])

markdownContent = ""

for issue in open_issues:
    print(issue.title)
    if "conference" in [label.name for label in issue.labels]:
        print(repr(issue.body))
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
            conferenceDates = dates_match.group(1)
            # Parse the end date of the conference
            endDateStr = conferenceDates.split("-")[1].strip()
            endDate = datetime.strptime(endDateStr, "%d %b %Y")
            # Check if the conference end date is greater than today
            if endDate > datetime.now():
                markdownContent += f"""
## {name_match.group(1)} ({dates_match.group(1)}) - {location_match.group(1)}

{summary_match.group(1)}

### Speaking

{speaking_match.group(1)}
"""

if markdownContent == "":
    markdownContent = "No conferences"

with conferences_path.open("r") as f:
    content = f.read()

newContent = re.sub(
    r"<!-- conferences starts -->.*<!-- conferences ends -->",
    f"<!-- conferences starts -->\n{markdownContent}\n<!-- conferences ends -->",
    content,
    flags=re.DOTALL,
)

# Write the new content to the file
with conferences_path.open("w") as f:
    f.write(newContent)
