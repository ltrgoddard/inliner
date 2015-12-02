#!/usr/bin/python

# inliner - converts reference-style Markdown endnotes to
#           Pandoc Markdown's inline footnotes

# by Louis Goddard <louisgoddard@gmail.com>

# Usage: python inliner.py [input.md] [output.md]

import sys

with open(str(sys.argv[1]),"r") as input:
  text = input.read()

counter = 1

while True:
  try:

    ref = "[^" + str(counter) + "]:"
    nextRef = "[^" + str(counter + 1) + "]:"
    cite = "[^" + str(counter) + "]"

    refStart = text.index(ref)
    refEnd = text.index(nextRef) - 2
  
    if counter < 10:
      offset = 6
    elif counter > 10 and counter < 100:
      offset = 7
    elif counter > 100 and counter < 1000:
      offset = 8
    else:
      offset = 9

    refStart = refStart + offset

    note = "^[" + text[refStart:refEnd] + "] "
    text = text.replace(cite, note)

    counter = counter + 1

  except:
 
    note = "^[" + text[refStart:] + "]"
    text = text.replace(cite, note)

    break

cutPoint = text.index("\n^")
text = text[1:cutPoint]

with open(str(sys.argv[2]),"w") as output:
  output.write(text)
