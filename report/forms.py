from django import forms
from .models import Profile

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
