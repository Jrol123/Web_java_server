import os
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json
from django.views import View
from django.contrib.auth.decorators import login_required
from WebDjango.apps.account.models import (UserInfo, Animals, Roles)
from WebDjango.apps.account.forms import (LoginForm, RegistrationForm)


def index(request):
    return render(request, 'index.html')


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')

    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {'form': form})


def user_registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(username=cd['username'],
                                            password=cd['password'],
                                            first_name=cd['first_name'],
                                            last_name=cd['last_name'])
            login(request, user)
            role = Roles.objects.get(role_name=cd['role_name'])
            info = UserInfo(user_id=user.id, role_id=role.id,
                            town=cd['town'],
                            phone_number=cd['phone'],
                            patronymic=cd['patronymic'])
            info.save()
            animals = cd['favourite_animals']
            for animal_name in animals:
                info.favourite_animals.add(Animals.objects.get(animal_name=animal_name))
            return render(request, 'registration/congrats.html', {'first': cd['first_name'],
                                                                  'second': cd['last_name'],
                                                                  'third': cd['patronymic'],
                                                                  'town': cd['town'],
                                                                  'phone': cd['phone']})

        else:
            return render(request, 'registration/create_new.html', {'form': form, "first": 0})
    else:
        form = RegistrationForm()

        return render(request, 'registration/create_new.html', {'form': form, "first": 1})


# def news(request):
#     return render(request, 'addition/news.html')
