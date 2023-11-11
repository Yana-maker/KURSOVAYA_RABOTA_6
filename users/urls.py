from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from users.apps import UserConfig
from users.views import RegisterView, ProfileView, generate_new_password, pass_verification

app_name = UserConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('register/', RegisterView.as_view(template_name='users/register.html'), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/genpassword', generate_new_password, name='genpassword'),
    path('profile/verification', pass_verification, name='verification')
]
