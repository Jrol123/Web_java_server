from django.test import TestCase
from .models import UserInfo
from .forms import RegistrationForm


class MyTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        UserInfo.objects.create(town='<TownName>', phone_number='89149755555')

    def test_town_label(self):
        user_info = UserInfo.objects.get(id=1)
        field_label = user_info._meta.get_field('town').verbose_name
        self.assertEquals(field_label, 'town')

    def test_phone_number_label(self):
        user_info = UserInfo.objects.get(id=1)
        phone_number = user_info._meta.get_field('phone_number').verbose_name
        self.assertEquals(phone_number, 'phone number')

    def test_town_length(self):
        user_info = UserInfo.objects.get(id=1)
        max_length = user_info._meta.get_field('town').max_length
        self.assertEquals(max_length, 50)

    def test_phone_number_length(self):
        user_info = UserInfo.objects.get(id=1)
        max_length = user_info._meta.get_field('phone_number').max_length
        self.assertEquals(max_length, 10)


class CreateUserFormTest(TestCase):

    # def test_form_username_label(self):
    #     form = RegistrationForm()
    #     self.assertTrue(form.fields['username'].label is None or form.fields['username'].label == 'username')

    def test_password(self):
        form_data = {'username': 'my_username',
                     'password': '123',
                     'password_repeat': '321',
                     'first_name': 'Name',
                     'last_name': 'Surname',
                     'patronymic': 'Patronymic',
                     'town': 'Town',
                     'phone': '89145555555',
                     'mail': 'grom-06@bk.ru',
                     'role_name': 'fnd'}
        form = RegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_mail(self):
        form_data = {'username': 'my_username',
                     'password': '123',
                     'password_repeat': '123',
                     'first_name': 'Name',
                     'last_name': 'Surname',
                     'patronymic': 'Patronymic',
                     'town': 'Town',
                     'phone': '89145555555',
                     'mail': 'some_text',
                     'role_name': 'fnd'}
        form = RegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_mail_is_not_null(self):
        form_data = {'username': 'my_username',
                     'password': '123',
                     'password_repeat': '123',
                     'first_name': 'Name',
                     'last_name': 'Surname',
                     'patronymic': 'Patronymic',
                     'town': 'Town',
                     'phone': '89145555555',
                     'mail': None,
                     'role_name': 'fnd'}
        form = RegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_username_is_not_null(self):
        form_data = {'username': None,
                     'password': '123',
                     'password_repeat': '123',
                     'first_name': 'Name',
                     'last_name': 'Surname',
                     'patronymic': 'Patronymic',
                     'town': 'Town',
                     'phone': '89145555555',
                     'mail': 'grom-06@bk.ru',
                     'role_name': 'fnd'}
        form = RegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_patronymic_is_not_null(self):
        form_data = {'username': 'my_username',
                     'password': '123',
                     'password_repeat': '123',
                     'first_name': 'Name',
                     'last_name': 'Surname',
                     'patronymic': None,
                     'town': 'Town',
                     'phone': '89145555555',
                     'mail': 'grom-06@bk.ru',
                     'role_name': 'fnd'}
        form = RegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())
