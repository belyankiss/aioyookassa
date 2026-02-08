from yookassa.types.base import YookassaObject


class Recipient(YookassaObject):
    account_id: int
    gateway_id: int