from datetime import datetime
from typing import Optional, Dict, Any, List

from pydantic import Field

from yookassa.enums import StatusPayment
from yookassa.types.amount import Amount
from yookassa.types.authorization_details import AuthorizationDetails
from yookassa.types.base import YookassaObject
from yookassa.types.confirmation import Confirmation, ConfirmationResponse
from yookassa.types.metadata import Metadata
from yookassa.types.payment_method_data import PaymentMethodData, PaymentMethod
from yookassa.types.recipient import Recipient


class PaymentRequest(YookassaObject):
    amount: Amount
    payment_method_data: PaymentMethodData
    confirmation: Confirmation
    description: str
    metadata: Dict[str, Any] = Field(default_factory=dict)
    capture: bool


class PaymentResponse(YookassaObject):
    id: str
    status: StatusPayment
    paid: bool
    amount: Amount
    description: str
    confirmation: Optional[ConfirmationResponse] = None
    recipient: Recipient
    payment_method: PaymentMethod
    created_at: datetime
    expires_at: Optional[datetime] = None
    test: bool
    refundable: bool
    metadata: Optional[Metadata] = None
    authorization_details: Optional[AuthorizationDetails] = None

class ListPayments(YookassaObject):
    type: str
    items: List[PaymentResponse]
