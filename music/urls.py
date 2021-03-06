from django.urls import path, re_path
from . import views

app_name = 'music'

urlpatterns = [
    path('', views.base, name='index'),
    path('allAlbums/', views.all_albums,name='all_albums'),
    path('addMusic/', views.add_music, name='add_music'),
    path("<int:album_id>/", views.get_album_details, name='get_album_details'),
    path("<int:album_id>/favorite", views.favorite, name='favorite'),
]