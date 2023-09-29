#' Script to read stdin, transform, and return it

i <- 1
for (line in readLines("stdin")) {
  cat(sprintf("%s %s\n", i, toupper(line)))
  i <- i + 1
}
