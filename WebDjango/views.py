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
from WebDjango.apps.account.models import (UserInfo, Animals, Roles, Subscribe, Quiz, Question)
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
            end_animals = []
            for animal_name in animals:
                animal_name_real = Animals.objects.get(animal_name=animal_name)
                info.favourite_animals.add(animal_name_real)
                end_animals.append(animal_name_real.real_name)
                print(animal_name_real.animal_name)
            return render(request, 'registration/congrats.html', {'first': cd['first_name'],
                                                                  'second': cd['last_name'],
                                                                  'third': cd['patronymic'],
                                                                  'town': cd['town'],
                                                                  'phone': cd['phone'],
                                                                  'animals': end_animals})

        else:
            return render(request, 'registration/create_new.html', {'form': form, "first": 0})
    else:
        form = RegistrationForm()

        return render(request, 'registration/create_new.html', {'form': form, "first": 1})


def excursions(request):
    return render(request, 'addition/Excursions.html')


def subscribtion(request):
    return render(request, 'addition/subscribtion.html')


@require_POST
@csrf_exempt
def save(request):
    text = request.POST.get('text')

    obj = Subscribe(mail=text)
    obj.save()

    response_data = {'message': 'Данные успешно обработаны'}
    return JsonResponse(response_data)


@login_required
def quiz(request):
    return render(request, 'addition/quiz.html')


@require_POST
@csrf_exempt
def save_quiz(request):
    obj = Quiz(who=request.POST.get('who'),
               how_know=request.POST.get('how_know'),
               form=request.POST.get('form'))
    obj.save()

    if request.POST.get('answ') != '':
        for my_id in request.POST.get('answ').split(','):
            obj.answer.add(Question.objects.get(id=int(my_id)))

    response_data = {'message': 'Данные успешно обработаны'}
    return JsonResponse(response_data)


def get_statistic(request):
    data = {}

    count_of_people = 0
    who = [
        [0, 0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    answers = [0, 0, 0, 0, 0, 0, 0]

    sub = {
        "Интересующийся": 0, "Студент географического факультета": 1, "Серёжа Глущенко": 2, "Учёный-географ": 3,
        "Преподаватель": 0, "Да": 1, "Артемий Громыко": 2,
        "Очень": 0, "Не совсем": 1, "Нет": 2
    }

    for obj in Quiz.objects.values():
        count_of_people += 1

        who[0][sub[obj['who']]] += 1
        who[1][sub[obj['how_know']]] += 1
        who[2][sub[obj['form']]] += 1

    for obj in Quiz.objects.all():
        for sub in obj.answer.values():
            answers[sub['id'] - 1] += 1

    ind = 0
    for i in range(3):
        if who[0][i] > who[0][ind]:
            ind = i

    tmp = {0: "интересующимися", 1: "студентами географического факультета", 2: "серёжей Глущенко",
           3: "учёными-географами"}

    data['who'] = tmp[ind]

    ind = 0
    for i in range(3):
        if who[1][i] > who[1][ind]:
            ind = i

    tmp = {0: "преподавателя", 1: "<ДАННЫЕ УДАЛЕНЫ>", 2: "Артемия Громыко"}

    data['how_know'] = tmp[ind]

    ind = 0
    for i in range(3):
        if who[2][i] > who[2][ind]:
            ind = i

    tmp = {0: "очень", 1: "не совсем", 2: "не"}

    data['form'] = tmp[ind]

    data['percent'] = [
        int(round(answers[0] / count_of_people * 100)),
        int(round(answers[1] / count_of_people * 100)),
        int(round(answers[2] / count_of_people * 100)),
        int(round(answers[3] / count_of_people * 100)),
        int(round(answers[4] / count_of_people * 100)),
        int(round(answers[5] / count_of_people * 100)),
        int(round(answers[6] / count_of_people * 100))
    ]

    return JsonResponse(data)
