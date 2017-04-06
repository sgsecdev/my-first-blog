from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.Post_detail, name='post_detail')
]