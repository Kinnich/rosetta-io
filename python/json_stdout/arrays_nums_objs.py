import json
import sys


my_strings = sys.argv[1:]

# 1. output an array
print(json.dumps(my_strings))

# 2. output numbers
# create and array of numbers based on the length of the string args
string_lengths = [len(string) for string in my_strings]
print(json.dumps(string_lengths))

# 3. output objects
# make a dict of the string and length of string as key value pairs
string_length_dict = {s:l for s,l in zip(my_strings, string_lengths)}
print(json.dumps(string_length_dict))

# 4. output arrays as values in an object
# make dict with the string as key and list of letters as value
string_letters_dict = {string: [s for s in string] for string in my_strings}
print(json.dumps(string_letters_dict))
