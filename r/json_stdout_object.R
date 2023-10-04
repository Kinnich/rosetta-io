# """Script reads string args and transforms into python dict"""

library(jsonlite)

# Get the command-line arguments (strings)
args <- commandArgs(trailingOnly = TRUE)

# Create a dictionary (list) with each string as a key and its length as the value
string_length_dict <- list()
for (string in args) {
  string_length_dict[string] = nchar(string)
}

# Convert the dictionary to JSON and print to stdout
cat(toJSON(string_length_dict))
