from abc import ABC,abstractmethod
from typing import Optional


class BaseRepoModel(ABC):
    @abstractmethod
    async def create(self,*args,**kwargs):
        ...

    @abstractmethod
    async def update(self,*args,**kwargs):
        ...

    @abstractmethod
    async def delete(self,*args,**kwargs):
        ...

    @abstractmethod
    async def get(self,*args,**kwargs):
        ...

    @abstractmethod
    async def getby_id(self,*args,**kwargs):
        ...

    @abstractmethod
    async def search(self,query:str,limit:Optional[int]=5,*args,**kwargs):
        ...


class BaseServiceModel(BaseRepoModel):
    ...