"""Script to read an argument and print as lowercase in stdout.
Note that command line arguments are not passed from stdin"""

if ARGV.length != 1
    puts "Make sure to enter an argument!"
    exit(1)
end

argument = ARGV[0].downcase
puts argument