from django.contrib import admin
from .models import Proveedor, Factura

# Register your models here.
admin.site.register(Proveedor)
# admin.site.register(Factura)

# Dedine the admin class for Factura
class FacturaAdmin(admin.ModelAdmin):
    pass

# Register the admin class for Factura with the model Factura
admin.site.register(Factura, FacturaAdmin)