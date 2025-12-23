from django import forms

class CalculatorForm(forms.Form):
    number1 = forms.FloatField(label='', widget=forms.NumberInput(attrs={'placeholder': 'Number 1', 'class': 'input'}))
    number2 = forms.FloatField(label='', widget=forms.NumberInput(attrs={'placeholder': 'Number 2', 'class': 'input'}))
    operation = forms.ChoiceField(choices=[
        ('add', '+'),
        ('subtract', '-'),
        ('multiply', '*'),
        ('divide', '/')
    ], widget=forms.Select(attrs={'class': 'select'}))
