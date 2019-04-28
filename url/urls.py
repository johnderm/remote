from django.conf.urls import  url
from . import views


urlpatterns = [
    url(r'^host/(\d+)$', views.host, name='host'),
    url(r'^host_list/(\w+)/(\w+)$', views.host_list, name='host_list'),
    url(r'^hostp/(?P<num1>\d+)/(?P<num2>\d+)$', views.hostp, name='hostp'),
    url(r'^qs/$', views.qs)
]