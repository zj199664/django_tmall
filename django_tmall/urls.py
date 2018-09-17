from django.conf.urls import url, include
from django.contrib import admin

from home import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url('^$', views.index),
    url('home/', include('apps.home.urls')),
    url('account/', include('apps.account.urls')),
    url('cate/', include('apps.cate_detaile.urls')),
    url('order/', include('apps.order.urls')),
    url('car/', include('apps.shopcar.urls')),
    url('pay/', include('apps.pay.urls')),
    url('shop/', include('apps.shop_detail.urls')),
]
