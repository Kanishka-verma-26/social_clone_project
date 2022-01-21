from django.db import models

# Create your models here.
from django.conf import settings
from django.urls import reverse
from django.db import models

import misaka                    # misaka allows us to actually to do link and bedding; in Reddit commenting system you can actually put links or a little bit of markdown text and thats what misaka actually does, "pip install misaka"


from groups.models import  Group            # so we can connect a post to an actual group

from django.contrib.auth import get_user_model           # returns the user model thats currently active in this project
User = get_user_model()                                  # this will going to connect the current post to whoever is logged in as a user


class Post(models.Model):
    user = models.ForeignKey(User, related_name="posts",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)         # editable = False because we are going to grab that directly from message
    group = models.ForeignKey(Group, related_name="posts",null=True, blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.message

    def save(self, *args, **kwargs):
        self.message_html = misaka.html(self.message)           # saving message in message_html field
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("posts:single", kwargs={"username": self.user.username,
                "pk": self.pk})

    class Meta:
        ordering = ["-created_at"]              # through '-' sign, that way we see then in descending order so the most recent posts are at the top
        unique_together = ["user", "message"]