from django.test import testcases
from ..celery import app
from ..tasks import retrieve_films


class CeleryTests(testcases.TestCase):
    """Tests asserting sending and execution of tasks, not logic"""

    def test_sending_task(self):
        app.send_task("retrieve_films")

    def test_running_task(self):
        retrieve_films()
