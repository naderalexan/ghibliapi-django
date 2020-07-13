from django.db import models


class Person(models.Model):
    id = models.UUIDField(primary_key=True, db_index=True)
    name = models.CharField(max_length=64)
