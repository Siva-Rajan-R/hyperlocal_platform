from pydantic import BaseModel
from ...core.enums.saga_state_enum import SagaStatusEnum,SagaStepsValueEnum
from ...core.typed_dicts.saga_status_typ_dict import SagaStateErrorTypDict,SagaStateExecutionTypDict
from typing import Optional,Dict


class CreateSagaStateSchema(BaseModel):
    id:str
    status:SagaStatusEnum
    type:str
    data:dict
    steps:Dict[str,SagaStepsValueEnum]
    execution:SagaStateExecutionTypDict
    error:Optional[SagaStateErrorTypDict]=None

class UpdateSagaStateSchema(BaseModel):
    id:str
    data:dict
    status:SagaStatusEnum
    type:str
    steps:Dict[str,SagaStepsValueEnum]
    execution:SagaStateExecutionTypDict
    error:Optional[SagaStateErrorTypDict]=None
    retry_count:Optional[int]=0