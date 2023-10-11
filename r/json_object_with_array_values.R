#' Script transforms command-line arguments into JSON object
library(jsonlite)

# Get the command-line arguments (strings)
args <- commandArgs(trailingOnly = TRUE)

# Create a named list with the string as the key and a list of uppercase letters as the value
string_letters <- list()
for (string in args) {
  letters <- toupper(strsplit(string, split="")[[1]])
  string_letters[[string]] <- letters
}

# Convert the named list to JSON and print to stdout
cat(toJSON(string_letters))
