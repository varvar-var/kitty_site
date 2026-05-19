from django import forms
from . models import Volunteer


class VolunteerForms(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = ('name', 'email')
        labels = {'name' : 'Ваше имя',
                  'email' : 'Ваша почта'}
        help_texts = {'name' : 'Напишите ваше имя',
                      'email' : 'Напишите вашу почту'}

    def clean_text(self):
        data = self.cleaned_data['name']
        if data == '':
            raise forms.ValidationError('Имя не должно быть пустым')
        return data      