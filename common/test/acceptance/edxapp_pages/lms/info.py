"""
Info pages for the main LMS site.
"""

from bok_choy.page_object import PageObject
from . import BASE_URL


class InfoPage(PageObject):
    """
    Info pages for the main site.
    These are basically static pages, so we use one page
    object to represent them all.
    """

    # Dictionary mapping section names to URL paths
    SECTION_PATH = {
        'about': '/about',
        'faq': '/faq',
        'press': '/press',
        'contact': '/contact',
        'terms': '/tos',
        'privacy': '/privacy',
        'honor': '/honor',
    }

    # Dictionary mapping URLs to expected css selector
    EXPECTED_CSS = {
        '/about': 'section.vision',
        '/faq': 'section.faq',
        '/press': 'section.press',
        '/contact': 'section.contact',
        '/tos': 'section.tos',
        '/privacy': 'section.privacy-policy',
        '/honor': 'section.honor-code',
    }

    @property
    def name(self):
        return "lms.info"

    def url(self, section=None):  #pylint: disable=W0221
        """
        URL to the info page called `section`, which must
        be one of the keys in `SECTION_PATH`.
        """
        return BASE_URL + self.SECTION_PATH[section]

    def is_browser_on_page(self):

        # Find the appropriate css based on the URL
        for url_path, css_sel in self.EXPECTED_CSS.iteritems():
            if self.browser.url.endswith(url_path):
                return self.is_css_present(css_sel)

        # Could not find the CSS based on the URL
        return False

    @classmethod
    def sections(cls):
        """
        Return list of available section names.
        """
        return cls.SECTION_PATH.keys()
