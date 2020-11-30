from django import forms
from .models import Tutor

class TutorForm(forms.ModelForm):
    class Meta:
        model = Tutor
        fields = ['rate','calendly','phone_number','why_GT','what_fav','best_spot','any_interesting', 'classes']
