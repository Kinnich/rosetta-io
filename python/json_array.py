"""Script takes args and turns into JSON array"""
import json
import sys


my_strings = sys.argv[1:]

# Cast to JSON and print to stdout
print(json.dumps(my_strings))
