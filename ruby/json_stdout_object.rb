# Script reads string args and transforms into python dict
require 'json'

my_strings = ARGV

# Make a dict with each string as a key and it's length as the value
string_length_dict = Hash[my_strings.map { |string| [string, string.length] }]

# Cast to JSON and print to stdout
puts JSON.generate(string_length_dict)


# ["hello \n \u0001 world 🥸"] ruby
#  "hello \n \u0001 world \ud83e\udd78" python