from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import forms as auth_forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User
from django.shortcuts import render


class SignUpForm(auth_forms.UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username',)
        field_classes = {"username": auth_forms.UsernameField}

    # def save(self, commit=True):
    #     user = super().save(commit=commit)
    #     user.username = user.first_name + '-' + user.last_name
    #
    #     if commit:
    #         user.save()
    #     return user


class SignUpView(views.CreateView):
    template_name = 'auth/sign-up.html'
    form_class = SignUpForm
    success_url = reverse_lazy('sign up')


