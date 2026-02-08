from datetime import datetime, timezone
from typing import List, Optional

from pydantic import Field, field_serializer

from yookassa.enums import StatusPayment
from yookassa.types.amount import Amount
from yookassa.types.base import YookassaObject
from yookassa.types.cart import Cart
from yookassa.types.delivery_method_data import DeliveryMethodData
from yookassa.types.metadata import Metadata


class PaymentData(YookassaObject):
    amount: Amount
    capture: bool = True
    description: str
    metadata: Metadata = Field(default_factory=Metadata)


class InvoiceRequest(YookassaObject):
    payment_data: PaymentData
    cart: List[Cart] = Field(default_factory=list)
    delivery_method_data: DeliveryMethodData
    locale: str = "ru_RU"
    expires_at: datetime
    description: str
    metadata: Metadata = Field(default_factory=Metadata)

    @field_serializer("expires_at")
    def serialize_date(self, v):
        return (
            v.astimezone(timezone.utc)
            .isoformat(timespec="milliseconds")
            .replace("+00:00", "Z")
        )



class InvoiceResponse(YookassaObject):
    id: str
    status: StatusPayment
    cart: List[Cart]


d = {
    "payment_data": {
        "amount": {
            "value": "10.00",
            "currency": "RUB"
        },
        "capture": True,
        "description": "Заказ №37",
        "metadata": {
            "order_id": "37"
        }
    },
    "cart": [
        {
            "description": "Товар арт. 12345",
            "price": {
                "value": "9.00",
                "currency": "RUB"
            },
            "discount_price": {
                "value": "7.00",
                "currency": "RUB"
            },
            "quantity": 1.000
        },
        {
            "description": "Товар арт. 67890",
            "price": {
                "value": "1.00",
                "currency": "RUB"
            },
            "quantity": 3.000
        }
    ],
    "delivery_method_data": {
        "type": "self"
    },
    "locale": "ru_RU",
    "expires_at": "2024-10-18T10:51:18.139Z",
    "description": "Счет на оплату заказа номер 37",
    "metadata": {
        "order_id": "37"
    }
}
