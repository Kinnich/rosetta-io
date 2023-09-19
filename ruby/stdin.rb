# Test script to get input, transform, and return it
# Testing that it reads line by line
# and that it does the transformation (to make sure that we're
# getting the stdin throught python)
i = 1

loop do
  begin
    user_input = gets.chomp
    puts "#{i} #{user_input.upcase}"
    i += 1
  rescue NoMethodError
    break
  end
end