from django.conf.urls import url

from apps.search import views

urlpatterns = [
    url('result/', views.search, name='search')
]
