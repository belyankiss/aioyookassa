from yookassa.methods.base import YookassaMethod
from yookassa.types.payment import PaymentResponse, PaymentRequest


class CreatePayment(YookassaMethod, PaymentRequest):
    __api_method__ = "post"
    __endpoint__ = "/payments"
    __returning__ = PaymentResponse
    __idempotence__ = True