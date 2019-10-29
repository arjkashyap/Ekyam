from django import forms
from .models import Question
class StartupForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['problem_title', 'problem_category', 'problem_description', 'problem_field'
        ]
