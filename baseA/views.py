from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from .models import Room,Topic, Message
from .form import RoomForm
# Create your views here.

# rooms = [
#     {'id':1,'name':'Let s learning Python!'},
#     {'id':2,'name':'Frontend developers'},
#     {'id':2,'name':'Desing'},
# ]

def loginRegister(request):
    
    page = 'login'
    
    if request.user.is_authenticated:
        return redirect('Home')
    
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        
        #ver se o usuario existe com try cacth
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User does not exist")
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request,user)
            return redirect('Home')
        else:
            messages.error(request, 'Username or password does not exist')
    
    context ={'page':page}
    return render(request,'baseA/login_register.html',context)


def logoutUser(request):
    #para logout simoplesmente tira o cokie de session
    logout(request)
    return redirect('Home')

#View para registrar na mesma pagina de Login
def registerUser(request):
    page = 'register'
    form = UserCreationForm()
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid:
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('Home')
        else:
            messages.error(request, 'An error ocurred during registration')
    
    context = {'creationUser': form}
    return render(request,'baseA/login_register.html',context)

def home(request):
    query = request.GET.get('q') if request.GET.get('q') != None else ''
    
    rooms = Room.objects.filter(
        Q(topic__name__icontains=query) |
        Q(name__icontains=query) |
        Q(description__contains=query) |
        Q(host__username__icontains=query)
    )
    topics = Topic.objects.all()
    
    room_count = rooms.count()
    
    #Context variable é para ficar melhor organizado o dicionario de variveis
    context = {'rooms':rooms,'topics':topics,'room_count':room_count}
    return render(request,'baseA/home.html',context)# tres propriedades, request, template e variaveis que vc quer passar pro seu template

def room(request,pk):
    
    #Conseguimos colocar logicas para poder mostrar valores dinamicos
    room = Room.objects.get(id=pk)
    messages = room.message_set.all().order_by('-created')
    participants = room.participants.all()
    
    if request.method == 'POST':
        message = Message.objects.create(
            user = request.user,
            room = room,
            body = request.POST.get('body')
        )
        room.participants.add(request.user)
        return redirect('Room',pk=room.id)
    
    context = {'room':room,'comments':messages,'participants':participants}
    return render(request,'baseA/room.html',context)

@login_required(login_url='login')
def createRoom(request):
    form = RoomForm()
    
    if request.method == 'POST':
        
        form = RoomForm(request.POST)
        #Se os valores estiverem validos, nada de errado
        if form.is_valid():
            form.save()
            #Redirecionar o usuario para a pagina home (o nome da pagina eh o mesmo do name em URLs)
            return redirect('Home')
    
    context = {'form':form}
    return render(request, 'baseA/room_form.html',context)

@login_required(login_url='login')
def updateRoom(request,pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)#Para poder colocar dados já nesse form precisa colocar o instancecom os dados q vc quer, se ficar vazio, vai vim um formulario vazio
    
    context = {'form':form}
    
    if request.user != room.host:
        return HttpResponse('You not allowed to be in here!!')
    
    
    if request.method == 'POST':
        form = RoomForm(request.POST,instance=room)
        #Se os valores estiverem validos, nada de errado
        if form.is_valid():
            form.save()
            #Redirecionar o usuario para a pagina home (o nome da pagina eh o mesmo do name em URLs)
            return redirect('Home')
    
    return render(request,'baseA/room_form.html',context)

@login_required(login_url='login')
def deleteRoom(request,pk):
    room = Room.objects.get(id=pk)
    
    if request.user != room.host:
        return HttpResponse('You not allowed to be in here!!')
    
    
    if request.method == 'POST':
        room.delete()
        return redirect('Home')
    
    return render(request,'baseA/delete.html',{'obj':room})

#Deletando uma mensagem
@login_required(login_url='login')
def deleteMessage(request,pk):
    message = Message.objects.get(id=pk)
    room_id = message.room.id
    if request.user != message.user:
        return HttpResponse('You not allowed to be in here!!')
    
    if request.method == 'POST':
        message.delete()
        return redirect('Room',room_id )
    
    return render(request,'baseA/delete.html',{'obj':message})
