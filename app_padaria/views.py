from django.shortcuts import render
from .models import Fila1
def home(request):
    return render(request, 'ecommerce/home.html')

def fila(request):
    nova_pessoa = Fila1()
    nova_pessoa.name =  request.POST.get('nome')
    nova_pessoa.telefone = request.POST.get('telefone')
    nova_pessoa.save()
    pessoas = {
        'pessoas' : Fila1.objects.all()
    }
    return render(request, 'ecommerce/fila.html', pessoas)
