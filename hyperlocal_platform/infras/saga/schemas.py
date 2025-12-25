from pydantic import BaseModel
from core.enums.saga_state_enum import SagaStatusEnum
from core.typed_dicts.saga_stats_typ_dict import SagaStatesErrorTypDict,SagaStatesExecutionTypDict


class CreatedSagaStatesSchema(BaseModel):
    id:str
    status:SagaStatusEnum
    type:str
    data:dict
    execution:SagaStatesExecutionTypDict
    error:SagaStatesErrorTypDict

class UpdateSagaStatesSchema(BaseModel):
    id:str
    data:dict
    status:SagaStatusEnum
    type:str
    execution:SagaStatesExecutionTypDict
    error:SagaStatesErrorTypDict
    retry_count:int