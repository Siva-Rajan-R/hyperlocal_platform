from typing import TypedDict


class SagaStatesExecutionTypDict(TypedDict):
    """This is current step and service of the event"""
    step:str
    service:str

class SagaStatesErrorTypDict(TypedDict):
    code:str
    debug:str
    user_msg:str