from service_objects.services import Service
from django import forms
from django.shortcuts import get_object_or_404
from db.models import User


class UserServices(Service):
    user_id = forms.IntegerField(required=True)

    def process(self):
        return get_object_or_404(User, id=self.cleaned_data['user_id'])


