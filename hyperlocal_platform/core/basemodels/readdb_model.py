from pydantic import BaseModel
from typing import Optional

class ReadDbBaseModel(BaseModel):
    payload:dict
    method:str
    condition:Optional[dict]=None