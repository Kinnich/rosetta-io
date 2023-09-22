"""Read a file (file path given as a command line argument),
and write to stdout
"""
import sys

file_path = sys.argv[1]

with open(file_path, 'r') as f:
    i = 1
    for line in f.readlines():
        print(i, line.upper(), end='')
        i += 1
