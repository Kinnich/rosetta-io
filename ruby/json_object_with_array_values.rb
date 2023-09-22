# Script takes arguments and transforms them into dict with arrays as dict values
# and returns as JSON
require 'json'

my_strings = ARGV

# Make dict with the string as key and list of letters as value
string_letters_dict = my_strings.to_h { |string| [string, string.upcase.chars] }

# Cast to JSON and print to stdout
puts JSON.generate(string_letters_dict)