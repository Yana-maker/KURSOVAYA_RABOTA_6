import secrets
from random import random

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView
from django.core.mail import send_mail, EmailMessage
from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


# Create your views here.
class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    extra_context = {
        'title': 'РЕГИСТРАЦИЯ'
    }
    success_url = reverse_lazy('users:verification')

    def form_valid(self, form):
        new_user = form.save()
        verification_code = secrets.token_hex(nbytes=5)
        new_user.code = verification_code
        new_user.save()
        send_mail(
            subject="Регистрация на сайте ",
            message=f'Поздравляем с успешной регистрацией , код для подтверждения {verification_code}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email],
        )
        return super().form_valid(form)

@login_required
def pass_verification(request):


    if request.method == 'POST':
        user_code = request.POST.get('code')
        user = User.objects.get(code=user_code)


        if user.code == user_code:
            user.is_active = True
            user.save()
            return redirect(reverse('users:login'))

    else:
        return render(request, 'users/verification_form.html')



class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    extra_context = {
        'title': 'РЕДАКТИРОВАНИЕ ПРОФИЛЯ'
    }
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user

@login_required
def generate_new_password(request):
    extra_context = {
        'title': 'ГЕНЕРАЦИЯ ПАРОЛЯ'
    }
    new_password = secrets.token_hex(nbytes=10)
    send_mail(
        "Вы сменили пароль",
        f'ваш новый пароль {new_password}',
        settings.EMAIL_HOST_USER,
        [request.user.email]
    )
    request.user.set_password(new_password)
    request.user.save()
    return redirect(reverse('catalog:home'))
