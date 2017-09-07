"""Common configuration constants
"""
import os
import logging
from zope.i18nmessageid import MessageFactory

PROJECTNAME = 'land.copernicus.downloads'
logger = logging.getLogger(PROJECTNAME)


def ENVPATH():
    """ GET DOWNLOADS_PATH from os env
    """
    path = os.environ.get('COPERNICUS_DOWNLOADS_PATH')
    if not path:
        path = os.environ.get('CLIENT_HOME', '/tmp')
        path = os.path.join(path, 'files')
        os.environ['COPERNICUS_DOWNLOADS_PATH'] = path
        logger.warn(
            'Missing environment var COPERNICUS_DOWNLOADS_PATH. Using %s', path)
    return path


def ENVNAME():
    """ Get DOWNLOADS_NAME from os env
    """
    name = os.environ.get('COPERNICUS_DOWNLOADS_NAME')
    if not name:
        name = 'files'
        os.environ['COPERNICUS_DOWNLOADS_NAME'] = name
        logger.warn(
            'Missing environment var COPERNICUS_DOWNLOADS_NAME. Using %s', name)
    return name

_ = MessageFactory('land.copernicus.downloads')
