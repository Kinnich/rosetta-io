"""Script outputs arrays of objects"""
import json
import sys


args = sys.argv[1:]

# Make a list of dictionaries from the given args, one dict per arg
my_array = [{arg.upper(): len(arg)} for arg in args]

# Cast to JSON and print to stdout
print(json.dumps(my_array))
