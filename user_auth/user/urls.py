from django.urls import path

from user.views.get_create_update import GetCreateUpdateUserView

urlpatterns = [
    # Создание, получение и изменение данных пользователя
    path('', GetCreateUpdateUserView.as_view(), name='user'),
]