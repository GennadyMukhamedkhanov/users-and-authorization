from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
    TokenObtainPairView
)


urlpatterns = [
    # Получение токена
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # Обновление токена
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # Проверка токена
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]