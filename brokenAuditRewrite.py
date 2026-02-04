import os
from datetime import datetime  
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
# no line breaks in the output
# user 999 problem, flag to say user unknown
# writing over the logs all the time rather than appending
# external input options, keep defaults as backups, cli args for input
# autoincrement event IDs



OUTPUT_FILE = "login_output.txt"

EXTERNAL_FILE = "login_attempts.txt"


class LoginAttempt:
    def __init__(self, user_id, name, success, timestamp):
        self.user_id = user_id
        self.name = name
        self.success = success
        self.timestamp = timestamp

    def is_successful(self):
        return self.success


attempts = []

with open(EXTERNAL_FILE, "r", encoding="utf-8") as f:
    for line in f:
        parts = line.strip().split(";")

        user_id = parts[0].split("=")[1]
        name = parts[1].split("=")[1]
        success = parts[2].split("=")[1].lower() == "true"
        timestamp = parts[3].split("=")[1]
        timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

        attempts.append(LoginAttempt(user_id, name, success, timestamp))

def output_attempts(attempts, output_file):
    successful = []
    failed = []

    for a in attempts:
        if a.is_successful():
            successful.append(a)
        else:
            failed.append(a)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("=== Successful Logins ===\n")

        for a in successful:
            f.write(f"{a.user_id},{a.name},{a.timestamp}\n")

        f.write("\n=== Failed Logins ===\n")

        for a in failed:
            f.write(f"{a.user_id},{a.name},{a.timestamp}\n")

output_attempts(attempts, OUTPUT_FILE)