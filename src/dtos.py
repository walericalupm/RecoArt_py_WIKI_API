from pydantic import BaseModel


class DescriptionDTO(BaseModel):
    Language: int
    Description: str


class DescriptionsDTO(BaseModel):
    RecoArtPaintCode: str
    WikipediaPaintCode: str
    Descriptions: list


