from django.conf.urls import url
from recharge import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]

