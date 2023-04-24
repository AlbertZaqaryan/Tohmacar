from django import forms
from .models import Parent, Child1, Child2, Child3


class ParentForm(forms.ModelForm):
    class Meta:
        model = Parent
        fields = ['name',]

class Child1Form(forms.ModelForm):
    class Meta:
        model = Child1
        fields = ['parent', 'name']


class Child2Form(forms.ModelForm):
    class Meta:
        model = Child2
        fields = ['parent', 'name']

class Child3Form(forms.ModelForm):
    class Meta:
        model = Child3
        fields = ['parent', 'name']