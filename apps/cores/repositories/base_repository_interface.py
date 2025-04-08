from abc import ABC, abstractmethod

class BaseRepositoryInterface(ABC):
    @abstractmethod
    def all(self):
        pass

    @abstractmethod
    def get(self, pk):
        pass

    @abstractmethod
    def create(self, **kwargs):
        pass

    @abstractmethod
    def update(self, instance, **kwargs):
        pass

    @abstractmethod
    def delete(self, instance):
        pass
