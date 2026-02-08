from typing import Optional

from pydantic import BaseModel


class YookassaError(BaseModel):
    type: str
    id: str
    description: str
    parameter: Optional[str] = None
    code: str