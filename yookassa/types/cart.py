from decimal import Decimal, ROUND_HALF_UP
from typing import Optional

from pydantic import field_serializer

from yookassa.types.amount import Amount
from yookassa.types.base import YookassaObject


class Cart(YookassaObject):
    description: str
    price: Amount
    discount_price: Optional[Amount] = None
    quantity: int

    @field_serializer("quantity")
    def str_quantity(self, v) -> str:
        value = Decimal(str(v))
        return str(value.quantize(Decimal("0.001"), rounding=ROUND_HALF_UP))