from django.test import TestCase
from django.urls import reverse, resolvers


# Create your tests here.

class HomeTest(TestCase):
	def test_view_status_code(self):
		url = reverse('home')
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)

	def test_home_url_resolves_home_view(self):
		view = resolvers('/')
		self.assertEqual(view.func, home)

