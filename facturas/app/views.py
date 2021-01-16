from django.shortcuts import render
from django.core.cache import cache
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.views.decorators.cache import never_cache
from app.models import Factura, Proveedor
from django.views import generic

# Create your views here.
@never_cache
def clear_cache(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    cache.clear()
    return HttpResponse('Cache has been cleared')

def index(request):
    """ View function for home page of the site """

    num_invoices = Factura.objects.all().count()
    num_providers = Proveedor.objects.all().count()

    context = {
        'num_invoices': num_invoices,
        'num_providers': num_providers,
    }

    return render(request, 'index.html', context=context)

class InvoiceListView(generic.ListView):
    model = Factura
    context_object_name = 'invoice_list'

class InvoiceDetailView(generic.DetailView):
    model = Factura