from rest_framework import generics
from team.models import CERT
from team.serializers import CERTSerializer

class CERTListCreate(generics.ListCreateAPIView):
    queryset = CERT.objects.all()
    serializer_class = CERTSerializer

class CRERTRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = CERT.objects.all()
    serializer_class = CERTSerializer

class CERTByCountryList(generics.ListAPIView):
    serializer_class = CERTSerializer

    def get_queryset(self):
        country_name = self.kwargs['country']  # Assuming you pass the country name as a URL parameter
        return CERT.objects.filter(country=country_name)