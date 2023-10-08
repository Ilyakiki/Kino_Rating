from django.test import TestCase
from kino.models import Movie,Actor,Director
# Create your tests here.

class ActorModelTestCase(TestCase):
    @staticmethod
    def print_info(message):
        count = Actor.objects.count()
        print(f'{message}: #all_movies={count}')

    # Подготовка БД
    def setUp(self):
        print('-' * 20)
        self.print_info("Start setUp")
        self.actor = Actor.objects.create(first_name='Шая',second_name='ЛаБаф', date_of_birth='1977-11-01', height=1.76,image=None)
        Actor.objects.create(first_name='Лео',second_name='Ди Каприо', date_of_birth='1965-11-01', height=1.65,image=None)
        Actor.objects.create(first_name='Марго',second_name='Робби', date_of_birth='1988-11-01', height=1.90,image=None)
        self.print_info("Finish setUp")

    # Проверка создания объекта Actor
    def test_actor_create(self):
        self.print_info('Start test_actor_create')
        self.assertEqual(self.actor.first_name, 'Шая')
        self.assertEqual(self.actor.second_name, 'ЛаБаф')
        self.assertEqual(self.actor.date_of_birth, '1977-11-01')
        self.assertEqual(self.actor.height, 1.76)
        self.print_info('Finish test_actor_create')

    # Проверка создания объекта Actor
    def test_actor_delete(self):
        self.print_info('Start test_actor_delete')
        open = Actor.objects.get(first_name='Шая')
        open.delete()
        actor = Actor.objects.all()
        self.assertEqual(len(actor), 2)
        self.print_info('Finish test_actor_delete')

    # Проверка получения всех записей Actor
    def test_actor_get_all_records(self):
        self.print_info('Start test_actor_get_all_records')
        actor = Actor.objects.all()
        self.assertEqual(len(actor), 3)
        self.print_info('Finish test_actor_get_all_records')

    # Проверка получения одной записи Actor
    def test_actor_get_one_record(self):
        self.print_info('Start test_actor_get_one_record')
        open = Actor.objects.get(first_name='Шая')
        self.assertEqual(open.second_name, 'ЛаБаф')
        self.assertEqual(open.height, 1.76)
        self.assertEqual(str(open.date_of_birth), '1977-11-01')
        self.print_info('Finish test_actor_get_one_record')

    # Проверка метода __str__ в Actor
    def test_actor_str(self):
        self.print_info('Start test_actor_str')
        expected = 'Шая ЛаБаф'
        self.assertEqual(str(self.actor), expected)
        self.print_info('Finish test_actor_str')


class DirectorModelTestCase(TestCase):
    @staticmethod
    def print_info(message):
        count = Director.objects.count()
        print(f'{message}: #all_movies={count}')

    # Подготовка БД
    def setUp(self):
        print('-' * 20)
        self.print_info("Start setUp")
        self.director = Director.objects.create(first_name='Фрэнк',second_name='Дарабонт', date_of_birth='1959-01-28', height=1.83,image=None,genres='Комедия')
        Director.objects.create(first_name='Майкл',second_name='Бэй', date_of_birth='1965-02-17', height=1.85,image=None,genres='Хоррор')
        self.print_info("Finish setUp")

    # Проверка создания объекта Director
    def test_director_create(self):
        self.print_info('Start test_director_create')
        self.assertEqual(self.director.first_name, 'Фрэнк')
        self.assertEqual(self.director.second_name, 'Дарабонт')
        self.assertEqual(self.director.date_of_birth, '1959-01-28')
        self.assertEqual(self.director.height,1.83)
        self.assertEqual(self.director.genres, 'Комедия')
        self.print_info('Finish test_director_create')

    # Проверка удаления объекта Director
    def test_director_delete(self):
        self.print_info('Start test_director_delete')
        open = Director.objects.get(first_name='Фрэнк')
        open.delete()
        director = Director.objects.all()
        self.assertEqual(len(director), 1)
        self.print_info('Finish test_director_get_all_records')


    # Проверка получения всех записей Director
    def test_director_get_all_records(self):
        self.print_info('Start test_director_get_all_records')
        director = Director.objects.all()
        self.assertEqual(len(director), 2)
        self.print_info('Finish test_director_get_all_records')

    # Проверка получения одной записи Director
    def test_director_get_one_record(self):
        self.print_info('Start test_director_get_one_record')
        open = Director.objects.get(first_name='Фрэнк')
        self.assertEqual(open.second_name, 'Дарабонт')
        self.assertEqual(open.height, 1.83)
        self.assertEqual(str(open.date_of_birth), '1959-01-28')
        self.assertEqual(open.genres, 'Комедия')
        self.print_info('Finish test_director_get_one_record')

    # Проверка метода __str__ в Director
    def test_director_str(self):
        self.print_info('Start test_director_str')
        expected = 'Фрэнк Дарабонт'
        self.assertEqual(str(self.director), expected)
        self.print_info('Finish test_director_str')

