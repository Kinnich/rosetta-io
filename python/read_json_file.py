"""Read JSON file, transform and print to stdout"""
import json
import sys

json_file = sys.argv[1]

with open(json_file, "r") as f:
    people = json.load(f)

for person in people:
    print(f"Hello, {person['age']} year old {person['first_name']}")
