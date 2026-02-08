from typing import List, Optional

from pydantic import Field

from yookassa.types.base import YookassaObject
from yookassa.types.refund import RefundResponse


class ListRefunds(YookassaObject):
    type: str = "list"
    items: List[RefundResponse] = Field(default_factory=list)
    next_cursor: Optional[str] = None