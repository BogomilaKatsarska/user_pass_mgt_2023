from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import generic as views
from django.contrib.auth.models import mixins as auth_mixins


class UsersListView(auth_mixins.LoginRequiredMixin, views.ListView):
    model = User
    template_name = 'web/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['has_email'] = self.request.user.has_email
        return context