from enum import Enum


class RoutingkeyActions(Enum):
    CREATE="create"
    DELETE="delete"
    UPDATE="update"

class RoutingkeyState(Enum):
    REQUESTED="requested"
    COMPLETED="completed"
    FAILED="failed"

class RoutingkeyVersions(Enum):
    V1="v1"
    V2="v2"