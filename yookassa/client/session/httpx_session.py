import uuid
from typing import Optional, Dict, cast, TYPE_CHECKING

from httpx import AsyncClient, BasicAuth

from yookassa.types.error import YookassaError

if TYPE_CHECKING:
    from yookassa.client.yookassa import Yookassa

from yookassa.methods.base import YookassaMethod, YookassaType

class YookassaException(Exception):
    def __init__(self, error: YookassaError):
        self.error = error
        super().__init__(f"{self.error.description}")


class HttpxSession:
    def __init__(
            self,
            timeout: int = 180,
            auth: BasicAuth = None,
            headers: Dict[str, str] = None,
            **kwargs
    ):
        self._session: Optional[AsyncClient] = None
        self.timeout = timeout
        self.kwargs = kwargs
        self._auth = auth
        self.headers = headers

    async def create_session(self) -> AsyncClient:
        if self._session is None or self._session.is_closed:
            self._session = AsyncClient(
                base_url="https://api.yookassa.ru/v3/",
                timeout=self.timeout,
                headers=self.headers,
                auth=self._auth
            )
        return self._session

    async def close(self):
        if self._session is not None and not self._session.is_closed:
            await self._session.aclose()

    async def make_request(self, method: YookassaMethod[YookassaType]) -> YookassaType:
        session = await self.create_session()
        if method.__api_method__ in ("post", "put", "delete"):
            json = method.model_dump()
        else:
            json = {}

        headers = self._create_idempotence_key() if method.__idempotence__ else None
        response = await session.request(
            method=method.__api_method__,
            url=method.__endpoint__,
            json=json,
            headers=headers
        )
        # response.raise_for_status()
        data = response.json()
        if data.get("type", False) == "error":
            error = YookassaError.model_validate(data)
            raise YookassaException(error=error)

        print(response.json())
        response_type: YookassaType = method.__returning__
        return cast(YookassaType, response_type.model_validate(response.json()))

    @staticmethod
    def _create_idempotence_key() -> Dict[str, str]:
        return {
            "Idempotence-Key": str(uuid.uuid4())
        }

    async def __call__(
            self,
            yookassa: "Yookassa",
            method: YookassaMethod[YookassaType],
            timeout: int | None = None
    ) -> YookassaType:
        return cast(YookassaType, await self.make_request(method))
