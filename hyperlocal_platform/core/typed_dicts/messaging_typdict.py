from typing import TypedDict,Any,Optional
from ..basemodels.readdb_model import ReadDbBaseModel

class EventPublishingTypDict(TypedDict):
    exchange_name:str
    routing_key:str
    payload:dict
    headers:dict

class SuccessMessagingTypDict(TypedDict):
    response:Any
    read_db:Optional[ReadDbBaseModel]=None
    set_response:Optional[bool]=False
    mark_completed:Optional[bool]=False
    emit_success:Optional[bool]=False
    emit_payload:Optional[EventPublishingTypDict]=None