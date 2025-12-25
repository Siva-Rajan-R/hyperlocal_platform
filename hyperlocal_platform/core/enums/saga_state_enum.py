from enum import Enum


class SagaStatusEnum(Enum):
    PENDING="PENDING"
    COMPLETED="COMPLETED"
    CANCELED="CANCELED"
    