from django import forms
from .models import Solution

class SolutionForm(forms.ModelForm):
    class Meta:
        model = Solution
        fields = ['code']
        widgets = {
            'code': forms.Textarea(attrs={'rows': 10, 'cols': 80}),
        }
