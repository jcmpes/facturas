from django.contrib import admin
from .models import Proveedor, Factura

# Register your models here.
admin.site.register(Proveedor)
admin.site.register(Factura)