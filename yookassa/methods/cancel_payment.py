from yookassa.methods.base import YookassaMethod
from yookassa.types.payment import PaymentResponse


class CancelPayment(YookassaMethod):
    __api_method__ = "post"
    __returning__ = PaymentResponse
    __idempotence__ = True

    id: str

    @property
    def __endpoint__(self) -> str:
        return f"/payments/{self.id}/cancel"