from django import forms
from .models import UserQuiz


class UserQuizForm(forms.ModelForm):
    class Meta:
        model = UserQuiz
        fields = ['answer']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance and instance.is_finished:
            for field_name in self.fields:
                self.fields[field_name].disabled = True