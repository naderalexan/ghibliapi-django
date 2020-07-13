from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from ..models import Film, Person


class FilmListViewTests(APITestCase):
    url = reverse("film-list")

    def setUp(self):
        film = Film(id="cb5b6452-32b4-4935-bfaa-1757ce423c72", title="Foo bar")
        film.save()

        person = Person(id="18d630f4-6a3f-4dc9-a39f-9b29cbcbe839", name="Alice Bob")
        person.save()
        film.people.add(person)
        film.save()

    def test_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
