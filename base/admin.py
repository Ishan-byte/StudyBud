from django.contrib import admin
# importing created models in the admin file to register it for viewing and working with the database table
from .models import Room, Message, Topic


# registering the Models in the Admin site
# Room 
admin.site.register(Room)
admin.site.register(Message)
admin.site.register(Topic)