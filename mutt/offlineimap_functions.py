#!/usr/bin/env python
import gnomekeyring
import re

def get_secret(display_name, keyring_name = "login"):
  for id in gnomekeyring.list_item_ids_sync(keyring_name):
    item = gnomekeyring.item_get_info_sync(keyring_name, id)
    if display_name == item.get_display_name():
      return item.get_secret()

top_level_folders = ['Drafts', 'Sent', 'Trash']

def convert_to_local(folder):
  folder = re.sub('INBOX\/', '', folder)
  folder = re.sub(' ', '_', folder)
  folder = first_to_lower(folder) if folder in top_level_folders else folder
  return folder

def first_to_lower(s):
  return s[0].lower() + s[1:] if s else None

def convert_to_remote(folder):
  folder = first_to_upper(folder) if first_to_upper(folder) in top_level_folders else folder
  folder = re.sub('_', ' ', folder)
  folder = "INBOX/" + folder if folder not in top_level_folders else folder
  return folder

def first_to_upper(s):
  return s[0].upper() + s[1:] if s else None

def filter_folder(folder):
  return not folder.startswith('Synchronisierungsprobleme') \
      and folder not in ['Junk-E-Mail', 'Postausgang']
