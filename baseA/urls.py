from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='Home'),
    path('room/<str:pk>',views.room, name='Room'), #para nao mudar tds os templates o nome da pagina caso precise mudar, usar nos templates {% url%}
    
    #room de formulario
    #para cada acao de update, or delete precisa de um novo path
    path('create-room/', views.createRoom, name='create-room'),
    path('update-room/<str:pk>', views.updateRoom, name='update-room'),
    path('delete-room/<str:pk>', views.deleteRoom, name='delete-room'),
    
    #Register and Login
    path('login/', views.loginRegister, name='login'),
]