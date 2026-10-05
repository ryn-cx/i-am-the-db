from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import ConfigDict
from typing import Any
from pydantic import BaseModel, Field

class Name(BaseModel):
    model_config = ConfigDict(defer_build=True)
    original_text: str = Field(..., alias='originalText')

class OriginalText(BaseModel):
    model_config = ConfigDict(defer_build=True)
    plain_text: str = Field(..., alias='plainText')

class Description(BaseModel):
    model_config = ConfigDict(defer_build=True)
    original_text: OriginalText = Field(..., alias='originalText')

class ListType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: str

class PageInfo(BaseModel):
    model_config = ConfigDict(defer_build=True)
    has_next_page: bool = Field(..., alias='hasNextPage')
    end_cursor: str = Field(..., alias='endCursor')

class TitleText(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text: str

class TitleType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: str
    text: str
    is_series: bool = Field(..., alias='isSeries')
    is_episode: bool = Field(..., alias='isEpisode')

class ReleaseYear(BaseModel):
    model_config = ConfigDict(defer_build=True)
    year: int
    end_year: int | None = Field(..., alias='endYear')

class ListItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: str
    title_text: TitleText = Field(..., alias='titleText')
    title_type: TitleType = Field(..., alias='titleType')
    release_year: ReleaseYear | None = Field(..., alias='releaseYear')

class Node(BaseModel):
    model_config = ConfigDict(defer_build=True)
    list_item: ListItem = Field(..., alias='listItem')

class Edge(BaseModel):
    model_config = ConfigDict(defer_build=True)
    node: Node

class Items(BaseModel):
    model_config = ConfigDict(defer_build=True)
    total: int
    page_info: PageInfo = Field(..., alias='pageInfo')
    edges: list[Edge]

class List(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: str
    name: Name
    description: Description | None
    list_type: ListType = Field(..., alias='listType')
    items: Items

class Data(BaseModel):
    model_config = ConfigDict(defer_build=True)
    list: List

class ExperimentalFields(BaseModel):
    model_config = ConfigDict(defer_build=True)
    list_: list[None] = Field(..., alias='list')

class Extensions(BaseModel):
    model_config = ConfigDict(defer_build=True)
    disclaimer: str
    experimental_fields: ExperimentalFields = Field(..., alias='experimentalFields')

class TitleListModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    data: Data
    extensions: Extensions
    _raw_input: Any = PrivateAttr(default=None)

    @model_validator(mode='wrap')
    @classmethod
    def _capture_raw_input(cls, data: Any, handler: ModelWrapValidatorHandler[Self]) -> Self:
        """Validate the model and keep the input it was built from."""
        model = handler(data)
        model._raw_input = data
        return model

    @property
    def raw_input(self) -> Any:
        """The input this model was validated from, as it was handed over."""
        return self._raw_input
