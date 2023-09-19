"""Read a file from file path (given as a command line arg),
print line by line with line numbers
"""
if ARGV.length != 1
    puts "Make sure to enter the filepath!"
    exit(1)
  end

  file_path = ARGV[0]

  begin
    i = 1
    File.open(file_path, 'r') do |f|
      f.each_line do |line|
        puts "#{i} #{line.upcase}"
        i += 1
      end
    end
  rescue Errno::ENOENT
    puts "File not found: #{file_path}"
    exit(1)
  end

