from .main import BASE
from sqlalchemy import Column,String,Integer,TIMESTAMP,func,text
from sqlalchemy.dialects.postgresql import JSONB

class SagaStates(BASE):
    __tablename__="saga_states"
    id=Column(String,primary_key=True)
    status=Column(String,nullable=False)
    type=Column(String,nullable=False)
    data=Column(JSONB,nullable=False)
    steps=Column(JSONB,nullable=False)
    execution=Column(JSONB,nullable=False,default=dict,server_default=text("'{}'::jsonb"))
    error=Column(JSONB,nullable=True)
    retry_count=Column(Integer,nullable=False,server_default=text("0"))
    created_at=Column(TIMESTAMP(timezone=True),server_default=func.now())