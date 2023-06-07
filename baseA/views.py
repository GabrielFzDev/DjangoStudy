from django.shortcuts import render
from .models import Room
# Create your views here.

# rooms = [
#     {'id':1,'name':'Let s learning Python!'},
#     {'id':2,'name':'Frontend developers'},
#     {'id':2,'name':'Desing'},
# ]

def home(request):
    rooms = Room.objects.all()
    #Context variable é para ficar melhor organizado o dicionario de variveis
    context = {'rooms':rooms}
    return render(request,'baseA/home.html',context)# tres propriedades, request, template e variaveis que vc quer passar pro seu template

def room(request,pk):
    
    #Conseguimos colocar logicas para poder mostrar valores dinamicos
    room = Room.objects.get(id=pk)
    context = {'room':room}
    return render(request,'baseA/room.html',context)
