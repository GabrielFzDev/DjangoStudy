from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)#Quando colocamos SET_NULL, o banco precisa saber que essa coluna pode ser nula também
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)#Quando colocamos SET_NULL, o banco precisa saber que essa coluna pode ser nula também
    name = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True) # null para nao ser nulo essa coluna, e blank para nao deixar q no formulario do HTML ficar nulo tambem
    participants = models.ManyToManyField(User, related_name='participants',blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)#Autonow para salver o snapshot toda vez que for dado update em algo, e auto now add para quando foi criado
    
    #Ordenação
    class Meta:
        ordering = ['-updated','created'] # com o - o mais novo vem primeiro, sem o - o mais novo fica por ultimo
    
    def __str__(self):
        return self.name
    
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    #FK da tabela de rooms, mais especificamente o ID, e o cascade para caso for deletado o Room, ficar nulo
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)#Autonow para salver o snapshot toda vez que for dado update em algo, e auto now add para quando foi criado
    
    def __str__(self):
        return self.body[0:50]