#!/usr/bin/env python
 
import offlineimap_functions as funcs
import sys
 
def display_usage():
  print "Usage:"
  print "%s display_name" % sys.argv[0]

if __name__ == '__main__':
  if len(sys.argv) == 1:
    display_usage()
    sys.exit(1)

  display_name = sys.argv[1]
  print funcs.get_secret(display_name)
