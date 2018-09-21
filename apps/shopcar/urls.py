from django.conf.urls import url

from apps.shopcar import views

urlpatterns = [
    url('add/', views.add),
    url('list/', views.list, name='car_list'),
    url('delete/', views.delete, name='car_delete'),
    url('update/', views.update_num, name='car_update')
]
