from django.forms import ModelForm
from .models import Room

#Jeito facil de criar um formulario
class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'