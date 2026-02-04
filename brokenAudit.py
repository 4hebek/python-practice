import os
from datetime import datetime, timezone  
import json

# imports not used, json, os,
# constants not all in capitals
# namings of the function
# do we have to close the file
# commented out code left out
# no line breaks in the output
# printing OutputFile title and not the actual file - intention unclear
# no annotations
# break the loop down into smaller functions, easier to maintain, e.g. one function for writing to the file
# users not used, different than the attempts, not dynamic
# duplicate print statements, or get rid in general
# team name added to the log
# OK and Not_OK instead of Success and Fail
# better logging
# data validation?
# headers for fields?
# error handling
# ensure main loop runs in a run guard(Doesn't run when imported)

# Major
# timestamp - do per event, not per batch, format should be string and utc
# external input options, keep defaults as backups, cli args for input
# autoincrement event IDs
# no line breaks in the output
# user 999 problem, flag to say user unknown
# writing over the logs all the time rather than appending


OUTPUT_FILE = "audit_output.txt"
TEAM_NAME = "AuthTeam"

def performAudit():
    print("Begin audit")

    users = ["user-100", "user-200", "user-300"]
    attempts = [
        ("user-100", True),
        ("user-200", False),
        ("user-100", False),
        ("user-999", True),
    ]

    timestampt = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    file = open(OUTPUT_FILE, "a", encoding="utf-8")

    for attempt in attempts:
        if attempt[0] not in users:
            outcome = "Unknown_User"
        elif attempt[1] == True:
            outcome = "Successful"
        else:
            outcome = "Failed"

        line = "time=" + timestampt + " user=" + attempt [0] + " team=" + TEAM_NAME + " result=" + outcome

        file.write(f"{line}\n")

    file.close()
    print("Audit finished. Results saved in:", OUTPUT_FILE)

performAudit()