from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

list_watchlist = MyWatchList.objects.all()

context = {
    'list_item' : list_watchlist,
    'name' : 'Trias Ahmad Fairuz',
    'id' : '2106633645'
}

# Create your views here.
def show_mywatchlist(request):

    return render(request, "mywatchlist.html", context)

def show_mywatchlist_xml(request):

    return HttpResponse(serializers.serialize("xml", list_watchlist), content_type="application/xml")

def show_mywatchlist_json(request):

    return HttpResponse(serializers.serialize("json", list_watchlist), content_type="application/json")
