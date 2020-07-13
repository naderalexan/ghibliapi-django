from .celery import app
from .services import film_service


@app.task(bind=True)
def retrieve_films(self):
    film_service.run()
