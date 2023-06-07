from django.db import models

# Create your models here.
class Room(models.Model):
    # host
    # topic
    name = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True) # null para nao ser nulo essa coluna, e blank para nao deixar q no formulario do HTML ficar nulo tambem
    # participants = 
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)#Autonow para salver o snapshot toda vez que for dado update em algo, e auto now add para quando foi criado
    
    def __str__(self):
        return self.name