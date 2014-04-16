#!/usr/bin/env python
import gnomekeyring

def get_secret(display_name, keyring_name = "login"):
  for id in gnomekeyring.list_item_ids_sync(keyring_name):
    item = gnomekeyring.item_get_info_sync(keyring_name, id)
    if display_name == item.get_display_name():
      return item.get_secret()
