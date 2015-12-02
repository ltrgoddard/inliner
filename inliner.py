#!/usr/bin/python

# inliner - converts reference-style Markdown endnotes to
#           Pandoc Markdown's inline footnotes

# By Louis Goddard <louisgoddard@gmail.com>

# USAGE: python inliner.py [input file] [output file]
#        [number of notes in file]

import sys
import re

with open(str(sys.argv[1]),"r") as input:
  text = input.readlines()

final = "".join(text)

counter = 1

while counter <= int(sys.argv[3]):

  ref = "[^" + str(counter) + "]:"
  cite = "[^" + str(counter) + "] "
  cite2 = "[^" + str(counter) + "]\n"
  matching = [s for s in text if ref in s]
  
  if counter < 10:
    note = "^[" + str(matching)[8:-4] + "] "
  elif counter > 10 and counter < 100:
    note = "^[" + str(matching)[9:-4] + "] "
  else:
    note = "^[" + str(matching)[10:-4] + "] "

  final = final.replace(cite, note)
  final = final.replace(cite2, note + "\n")

  counter = counter + 1

offcut = final.find("[^1]:")

final = final[:offcut]

with open(str(sys.argv[2]),"w") as output:
  output.write(final)
