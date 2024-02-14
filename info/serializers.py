from rest_framework import serializers
from info.models import CERT

class CERTSerializer(serializers.ModelSerializer):
    class Meta:
        model = CERT
        fields = '__all__'
