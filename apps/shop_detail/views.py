from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from apps.home.models import *


def detail(request):
    if request.method == 'GET':
        try:
            shop_id = request.GET.get('id')
            if shop_id:
                # 获取商品的所有信息
                shop = Shop.objects.get(shop_id=shop_id)
                # 获取商品的图片信息
                shop.imgs = shop.shopimage_set.all()
                # 获取商品的参数信息
                shop.values = shop.propertyvalue_set.all()
                # for value in shop.values:
                # 获取商品的评论信息
                shop.reviews = shop.review_set.all()
                shop.count = shop.review_set.all().count()
                for review in shop.reviews:
                    user_p = UserProfile.objects.filter(uid=review.user_id).first()
                    name = User.objects.filter(id=user_p.user_id).first().username
                return render(request, 'detail.html', {'shop': shop,'name':name})
        except:
            return render(request, 'error.html')
    else:
        return render(request, 'error.html')
