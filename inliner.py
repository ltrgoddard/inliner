#!/usr/bin/env python

# inliner - converts reference-style Markdown endnotes to
# Pandoc Markdown's inline footnotes

# by Louis Goddard <louisgoddard@gmail.com>

# Usage: python inliner.py [input.markdown] [output.markdown]

import sys

with open(str(sys.argv[1]),"r") as input:
    text = input.read()

counter = 0

while True:
    try:

        counter = counter + 1

        ref = "[^" + str(counter) + "]:"
        nextRef = "[^" + str(counter + 1) + "]:"
        cite = "[^" + str(counter) + "]"

        refStart = text.index(ref)
        refEnd = text.index(nextRef) - 2
   
        offset = len(str(counter)) + 5

        note = "^[" + text[refStart+offset:refEnd] + "]"
        text = text.replace(cite, note)

    except:

        break
    
note = "^[" + text[refStart+offset:len(text)-1] + "]"
text = text.replace(cite, note)
text = text.replace("\n    ", " ")

cutPoint = text.index("\n^")
text = text[0:cutPoint]

with open(str(sys.argv[2]),"w") as output:
    output.write(text)
