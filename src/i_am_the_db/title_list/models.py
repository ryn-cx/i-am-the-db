# ruff: noqa: D100
from typing import TYPE_CHECKING

from good_ass_pydantic_integrator import load

from .optional_models import TitleListModel as OptionalModel
from .strict_models import TitleListModel as StrictModel

if TYPE_CHECKING:
    from .strict_models import (
        Data,
        Description,
        Edge,
        ExperimentalFields,
        Extensions,
        Items,
        List,
        ListItem,
        ListType,
        Name,
        Node,
        OriginalText,
        PageInfo,
        ReleaseYear,
        TitleListModel,
        TitleText,
        TitleType,
    )
else:
    from .optional_models import (
        Data,
        Description,
        Edge,
        ExperimentalFields,
        Extensions,
        Items,
        List,
        ListItem,
        ListType,
        Name,
        Node,
        OriginalText,
        PageInfo,
        ReleaseYear,
        TitleListModel,
        TitleText,
        TitleType,
    )

__all__ = [
    "Data",
    "Description",
    "Edge",
    "ExperimentalFields",
    "Extensions",
    "Items",
    "List",
    "ListItem",
    "ListType",
    "Name",
    "Node",
    "OriginalText",
    "PageInfo",
    "ReleaseYear",
    "TitleListModel",
    "TitleText",
    "TitleType",
    "model_validate_json",
]


def model_validate_json(data: str | bytes | object, log_id: str) -> TitleListModel:
    """Read a downloaded file into TitleListModel."""
    return load.model_validate_json(StrictModel, OptionalModel, data, log_id)
