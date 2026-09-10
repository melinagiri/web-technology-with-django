from django.urls import path
from songs import views

urlpatterns = [
   
    path('', views.song_list, name='song_list'),                 # /songs/
    path('<int:song_id>/', views.song_detail, name='song_detail'),  # /songs/1/
]
