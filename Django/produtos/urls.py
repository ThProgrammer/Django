from django.urls import path
from . import views


#Aqui criaremos as urls da nossa aplicação, e cada url chamará uma função diferente

urlpatterns = [
    path('ver_produto/', views.ver_produto, name="ver_produto"), #chamará a função ver_produto em views
    path('inserir_produto/', views.inserir_produto, name ="inserir_produto")  #chamará a função inserir_produto em views
]