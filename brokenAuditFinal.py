import os
from datetime import datetime  
import json

TEAMname = "AuthTeam"
EXTERNAL_FILE = "/home/manhyeung/qapractice/PythonQA/python2801/user_loggings.txt"
input_file = open(EXTERNAL_FILE, "r", encoding="utf-8")
output_file = open("output.txt", "w", encoding="utf-8")

users = ["user-100", "user-200", "user-300"]
attempts = [
    ("user-100", True),
    ("user-200", False),
    ("user-100", False),
    ("user-999", True),
]


def doStuff():
    print("hello welcome to the audit thing")

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
        with open("output_test.txt",'a') as output_file:
            print(f"[Logs] TimeStamp {timestamp_value}: {user_id} {user_name} {login_attempt}", file=output_file)
    
    #read_lines(input_file)
    input_file.close()
    output_file.close()
    print("done. output file maybe created:", output_file)

doStuff()
read_lines(input_file)