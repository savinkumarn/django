from _ast import alias

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,Http404
from .models import Album,Song
# Create your views here.


def index(request):
    all_albums = Album.objects.all()
    context = {
        'all_albums': all_albums,
    }
    return render(request,'music/index.html',context)


def add_music(request):
    return HttpResponse("<h1>This is Music App Add Music Page</h1>")


def get_album_details(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/details.html', {'album': album, 'songs': album.song_set.all()})


def favorite(request,album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except (KeyError,Song.DoesNotExist):
        return render(request,'music/details.html',
                      {'album': album, 'error_message': "Not a valid Song"})
    else:
        if 'Like' in request.POST:
            selected_song.is_favorite = True
        elif 'Dislike' in request.POST:
            selected_song.is_favorite = False
        selected_song.save()
        return render(request, 'music/details.html', {'album': album, 'songs': album.song_set.all()})
