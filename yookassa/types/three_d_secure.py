from yookassa.types.base import YookassaObject


class ThreeDSecure(YookassaObject):
    applied: bool
    method_completed: bool
    challenge_completed: bool