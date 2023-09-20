# Script reads streaming input text and then prints capitalized string to stdout

STDOUT.sync = true

while input = gets
  puts input.upcase
end