from django.urls import path
from app.views import lesson_list

urlpatterns = [
    path('maratona/', lesson_list)
]
