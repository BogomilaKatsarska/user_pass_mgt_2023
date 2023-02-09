from django import forms
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import forms as auth_forms, authenticate, login, views as auth_views
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User
from django.shortcuts import render
=

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

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result



class SignInForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


def sign_in(request):
    if request.method == 'GET':
        form = SignInForm()
    else:
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
    #       user = authenticate(request, **form.cleaned_data) <-- same as above
            print(user)

            if user:
                login(request, user)
    context = {
        'form': form,
    }

    return render(request, 'auth/sign-in.html', context)


class SignInView(auth_views.LoginView):
    template_name = 'auth/sign-in.html'
    success_url = reverse_lazy('index')

    def get_success_url(self):
        if self.success_url:
            return self.success_url

        return self.get_redirect_url() or self.get_default_redirect_url()



class SignOutView(auth_views.LogoutView):
    template_name = 'auth/sign-out.html'
