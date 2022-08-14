from django.contrib import admin
# importing created models in the admin file to register it for viewing and working with the database table
from .models import Room, Message, Topic, User


# registering the Models in the Admin site
admin.site.register(User)
admin.site.register(Room)
admin.site.register(Message)
admin.site.register(Topic)