from rest_framework.test import RequestsClient
from django.test import testcases

from ..models import Film, Person
from ..services import film_service
from ..utils import call_url


class ServicesTests(testcases.TestCase):
    API_CLIENT = RequestsClient

    def test_film_service(self):
        response = call_url(f"{film_service.BASE_URL}{film_service.FILMS_PATH}")
        num_films = len(response)

        response = call_url(f"{film_service.BASE_URL}{film_service.PEOPLE_PATH}")
        num_people = len(response)

        film_service.run()

        assert Film.objects.all().count() == num_films
        assert Person.objects.all().count() == num_people
