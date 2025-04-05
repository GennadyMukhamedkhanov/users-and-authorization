from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from user.serializers.users import UserDataSerializer
from user.services.create import CreateUsersService
from user.services.update import UserUpdateService


class GetCreateUpdateUserView(APIView):

    def get(self, request, *args, **kwargs):
        self.permission_classes = [IsAuthenticated, ]
        self.check_permissions(request)

        user = UserDataSerializer(request.user).data
        return Response(user, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        self.permission_classes = [AllowAny, ]
        self.check_permissions(request)
        CreateUsersService.execute(request.data)
        return Response(status=status.HTTP_201_CREATED)

    def patch(self, request, *args, **kwargs):
        self.permission_classes = [IsAuthenticated, ]
        self.check_permissions(request)

        obj = UserUpdateService.execute(request.data | {'id': request.user.id})
        user = UserDataSerializer(obj).data

        return Response(user, status=status.HTTP_200_OK)
