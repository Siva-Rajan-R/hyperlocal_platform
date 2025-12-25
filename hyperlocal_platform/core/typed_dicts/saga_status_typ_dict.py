from typing import TypedDict


class SagaStateExecutionTypDict(TypedDict):
    """This is current step and service of the event"""
    step:str
    service:str

class SagaStateErrorTypDict(TypedDict):
    code:str
    debug:str
    user_msg:str