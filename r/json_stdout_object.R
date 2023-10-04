#' Script reads string arguments and transforms to JSON object

library(jsonlite)

# Get the command-line arguments (strings)
args <- commandArgs(trailingOnly = TRUE)

# Create a named list with each string as a key and its length as an atomic vector
string_length <- list()
for (string in args) {
  string_length[[string]] <- nchar(string)
}

# Convert list to JSON and print to stdout
# `auto_unbox`flag marks atomic vectors as singletons with 1 element so that the
# value won't turn into an array when encoded into JSON
cat(toJSON(string_length, auto_unbox = TRUE))
