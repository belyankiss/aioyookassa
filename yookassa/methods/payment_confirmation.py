from typing import Optional

from yookassa.methods.base import YookassaMethod
from yookassa.types.amount import Amount
from yookassa.types.payment import PaymentResponse


class PaymentConfirmation(YookassaMethod):
    __api_method__ = "post"
    __idempotence__ = True
    __returning__ = PaymentResponse

    id: str
    amount: Optional[Amount] = None

    @property
    def __endpoint__(self) -> str:
        return f"/payments/{self.id}/capture"