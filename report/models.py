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
    passed_courses = models.TextField(blank=True, default='')
    failed_courses = models.TextField(blank=True, default='')

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.tipo_usuario} - NUSP: {self.nusp}"
    
    def get_passed_courses(self):
        return self.passed_courses.split(',') if self.passed_courses else []
    
    def set_passed_courses(self, passed_courses_list):
        self.passed_courses = ','.join(passed_courses_list)

    def get_failed_courses(self):
        return self.failed_courses.split(',') if self.failed_courses else []

    def set_failed_courses(self, failed_courses_list):
        self.failed_courses = ','.join(failed_courses_list)


class Disciplina(models.Model):
    responsavel = models.ForeignKey(Profile, on_delete=models.PROTECT)
    codigo = models.CharField(max_length=7, unique=True)
    nome = models.CharField(max_length=255)
    creditos = models.CharField(max_length=10)
    carga_horaria_semanal = models.CharField(max_length=50)
    

    def __str__(self):
        return self.nome
    
class Relatorio(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('avaliado_orientador', 'Avaliado pelo Orientador'),
        ('avaliado_coordenador', 'Avaliado pelo Coordenador'),
    ]

    AVALIACAO_ULTIMO_RELATORIO = [
        ('Aprovado', 'Aprovado'),
        ('Aprovado com ressalvas', 'Aprovado com ressalvas'),
        ('Insatisfatório', 'Insatisfatório'),
        ('Não se aplica (é o primeiro relatório)', 'Não se aplica (é o primeiro relatório)'),
    ]

    OPCOES_APROVACOES_REPROVACOES_ARTIGOS = [
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4 ou mais', '4 ou mais'),
    ]

    OPCOES_EXAMES = [
        ('Sim. Fui aprovado', 'Sim. Fui aprovado'),
        ('Sim. Fui reprovado', 'Sim. Fui reprovado'),
        ('Não', 'Não'),
    ]

    OPCOES_APOIO = [
        ('Sim', 'Sim'),
        ('Não', 'Não'),
    ]

    # Dados do aluno
    email = models.CharField(max_length=50)
    nome_aluno = models.CharField(max_length=250)
    nome_orientador = models.CharField(max_length=250)
    nusp = models.CharField(max_length=11)
    lattes = models.URLField()
    data_atualizacao_lattes = models.DateField()
    curso = models.CharField(max_length=9)
    data_matricula = models.DateField()

    # Orientador relacionado
    orientador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='relatorios_orientador')

    # Avaliações
    avaliacao_ultimo_relatorio = models.CharField(max_length=38, choices=AVALIACAO_ULTIMO_RELATORIO)
    aporvacoes_inicio_curso = models.CharField(max_length=9, choices=OPCOES_APROVACOES_REPROVACOES_ARTIGOS)
    reprovacoes_semestre_anterior = models.CharField(max_length=9, choices=OPCOES_APROVACOES_REPROVACOES_ARTIGOS)
    reprovacoes_inicio_curso = models.CharField(max_length=9, choices=OPCOES_APROVACOES_REPROVACOES_ARTIGOS)
    realizacao_exame_idiomas = models.CharField(max_length=18, choices=OPCOES_EXAMES)
    realizacao_exame_qualificacao = models.CharField(max_length=18, choices=OPCOES_EXAMES)
    prazo_qualificacao = models.DateField(blank=True, null=True)
    prazo_dissertacao = models.DateField()
    artigos_em_escrita = models.CharField(max_length=9, choices=OPCOES_APROVACOES_REPROVACOES_ARTIGOS)
    artigos_em_avaliacao = models.CharField(max_length=9, choices=OPCOES_APROVACOES_REPROVACOES_ARTIGOS)
    artigos_publicados = models.CharField(max_length=9, choices=OPCOES_APROVACOES_REPROVACOES_ARTIGOS)

    # Atividades e outras atualizações
    atividades_academicas_semestre_atual = models.TextField()
    atividades_pesquisa = models.TextField()
    declaracao_adicional = models.TextField(blank=True, null=True)
    precisa_apoio = models.CharField(max_length=3, choices=OPCOES_APOIO)

    # Pareceres e status
    data_criacao = models.DateField()

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    parecer_orientador = models.CharField(max_length=22, blank=True, null=True)
    conceito_orientador = models.CharField(
        max_length=22,
        choices=[
            ('adequado', 'Adequado'),
            ('adequado_com_ressalvas', 'Adequado com Ressalvas'),
            ('insatisfatorio', 'Insatisfatório'),
        ],
        blank=True,
        null=True,
    )

    parecer_coordenador = models.CharField(max_length=22, blank=True, null=True)
    conceito_coordenador = models.CharField(
        max_length=22,
        choices=[
            ('adequado', 'Adequado'),
            ('adequado_com_ressalvas', 'Adequado com Ressalvas'),
            ('insatisfatorio', 'Insatisfatório'),
        ],
        blank=True,
        null=True,
    )

    primeira_avaliacao = models.BooleanField(default=True)                          #mudar apos parecer do coordenador
    segunda_avaliacao = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nusp}; Orientador: {self.nome_orientador}; Data de criação: {self.data_criacao}"
