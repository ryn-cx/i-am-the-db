# TODO: Validate
import pytest
from get_around import build_client_automatically

from i_am_the_db import IAmTheDB


# TODO: Validate
@pytest.fixture(scope="session")
def client() -> IAmTheDB:
    return IAmTheDB(build_client_automatically())
