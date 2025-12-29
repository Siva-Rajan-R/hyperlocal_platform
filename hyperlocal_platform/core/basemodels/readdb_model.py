from pydantic import BaseModel


class ReadDbBaseModel(BaseModel):
    payload:dict
    method:str
    condition:dict