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
def status(request):
    list_watchlist = MyWatchList.objects.all()
    counter = 0
    for watchlist in list_watchlist:
        if watchlist.watched == "Yes":
            counter += 1
    if counter >= len(list_watchlist)-counter:
        return  "Selamat, kamu sudah banyak menonton!"
    else:
        return  "Wah, kamu masih sedikit menonton!"


def show_mywatchlist(request):
    list_watchlist = MyWatchList.objects.all()
    context = {
    'list_item' : list_watchlist,
    'name' : 'Trias Ahmad Fairuz',
    'id' : '2106633645',
    'status' : status(request)

}

    return render(request, "mywatchlist.html", context)



def show_mywatchlist_xml(request):

    list_watchlist = MyWatchList.objects.all()


    return HttpResponse(serializers.serialize("xml", list_watchlist), content_type="application/xml")

def show_mywatchlist_json(request):

    list_watchlist = MyWatchList.objects.all()


    return HttpResponse(serializers.serialize("json", list_watchlist), content_type="application/json")
