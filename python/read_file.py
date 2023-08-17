"""Read a file from file path (given as a command line arg),
print line by line with line numbers
"""
import sys

if len(sys.argv) != 2:
    print("Make sure to enter the filepath!")
    sys.exit(1)

file_path = sys.argv[1]

with open(file_path, 'r') as f:
    i = 1
    for line in f.readlines():
        print(i, line.upper())
        i += 1
