# """Script writes an array of objects to stdout"""
library(jsonlite)

# Get the command-line arguments
args <- commandArgs(trailingOnly = TRUE)

# Create an array of named lists from the given args, one list per arg
myArray <- list()
for (arg in args) {
    string_length <- list()
    string_length[[toupper(arg)]] <- nchar(arg)
    myArray[[length(myArray)+1]] <- string_length
}

# Convert the array to a JSON array and print to stdout
cat(toJSON(myArray, auto_unbox=TRUE))
