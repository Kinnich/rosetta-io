# Script takes control characters and outputs valid JSON
require 'json'

test_string = ARGV[0]

# Cast to JSON and print to stdout
puts JSON.generate(test_string)
