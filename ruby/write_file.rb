"""Script to write text to a new file.
Run script as `ruby write_file.rb <output_file>.txt 'some text'`
"""
outfile = ARGV[0]
text = ARGV[1]

begin
    File.open(outfile, 'w') do |f|
        f.write(text.upcase)
    end
end