from django.db import models

# Create your models here.
from django.conf import settings
from django.urls import reverse
from django.db import models
from django.utils.text import slugify           # (slugify allows us to remove any character that aren't alphanumerics or underscores or hyphens; and  basically the idea behind that is if you have a string that has spaces in it and you want to use that as part of the URL, its going to be able to lowercase and add dashes instead of spaces )

# from accounts.models import User

import misaka                       # misaka allows us to actually to do link and bedding; in Reddit commenting system you can actually put links or a little bit of markdown text and thats what misaka actually does, "pip install misaka"

from django.contrib.auth import get_user_model       # returns the user model thats currently active in this project
User = get_user_model()                             # call things of the current user




# https://docs.djangoproject.com/en/1.11/howto/custom-template-tags/#inclusion-tags
# This is for the in_group_members check template tag


from django import template
register = template.Library()



class Group(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)             # A slug is a short label for something, containing only letters, numbers, underscores or hyphens. They’re generally used in URLs; "SlugField.allow_unicode" If True, the field accepts Unicode letters in addition to ASCII letters. Defaults to False; link : "https://docs.djangoproject.com/en/4.0/ref/models/fields/"
    description = models.TextField(blank=True, default='')
    description_html = models.TextField(editable=False, default='', blank=True)          # editable = False because we are going to grab that directly from description
    members = models.ManyToManyField(User,through="GroupMember")                        # all members that belong to a particular group

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)            # saving description in description_html field
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("groups:single", kwargs={"slug": self.slug})


    class Meta:
        ordering = ["name"]


class GroupMember(models.Model):
    group = models.ForeignKey(Group, related_name="memberships",on_delete=models.CASCADE)            # a group member can have a membership to a Group
    user = models.ForeignKey(User,related_name='user_groups',on_delete=models.CASCADE)                # a user can belong to multiple groups

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ("group", "user")