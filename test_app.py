from app import app
from unittest import TestCase
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):
    def test_index(self):
        with app.test_client() as client:
            res = client.get("/")
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn("<h1>BOGGLE</h1>", html)

    def test_guess(self):
        with app.test_client() as client:
            res = client.get('/guess', data={"guess": "a"})
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 405)

    def test_save(self):
        with app.test_client() as client:
            res = client.get('/save', data={"score": "10", "played": "1"})
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 405)

    def test_guess_post(self):
        with app.test_client() as client:
            res = client.post('/guess', data={"guess": "a"})
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn("Word added! Keep Going", html)

    def test_save_post(self):
        with app.test_client() as client:
            res = client.post('/save', data={"score": "10", "played": "1"})
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn("High Score: 10", html)
            