import uuid
from django.db import models
from django_countries.fields import CountryField
from django.core.exceptions import ValidationError

class CERT(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    country = CountryField()
    name = models.CharField(max_length=100)
    website = models.URLField()

    def __str__(self):
        return f"{self.name} - {self.get_country_display()}"

    def save(self, *args, **kwargs):
        # Check if an instance with the same country and name already exists
        if CERT.objects.filter(country=self.country, name=self.name).exists():
            # If exists, raise a ValidationError
            raise ValidationError("A CERT with the same country and name already exists.")
        else:
            # If does not exist, save normally
            if not self.id:
                # Generate UUID for new instances
                self.id = uuid.uuid4()
            super().save(*args, **kwargs)
