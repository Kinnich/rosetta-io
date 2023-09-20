# Read JSON file, transform and print to stdout
require 'json'

json_file = ARGV[0]

people = JSON.parse(File.read(json_file))

people.each do |person|
  puts "Hello, #{person['age']} year old #{person['first_name']}"
end