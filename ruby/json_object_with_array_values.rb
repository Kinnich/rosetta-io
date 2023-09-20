# Script takes arguments and transforms them into dict with arrays as dict values
# and returns as JSON
require 'json'

my_strings = ARGV

# Make dict with the string as key and list of letters as value
string_letters_dict = Hash[my_strings.map { |string| [string, string.chars.map(&:upcase)]}]

# Cast to JSON and print to stdout
puts JSON.generate(string_letters_dict)
