from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='Home'),
    path('room/<str:pk>',views.room, name='Room'), #para nao mudar tds os templates o nome da pagina caso precise mudar, usar nos templates {% url%}
]