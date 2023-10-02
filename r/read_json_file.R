#' Read JSON file, transform and print to stdout

library(jsonlite)

# Get the JSON file path from the command line arguments
args <- commandArgs(trailingOnly = TRUE)

# Read and parse the JSON file as a list of named lists
people <- fromJSON(args[1])

# Iterate through the list of people and print the transformed message
for (i in 1:nrow(people)){
    cat(paste0("Hello, ", people$age[i], " year old ", people$first_name[i], "\n"))
}
