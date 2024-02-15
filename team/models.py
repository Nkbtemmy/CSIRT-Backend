import uuid
from django.db import models
from django_countries.fields import CountryField

class CERT(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    country = CountryField()
    name = models.CharField(max_length=100)
    website = models.URLField()

    def __str__(self):
        return f"{self.name} - {self.get_country_display()}"
    