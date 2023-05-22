from pydantic import BaseModel, StrBytes, UUID4, AnyUrl


class UserReturn(BaseModel):
    id: int
    uuid: UUID4


class AudioRequest(BaseModel):
    id: int
    uuid: UUID4
    audio: File


class AudioResponseURL(BaseModel):
    url: AnyUrl
