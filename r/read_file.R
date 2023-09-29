#' Read a file (file path given as a command line argument),
#' and write to stdout


# Get the file path from the command line argument
file_path <- commandArgs(trailingOnly = TRUE)[1]

# Open the file for reading
con <- file(file_path, "r")

# Read and print lines from the file
i <- 1
while (length(line <- readLines(con, n = 1)) > 0) {
  cat(i, toupper(line), sep = " ", fill = TRUE)
  i <- i + 1
}

# Close the file connection
close(con)
