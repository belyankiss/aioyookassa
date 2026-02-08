from pydantic import ConfigDict

from yookassa.types.base import YookassaObject


class Metadata(YookassaObject):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        extra="allow"
    )