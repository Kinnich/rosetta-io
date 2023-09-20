# Read a file from file path (given as a command line arg),
# print line by line with line numbers

file_path = ARGV[0]

begin
  File.open(file_path, 'r') do |f|
    f.each_line.with_index do |line, i|
      puts "#{i+1} #{line.upcase}"
    end
  end
rescue Errno::ENOENT
  puts "File not found: #{file_path}"
  exit(1)
end

