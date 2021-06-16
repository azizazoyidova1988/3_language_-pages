from django import forms
from .models import Subscribers


class SubscribersForm(forms.ModelForm):
    class Meta:
        model = Subscribers
        fields = "__all__"
        labels={
            "name":"Enter name"
        }