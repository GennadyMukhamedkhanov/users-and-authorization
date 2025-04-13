from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from user.serializers.users import UserDataSerializer
from user.services.list import UsersServices


class GetUsersView(APIView):

    def get(self, request, *args, **kwargs):
        users = UsersServices.execute({})
        serializer = UserDataSerializer(users, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)
