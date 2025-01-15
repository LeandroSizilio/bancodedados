from re import T
from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)
    endereco = models.ForeignKey('Endereco', on_delete=models.CASCADE, null=True, blank=True)
    instagram = models.CharField(max_length=100)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    indicado_por = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='referenciados')
    parentes = models.ForeignKey(
        'self', 
        on_delete=models.CASCADE, 
        null=True,  
        blank=True, 
        choices=[
            ('pai', 'Pai'),
            ('mae', 'Mãe'),
            ('irma', 'Irmã'),
            ('filho', 'Filho'),
            ('avo', 'Avô/Avó')
        ],
        related_name='parente')
    servico = models.ForeignKey('TipoServico', on_delete=models.CASCADE, null=True, blank=True, verbose_name = "Serviço")
    

    def __str__(self):
        return self.nome + ' - ' + self.email + ' - ' + self.telefone + ' - ' + self.instagram + ' - ' + str(self.data_cadastro)    

class Endereco(models.Model):
    rua = models.CharField(max_length=100)
    numero = models.IntegerField()
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    cep = models.CharField(max_length=8)

    def __str__(self):
        return self.rua + ' - ' + str(self.numero) + ' - ' + self.bairro + ' - ' + self.cidade + ' - ' + self.estado + ' - ' + self.cep
    
class Servico(models.Model):        
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    data_evento = models.DateTimeField()
    status = models.CharField(max_length=10, choices=[('pendente', 'Pendente'), ('concluido', 'Concluído'), ('cancelado', 'Cancelado')])
    tipo_servico = models.ForeignKey('TipoServico', on_delete=models.CASCADE, default=None, blank=True, null=True)
    

    def __str__(self):
        return self.descricao + ' - ' + str(self.preco) + ' - ' + str(self.data_evento) + ' - ' + self.status + ' - ' + str(self.cliente) + ' - ' + str(self.tipo_servico)
    
class TipoServico(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    custo = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0.00)

    def __str__(self):
        return self.nome + ' - ' + self.descricao + ' - ' + str(self.custo) 