from rest_framework import serializers

from db.models import User


class UserDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'username',
        )
