from service_objects.services import Service

from db.models import User


class UsersServices(Service):

    def process(self):
        return User.objects.all()
