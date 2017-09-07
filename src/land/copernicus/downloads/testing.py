# -*- coding: utf-8 -*-
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import land.copernicus.downloads


class LandCopernicusDownloadsLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=land.copernicus.downloads)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'land.copernicus.downloads:default')


LAND_COPERNICUS_DOWNLOADS_FIXTURE = LandCopernicusDownloadsLayer()


LAND_COPERNICUS_DOWNLOADS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(LAND_COPERNICUS_DOWNLOADS_FIXTURE,),
    name='LandCopernicusDownloadsLayer:IntegrationTesting'
)


LAND_COPERNICUS_DOWNLOADS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(LAND_COPERNICUS_DOWNLOADS_FIXTURE,),
    name='LandCopernicusDownloadsLayer:FunctionalTesting'
)


LAND_COPERNICUS_DOWNLOADS_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        LAND_COPERNICUS_DOWNLOADS_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='LandCopernicusDownloadsLayer:AcceptanceTesting'
)
