from django.urls import path
from .views import CircuitDetail, CircuitList, LivreurList, LivreurDetail, VehiculeList, VehiculeDetail

urlpatterns = [
    path('livreur/', LivreurList.as_view(), name='livreurs'),
    path('livreur/<int:id>', LivreurDetail.as_view(), name='livreur'),
    path('vehicule/', VehiculeList.as_view(), name='vehicules'),
    path('vehicule/<int:id>', VehiculeDetail.as_view(), name='vehicule'),
    path('circuit/', CircuitList.as_view(), name='circuits'),
    path('circuit/<int:id>', CircuitDetail.as_view(), name='circuit'),
]
