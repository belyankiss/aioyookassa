from yookassa.types.base import YookassaObject
from yookassa.types.three_d_secure import ThreeDSecure


class AuthorizationDetails(YookassaObject):
    rrn: int
    auth_code: int
    three_d_secure: ThreeDSecure