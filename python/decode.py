"""Script to decode Base64 text"""
import base64
import sys

encoded_string = sys.argv[1]

decoded_string = base64.b64decode(encoded_string).decode()

print(decoded_string)