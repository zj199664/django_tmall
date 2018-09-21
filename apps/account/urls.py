from django.conf.urls import url

from apps.account import views

urlpatterns = [
    url('login/', views.login_view, name='login'),
    url('register/', views.register_view, name='register'),
    url('logout/', views.logout_view, name='logout')
]
