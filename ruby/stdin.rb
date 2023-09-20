# Test script to get input, transform, and write to stdout

i = 1

while user_input = gets
  begin
    user_input.chomp
    puts "#{i} #{user_input.upcase}"
    i += 1
  rescue NoMethodError
    break
  end
end