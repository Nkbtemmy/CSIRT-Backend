from rest_framework import generics
from team.models import CERT
from team.serializers import CERTSerializer

class CERTListCreate(generics.ListCreateAPIView):
    queryset = CERT.objects.all()
    serializer_class = CERTSerializer

class CRERTRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = CERT.objects.all()
    serializer_class = CERTSerializer