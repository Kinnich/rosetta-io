# Script outputs arrays of objects as JSON
require 'json'

my_strings = ARGV

# Make a list of dictionaries from the given arguments, one dict per arg
my_array = my_strings.map { |string| {string.upcase => string.length} }

# Cast to JSON and print to stdout
puts JSON.generate(my_array)