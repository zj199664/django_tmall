from django.shortcuts import render

# Create your views here.
from apps.home.models import *


def search(request):
    if request.method == 'GET':
        keyword = request.GET.get('keyword')
        shops = Shop.objects.filter(name__icontains=keyword).values('shop_id', 'name').order_by('shop_id')
        for shop in shops:
            img = ShopImage.objects.filter(shop_id=shop.get('shop_id')).first()
            shop.update(img=img)
        return render(request, 'search.html', {'shops': shops})
    else:
        return render(request, 'error.html')
