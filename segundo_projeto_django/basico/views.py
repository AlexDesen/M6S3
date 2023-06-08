from django.shortcuts import render
from basico.forms import Contato
""" 
A função reserva irá, numa requisição post,validadas as informações, retornar a página com uma mensagem
de sucesso. Se a requisição for get a mesma retorna um formulário vazio.
"""
def reserva(requests):
   formulario = Contato(requests.POST or None)
   contexto = {'sucesso': False}
   if requests.method == "POST":
      formulario.save()
      contexto ['sucesso'] = True
   contexto['formulario'] = formulario
   
   return render(requests,'reserva_pet.html',contexto)



   