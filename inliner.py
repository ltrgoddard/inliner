#!/usr/bin/python

# inliner - converts reference-style Markdown endnotes to
#           Pandoc Markdown's inline footnotes

# by Louis Goddard <louisgoddard@gmail.com>

# Usage: python inliner.py [input.md] [output.md]

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
  
    if counter < 11:
      offset = 6
    elif counter > 11 and counter < 101:
      offset = 7
    elif counter > 101 and counter < 1001:
      offset = 8
    else:
      offset = 9

    note = "^[" + text[refStart+offset:refEnd] + "] "
    text = text.replace(cite, note)

  except:

    break
  
note = "^[" + text[refStart+offset:len(text)-1] + "]"
text = text.replace(cite, note)

cutPoint = text.index("\n^")
text = text[0:cutPoint]

with open(str(sys.argv[2]),"w") as output:
  output.write(text)
