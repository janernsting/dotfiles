#!/usr/bin/env python

import subprocess
import re

def get_secret(display_name):
  return subprocess.check_output(['python', 'getsecret.py', display_name])

top_level_folders = ['Drafts', 'Sent', 'Trash', 'Junk', ]
translation = { 'Junk': 'spam', }
inverse_translation = {v:k for k, v in translation.items()}

def convert_to_local(folder):
  folder = re.sub('INBOX\/', '', folder)
  folder = re.sub(' ', '_', folder)
  folder = translation.get(folder, folder)
  folder = first_to_lower(folder) if folder in top_level_folders else folder
  return folder

def first_to_lower(s):
  return s[0].lower() + s[1:] if s else None

def convert_to_remote(folder):
  folder = first_to_upper(folder) if first_to_upper(folder) in top_level_folders else folder
  folder = inverse_translation.get(folder, folder)
  folder = re.sub('_', ' ', folder)
  folder = "INBOX/" + folder if folder not in top_level_folders \
      and not folder.startswith('INBOX') else folder
  return folder

def first_to_upper(s):
  return s[0].upper() + s[1:] if s else None

def filter_folder(folder):
  return not folder.startswith('Synchronisierungsprobleme') \
      and folder not in ['Unsent Messages']
