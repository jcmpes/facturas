from django.contrib import admin
from .models import Proveedor, Factura

# Register your models here.
# admin.site.register(Proveedor)
# admin.site.register(Factura)

# Dedine the admin class for Factura
class FacturaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'proveedor', 'fecha_creacion', 'fecha_vencimiento')
    list_filter = ('fecha_creacion', 'fecha_vencimiento')

# Register the admin class for Factura with the model Factura
admin.site.register(Factura, FacturaAdmin)

class FacturaInline(admin.TabularInline):
    model = Factura

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display: ('codigo', 'nombre')
    inlines = [FacturaInline] 