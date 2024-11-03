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
    image = models.ImageField(upload_to='images/users', default='images/users/default.png')
    birth_date = models.DateField(blank=True, null=True)
    country = models.CharField(max_length=32, blank=True)
    state = models.CharField(max_length=32, blank=True)
    city = models.CharField(max_length=32, blank=True)
    nationality = models.CharField(max_length=32, blank=True)
    course = models.CharField(max_length=250, blank=True)
    advisor = models.CharField(max_length=50, blank=True)
    lattes = models.URLField(blank=True)
    enrollment_date = models.DateField(blank=True, null=True)
    exam_date = models.DateField(blank=True, null=True)
    language_exam_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.tipo_usuario} - NUSP: {self.nusp}"