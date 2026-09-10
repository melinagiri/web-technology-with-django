from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def song_list(request): 
    # return render(request, 'songs/song_list.html')
    return HttpResponse("list of songs will be displayed here")

def song_detail(request, song_id):
    return HttpResponse(f"Details of song with ID: {song_id}")
