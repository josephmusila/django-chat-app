from django.shortcuts import render

# Create your views here.

def lobby(request):
    return render(request,"base/lobby.html")


def room(request, room_name):
    return render(request, 'base/room.html', {
        'room_name': room_name
    })