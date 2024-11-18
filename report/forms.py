from django import forms
from .models import Profile, Relatorio

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'image', 'birth_date', 'country', 'state', 'city', 
            'nationality', 'course', 'advisor', 'lattes', 'enrollment_date', 
            'exam_date', 'language_exam_date'
        ]
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
            'enrollment_date': forms.DateInput(attrs={'type': 'date'}),
            'exam_date': forms.DateInput(attrs={'type': 'date'}),
            'language_exam_date': forms.DateInput(attrs={'type': 'date'}),
        }

class RelatorioForm(forms.ModelForm):
    class Meta:
        model = Relatorio
        fields = [
            'data_atualizacao_lattes',
            'avaliacao_ultimo_relatorio',
            'aporvacoes_inicio_curso',
            'reprovacoes_semestre_anterior',
            'reprovacoes_inicio_curso',
            'realizacao_exame_idiomas',
            'realizacao_exame_qualificacao',
            'prazo_qualificacao',
            'prazo_dissertacao',
            'artigos_em_escrita',
            'artigos_em_avaliacao',
            'artigos_publicados',
            'atividades_academicas_semestre_atual',
            'atividades_pesquisa',
            'declaracao_adicional',
            'precisa_apoio',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})