# Create a raw vector with a null character
my_raw_vector <- as.raw(0)

# # Print the raw vector
# cat("Raw vector:", my_raw_vector, "\n")

# Convert the raw vector to a character string for manipulation/display
# my_string <- rawToChar(my_raw_vector)

# # Print the character string
# cat("Character string:", my_string, "\n")

# control_char_representation <- paste0("\\", format(as.raw(0), width = 2, zero.print = ""))

# control_char_representation <- utf8ToInt("\0")
cat("Hello World", my_raw_vector)
# cat("Hello World \0")