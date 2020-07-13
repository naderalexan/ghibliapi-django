from .utils import call_url, extract_uuid_v4
from .models import Person, Film


class FilmService:
    BASE_URL: str = "https://ghibliapi.herokuapp.com"

    FILMS_PATH: str = "/films"
    PEOPLE_PATH: str = "/people"

    def run(self):
        films_data = self._retrieve_data(self.FILMS_PATH)
        for film_data in films_data:
            self._perform_create_film(film_data)

        people_data = self._retrieve_data(self.PEOPLE_PATH)
        for person_data in people_data:
            self._perform_create_person(person_data)

    def _retrieve_data(self, path):
        url = f"{self.BASE_URL}{path}"
        return call_url(url)

    @staticmethod
    def _perform_create_person(data):
        person, _ = Person.objects.get_or_create(id=data["id"], name=data["name"])
        films_ids = [extract_uuid_v4(film_url) for film_url in data.get("films", [])]
        [person.films.add(film_id) for film_id in films_ids]
        person.save()

    @staticmethod
    def _perform_create_film(data):
        Film.objects.get_or_create(id=data["id"], title=data["title"])


film_service = FilmService()
