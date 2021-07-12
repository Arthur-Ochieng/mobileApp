from django import forms
from main.models import Saving, Loaning, List

class SavingForm (forms.ModelForm):
    class Meta:
        model = Saving
        fields = "__all__"

class LoaningForm (forms.ModelForm):
    class Meta:
        model = Loaning
        fields = "__all__"

class ListForm (forms.ModelForm):
    class Meta:
        model = List
        fields = "__all__"