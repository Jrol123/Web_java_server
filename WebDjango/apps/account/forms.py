from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import re


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Имя пользователя",
        'required': "",
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'id': "myInput",
        'placeholder': "пароль",
        'required': "",
    }))

    def clean_password(self):
        cd = self.cleaned_data
        user = authenticate(username=cd['username'], password=cd['password'])
        if user is None:
            raise ValidationError('')
        return cd['password']

    def clean_username(self):
        cd = self.cleaned_data
        return cd['username']


class RegistrationForm(forms.Form):
    username = forms.CharField(help_text="Введите имя аккаунта", required=True,
                               label='Имя пользователя',
                               widget=forms.TextInput(
                                   attrs={
                                       'class': "form-control",
                                       'placeholder': ""
                                   }
                               ))
    password = forms.CharField(help_text="Введите пароль", required=True,
                               label='Пароль',
                               widget=forms.PasswordInput(
                                   attrs={
                                       'class': "form-control",
                                       'placeholder': ""
                                   }
                               ))
    password_repeat = forms.CharField(help_text="Введите пароль еще раз", required=True,
                                      label='Повторите пароль',
                                      widget=forms.PasswordInput(
                                          attrs={
                                              'class': "form-control",
                                              'placeholder': ""
                                          }
                                      ))
    first_name = forms.CharField(help_text="Введите имя", required=True,
                                 label='Имя',
                                 widget=forms.TextInput(
                                     attrs={
                                         'class': "form-control",
                                         'placeholder': ""
                                     }
                                 ))
    last_name = forms.CharField(help_text="Введите фамилию", required=True,
                                label='Фамилия',
                                widget=forms.TextInput(
                                    attrs={
                                        'class': "form-control",
                                        'placeholder': ""
                                    }
                                ))
    patronymic = forms.CharField(help_text="Введите отчество", required=True,
                                 label='Отчество',
                                 widget=forms.TextInput(
                                     attrs={
                                         'class': "form-control",
                                         'placeholder': ""
                                     }
                                 ))
    mail = forms.EmailField(help_text="Введите почту", required=True,
                            label='Почта',
                            widget=forms.TextInput(
                                attrs={
                                    'class': "form-control",
                                    'placeholder': ""
                                }
                            ))
    town = forms.CharField(help_text="Из какого вы города?", required=True,
                           label='Ваш город',
                           widget=forms.TextInput(
                               attrs={
                                   'class': "form-control",
                                   'placeholder': ""
                               }
                           ))
    phone = forms.CharField(help_text="Введите номер телефона", required=True,
                            label='Номер телефона',
                            widget=forms.TextInput(
                                attrs={
                                    'class': "form-control",
                                    'placeholder': ""
                                }
                            ))
    role_name = forms.ChoiceField(help_text="Выберите вашу роль", required=True,
                                  label='Ваша роль',
                                  choices=[
                                      ('adm', 'Администратор'),
                                      ('fnd', 'Соискатель'),
                                      ('prd', 'Представитель'),
                                  ],
                                  widget=forms.Select(
                                      attrs={
                                          'class': "form-control"
                                      }
                                  ))

    favourite_animals = forms.MultipleChoiceField(
        label='Выберите любимых животных',
        required=False,
        widget=forms.CheckboxSelectMultiple(attrs={}),
        choices=[
            ('jag', 'Ягуар'), ('cai', 'Кайман'), ('spd', 'Коричневый паук')
        ]
    )

    def clean_user_name(self):
        name = self.cleaned_data['username']

        name_list = User.objects.values('username')  # список свойств в формате:
        # [{'username': 'MyUsername1'}, {'username': 'MyUsername2'}, ...]
        for val in name_list:
            if name == val['username']:
                raise ValidationError('Такой username уже существует')

        return name

    def clean_password(self):
        password = self.cleaned_data['password']

        return password

    def clean_password_repeat(self):
        password = self.cleaned_data['password']
        password_rep = self.cleaned_data['password_repeat']

        if password_rep != password:
            raise ValidationError('Пароли должны совпадать')

        return password_rep

    @staticmethod
    def validate_phone_number(phone_number):
        pattern = r'^\+?\d+$'
        return re.match(pattern, phone_number)

    def clean_phone(self):
        phone = self.cleaned_data['phone']

        if not self.validate_phone_number(phone):
            raise ValidationError('Введите корректный номер')

        return phone
