#' Script to read input from stdin, line by line, transform, and write to stdout

f <- file("stdin")
open(f)
while(length(line <- readLines(f, n = 1L)) > 0) {
  cat(toupper(line), fill = TRUE)
}
