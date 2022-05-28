from .models import Livreur, Vehicule, Circuit
from .serializers import CircuitSerializer, VehiculeSerializer, LivreurSerializer
from rest_framework import generics


class LivreurList(generics.ListCreateAPIView):
    queryset = Livreur.objects.all()
    serializer_class = LivreurSerializer




class LivreurDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Livreur.objects.all()
    serializer_class = LivreurSerializer
    lookup_field = 'id'




class VehiculeList(generics.ListCreateAPIView):
    queryset = Vehicule.objects.all()
    serializer_class = VehiculeSerializer




class VehiculeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vehicule.objects.all()
    serializer_class = VehiculeSerializer
    lookup_field = 'id'



class CircuitList(generics.ListCreateAPIView):
    queryset = Circuit.objects.all()
    serializer_class = CircuitSerializer




class CircuitDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Circuit.objects.all()
    serializer_class = CircuitSerializer
    lookup_field = 'id'
