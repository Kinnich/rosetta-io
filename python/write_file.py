"""Script to write text to a new file.
Run script as `python write_file.py <output_file>.py "some text"`
"""
import sys
import os

outfile = sys.argv[1]
text = sys.argv[2]

with open(outfile, 'w') as f:
    f.write(text.upper())
