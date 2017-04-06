from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.Post_detail, name='post_detail'),
    url(r'^post/(?P<pk>[0-9]+)/edit$', views.Post_edit, name='post_edit'),
    url(r'^post/(?P<pk>[0-9]+)/delete$', views.Post_delete, name='post_delete'),
    url(r'^post/new/$', views.Post_new, name='post_new'),
]