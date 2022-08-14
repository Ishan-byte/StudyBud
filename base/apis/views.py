from re import I
from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Room
from .serializers import RoomSerializer

@api_view(['GET'])
def getroutes(request):
    person = {'name' : 'Ishan', 'age' : 12} 
    return Response(person)

@api_view(['GET'])
def getrooms(request):
    rooms = Room.objects.all()
    room_serialized = RoomSerializer(rooms, many=True)
    return Response(room_serialized.data)


@api_view(['GET'])
def getroom(request, pk):
    room = Room.objects.get(id = pk)
    room_serialized = RoomSerializer(room, many = False)
    return Response(room_serialized.data)