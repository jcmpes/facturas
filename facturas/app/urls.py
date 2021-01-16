from django.urls import path
from . import views

# Create your views here
urlpatterns = [
    path('clear_cache/', views.clear_cache),
    path('', views.index, name='index'),
    path('invoices/', views.InvoiceListView.as_view(), name='invoices'),
]

