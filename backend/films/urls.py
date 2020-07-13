from rest_framework.routers import SimpleRouter

from .views.film_list_view import FilmListView

router = SimpleRouter()
router.register("films", FilmListView)
urlpatterns = router.urls
