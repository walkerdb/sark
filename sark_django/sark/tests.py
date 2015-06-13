from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.test import TestCase

from .views import home


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()  #1
        response = home(request)  #2
        self.assertTrue(response.content.startswith(b'<html>'))  #3
        self.assertIn(b'<title>Leo Sarkisian MTiA Archive</title>', response.content)  #4
        self.assertTrue(response.content.endswith(b'</html>'))  #5