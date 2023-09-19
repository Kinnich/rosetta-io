"""Test script to get input, transform, and write to stdout"""

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