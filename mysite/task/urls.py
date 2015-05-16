from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^get_task/$', views.get_task, name='get_task'),
    url(r'^update_status/(?P<ident>[0-9]+)/$', views.update_status, name='update_status'),
]
