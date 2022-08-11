from django.forms import ModelForm
from .models import Room

# creating class based form inheriting the model form

class RoomForm(ModelForm):
    class Meta():
        model = Room
        fields = '__all__'
