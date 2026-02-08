from datetime import datetime

from pydantic import Field

from yookassa.enums import StatusPayment
from yookassa.types.amount import Amount
from yookassa.types.base import YookassaObject
from yookassa.types.metadata import Metadata


class RefundAuthorizationDetails(YookassaObject):
    rrn: int

class RefundRequest(YookassaObject):
    amount: Amount
    payment_id: str


class RefundResponse(YookassaObject):
    id: str
    status: StatusPayment
    amount: Amount
    created_at: datetime
    payment_id: str
    refund_authorization_details: RefundAuthorizationDetails
    metadata: Metadata = Field(default_factory=Metadata)