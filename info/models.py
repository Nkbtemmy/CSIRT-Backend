import uuid
from django.db import models
from country.models import Country

class CERT(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    website = models.URLField()

    def __str__(self):
        return self.name
    