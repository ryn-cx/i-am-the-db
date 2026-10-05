from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from typing import Any
from pydantic import BaseModel, ConfigDict, Field

class Name(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    original_text: str | Any = Field(None, alias='originalText', union_mode='left_to_right')

class OriginalText(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    plain_text: str | Any = Field(None, alias='plainText', union_mode='left_to_right')

class Description(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    original_text: OriginalText | Any = Field(None, alias='originalText', union_mode='left_to_right')

class ListType(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | Any = Field(default=None, union_mode='left_to_right')

class PageInfo(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    has_next_page: bool | Any = Field(None, alias='hasNextPage', union_mode='left_to_right')
    end_cursor: str | Any = Field(None, alias='endCursor', union_mode='left_to_right')

class TitleText(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: str | Any = Field(default=None, union_mode='left_to_right')

class TitleType(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | Any = Field(default=None, union_mode='left_to_right')
    text: str | Any = Field(default=None, union_mode='left_to_right')
    is_series: bool | Any = Field(None, alias='isSeries', union_mode='left_to_right')
    is_episode: bool | Any = Field(None, alias='isEpisode', union_mode='left_to_right')

class ReleaseYear(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    year: int | Any = Field(default=None, union_mode='left_to_right')
    end_year: int | Any = Field(None, alias='endYear', union_mode='left_to_right')

class ListItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | Any = Field(default=None, union_mode='left_to_right')
    title_text: TitleText | Any = Field(None, alias='titleText', union_mode='left_to_right')
    title_type: TitleType | Any = Field(None, alias='titleType', union_mode='left_to_right')
    release_year: ReleaseYear | Any = Field(None, alias='releaseYear', union_mode='left_to_right')

class Node(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    list_item: ListItem | Any = Field(None, alias='listItem', union_mode='left_to_right')

class Edge(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    node: Node | Any = Field(default=None, union_mode='left_to_right')

class Items(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    total: int | Any = Field(default=None, union_mode='left_to_right')
    page_info: PageInfo | Any = Field(None, alias='pageInfo', union_mode='left_to_right')
    edges: list[Edge] | Any = Field(default=None, union_mode='left_to_right')

class List(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | Any = Field(default=None, union_mode='left_to_right')
    name: Name | Any = Field(default=None, union_mode='left_to_right')
    description: Description | Any = Field(default=None, union_mode='left_to_right')
    list_type: ListType | Any = Field(None, alias='listType', union_mode='left_to_right')
    items: Items | Any = Field(default=None, union_mode='left_to_right')

class Data(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    list: List | Any = Field(default=None, union_mode='left_to_right')

class ExperimentalFields(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    list_: list[Any] | Any = Field(None, alias='list', union_mode='left_to_right')

class Extensions(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    disclaimer: str | Any = Field(default=None, union_mode='left_to_right')
    experimental_fields: ExperimentalFields | Any = Field(None, alias='experimentalFields', union_mode='left_to_right')

class TitleListModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    data: Data | Any = Field(default=None, union_mode='left_to_right')
    extensions: Extensions | Any = Field(default=None, union_mode='left_to_right')
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
