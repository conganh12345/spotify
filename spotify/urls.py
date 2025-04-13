"""
URL configuration for spotify project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.cores.urls')),  
    path('user/', include('apps.users.urls')), 
    path('group/', include('apps.groups.urls')),
    path('artist/', include('apps.artists.urls')), 
    path('genre/',include('apps.genres.urls')),
    path('api/', include('apps.genres.api_urls')), 
    path('album/',include('apps.albums.urls')),
    path('song/',include('apps.songs.urls')),
    path('api/',include('apps.artist_follows.api_urls')),
    path('api/',include('apps.album_plays.api_urls')),
    path('api/',include('apps.song_plays.api_urls')),
    path('api/',include('apps.songs.api_urls')),
    path('api/',include('apps.playlists.api_urls')),
    path('api/',include('apps.playlists_songs.api_urls')),




   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
