import json

file_path = "person-records.json"

with open(file_path, "r") as file:
    data = json.load(file)

for person in data:
    print(f"Hello, {person['age']} year old {person['first_name']}")
