from django.urls import path
from .views import QAndAnsList

urlpatterns = [
    path('qAndAnswers/',QAndAnsList.as_view(), name='qAndAnsList')
]
