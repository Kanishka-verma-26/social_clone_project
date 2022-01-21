from django.urls import path
from django.contrib.auth import views as auth_views         #( django1.11 introduced a LoginView and LogoutView so we actually dont have to take care of those in our views.py file anymore; previously we have to create a LoginView and LogoutView in our views.py file but now its taken care for us and now its located inside "django.contrib.auth" views )
from . import views

app_name = 'accounts'

# define LOGIN_REDIRECT_URL and  LOGOUT_REDIRECT_URL in settings.py

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(template_name="accounts/login.html"),name='login'),         # for LoginView we have to connect it to your template name
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),                                        # for LogoutView we have a default view that we can use, it will essentially take back to our homepage
    path("signup/", views.SignUp.as_view(), name="signup"),
]