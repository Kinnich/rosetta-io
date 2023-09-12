"""Script takes control characters and outputs valid JSON"""
import json
import sys

test_string = sys.argv[1:]
# test_string = 'hello \n \0 world'
# Cast to JSON and print to stdout
# print(test_string)
print(json.dumps(test_string))
