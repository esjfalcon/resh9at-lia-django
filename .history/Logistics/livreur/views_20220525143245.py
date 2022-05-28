from .models import Livreur, Vehicule, Circuit
from .serializers import VehiculeSerializer, LivreurSerializer
from rest_framework import generics


class LivreurList(generics.ListCreateAPIView):
    queryset = Livreur.objects.all()
    serializer_class = LivreurSerializer




class LivreurDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Livreur.objects.all()
    serializer_class = LivreurSerializer
    lookup_field = 'id'



