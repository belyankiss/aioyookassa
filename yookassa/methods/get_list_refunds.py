from yookassa.methods.base import YookassaMethod
from yookassa.types.list_refunds import ListRefunds


class GetListRefunds(YookassaMethod):
    __api_method__ = "get"
    __endpoint__ = "/refunds"
    __returning__ = ListRefunds
    __idempotence__ = False