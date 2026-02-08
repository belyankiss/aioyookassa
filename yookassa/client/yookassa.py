from datetime import datetime
from decimal import Decimal
from typing import TypeVar, Union, List, Optional

from httpx import BasicAuth

from yookassa.client.session.httpx_session import HttpxSession
from yookassa.enums import Currency, PaymentType, ConfirmationType
from yookassa.methods.base import YookassaMethod
from yookassa.methods.cancel_payment import CancelPayment
from yookassa.methods.create_invoice import CreateInvoice
from yookassa.methods.create_payment import CreatePayment
from yookassa.methods.create_refund import CreateRefund
from yookassa.methods.get_list_payments import GetListPayments
from yookassa.methods.get_list_refunds import GetListRefunds
from yookassa.methods.get_me import GetMe
from yookassa.methods.get_payment import GetPaymentInfo
from yookassa.methods.payment_confirmation import PaymentConfirmation
from yookassa.types.amount import Amount
from yookassa.types.cart import Cart
from yookassa.types.confirmation import Confirmation
from yookassa.types.delivery_method_data import DeliveryMethodData
from yookassa.types.invoice import PaymentData
from yookassa.types.list_refunds import ListRefunds
from yookassa.types.me import Me
from yookassa.types.metadata import Metadata
from yookassa.types.payment import PaymentResponse
from yookassa.types.payment_method_data import PaymentMethodData
from yookassa.types.refund import RefundResponse

T = TypeVar("T")


class Yookassa:
    def __init__(
            self,
            shop_id: int,
            secret_key: str,
            **kwargs
    ):
        self._auth = BasicAuth(
            username=str(shop_id),
            password=secret_key
        )

        self._headers = {
            "Content-Type": "application/json"
        }

        self.session = HttpxSession(auth=self._auth, headers=self._headers, **kwargs)

    async def get_me(self) -> Me:
        me = GetMe()
        return await self(me)

    async def create_payment(
            self,
            amount: Union[float, int],
            description: str,
            metadata: Metadata | None = None,
            capture: bool = True,
            return_url: str = "https://www.example.com/return_url",
            confirmation_type: ConfirmationType = ConfirmationType.REDIRECT,
            currency: Currency = Currency.RUB,
            payment_type: PaymentType = PaymentType.BANK_CARD
    ) -> PaymentResponse:
        if metadata is None:
            metadata = Metadata()
        payment = CreatePayment(
            amount=Amount(value=amount, currency=currency),
            payment_method_data=PaymentMethodData(type=payment_type),
            confirmation=Confirmation(type=confirmation_type, return_url=return_url),
            description=description,
            capture=capture,
            metadata=metadata.model_dump()
        )
        return await self(payment)

    async def get_payment_info(self, ident: str) -> PaymentResponse:
        payment = GetPaymentInfo(id=ident)
        return await self(payment)

    async def get_list_payments(self) -> List[PaymentResponse]:
        payments = GetListPayments()
        result = await self(payments)
        return result.items

    async def confirm_payment(self, ident: str, amount: Optional[Union[int, float]] = None) -> PaymentResponse:
        payment = PaymentConfirmation(id=ident, amount=Amount(value=amount) if amount is not None else None)
        return await self(payment)

    async def cancel_payment(self, ident: str) -> PaymentResponse:
        payment = CancelPayment(id=ident)
        return await self(payment)

    async def create_invoice(
            self,
            *cart: Cart,
            description: str,
            metadata: Metadata | None = None,
            expires_at: datetime,
            delivery_type: str = "self"
    ):
        if metadata is None:
            metadata = Metadata()
        price = 0
        for c in cart:
            price += (c.price.value * c.quantity)

        invoice = CreateInvoice(
            payment_data=PaymentData(
                amount=Amount(value=price),
                description=description,
                metadata=metadata
            ),
            delivery_method_data=DeliveryMethodData(type=delivery_type),
            expires_at=expires_at,
            description=description,
            metadata=metadata,
            cart=list(cart)
        )

        return await self(invoice)

    async def create_refund(self, ident: str, amount: Union[float, int]) -> RefundResponse:
        refund = CreateRefund(amount=Amount(value=amount), payment_id=ident)
        return await self(refund)

    async def get_list_refunds(self) -> ListRefunds:
        refunds = GetListRefunds()
        return await self(refunds)

    async def __call__(self, method: YookassaMethod[T], request_timeout: int | None = None) -> T:
        return await self.session(self, method, timeout=request_timeout)
