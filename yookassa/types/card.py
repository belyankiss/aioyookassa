from yookassa.types.base import YookassaObject
from yookassa.types.card_product import CardProduct


class Card(YookassaObject):
    first6: int
    last4: int
    expiry_year: int
    expiry_month: int
    card_type: str
    card_product: CardProduct
    issuer_country: str