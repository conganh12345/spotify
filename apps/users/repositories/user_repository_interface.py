from apps.cores.repositories.base_repository_interface import BaseRepositoryInterface
from abc import abstractmethod

class UserRepositoryInterface(BaseRepositoryInterface):
    @abstractmethod
    def find_by_email(self, email):
        pass
