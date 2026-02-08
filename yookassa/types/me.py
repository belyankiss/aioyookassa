from typing import List, Optional

from yookassa.types.base import YookassaObject
from yookassa.types.fiscalization import Fiscalization


class Me(YookassaObject):
    account_id: str
    test: bool
    fiscalization: Optional[Fiscalization] = None
    fiscalization_enabled: bool
    payment_methods: List[str]
    status: str