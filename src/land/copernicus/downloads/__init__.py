""" Main product initializer
"""
import os
from land.copernicus.downloads.config import ENVPATH, ENVNAME, PROJECTNAME
from land.copernicus.downloads.content.DirectoryView import registerDirectory

def initialize(context):
    """Initializer called when used as a Zope 2 product.
    """
    name = ENVNAME()
    path = ENVPATH()
    if not os.path.exists(path):
        os.makedirs(path)
    registerDirectory(path, PROJECTNAME)
