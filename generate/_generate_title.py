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

MODEL_NAME = "TitleModel"


# TODO: Validate
class TitleId(RecordingId[IAmTheDB]):
    title_id: str

    # TODO: Validate
    def download(self, client: IAmTheDB) -> str:
        return client.title.download(self.title_id)


TITLES = load_named_ids(GENERATOR_PATHS, MODEL_NAME, TitleId)


# TODO: Validate
def generate_title(client: IAmTheDB) -> None:
    download_named_missing(GENERATOR_PATHS, MODEL_NAME, TITLES, client)
    rebuild_model(GENERATOR_PATHS, MODEL_NAME, TitleId)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_title(IAmTheDB(build_client_automatically()))
