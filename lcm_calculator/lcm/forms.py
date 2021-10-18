from django import forms

class lcm_form(forms.Form):
    num1 = forms.IntegerField(label="Number 1")
    num2 = forms.IntegerField(label="Number 2")