from apps.cores.repositories.base_repository_interface import BaseRepositoryInterface

class BaseRepository(BaseRepositoryInterface):
    def __init__(self, model):
        self.model = model

    def all(self):
        return self.model.objects.all()

    def get(self, pk):
        try:
            return self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            return None

    def create(self, **kwargs):
        return self.model.objects.create(**kwargs)

    def update(self, instance, **kwargs):
        for attr, value in kwargs.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    def delete(self, instance):
        instance.delete()
