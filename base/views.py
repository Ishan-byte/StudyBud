from django.shortcuts import render
from .models import Room


# Views of the base application

# Home
def home(request):
    rooms = Room.objects.all()
    context = {'rooms' :  rooms }
    return render(request, 'base/home.html', context) 

# Room
def room(request, pk):
    room = Room.objects.get(id = pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)

# Room Form
def createRoom(request):
    context = {}
    return render(request, 'base/room_form.html', context)