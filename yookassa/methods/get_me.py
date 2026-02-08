from yookassa.methods.base import YookassaMethod
from yookassa.types.me import Me


class GetMe(YookassaMethod):
    __api_method__ = "get"
    __endpoint__ = "/me"
    __returning__ = Me
    __idempotence__ = True