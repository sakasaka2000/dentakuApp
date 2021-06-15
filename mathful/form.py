from django import forms

class numForm(forms.Form):
  num1 = forms.DecimalField(label='変数１', initial=2, required=True)
  num2 = forms.DecimalField(label='変数２', initial=1, required=True)
  