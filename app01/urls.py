from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login', views.login, name='login'),
    url(r'^index', views.index, name='index'),
    url(r'^logout', views.logout, name='logout'),
    url(r'^querydict',views.querydict, name='querydict'),
    url(r'^josn_data',views.josn_data, name='josn_data'),
    url(r'^not_josn_data',views.not_josn_data, name='not_josn_data'),
    url(r'^get_header',views.get_header,name='get_header')
]