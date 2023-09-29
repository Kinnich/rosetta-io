#' Script to read stdin, transform, and return it

i <- 1
for (line in readLines("stdin")) {
  cat(i, toupper(line), sep = " ", fill = TRUE) # fill flag adds new line
  i <- i + 1
}
