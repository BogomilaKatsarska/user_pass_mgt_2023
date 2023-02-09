from django.contrib.auth.models import User
from django.db import models


'''
It is used to change the behaviour of an existing model
without affecting the existing DB schema
'''


class AppUser(User):
    class Meta:
        proxy = True
        ordering = ('first_name', 'last_name')

    def some_behaviour(self):
        pass

    def has_email(self):
        return self.email is not None