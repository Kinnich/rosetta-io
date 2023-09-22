"""Script takes args and transforms into python dict with arrays as dict values"""
import json
import sys


my_strings = sys.argv[1:]

# Make dict with the string as key and list of letters as value
string_letters_dict = {string: [s.upper() for s in string] for string in my_strings}

# Cast to JSON and print to stdout
print(json.dumps(string_letters_dict))
