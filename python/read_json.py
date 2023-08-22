"""Read JSON file from stdin line by line"""
import json

json_input = ""

while True:
    try:
        json_input += input()
    except EOFError:
        break

data = json.loads(json_input)

for person in data:
    print(f"Hello, {person['age']} year old {person['first_name']}")
