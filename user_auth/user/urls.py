from django.urls import path

from user.views.get import GetUserView
from user.views.get_create_update import GetCreateUpdateUserView
from user.views.list import GetUsersView

urlpatterns = [
    # Создание, получение и изменение данных пользователя
    path('', GetCreateUpdateUserView.as_view(), name='user'),
    path('list/', GetUsersView.as_view(), name='user_list'),
    path('<int:id>/', GetUserView.as_view(), name='get_user'),
]