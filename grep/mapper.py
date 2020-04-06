#!/usr/bin/env python
"""mapper.py"""

import sys

start = sys.argv[2]
end = sys.argv[4]
find = sys.argv[6]
anycapitalized = sys.argv[8]

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()
    # increase counters
    for word in words:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        if word.startswith(start):
            print '%s\t%s' % (word, 1)
        elif word.endswith(end):
            print '%s\t%s' % (word, 1)
        elif word.find(find) != -1:
            print '%s\t%s' % (word, 1)
        elif anycapitalized == 'True' and word.islower() is False:
            print '%s\t%s' % (word, 1)
        else:
            print '%s\t%s' % (word, 0)
