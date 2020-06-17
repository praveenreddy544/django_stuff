from django import forms
from tolist_app.models import Tasklist

class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasklist
        fields = ['task','done']