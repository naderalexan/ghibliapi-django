from http.client import HTTPException

from django.test import testcases

from ..utils import call_url, extract_uuid_v4
from ..services import film_service


class UtilsTests(testcases.TestCase):
    def test_call_url(self):
        data = call_url(f"{film_service.BASE_URL}{film_service.FILMS_PATH}")
        assert isinstance(data, list) or isinstance(data, dict)

    def test_call_url_invalid(self):
        self.assertRaises(HTTPException, call_url, f"{film_service.BASE_URL}/wrongpath")

    def test_extract_uuid_v4(self):
        uuid_actual = "ba924631-068e-4436-b6de-f3283fa848f0"
        text = f"https://ghibliapi.herokuapp.com/people/{uuid_actual}/helloworld"
        uuid_result = extract_uuid_v4(text)
        assert uuid_actual == uuid_result

    def test_extract_uuid_v4_invalid(self):
        text = "aint got not valid uuid"
        self.assertRaises(ValueError, extract_uuid_v4, text)

        uuid = "ba924631-068e-4436-b6de-f3283fa848f0"
        text = f"got too many/{uuid}/{uuid}"
        self.assertRaises(ValueError, extract_uuid_v4, text)
