from django.urls import path
from . import views

urlpatterns = [
    path('', views.problem_detail, name='problem_detail'),
]
