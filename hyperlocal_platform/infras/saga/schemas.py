from pydantic import BaseModel
from core.enums.saga_state_enum import SagaStatusEnum
from hyperlocal_platform.core.typed_dicts.saga_status_typ_dict import SagaStateErrorTypDict,SagaStateExecutionTypDict


class CreateSagaStateSchema(BaseModel):
    id:str
    status:SagaStatusEnum
    type:str
    data:dict
    execution:SagaStateExecutionTypDict
    error:SagaStateErrorTypDict

class UpdateSagaStateSchema(BaseModel):
    id:str
    data:dict
    status:SagaStatusEnum
    type:str
    execution:SagaStateExecutionTypDict
    error:SagaStateErrorTypDict
    retry_count:int