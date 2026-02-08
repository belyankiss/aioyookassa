from yookassa.methods.base import YookassaMethod
from yookassa.types.payment import PaymentResponse

i = "311a8382-000f-5001-9000-137febac69a6"

class GetPaymentInfo(YookassaMethod):
    __api_method__ = "get"
    __returning__ = PaymentResponse
    __idempotence__ = False

    id: str

    @property
    def __endpoint__(self) -> str:
        return f"/payments/{self.id}"