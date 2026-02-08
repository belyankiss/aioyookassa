from pydantic import BaseModel, ConfigDict


class YookassaObject(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)