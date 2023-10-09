#' Script takes control characters and emoji and outputs valid JSON

library(jsonlite)

# Get the command-line arguments (strings)
args <- commandArgs(trailingOnly = TRUE)

cat(toJSON(args, auto_unbox = TRUE))
