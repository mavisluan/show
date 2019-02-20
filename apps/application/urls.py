from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$', views.new),
    url(r'^(?P<id>\d+)$', views.show_info),
    url(r'^(?P<id>\d+)/edit$', views.edit),
    url(r'^create$', views.process_add),
    url(r'^(?P<id>\d+)/update$', views.process_edit),
    url(r'^(?P<id>\d+)/destroy$', views.process_delete),
]
