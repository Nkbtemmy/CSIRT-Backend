import uuid
from django.db import models
from django_countries.fields import CountryField

# Create your models here.

class Country(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    country = CountryField()

    def __str__(self):
        return self.name

