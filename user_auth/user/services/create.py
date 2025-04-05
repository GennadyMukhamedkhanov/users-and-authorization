from django import forms
from rest_framework.exceptions import ParseError
from service_objects.services import Service
from django.db.models import Q

from db.models import User


class CreateUsersService(Service):
    phone_number = forms.CharField(required=True)
    email = forms.CharField(required=True, error_messages={'invalid': 'Введен неверный email'})
    password = forms.CharField(required=True)
    username = forms.CharField(required=True)

    def process(self):
        self.user_presence()
        self.create_user()
        return True

    def user_presence(self):
        users = User.objects.filter(
            Q(email=self.cleaned_data['email']) |
            Q(phone_number=self.cleaned_data['phone_number'])
        )
        if users.exists():
            raise ParseError(
                detail='Пользователь с такими данными уже существует.',
            )

    def create_user(self):
        User.objects.create_user(
            email=self.cleaned_data['email'],
            phone_number=self.cleaned_data['phone_number'],
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password']
        )

        return self
