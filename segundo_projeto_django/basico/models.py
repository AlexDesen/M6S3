from django.db import models


class ReservaModels(models.Model):
    nome_do_pet = models.CharField(verbose_name='Nome do pet',max_length=50)
    telefone = models.CharField(verbose_name='Telefone',max_length=50)
    data_da_reserva = models.DateField(verbose_name='Data de reserva')
    observacoes = models.TextField(verbose_name='Observações', default='nulo')
