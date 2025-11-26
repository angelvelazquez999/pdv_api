from pydantic import BaseModel
from typing import List, Optional

from datetime import datetime, date

class ResponseModel(BaseModel):
    Message: str

class ResponseModelPath(ResponseModel):
    path: str

class ResponseModelID(BaseModel):
    id: int

class SafeDelete(BaseModel):
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        json_encoders = {
            datetime: lambda v: v.strftime("%d-%m-%Y %H:%M:%S") if v else None,
            date: lambda v: v.strftime("%d-%m-%Y") if v else None
        }
