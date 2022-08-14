from django.forms import ModelForm
from .models import User, Room
from django.contrib.auth.forms import UserCreationForm
# creating class based form inheriting the model form

class RoomForm(ModelForm):
    class Meta():
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']
    
class UserForm(ModelForm):
    class Meta():
        model = User
        fields = ['avatar', 'name', 'username', 'email', 'bio']


class MyUserCreationForm(UserCreationForm):
    class Meta():
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']
