from django.db.models import Sum

from apps.home.models import *


def shop_count(request):
    count = 0
    if request.user.is_authenticated():
        count = ShopCar.objects.filter(user_id=request.user.userprofile.uid, status=1).aggregate(
            sum=Sum('number')).get('sum')
    return {'count': count}
