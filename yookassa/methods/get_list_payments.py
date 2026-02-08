from yookassa.methods.base import YookassaMethod
from yookassa.types.payment import ListPayments


class GetListPayments(YookassaMethod):
    __api_method__ = "get"
    __endpoint__ = "/payments"
    __returning__ = ListPayments
    __idempotence__ = False