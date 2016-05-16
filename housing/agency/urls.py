from django.conf.urls import url
from django.core.urlresolvers import reverse

from . import views

urlpatterns = [
    url(r'^$', views.home_page, name='home'),
    url(r'^add$', views.add_house, name='add'),
    url(r'^post/(?P<slug>[\w-]+)/$', views.house_detail, name='post'),
    url(r'^post/(?P<slug>[\w-]+)/edit/$', views.update_house, name='edit'),
    url(r'^post/(?P<slug>[\w-]+)/delete/$', views.delete_house, name='delete'),
    
]