# Write the null character to stdout

# R character strings don't support the null char so convert to binary
text_raw <- charToRaw("Hello World ")
null_char_raw <- as.raw(0)
new_line_raw <- charToRaw("\n")
raw_vector <- c(text_raw, null_char_raw, new_line_raw)

# Write to a temporary binary file
writeBin(raw_vector, "temp_binary_file.bin")

# Read to stdout, intern=FALSE so output is not captured as a character vector
system("cat temp_binary_file.bin", intern = FALSE)

# Delete the temp file
unlink("temp_binary_file.bin")
