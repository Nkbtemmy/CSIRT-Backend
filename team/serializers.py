from rest_framework import serializers
from django_countries.serializer_fields import CountryField
from team.models import CERT
from rest_framework.exceptions import ValidationError

    
class CERTSerializer(serializers.ModelSerializer):
    country = CountryField(name_only=True)
    class Meta:
        model = CERT
        fields = '__all__'

    def create(self, validated_data):
        try:
            # Check if a CERT instance with the same country and name already exists
            country = validated_data.get('country')
            name = validated_data.get('name')
            if CERT.objects.filter(country=country, name=name).exists():
                # If exists, raise a ValidationError
                raise ValidationError("A CERT with the same country and name already exists.")
            
            # If does not exist, create and return the CERT instance
            return CERT.objects.create(**validated_data)
        except Exception as e:
            print(f"Serialization Error: {e}")
            raise

