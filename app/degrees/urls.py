from .views import create_degree_api, list_all_degrees
from django.urls import path

urlpatterns = [
    path('', create_degree_api, name='create_degree'),
    path('all/', list_all_degrees, name='list_all_degrees'),
    path('<int:degree_id>/', create_degree_api, name='delete_degree_by_id'),
]
