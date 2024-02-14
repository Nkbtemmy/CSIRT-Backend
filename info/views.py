from rest_framework import generics
from info.models import CERT
from info.serializers import CERTSerializer

class CERTListCreate(generics.ListCreateAPIView):
    queryset = CERT.objects.all()
    serializer_class = CERTSerializer

class CRERTRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = CERT.objects.all()
    serializer_class = CERTSerializer
