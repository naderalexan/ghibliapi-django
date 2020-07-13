from rest_framework import serializers

from ..models import Film
from .person_serializer import PersonSerializer


class FilmSerializer(serializers.ModelSerializer):
    people = PersonSerializer(many=True)

    class Meta:
        model = Film
        fields = (
            "id",
            "title",
            "people",
        )
