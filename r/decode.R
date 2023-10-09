#' Script to decode Base64 text

library(base64enc)

# Get the command-line arguments (strings)
args <- commandArgs(trailingOnly = TRUE)

# Decode from base64 to raw bytes then convert raw bytes to string
decoded_string <- rawToChar(base64decode(args))

cat(decoded_string, fill = TRUE)
