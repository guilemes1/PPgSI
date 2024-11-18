import os
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from django.contrib.auth.models import User
from report.models import Disciplina, Profile

def criar_orientadores():
    orientadores = [
        {'username': 'orientador1', 'first_name': 'Orientador', 'last_name': '1', 'email': 'orientador1@usp.br', 'password': '1234', 'nusp': '00000000', 'tipo_usuario': 'orientador'},
        {'username': 'orientador2', 'first_name': 'Orientador', 'last_name': '2', 'email': 'orientador2@usp.br', 'password': '1234', 'nusp': '11111111', 'tipo_usuario': 'orientador'}
    ]
    
    for orientador in orientadores:
        user = User.objects.create_user(
            username=orientador['username'],
            first_name=orientador['first_name'],
            last_name=orientador['last_name'],
            email=orientador['email'],
            password=orientador['password']
        )
        
        profile = Profile.objects.create(
            user=user,
            nusp=orientador['nusp'],
            tipo_usuario=orientador['tipo_usuario']
        )

def criar_coordenadores():
    coordenadores = [
        {'username': 'coordenador1', 'first_name': 'Coordenador', 'last_name': '1', 'email': 'coordenador1@usp.br', 'password': '1234', 'nusp': '22222222', 'tipo_usuario': 'coordenador'},
        {'username': 'coordenador2', 'first_name': 'Coordenador', 'last_name': '2', 'email': 'coordenador2@usp.br', 'password': '1234', 'nusp': '33333333', 'tipo_usuario': 'coordenador'}
    ]
    
    for coordenador in coordenadores:
        user = User.objects.create_user(
            username=coordenador['username'],
            first_name=coordenador['first_name'],
            last_name=coordenador['last_name'],
            email=coordenador['email'],
            password=coordenador['password']
        )
        
        profile = Profile.objects.create(
            user=user,
            nusp=coordenador['nusp'],
            tipo_usuario=coordenador['tipo_usuario']
        )

