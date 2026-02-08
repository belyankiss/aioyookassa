from decimal import Decimal, ROUND_HALF_UP
from typing import Union

from pydantic import Field, field_validator, field_serializer

from yookassa.enums import Currency
from yookassa.types.base import YookassaObject


class Amount(YookassaObject):
    value: Union[int, float] = Field(gt=0.00)
    currency: Currency = Currency.RUB

    @field_validator("value")
    @classmethod
    def round_value(cls, v: float) -> float:
        return round(v, 2)

    @field_serializer("value")
    def str_value(self, v) -> str:
        value = Decimal(str(v))
        return str(value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))

