## Sobre
Projeto em desenvolvimento para a disciplina de Engenharia de Sistemas de Informação. 
Consiste em uma aplicação web para criação e avaliação de relatórios do Programa de Pós Graduação em Sistemas de Informação.
As principais tecnologias utilizadas são os frameworks Django (5.1.2) e Bootstrap (5.3.3).

## Execução em Linux
- Faca download e extracao dos arquivos
- Acesse a pasta pelo terminal e execute os seguintes comandos:
     - python3 -m venv .venv
     - source .venv/bin/activate
     - pip install -r requirements.txt
     - python3 manage.py makemigrations
     - python3 manage.py migrate
     - python3 manage.py createsuperuser
     - python3 manage.py shell
     - from report.scripts.popular_models import criar_orientadores, criar_coordenadores, popular_disciplinas
     - quit()
     - python3 manage.py runserver
- No navegador, acesse o endereço http://127.0.0.1:8000/
- Ao terminar de utilizar, aperte Ctrl + C no terminal e execute o comando deactivate

## Execução em Windows
- Necessário ter o python instalado (https://www.python.org/downloads/windows/)
- Faca download e extração dos arquivos deste repositório
- Acesse a pasta pelo terminal e execute os seguintes comandos:
	- python -m venv venv
	- .\venv\bin\activate
	- pip install -r requirements.txt
	- python manage.py makemigrations
	- python manage.py migrate
	- python manage.py createsuperuser
	- python manage.py shell
	- from report.scripts.popular_models import criar_orientadores, criar_coordenadores, popular_disciplinas
	- quit()
	- python manage.py runserver
- No navegador, acesse o endereço http://127.0.0.1:8000/
- Ao terminar de utilizar, aperte Ctrl + C no terminal e execute o comando deactivate




*Note que, ao extrair, pode ser que duas pastas com o mesmo nome sejam criadas. O caminho correto onde os comandos devem ser executados seria algo como C:\Users\nome\Downloads\PPgSI-main\PPgSI-main
