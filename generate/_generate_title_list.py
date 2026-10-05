# TODO: Validate
from __future__ import annotations

import logging

from get_around import build_client_automatically
from good_ass_pydantic_integrator.recordings import (
    RecordingId,
    download_named_missing,
    load_named_ids,
    rebuild_model,
)

from generate.constants import GENERATOR_PATHS
from i_am_the_db import IAmTheDB

MODEL_NAME = "TitleListModel"


# TODO: Validate
class TitleListId(RecordingId[IAmTheDB]):
    list_id: str

    # TODO: Validate
    def download(self, client: IAmTheDB) -> str:
        return client.title_list.download(self.list_id)


TITLE_LISTS = load_named_ids(GENERATOR_PATHS, MODEL_NAME, TitleListId)


# TODO: Validate
def generate_title_list(client: IAmTheDB) -> None:
    download_named_missing(GENERATOR_PATHS, MODEL_NAME, TITLE_LISTS, client)
    rebuild_model(GENERATOR_PATHS, MODEL_NAME, TitleListId)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_title_list(IAmTheDB(build_client_automatically()))
