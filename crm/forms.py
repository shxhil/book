from django import forms
from crm.models import Book
from django.contrib.auth.models import User



class BookModelForm(forms.ModelForm):
    class Meta:
        model=Book

        fields="__all__"

        widgets={
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "author":forms.TextInput(attrs={"class":"form-control"}),
            "price":forms.NumberInput(attrs={"class":"form-control"}),
            "publishdate":forms.NumberInput(attrs={"class":"form-control"}),
            "genre":forms.TextInput(attrs={"class":"form-control"}),
            "publisher":forms.TextInput(attrs={"class":"form-control"}),
            "about":forms.Textarea(attrs={"class":"form-control","rows":5}),
        }


class RegistrationForm(forms.ModelForm):
    class Meta:
        model=User

        fields=["username","password","email"]

        widgets={
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "password":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.TextInput(attrs={"class":"form-control"}),
        }

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))