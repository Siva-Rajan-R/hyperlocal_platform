from abc import ABC,abstractmethod


class CommonBaseReadDBModel(ABC):
    @abstractmethod
    async def create(self):
        ...

    @abstractmethod
    async def update():
        ...

    @abstractmethod
    async def delete():
        ...