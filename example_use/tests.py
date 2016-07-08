from django.test import TestCase
from django.core.urlresolvers import reverse


class TestForm(TestCase):

    def test_response(self):
        self.response = self.client.get(reverse('form_search'))
        self.assertEqual('200', self.response.status_code)

