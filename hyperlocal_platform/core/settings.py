from pydantic_settings import BaseSettings
from pydantic import Field
from .constants import ENV_PREFIX

class HyperLocalPlatformSettings(BaseSettings):
    DATABASE_URL:str=Field(...,description="This contains infrastructure database url (saga,logs)")
    REDIS_URL:str=Field(...,description="This Contains infrastructure redis url, for all the services")

    model_config={
        "case_sensitive":False,
        "env_prefix":ENV_PREFIX
    }

