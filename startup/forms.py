from django import forms
from .models import Startup
class StartupForm(forms.ModelForm):
    class Meta:
        model = Startup
        fields = ['startup_name', 'startup_product', 'startup_date', 'startup_sector', 'startup_team_size',
        'startup_desc', 'startup_team_condition', 'startup_team'
        ]
