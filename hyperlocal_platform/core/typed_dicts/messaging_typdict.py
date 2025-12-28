from typing import TypedDict,Any,Optional

class EventPublishingTypDict(TypedDict):
    exchange_name:str
    routing_key:str
    payload:dict
    headers:dict

class SuccessMessagingTypDict(TypedDict):
    response:Any
    set_response:Optional[bool]=False
    mark_completed:Optional[bool]=False
    emit_success:Optional[bool]=False
    emit_payload:Optional[EventPublishingTypDict]=None