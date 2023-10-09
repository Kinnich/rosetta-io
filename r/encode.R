#' Script to encode text as Base64

library(base64enc)

# Get the command-line arguments (strings)
args <- commandArgs(trailingOnly = TRUE)

# Convert string to raw bytes then encode as base64
encoded_string <- base64encode(charToRaw(args))

cat(encoded_string, fill = TRUE)
