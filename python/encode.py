"""Script to encode a string as Base64"""
import base64
import sys

test_string = sys.argv[1]

# Encode string argument as bytes, encode as base64 then decode as string
encoded_string = base64.b64encode(test_string.encode()).decode()

# Print as a string, not bytes
print(encoded_string)
