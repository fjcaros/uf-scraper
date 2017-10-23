from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^list$', views.list, name='list'),
    url(r'^price$', views.price, name='price'),
]