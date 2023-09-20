# Script to write text to a new file
# Run script as `ruby write_file.rb <output_file>.txt 'some text'`

outfile, text = ARGV

File.write(outfile, text.upcase)