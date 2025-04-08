from django.contrib.auth.models import User
from apps.cores.repositories.base_repository import BaseRepository
from apps.users.repositories.user_repository_interface import UserRepositoryInterface

class UserRepository(BaseRepository, UserRepositoryInterface):
    def __init__(self):
        super().__init__(User)

    def find_by_email(self, email):
        return self.model.objects.filter(email=email).first()
