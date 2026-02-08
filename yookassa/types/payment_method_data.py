from typing import Optional

from yookassa.enums import PaymentType, CardPaymentStatus
from yookassa.types.base import YookassaObject
from yookassa.types.card import Card


class PaymentMethodData(YookassaObject):
    type: PaymentType = PaymentType.BANK_CARD

class PaymentMethod(PaymentMethodData):
    id: str
    saved: bool
    status: CardPaymentStatus
    title: str = ""
    card: Optional[Card] = None