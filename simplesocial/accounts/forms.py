from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm      # built in user creation form to authorization package


class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ("username", "email", "password1", "password2")
        model = get_user_model()            # returns the User model that is active in this point

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Display name"
        self.fields["email"].label = "Email address"