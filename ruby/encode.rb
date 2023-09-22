# Script to encode a string as Base64
# Note that Line feeds are added to every 60 encoded characters
require 'base64'


test_string = ARGV[0]

# Encode string argument as string
encoded_string = Base64.encode64(test_string)

puts encoded_string