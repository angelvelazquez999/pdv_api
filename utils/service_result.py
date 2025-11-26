from typing import Any
from utils.app_exceptions import AppExceptionCase


class ServiceResult:    
    def __init__(self, data: Any):
        if isinstance(data, AppExceptionCase):
            self.success = False
            self.error = data
            self.data = None
        else:
            self.success = True
            self.data = data
            self.error = None
    
    def unwrap(self):
        if not self.success:
            raise self.error
        return self.data


def handle_result(result: ServiceResult) -> Any:
    return result.unwrap()
