from django.db import models
from django.contrib.auth.models import User

#Atributos do User padrão
##username: Único. Pode ser utilizado para login.
##first_name: Opcional.
##last_name: Opcional.
##email: Opcional, mas pode ser configurado como obrigatório e usado para login.
##password: Armazenada com criptografia.
##is_staff: Boolean para indicar se o usuário pode acessar o painel de administrador.
##is_active: Boolean. Usuários inativos não podem fazer login.
##is_superuser: Boolean para indicar usuários que possuem todas as permissões.
##last_login: A data e hora.
##date_joined: A data e hora.

class Profile(models.Model):
    USER_TYPE_CHOICES = [
        ('aluno', 'Aluno'),
        ('coordenador', 'Coordenador'),
        ('orientador', 'Orientador'),
    ]

    user = models.OneToOneField(User, on_delete=models.PROTECT)
    nusp = models.CharField(max_length=11, unique=True) 
    rg = models.CharField(max_length=11)
    tipo_usuario = models.CharField(max_length=12, choices=USER_TYPE_CHOICES)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.tipo_usuario} - NUSP: {self.nusp}"