""" Various setup
"""
from land.copernicus.downloads.config import ENVNAME, PROJECTNAME
from eea.downloads.content.DirectoryView import createDirectoryView


def setupVarious(context):
    """ Do some various setup.
    """
    if context.readDataFile('land.copernicus.downloads.txt') is None:
        return

    site = context.getSite()
    name = ENVNAME()
    if name not in site.objectIds():
        createDirectoryView(site, PROJECTNAME, name)
