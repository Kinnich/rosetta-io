"""Read JSON file from stdin line by line"""
require 'json'

json_input = ""

loop do
  begin
    line = gets
    break if line.nil? # Exit the loop when input is nil (EOF)

    json_input += line
  end
end

data = JSON.parse(json_input)

data.each do |person|
  puts "Hello, #{person['age']} year old #{person['first_name']}"
end