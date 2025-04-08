from django.contrib.auth.models import Group
from apps.cores.repositories.base_repository import BaseRepository
from apps.groups.repositories.group_repository_interface import GroupRepositoryInterface

class GroupRepository(BaseRepository, GroupRepositoryInterface):
    def __init__(self):
        super().__init__(Group)

