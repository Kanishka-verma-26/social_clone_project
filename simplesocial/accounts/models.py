from django.db import models

# Create your models here.
from django.contrib import auth
from django.db import models
from django.utils import timezone


# we actually dont need to register the User model in admin.py bcoz we are using django built in User's model

class User(auth.models.User, auth.models.PermissionsMixin):         # API reference model "https://docs.djangoproject.com/en/4.0/ref/contrib/auth/"
    # we are using "auth.models.User" to automatically set up a form for someone to signup to become a user

    def __str__(self):
        return "@{}".format(self.username)