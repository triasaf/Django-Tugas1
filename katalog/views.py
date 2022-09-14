from django.shortcuts import render
from katalog.models import CatalogItem

data_catalog_item = CatalogItem.objects.all()
context = {
    'list_item' : data_catalog_item,
    'name' : 'Trias Ahmad Fairuz',
    'id' : '2106633645'

}

def show_catalog(request):
    return render(request, 'katalog.html', context)

# TODO: Create your views here.
