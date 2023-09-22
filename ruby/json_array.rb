# Script takes args and turns into JSON array
require 'json'

my_strings = ARGV

puts JSON.generate(my_strings)