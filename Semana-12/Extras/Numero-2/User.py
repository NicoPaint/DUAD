from abc import ABC, abstractmethod

class User(ABC):
    @abstractmethod
    def get_role(self):
        pass

    @abstractmethod
    def has_permission(permission):
        pass