
from .models import Profile
from django.db.models import Q 
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'home.html')


############################################################################# CADASTRO
def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            if request.POST['email'] == request.POST['email_confirmation']:
                try:
                    email = request.POST['email']
                    username = email.split('@')[0]
                    nusp = request.POST['nusp']
                    rg = request.POST['rg']
                    tipo_usuario = request.POST.get('tipo_usuario')

                    if not nusp.isdigit():
                        return render(request, 'signup.html', {
                            'form': UserCreationForm,
                            'error': 'NUSP deve conter apenas dígitos!'
                        })
                    
                    if not rg.isdigit():
                        return render(request, 'signup.html', {
                            'form': UserCreationForm,
                            'error': 'RG deve conter apenas dígitos!'
                        })

                    if len(rg) > 11 or len(nusp) > 11:
                        return render(request, 'signup.html', {
                            'form': UserCreationForm,
                            'error': 'RG e NUSP não podem ter mais de 11 dígitos!'
                        })

                    #Se for aluno, is_active recebe True
                    is_active = tipo_usuario == 'aluno'

                    user = User.objects.create_user(
                        username=username,
                        password=request.POST['password1'],
                        first_name=request.POST['first_name'],
                        last_name=request.POST['last_name'],
                        email=email,
                        is_active=is_active
                    )

                    profile = Profile.objects.create(
                        user=user,
                        nusp=nusp,
                        rg=rg,
                        tipo_usuario=tipo_usuario
                    )

                    user.save()
                    profile.save()

                    message = 'Usuário criado com sucesso!'
                    if not is_active:
                        message += ' Orientadores e Coordenadores devem aguardar aprovação do administrador antes de efetuar login.'

                    return render(request, 'signin.html', {
                        'user_created': message
                    })

                except ValueError:
                    return render(request, 'signup.html', {
                        'form': UserCreationForm,
                        'error': 'NUSP e RG devem ser valores válidos!'
                    })
                except Exception as e:
                    return render(request, 'signup.html', {
                        'form': UserCreationForm,
                        'error': f'Erro: {str(e)}'
                    })
            else:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'Os e-mails não correspondem!'
                })

        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'Senhas divergentes!'
        })


######################################################################### LOGIN
def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user_input = request.POST['username']
        password = request.POST['password']

        try:
            user = authenticate(request, 
                                username=Profile.objects.get(Q(user__username=user_input) | Q(user__email=user_input) | Q(nusp=user_input)).user.username,
                                password=password)

            if user is None:
                return render(request, 'signin.html', {
                    'form': AuthenticationForm,
                    'error': 'Usuário e/ou senha incorreto(s)'
                })

            login(request, user)

            profile = Profile.objects.get(user=user)
            if profile.tipo_usuario == 'aluno':
                return redirect('aluno')
            elif profile.tipo_usuario == 'coordenador':
                return redirect('coordenador')
            elif profile.tipo_usuario == 'orientador':
                return redirect('orientador')

        except Profile.DoesNotExist:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Usuário não encontrado!'
            })
        
@login_required
def aluno(request):
    return render(request, 'aluno.html')

@login_required
def orientador(request):
    return render(request, 'orientador.html')

@login_required
def coordenador(request):
    return render(request, 'coordenador.html')


@login_required
def sair(request):
    logout(request)
    return redirect('home')