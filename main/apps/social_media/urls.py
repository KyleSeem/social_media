# apps/social_media/urls.py

from django.conf.urls import url
from . import views

app_name = 'social_media'
urlpatterns = [
    url(r'^$', views.index, name='index'), # dashboard
    url(r'^myAccount$', views.myAccount, name='myAccount'),
    url(r'^myAlbum$', views.myAlbum, name='myAlbum'),
    url(r'^add_photo$', views.add_photo, name='add_photo'),
    url(r'^new_post$', views.new_post, name='new_post'),
    url(r'^scrap$', views.scrap, name='scrap'),
]
