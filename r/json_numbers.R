#' Script takes args and outputs a list of lengths

library(jsonlite)

# Get the command-line arguments (strings)
args <- commandArgs(trailingOnly = TRUE)

# Calculate the lengths of the strings and store them in an array
string_lengths <- sapply(args, nchar)

# Convert the array of string lengths to a JSON array and print to stdout
cat(toJSON(string_lengths))
