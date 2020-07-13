from django.db import models
from .person import Person


class Film(models.Model):
    id = models.UUIDField(primary_key=True, db_index=True)
    title = models.CharField(max_length=128)
    people = models.ManyToManyField(Person, related_name="films")
