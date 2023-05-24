from django.shortcuts import render
from django.http import HttpResponse #O que é http??

# Create your views here.


def ver_produto(request):
    return render(request, "ver_produto.html")

def inserir_produto(request):
    return render(request, 'inserir_produto.html')

#def ver_produto(request):
    #return HttpResponse('Estou no "ver"')


#def inserir_produto(request):
    #return HttpResponse('Estou no "inserir"')
