from abc import ABC, abstractmethod
from typing import Generic, TYPE_CHECKING, ClassVar, Any, TypeVar

from pydantic import BaseModel, ConfigDict

from yookassa.types.base import YookassaObject

YookassaType = TypeVar("YookassaType", bound=YookassaObject)


class YookassaMethod(BaseModel, Generic[YookassaType], ABC):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    if TYPE_CHECKING:
        __api_method__: ClassVar[str]
        __endpoint__: ClassVar[str]
        __returning__: ClassVar[Any]
        __idempotence__: ClassVar[bool] = False
    else:

        @property
        @abstractmethod
        def __api_method__(self) -> str:
            pass

        @property
        @abstractmethod
        def __endpoint__(self) -> str:
            pass

        @property
        @abstractmethod
        def __returning__(self) -> YookassaType:
            pass


