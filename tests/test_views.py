from django.test import TestCase

class TestMelanzh(TestCase):
    # Проверка главной страницы
    def test_homepage(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    # Проверка списка актеров
    def test_list_actors(self):
        response = self.client.get('/actors/')
        self.assertEqual(response.status_code, 200)

    # Проверка списка режиссеров
    def test_list_directors(self):
        response = self.client.get('/directors/')
        self.assertEqual(response.status_code, 200)

    # Проверка списка фильмов
    def test_list_movies(self):
        response = self.client.get('/movies/')
        self.assertEqual(response.status_code, 200)