from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from user.serializers.users import UserDataSerializer
from user.services.get import UserServices


class GetUserView(APIView):

    def get(self, request, **kwargs):
        user = UserServices.execute({'user_id': kwargs.get('id')})
        serializer = UserDataSerializer(user).data
        return Response(serializer, status=status.HTTP_200_OK)
