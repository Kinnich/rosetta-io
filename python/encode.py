"""Script to encode a string as Base64"""
import base64
import sys

test_string = sys.argv[1]

# Encode string argument as bytes
test_bytes = test_string.encode("utf-8")

encoded_bytes = base64.b64encode(test_bytes)

# Print as a string, not bytes
print(encoded_bytes.decode("utf-8"))
