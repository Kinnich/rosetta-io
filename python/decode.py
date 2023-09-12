"""Script to decode Base64 text"""
import base64
import sys

encoded_string = sys.argv[1]

decoded_bytes = base64.b64decode(encoded_string)

print(decoded_bytes.decode("utf-8"))