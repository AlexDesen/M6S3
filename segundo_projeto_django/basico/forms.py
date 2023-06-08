'''
Comando para a verificação do formulárai - neste caso - forms.is_valid()
Comando para criação da html
Comando no terminal do python com o abiente do django - python manage.py shell

'''

from django import forms
from basico.models import ReservaModels

class Contato(forms.ModelForm):
    class Meta():
        model = ReservaModels
        fields = ['nome_do_pet','telefone','data_da_reserva','observacoes']
    
   