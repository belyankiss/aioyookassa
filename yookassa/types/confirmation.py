from yookassa.enums import ConfirmationType
from yookassa.types.base import YookassaObject


class Confirmation(YookassaObject):
    type: ConfirmationType = ConfirmationType.REDIRECT
    return_url: str = "https://www.example.com/return_url"

class ConfirmationResponse(Confirmation):
    confirmation_url: str