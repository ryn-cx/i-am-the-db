# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from i_am_the_db.exceptions import TitleNotFoundError

if TYPE_CHECKING:
    from i_am_the_db import IAmTheDB

TITLE_IDS = [
    pytest.param("tt0111161", id="movie"),
    pytest.param("tt0386676", id="show"),
    pytest.param("tt0664521", id="episode"),
]

NOT_TITLE_IDS = [
    pytest.param("tt0000000", id="title that does not exist"),
    pytest.param("nm0000001", id="person asked for as a title"),
]


# TODO: Validate
@pytest.mark.parametrize("title_id", TITLE_IDS)
def test_download(client: IAmTheDB, title_id: str) -> None:
    title = client.title(title_id).data.title
    assert title.id == title_id
    assert title.title_text.text


# TODO: Validate
@pytest.mark.parametrize("title_id", NOT_TITLE_IDS)
def test_download_invalid(client: IAmTheDB, title_id: str) -> None:
    with pytest.raises(TitleNotFoundError):
        client.title.download(title_id)
