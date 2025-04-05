from django.db import models
from django.contrib.auth.models import User
from enum import Enum, IntEnum


class UserStatus(IntEnum):
    INACTIVE = 0
    ACTIVE = 1

    @property
    def text(self):
        text_mapping = {
            self.INACTIVE: "Tắt",
            self.ACTIVE: "Bật"
        }
        return text_mapping[self]
    
    @property
    def badge(self):
        return {
            self.INACTIVE: "danger",
            self.ACTIVE: "success"
        }[self]

    @classmethod
    def from_boolean(cls, value):
        return cls.ACTIVE if value else cls.INACTIVE

    def to_boolean(self):
        return self == UserStatus.ACTIVE
    