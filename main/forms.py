from django import forms
from main.models import Members

class MembersForm (forms.ModelForm):
    class Meta:
        model = Members
        fields = "__all__"