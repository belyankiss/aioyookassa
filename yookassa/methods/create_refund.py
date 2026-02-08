from yookassa.methods.base import YookassaMethod
from yookassa.types.refund import RefundRequest, RefundResponse


class CreateRefund(YookassaMethod, RefundRequest):
    __api_method__ = "post"
    __endpoint__ = "/refunds"
    __returning__ = RefundResponse
    __idempotence__ = True