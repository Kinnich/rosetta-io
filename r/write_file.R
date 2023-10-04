# 'Script to write text to a new file.

# Get the command-line arguments
args <- commandArgs(trailingOnly = TRUE)
outfile <- args[1]
text <- args[2]

# Open the output file and write text in uppercase
writeLines(toupper(text), outfile, sep="")
