from django.db import models
from django.contrib.auth.models import User

#Atributos do User padrão
##username: Um campo obrigatório que identifica o usuário de forma única. É utilizado para login.
##first_name: O primeiro nome do usuário, opcional.
##last_name: O sobrenome do usuário, opcional.
##email: O email do usuário, opcional, mas pode ser configurado como obrigatório para cadastro.
##password: A senha do usuário, armazenada de forma criptografada.
##is_staff: Um campo booleano que indica se o usuário pode acessar o painel de administração (True) ou não (False).
##is_active: Um campo booleano que indica se o usuário está ativo. Usuários inativos não podem fazer login.
##is_superuser: Um campo booleano que indica se o usuário tem todas as permissões (True) ou não (False).
##last_login: A data e hora do último login.
##date_joined: A data e hora em que o usuário foi criado/cadastrado

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