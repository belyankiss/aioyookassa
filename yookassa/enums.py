from enum import StrEnum


class Currency(StrEnum):
    RUB = "RUB"

class PaymentType(StrEnum):
    BANK_CARD = "bank_card"

class ConfirmationType(StrEnum):
    REDIRECT = "redirect"

class StatusPayment(StrEnum):
    PENDING = "pending"
    WAITING_FOR_CAPTURE = "waiting_for_capture"
    SUCCEEDED = "succeeded"
    CANCELED = "canceled"

class CardPaymentStatus(StrEnum):
    INACTIVE = "inactive"
    ACTIVE = "active"