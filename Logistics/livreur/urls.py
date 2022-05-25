from django.urls import path
from .views import LivreurList, LivreurDetail

urlpatterns = [
    path('', LivreurList.as_view(), name='livreurs'),
    path('<int:id>', LivreurDetail.as_view(), name='livreur'),
]
