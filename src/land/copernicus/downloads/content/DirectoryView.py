""" Custom Filesystem Directory View
"""
from eea.downloads.content.DirectoryView import DirectoryView, registerDirectory
from eea.downloads.content.DirectoryView import PatchedFSFile as FSFile

class PatchedFSFile(FSFile):
    """ Custom FS File
    """
    def manage_FTPget(self, REQUEST, RESPONSE):
        """ Custom ftp """
        print "=== Google analytics here ==="
        return super(PatchedFSFile, self).manage_FTPget(REQUEST, RESPONSE)

DirectoryView.registerFileExtension('zip', PatchedFSFile)

__all__ = [
    registerDirectory.__name__,
]
