.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

==============================================================================
land.copernicus.downloads
==============================================================================

Expose a FTP path. Track downloads using eea.googletracker.

eea.googletracker should not be installed in the portal, unless you need to
enable its `at_download` tracking functionality.

Example config (FS mounted at /Plone/files):

* go to https://website/Plone/files/manage_access and grant "FTP Access" to "Member"
* instruct user to access ftp://website/Plone/files


Features
--------

- Can be bullet points


Examples
--------

This add-on can be seen in action at the following sites:
- Is there a page on the internet where everybody can see the features?


Documentation
-------------

Full documentation for end users can be found in the "docs" folder, and is also available online at http://docs.plone.org/foo/bar


Translations
------------

This product has been translated into

- Klingon (thanks, K'Plai)


Installation
------------

Install land.copernicus.downloads by adding it to your buildout::

    [buildout]

    ...

    eggs =
        land.copernicus.downloads


and then running ``bin/buildout``


Contribute
----------

- Issue Tracker: https://github.com/collective/land.copernicus.downloads/issues
- Source Code: https://github.com/collective/land.copernicus.downloads
- Documentation: https://docs.plone.org/foo/bar


Support
-------

If you are having issues, please let us know.
We have a mailing list located at: project@example.com


License
-------

The project is licensed under the GPLv2.
