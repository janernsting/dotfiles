from hamcrest import *
import unittest
import offlineimap_functions as funcs


class RemoteToLocalTest(unittest.TestCase):
  def convert(self, folder):
    return funcs.convert_to_local(folder)

  def assert_converts_to(self, actual_folder, expected_folder):
    assert_that(self.convert(actual_folder), equal_to(expected_folder))

  def testInboxRemainsUnchanged(self):
    inbox = 'INBOX'
    self.assert_converts_to(inbox, inbox)

  def testSubfolderBecomesFolder(self):
    subfolder = 'INBOX/Archiv'
    folder = 'Archiv'
    self.assert_converts_to(subfolder, folder)

  def testChangeCaseForTopLevelFolders(self):
    self.assert_converts_to('Drafts', 'drafts')
    self.assert_converts_to('Sent', 'sent')
    self.assert_converts_to('Trash', 'trash')

  def testConvertSpacesToUnderscores(self):
    self.assert_converts_to('INBOX/EAI 2013', 'EAI_2013')

  def testTranslateJunkEMailToSpam(self):
    self.assert_converts_to('Junk', 'spam')


class LocalToRemoteTest(unittest.TestCase):
  def convert(self, folder):
    return funcs.convert_to_remote(folder)

  def assert_converts_to(self, actual_folder, expected_folder):
    assert_that(self.convert(actual_folder), equal_to(expected_folder))

  def testInboxRemainsUnchanged(self):
    self.assert_converts_to('INBOX', 'INBOX')

  def testChangeCaseForTopLevelFolders(self):
    self.assert_converts_to('drafts', 'Drafts')
    self.assert_converts_to('sent', 'Sent')
    self.assert_converts_to('trash', 'Trash')

  def testConvertOtherFolderToSubfolder(self):
    self.assert_converts_to('archive', 'INBOX/archive')

  def testConvertUnderscoresToSpaces(self):
    self.assert_converts_to('EAI_2013', 'INBOX/EAI 2013')

  def testPrefixInboxOnlyIfAbsent(self):
    self.assert_converts_to('INBOX/MD2', 'INBOX/MD2')

  def testTranslateSpamToJunkEMail(self):
    self.assert_converts_to('spam', 'Junk')


class FolderfilterTest(unittest.TestCase):
  def testExcludeSyncProblems(self):
    assert_that(not funcs.filter_folder('Synchronisierungsprobleme'))
    assert_that(not funcs.filter_folder('Synchronisierungsprobleme.Konflikte'))

  def testExcludeUnsentMessages(self):
    assert_that(not funcs.filter_folder('Unsent Messages'))

  def testIncludeOthers(self):
    assert_that(funcs.filter_folder('INBOX'))
    assert_that(funcs.filter_folder('Sent'))
