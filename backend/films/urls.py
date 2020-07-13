from django.shortcuts import redirect
from django.urls import path
from rest_framework import permissions
from rest_framework.routers import SimpleRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .views.film_list_view import FilmListView

schema_view = get_schema_view(
    openapi.Info(
        title="Films API",
        default_version="v1",
        contact=openapi.Contact(email="alexan.nader@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
router = SimpleRouter()
router.register("films", FilmListView)

urlpatterns = [
    path("docs/", schema_view.with_ui("swagger", cache_timeout=0)),
    path("movies/", lambda request: redirect("film-list", permanent=True)),
] + router.urls
