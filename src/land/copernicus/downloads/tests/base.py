""" Testing
"""
import os
import shutil
import tempfile
from plone.testing import z2
from plone.app.testing import TEST_USER_ID
from plone.app.testing import setRoles
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import FunctionalTesting


class Fixture(PloneSandboxLayer):
    """ Testing Policy
    """
    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        """ Setup Zope
        """
        self.PATH = tempfile.mkdtemp()
        os.environ["COPERNICUS_DOWNLOADS_PATH"] = self.PATH
        os.environ["COPERNICUS_DOWNLOADS_NAME"] = 'files'

        import land.copernicus.downloads
        self.loadZCML(package=land.copernicus.downloads)
        z2.installProduct(app, 'eea.downloads')
        z2.installProduct(app, 'land.copernicus.downloads')

    def tearDownZope(self, app):
        """ Uninstall Zope
        """
        shutil.rmtree(self.PATH)
        z2.uninstallProduct(app, 'land.copernicus.downloads')

    def setUpPloneSite(self, portal):
        """ Setup Plone
        """
        self.applyProfile(portal, 'land.copernicus.downloads:default')

        # Login as manager
        setRoles(portal, TEST_USER_ID, ['Manager'])

        # Create testing environment
        portal.invokeFactory("Folder", "sandbox", title="Sandbox")

FIXTURE = Fixture()
FUNCTIONAL_TESTING = FunctionalTesting(bases=(FIXTURE,),
                                       name='LandCopernicusDownloads:Functional')
