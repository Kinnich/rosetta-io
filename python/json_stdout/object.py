"""Script reads string args and transforms into python dict"""
import json
import sys


my_strings = sys.argv[1:]

string_lengths = [len(string) for string in my_strings]

# Make a dict with each string as a key and it's length as the value
string_length_dict = {s:l for s,l in zip(my_strings, string_lengths)}

# Cast to JSON and print to stdout
print(json.dumps(string_length_dict))
