from django.conf.urls import url
from . import views

app_name = 'social_media'
urlpatterns = [
    url(r'^$', views.index, name='index'), # dashboard
    url(r'^account/(?P<id>\d+)$', views.account, name='account'),
    url(r'^myAlbum$', views.myAlbum, name='myAlbum'),
    url(r'^poop$', views.poop, name='poop'),
    url(r'^add_photo$', views.add_photo, name='add_photo'), # post section - select and save photo form
    url(r'^add_new_post/(?P<id>\d+)$', views.new_brick, name='new_brick'), # post section - add caption and save brick form
    # url(r'^add_photo_success$', views.add_photo_success, name='add_photo_success'),
]
