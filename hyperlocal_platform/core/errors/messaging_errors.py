from ..enums.error_enums import ErrorTypeSEnum
from ..typed_dicts.messaging_typdict import EventPublishingTypDict
from ..typed_dicts.saga_status_typ_dict import SagaStateErrorTypDict
from typing import Optional

class CommonMessagingError(Exception):
    def __init__(
        self,
        type:ErrorTypeSEnum,
        error:SagaStateErrorTypDict,
        compensation:Optional[bool]=False,
        compensation_payload:Optional[EventPublishingTypDict]=None
    ):
        self.type=type.value if isinstance(type,ErrorTypeSEnum) else type
        self.error=error
        self.compensation=compensation
        self.compensation_payload=compensation_payload

        super().__init__(error.get("debug"))
    
    def __str__(self):
        return f"{self.type} : {self.error.get("code")} => {self.error.get("debug")}, ADDTIONAL INFOS : COMPENSATION => {self.compensation}, COMPENSATION PAYLOAD => {self.compensation_payload}"


class CommonBussinessError(CommonMessagingError):
    "This contains not retryable error, and which errors are expected"

class CommonRetryableError(CommonMessagingError):
    "This error type can be re-tryable, cause based on tempory system failures"

class CommonFatalError(CommonMessagingError):
    "This error should be thrown when the system has a permant failure, bug and not solvable by own"

