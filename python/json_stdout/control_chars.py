"""Script takes control characters and outputs valid JSON"""
import json
import sys

test_string = sys.argv[1]

# Cast to JSON and print to stdout
print(json.dumps(test_string))
