# Script takes string arguments and outputs a JSON array of numbers representing
# the length of each argument
require 'json'

my_strings = ARGV

string_lengths = my_strings.map(&:length)

puts JSON.generate(string_lengths)