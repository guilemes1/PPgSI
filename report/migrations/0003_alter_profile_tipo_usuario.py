# Generated by Django 5.1.2 on 2024-10-31 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0002_alter_profile_nusp_alter_profile_rg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='tipo_usuario',
            field=models.CharField(choices=[('Aluno', 'Aluno'), ('Coordenador', 'Coordenador'), ('Orientador', 'Orientador')], max_length=12),
        ),
    ]
