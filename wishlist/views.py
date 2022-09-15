from django.shortcuts import render
from wishlist.models import ItemWishlist
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_wishlist(request):
    return render(request, "wishlist.html", context)

def show_xml(request):
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request,id):
    data_json = ItemWishlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data_json), content_type="application/json")

data_wishlist_item = ItemWishlist.objects.all()
context = {
    'list_item': data_wishlist_item,
    'name': 'Muhammad Alif Ismady'
}

data = ItemWishlist.objects.all()




