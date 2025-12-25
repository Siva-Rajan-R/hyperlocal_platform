from abc import ABC,abstractmethod
from sqlalchemy.ext.asyncio import AsyncSession

class CommonBaseConsumerModel(ABC):
    def __init__(self,session:AsyncSession,payload:dict,headers:dict,saga_id:str):
        self.session=session
        self.payload=payload
        self.headers=headers
        self.saga_id=saga_id

    @abstractmethod
    async def create(self):
        ...

    @abstractmethod
    async def update(self):
        ...

    @abstractmethod
    async def delete(self):
        ...

    