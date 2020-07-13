from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from ..models import Film
from ..serializers import FilmSerializer


class FilmListView(mixins.ListModelMixin, GenericViewSet):
    serializer_class = FilmSerializer
    queryset = Film.objects.all().prefetch_related("people")
