#' Script reads command line arguments and writes to stdout in lowercase

cat(tolower(commandArgs(trailingOnly = TRUE)), fill = TRUE)
