""" Custom Filesystem Directory View
"""
from eea.downloads.content.DirectoryView import DirectoryView, registerDirectory
from eea.downloads.content.DirectoryView import PatchedFSFile as FSFile

from eea.googletracker.browser import track_download


class UAOpener(track_download.UAOpener):
    def set_user_agent(self, context):
        try:
            user_agent = context.REQUEST.environ['HTTP_USER_AGENT']
            self.addheaders = [('User-Agent', user_agent)]
        except Exception:
            # FTP Transfers seem to be missing the user agent.
            pass


class TrackDownload(track_download.TrackDownload):

    def __call__(self, *args, **kwargs):
        super(TrackDownload, self).__call__(*args, **kwargs)

    def get_opener(self):
        url_opener = UAOpener()
        url_opener.set_user_agent(self.context)
        return url_opener

    def get_vocabulary_value(self, obj, _):
        """ Always return the filename """
        return obj.id

    def get_account(self):
        return super(TrackDownload, self).get_account() or ''

    def trackPageview(self, obj, opener):
        """ Don't track as page view, only as event """
        return

    def get_event_category(self, _):
        return 'FTP File'

    def get_remote_ip(self):
        try:
            return self.context.REQUEST.environ['REMOTE_ADDR']
        except:
            track_download._log('get_remote_ip')
            return '0.0.0.0'


class PatchedFSFile(FSFile):
    """ Custom FS File """

    def manage_FTPget(self, REQUEST, RESPONSE):
        """ Custom ftp get """
        TrackDownload(self, REQUEST)(self, None)

        return super(PatchedFSFile, self).manage_FTPget(REQUEST, RESPONSE)


DirectoryView.registerFileExtension('zip', PatchedFSFile)


__all__ = [
    registerDirectory.__name__,
]
