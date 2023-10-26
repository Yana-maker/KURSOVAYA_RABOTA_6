from random import random

from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView
from django.core.mail import send_mail
from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


# Create your views here.
class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:verification')

    def form_valid(self, form):
        new_user = form.save()
        verification_code = ''.join([str(random.randint(0, 5) for i in range(12))])
        form.verification_code = verification_code
        form.save()
        send_mail(
            "Регисттрация на сайте ",
            'поздравляем с успешной регистрацией',
            settings.EMAIL_HOST_USER,
            [new_user.email],
            True,
            f'ваш код для подтверждения почты - {verification_code}'
        )

        return super().form_valid(form)


def verification_check(self, request):
    request.method = 'POST'
    user_input = request.POST.get('user_input')
    if user_input == request.user.verification_code:
        request.user.is_active = True
    else:
        return "неверный код подтверждения"


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


def generate_new_password(request):
    new_password = ''.join([str(random.randint(0, 9) for i in range(12))])
    send_mail(
        "Вы сменили пароль",
        f'ваш новый пароль {new_password}',
        settings.EMAIL_HOST_USER,
        [request.user.email]
    )
    request.user.set_password(new_password)
    request.user.save()
    return redirect(reverse('catalog:home'))
