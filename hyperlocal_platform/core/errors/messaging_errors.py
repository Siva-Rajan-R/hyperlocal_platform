
class CommonMessagingBaseError(Exception):
    """Base messaging error"""

class CommonBussinessError(CommonMessagingBaseError):
    "This contains not retryable error, and which errors are expected"

class CommonRetryableError(CommonMessagingBaseError):
    "This error type can be re-tryable, cause based on tempory system failures"

class CommonFatalError(CommonMessagingBaseError):
    "This error should be thrown when the system has a permant failure, bug and not solvable by own"

