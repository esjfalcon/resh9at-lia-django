from rest_framework import serializers
from .models import Livreur, Vehicule, Circuit


class LivreurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livreur
        fields = ('id', 'name', 'age')


class VehiculeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicule
        fields = ('id', 'name', 'immatriculation')


class CircuitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Circuit
        fields = ('livruer', 'vehicule', 'name')