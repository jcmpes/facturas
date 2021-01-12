from django.urls import path
from . import views

urlpatterns = [
    path('clear_cache/', views.clear_cache),
]