def popular_disciplinas():
    disciplinas = [
        {'responsavel': '00000000', 'codigo': 'SIN5000', 'nome': 'Metodologia da Pesquisa em Sistemas de Informação', 'creditos': '8 créditos', 'carga_horaria_semanal': '4 horas-aula'},
        {'responsavel': '00000000', 'codigo': 'SIN5013', 'nome': 'Análise de Algoritmos e Estruturas de Dados', 'creditos': '8 créditos', 'carga_horaria_semanal': '4 horas-aula'},
        {'responsavel': '00000000', 'codigo': 'SIN5005', 'nome': 'Tópicos em Engenharia de Software', 'creditos': '8 créditos', 'carga_horaria_semanal': '4 horas-aula'},
        {'responsavel': '00000000', 'codigo': 'SIN5009', 'nome': 'Gestão de Processos de Negócio', 'creditos': '8 créditos', 'carga_horaria_semanal': '4 horas-aula'},
        {'responsavel': '00000000', 'codigo': 'SIN5010', 'nome': 'Gestão de Projetos em Computação', 'creditos': '8 créditos', 'carga_horaria_semanal': '4 horas-aula'},
        {'responsavel': '00000000', 'codigo': 'SIN5015', 'nome': 'Economia da Informação', 'creditos': '8 créditos', 'carga_horaria_semanal': '4 horas-aula'},
        {'responsavel': '00000000', 'codigo': 'SIN5019', 'nome': 'Laboratório de Inovação em Sistemas de Informação', 'creditos': '8 créditos', 'carga_horaria_semanal': '4 horas-aula'},
        {'responsavel': '00000000', 'codigo': 'SIN5022', 'nome': 'Teste de Software', 'creditos': '8 créditos', 'carga_horaria_semanal': '4 horas-aula'},
        {'responsavel': '00000000', 'codigo': 'SIN5025', 'nome': 'Mineração de Processos', 'creditos': '8 créditos', 'carga_horaria_semanal': '4 horas-aula'},
        {'responsavel': '00000000', 'codigo': 'SIN5027', 'nome': 'Sistemas de Informação para Ciberdemocracia', 'creditos': '8 créditos', 'carga_horaria_semanal': '4 horas-aula'},
        {'responsavel': '00000000', 'codigo': 'SIN5029', 'nome': 'Interação Humano-Computador', 'creditos': '8 créditos', 'carga_horaria_semanal': '4 horas-aula'},
        {'responsavel': '00000000', 'codigo': 'SIN5030', 'nome': 'Estudos Organizacionais em Mundos Virtuais/Metaverso', 'creditos': '8 créditos', 'carga_horaria_semanal': '4 horas-aula'},
        {'responsavel': '00000000', 'codigo': 'SIN5006', 'nome': 'Inteligência Computacional', 'creditos': '8 créditos', 'carga_horaria_semanal': '4 horas-aula'},
        {'responsavel': '00000000', 'codigo': 'SIN5007', 'nome': 'Reconhecimento de Padrões', 'creditos': '8 créditos', 'carga_horaria_semanal': '4 horas-aula'},
        {'responsavel': '00000000', 'codigo': 'SIN5008', 'nome': 'Estatística Computacional', 'creditos': '8 créditos', 'carga_horaria_semanal': '4 horas-aula'},
        {'responsavel': '00000000', 'codigo': 'SIN5014', 'nome': 'Fundamentos de Processamento Gráfico', 'creditos': '8 créditos', 'carga_horaria_semanal': '4 horas-aula'},
        {'responsavel': '00000000', 'codigo': 'SIN5016', 'nome': 'Aprendizado de Máquina', 'creditos': '8 créditos', 'carga_horaria_semanal': '4 horas-aula'},
        {'responsavel': '00000000', 'codigo': 'SIN5017', 'nome': 'Mineração de Dados', 'creditos': '8 créditos', 'carga_horaria_semanal': '4 horas-aula'},
        {'responsavel': '00000000', 'codigo': 'SIN5018', 'nome': 'Aprendizado Estatístico', 'creditos': '8 créditos', 'carga_horaria_semanal': '4 horas-aula'},
        {'responsavel': '00000000', 'codigo': 'SIN5021', 'nome': 'Planejamento Probabilístico e Aprendizado por Reforço', 'creditos': '8 créditos', 'carga_horaria_semanal': '4 horas-aula'},
        {'responsavel': '00000000', 'codigo': 'SIN5023', 'nome': 'Reconhecimento Sintático e Estrutural de Padrões', 'creditos': '8 créditos', 'carga_horaria_semanal': '4 horas-aula'},
        {'responsavel': '00000000', 'codigo': 'SIN5024', 'nome': 'Laboratório de Otimização Combinatória', 'creditos': '8 créditos', 'carga_horaria_semanal': '4 horas-aula'},
        {'responsavel': '00000000', 'codigo': 'SIN5025', 'nome': 'Mineração de Processos', 'creditos': '8 créditos', 'carga_horaria_semanal': '4 horas-aula'},
        {'responsavel': '00000000', 'codigo': 'SIN5026', 'nome': 'Introdução à Otimização Combinatória', 'creditos': '8 créditos', 'carga_horaria_semanal': '4 horas-aula'},
        {'responsavel': '00000000', 'codigo': 'SIN5028', 'nome': 'Análise de Redes Sociais', 'creditos': '8 créditos', 'carga_horaria_semanal': '4 horas-aula'},
        {'responsavel': '00000000', 'codigo': 'SIN5031', 'nome': 'Tópicos em Análise Computacional de Som e Música', 'creditos': '4 créditos', 'carga_horaria_semanal': '2 horas-aula'},
        {'responsavel': '00000000', 'codigo': 'SIN5032', 'nome': 'Experimentação em Aprendizado de Máquina Supervisionado', 'creditos': '8 créditos', 'carga_horaria_semanal': '4 horas-aula'},
        {'responsavel': '00000000', 'codigo': 'SIN5033', 'nome': 'Grafos de Conhecimento e Ontologias', 'creditos': '8 créditos', 'carga_horaria_semanal': '4 horas-aula'},
]
    for disc in disciplinas:
        responsavel = Profile.objects.get(nusp=disc['responsavel'])

        Disciplina.objects.get_or_create(
            responsavel=responsavel,
            codigo=disc['codigo'],
            nome=disc['nome'],
            creditos=disc['creditos'],
            carga_horaria_semanal=disc['carga_horaria_semanal']
        )

criar_orientadores()
criar_coordenadores()
popular_disciplinas()
