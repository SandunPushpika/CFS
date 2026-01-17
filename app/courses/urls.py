from .views import create_course, list_all_courses, get_course_by_degree
from django.urls import path

urlpatterns = [
    path('', create_course, name='create_course'),
    path('all/', list_all_courses, name='list_all_courses'),
    path('by-degree/', get_course_by_degree, name='get_course_by_degree'),
    path('<int:course_id>/', create_course, name='delete_course_by_id'),
]