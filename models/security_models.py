from abc import ABC,abstractmethod


class SecurityModel(ABC):
    @staticmethod
    @abstractmethod
    def generate(*args,**kwargs):
        ...

    @staticmethod
    @abstractmethod
    def verify(*args,**kwargs):
        ...

    