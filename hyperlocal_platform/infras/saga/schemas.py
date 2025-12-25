from pydantic import BaseModel
from core.enums.saga_state_enum import SagaStatusEnum


class CreatedSagaStatesSchema(BaseModel):
    id:str
    status:SagaStatusEnum
    type:str
    data:dict

class UpdateSagaStatesSchema(BaseModel):
    id:str
    data:dict