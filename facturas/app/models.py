from django.db import models
from django.utils.translation import gettext as _
import datetime

# Create your models here.
class Proveedor(models.Model):
    # Fields
    codigo = models.IntegerField()
    nombre = models.CharField(max_length=16)
    comentarios = models.TextField(blank=True, null=True)

    # Metadata
    class Meta:
        ordering = ['codigo']

    # Methods
    def __str__(self):
        return self.nombre


class Factura(models.Model):
    # Fields
    codigo = models.CharField(max_length=32, help_text='Introduce el código de la factura')
    autor = models.CharField(max_length=16)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.PROTECT)
    fecha_creacion = models.DateField(_("Fecha"), default=datetime.date.today)
    fecha_vencimiento = models.DateField(null=True, blank=True)
    pdf = models.FileField(upload_to="documentos/%Y/%m/%d/")
    cantidad = models.DecimalField(_("Precio ex. IVA."), decimal_places=2, max_digits=6)
    tipo_iva = models.IntegerField(_("% IVA"), default=21)
    observaciones = models.TextField(_("Observaciones"))

    # Metadata
    class Meta:
        ordering = ['-fecha_creacion']

    # Methods
    def __str__(self):
        return self.codigo

