from django import forms
from rest_framework.exceptions import NotFound

from service_objects.services import Service

from db.models import User


class UserUpdateService(Service):
    id = forms.IntegerField()
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    email = forms.EmailField(required=False)
    phone_number = forms.CharField(required=False)
    username = forms.CharField(required=False)

    def process(self):
        return self.update_user()

    def update_user(self):
        user = self.get_user()
        user.first_name = self.cleaned_data.get('first_name') if self.cleaned_data.get(
            'first_name') else user.first_name
        user.last_name = self.cleaned_data['last_name'] if self.cleaned_data['last_name'] else user.last_name
        user.email = self.cleaned_data['email'] if self.cleaned_data['email'] else user.email
        user.phone_number = self.cleaned_data['phone_number'] if self.cleaned_data[
            'phone_number'] else user.phone_number
        user.username = self.cleaned_data['username'] if self.cleaned_data['username'] else user.username
        user.save()
        return user

    def get_user(self):
        users = User.objects.filter(id=self.cleaned_data['id'])
        if not users.exists():
            raise NotFound('Позьзователь не найден')
        return users.first()
