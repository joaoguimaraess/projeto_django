from django.db import models

# Create your models here.
class Fila(models.Model):
    id1 = models.AutoField(primary_key=True)
    name = models.TextField(max_length=255)

class Fila1(models.Model):
    id1 = models.AutoField(primary_key=True)
    name = models.TextField(max_length=255, null = True)
    telefone = models.IntegerField(null = True)
