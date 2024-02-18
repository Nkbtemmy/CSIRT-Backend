from rest_framework import generics, filters
from team.models import CERT
from team.serializers import CERTSerializer
# from corsheaders.middleware import corsheaders
from django_filters.rest_framework import DjangoFilterBackend

class CERTListCreate(generics.ListCreateAPIView):
    queryset = CERT.objects.all()
    serializer_class = CERTSerializer

class CRERTRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = CERT.objects.all()
    serializer_class = CERTSerializer

class CERTByCountryList(generics.ListAPIView):
    serializer_class = CERTSerializer
    queryset = CERT.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['country']
