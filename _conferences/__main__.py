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
    if "conference" in [label.name for label in issue.labels]:
        # Extract conference date from issue body
        match = re.search(r"conference_dates: (.*)", issue.body)
        if match:
            conferenceDates = match.group(1)
            # Parse the end date of the conference
            endDateStr = conferenceDates.split("-")[1].strip()
            endDate = datetime.strptime(endDateStr, "%d %b %Y")
            # Check if the conference end date is greater than today
            if endDate > datetime.now():
                markdownContent += f"""
## {issue.title}, City, Region, Country

{issue.body}

### Speaking
- PERSON - TALK or ROLE NAME
"""

if markdownContent == "":
    markdownContent = "No conferences"

with conferences_path.open("r") as f:
    content = f.read()

newContent = re.sub(
    r"<!-- conferences starts -->.*<!-- conferences ends -->",
    f"<!-- conferences starts -->\n{markdownContent}<!-- conferences ends -->",
    content,
    flags=re.DOTALL,
)

# Write the new content to the file
with conferences_path.open("w") as f:
    f.write(newContent)
