# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from land.copernicus.downloads.tests.base import FUNCTIONAL_TESTING

import unittest


class TestSetup(unittest.TestCase):
    """Test that land.copernicus.downloads is properly installed."""

    layer = FUNCTIONAL_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if land.copernicus.downloads is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'land.copernicus.downloads'))

    def test_browserlayer(self):
        """Test that ILandCopernicusDownloadsLayer is registered."""
        from land.copernicus.downloads.interfaces import (
            ILandCopernicusDownloadsLayer)
        from plone.browserlayer import utils
        self.assertIn(ILandCopernicusDownloadsLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = FUNCTIONAL_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['land.copernicus.downloads'])

    def test_product_uninstalled(self):
        """Test if land.copernicus.downloads is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'land.copernicus.downloads'))

    def test_browserlayer_removed(self):
        """Test that ILandCopernicusDownloadsLayer is removed."""
        from land.copernicus.downloads.interfaces import \
            ILandCopernicusDownloadsLayer
        from plone.browserlayer import utils
        self.assertNotIn(ILandCopernicusDownloadsLayer, utils.registered_layers())
