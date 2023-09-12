"""Script to encode a string as Base64"""
import base64
import sys

test_string = sys.argv[1]

# encode string argument as bytes
string_bytes = test_string.encode("utf-8")

print(base64.b64encode(string_bytes))
