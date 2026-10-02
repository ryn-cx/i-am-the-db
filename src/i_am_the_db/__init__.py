# TODO: Validate
"""Contains the IAmTheDB class."""

from __future__ import annotations

from http import HTTPStatus
from logging import NullHandler, getLogger
from time import monotonic, sleep
from typing import Any

from get_around import GetAround

from i_am_the_db.exceptions import HTTPError
from i_am_the_db.title import Title

logger = getLogger(__name__)
logger.addHandler(NullHandler())

API_URL = "https://caching.graphql.imdb.com/"


# TODO: Validate
class IAmTheDB:
    """IMDb API wrapper.

    Talks to the GraphQL API imdb.com reads its pages from. It needs no account.
    """

    # TODO: Validate
    def __init__(
        self,
        get_around_client: GetAround | None = None,
        sleep_time: float = 0,
    ) -> None:
        """Initializes the IAmTheDB client.

        The client holds one attribute per endpoint, so `client.title(id)` looks
        a title up and `client.title.download(id)` and `client.title.load(data)`
        are the halves of it.
        """
        self.get_around_client = get_around_client or GetAround()
        self.sleep_time = sleep_time

        self.title = Title(self)

    # TODO: Validate
    def _headers(self) -> dict[str, str]:
        # The API refuses a request that does not name the client it comes from.
        return {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "x-imdb-client-name": "imdb-web-next-localized",
            "x-imdb-user-country": "US",
            "x-imdb-user-language": "en-US",
        }

    # TODO: Validate
    def download(
        self,
        query: str,
        variables: dict[str, Any],
        log_id: str,
    ) -> str:
        """Run a GraphQL query and return the body as text.

        Raises:
            HTTPError: If the request is answered with anything but a 200.
        """
        logger.debug("Downloading: %s", log_id)
        start = monotonic()
        response = self.get_around_client.post(
            API_URL,
            json={"query": query, "variables": variables},
            headers=self._headers(),
            timeout=60,
        )

        if response.status_code != HTTPStatus.OK:
            raise HTTPError(response.status_code, response.text)

        logger.debug("Downloaded %s (%.4f s)", log_id, monotonic() - start)
        sleep(self.sleep_time)
        return response.text
