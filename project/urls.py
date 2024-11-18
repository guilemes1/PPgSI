"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from report.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),

    path('signup/', signup, name='signup'),
    path('complete_profile/', complete_profile, name='complete_profile'),
    path('signin/', signin, name='signin'),
    path('sair/', sair, name='sair'),

    path('user_area/', user_area, name='user_area'),
    path('aluno/', aluno, name='aluno'),
    path('orientador/', orientador, name='orientador'),
    path('coordenador/', coordenador, name='coordenador'),

    path('create_report/', create_report, name='create_report'),


    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
