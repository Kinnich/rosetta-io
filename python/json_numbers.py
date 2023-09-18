"""Script takes args and outputs a list of lengths"""
import json
import sys


my_strings = sys.argv[1:]

# Create an array of numbers based on the length of the string args
string_lengths = [len(string) for string in my_strings]

# Cast to JSON and print to stdout
print(json.dumps(string_lengths))
