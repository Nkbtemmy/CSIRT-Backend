from rest_framework import serializers
from django_countries.serializer_fields import CountryField
from team.models import CERT
from django_countries.serializers import CountryFieldMixin

    
class CERTSerializer(serializers.ModelSerializer):
    country = CountryField(name_only=True)
    class Meta:
        model = CERT
        fields = '__all__'

