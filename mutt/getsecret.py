#!/usr/bin/env python
 
import gnomekeyring
import sys
 
def get_secret(display_name, keyring_name = "login"):
  for id in gnomekeyring.list_item_ids_sync(keyring_name):
    item = gnomekeyring.item_get_info_sync(keyring_name, id)
    if display_name == item.get_display_name():
      print item.get_secret(),

def display_usage():
  print "Usage:"
  print "%s display_name" % sys.argv[0]

if __name__ == '__main__':
  if len(sys.argv) == 1:
    display_usage()
    sys.exit(1)

  display_name = sys.argv[1]
  get_secret(display_name)
