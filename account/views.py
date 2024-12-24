from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .forms import LoginForm, RegistrationForm
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Перенаправляем пользователя на нужную страницу
                return redirect('index')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Создаем нового пользователя
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
                email=form.cleaned_data['email'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name']
            )
            user.save()
            # Сохраняем нового пользователя
            messages.success(request, _('Your account has been created: you can log in to the site.'))
            return redirect('login')  # Перенаправляем на login после успешной регистрации
    else:
        form = RegistrationForm()
    
    return render(request, 'register.html', {'form': form})