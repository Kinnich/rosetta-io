#' Script to read input from stdin, line by line, transform, and write to stdout

while(length(line <- readLines("stdin", n = 1L)) > 0) {
  cat(toupper(line), fill = TRUE)
}
