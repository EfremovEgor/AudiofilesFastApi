from pydantic import BaseModel
from pydantic import UUID4


class UserReturn(BaseModel):
    id: int
    uuid: UUID4
