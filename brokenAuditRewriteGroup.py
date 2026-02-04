import os
from datetime import datetime  
import json

#datestamp = time() YYYY_DD
DUMMY_FILE = "logs_(timestamp).txt"
__EXTERNAL_FILE = "C:\\Users\\aahmad\\Coding Live Lessons\\files\\user_logging.txt"
__AUTH_TEAM = "Auth Team"
input_file = open(__EXTERNAL_FILE, "r", encoding="utf-8")
output_file = open("output.txt", "w", encoding="utf-8")


def logging_result(value: bool) -> str:
    if value == 1:
        return "Successful"
    elif value == 0:
        return "Failed"
    else:
        return "Error occurred"

def read_lines(file_obj):
    for raw_line in file_obj:
        line = raw_line.strip()
        if not line:
            continue  # skip blank lines

        parts = line.split(";")
        if len(parts) != 4:
            print(f"Skipping malformed line: {line}")
            continue

        user_id = parts[0]
        user_name = parts[1].strip('"')
        login_attempt = parts[2]
        timestamp_value = parts[3]

        var = logging_result(bool(login_attempt))
        #print(f"{var}")
        print(f"{user_id} {user_name} {login_attempt} {timestamp_value}", file=output_file)
        
read_lines(input_file)
input_file.close()
output_file.close()