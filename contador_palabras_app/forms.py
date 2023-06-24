from django import forms

class InputForm(forms.Form):
    texto = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={'style': 'height: 100px; width: 200px;'}),
    )