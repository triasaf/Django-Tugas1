from django.test import TestCase, Client

class TestUrl(TestCase):
    def test_html(self):
        response = Client().get('http://localhost:8000/mywatchlist/html/')
        self.assertEqual(response.status_code, 200)

    def test_xml(self):
        response = Client().get('http://localhost:8000/mywatchlist/xml/')
        self.assertEqual(response.status_code, 200)

    def test_json(self):
        response = Client().get('http://localhost:8000/mywatchlist/json/')
        self.assertEqual(response.status_code, 200)