from pydantic import BaseModel
from typing import Optional,Any

class ReadDbBaseModel(BaseModel):
    payload:Any
    method:str
    condition:Optional[dict]=None