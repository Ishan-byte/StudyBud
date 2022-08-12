from itertools import pairwise
from types import TracebackType
from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Room, Topic, Message
from django.contrib.auth.models import User
from .forms import RoomForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Views of the base application

# Login
def loginUser(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
           user = User.objects.get(username = username)
        except:
            messages.error(request, 'User does not exists.')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'User name or password does not exist')

    context = {'page': page}
    return render(request, 'base/login_register.html', context)


# Register
def register(request):
    page = 'register'
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit='False')
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occured during registration.')

    context = {'page': page, 'form' : form}
    return render(request, 'base/login_register.html', context)

# Log out user
def logOutUser(request):
    logout(request)
    return redirect('home')

# Home
def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    rooms = Room.objects.filter( Q(topic__name__icontains = q) 
                                 | 
                                 Q(name__icontains = q)        
                                 | 
                                 Q(description__icontains = q) 
                                 |
                                 Q(host__username__icontains = q)
    )
    room_count = rooms.count()
    topics = Topic.objects.all()

    room_messages = Message.objects.filter(
        Q(room__topic__name__icontains = q))

    context = {'rooms' :  rooms , 'topics': topics, 'room_count' : room_count, 'room_messages': room_messages}
    return render(request, 'base/home.html', context) 


# Room
def room(request, pk):
    room = Room.objects.get(id = pk)
    room_messages = room.message_set.all()
    participants = room.participants.all()
    

    if request.method == 'POST':
        message = Message.objects.create(
            user = request.user,
            room = room,
            body = request.POST.get('body')
        )
        room.participants.add(request.user)
        return redirect('room', pk = room.id)


    context = { 'room': room, 'room_messages': room_messages , 'participants': participants}
    return render(request, 'base/room.html', context)


# Create Room 
@login_required(login_url='login')
def createRoom(request):
    term = 'Create'
    form = RoomForm()
    topics = Topic.objects.all()
    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)

        Room.objects.create(
            host = request.user,
            topic = topic,
            name = request.POST.get('name'),
            description = request.POST.get('description')
        )


        return redirect('home')

    context = {'form': form, 'topics': topics, 'term': term}
    return render(request, 'base/room_form.html', context)
 

# Update Room
@login_required(login_url='login')
def updateRoom(request, pk): 
    term = 'Update'
    room = Room.objects.get(id = pk)
    form = RoomForm(instance = room)

    if request.user != room.host:
        return HttpResponse("You are not allowed to update another user's room")

    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name = topic_name)
        room.name = request.POST.get('name')
        room.topic = topic
        room.description = request.POST.get('description')
        room.save()
        return redirect('home')

    context = {'form': form, 'room': room, 'term': term}
    return render(request, 'base/room_form.html', context)


# Delete Room 
@login_required(login_url='login')
def deleteRoom(request, pk):
    room = Room.objects.get(id = pk)

    if request.user != room.host:
        return HttpResponse("You are not allowed to delete another user's room")

    if request.method == 'POST':
        room.delete()
        return redirect('home')

    return render(request, 'base/delete.html', {'obj': room})

# Delete Message
@login_required(login_url='login')
def deleteMessage(request, pk):
    message = Message.objects.get(id = pk)

    if request.user != message.user:
        return HttpResponse("You are not allowed to delete another user's message")

    if request.method == 'POST':
        message.delete()
        return redirect('room', pk = message.room.id)

    return render(request, 'base/delete.html', {'obj': message})


# User Profile
def userProfile(request, pk):
    user = User.objects.get(id = pk)
    rooms = user.room_set.all()
    room_messages = user.message_set.all()
    room_count = Room.objects.all().count()
    topics = Topic.objects.all()
    context = { 'user' : user , 'rooms': rooms, 'topics' : topics, 'room_messages': room_messages, 'room_count' : room_count}
    return render(request, 'base/profile.html', context)