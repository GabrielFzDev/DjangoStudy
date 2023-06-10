from django.urls import path
from . import views

urlpatterns = [
    #Register, Login and logout
    path('login/', views.loginRegister, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),
    
    path('',views.home, name='Home'),
    path('room/<str:pk>',views.room, name='Room'), #para nao mudar tds os templates o nome da pagina caso precise mudar, usar nos templates {% url%}
    
    #message formulario
    path('delete-message/<str:pk>', views.deleteMessage, name='delete-message'),
    
    #room de formulario
    #para cada acao de update, or delete precisa de um novo path
    path('create-room/', views.createRoom, name='create-room'),
    path('update-room/<str:pk>', views.updateRoom, name='update-room'),
    path('delete-room/<str:pk>', views.deleteRoom, name='delete-room'),
    
    
    
]