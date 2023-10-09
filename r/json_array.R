#' Script takes command line arguments and turns into JSON array
library(jsonlite)

# Get the command-line arguments (strings)
args <- commandArgs(trailingOnly = TRUE)

# Convert the strings to a JSON array and print to stdout
cat(toJSON(args))
