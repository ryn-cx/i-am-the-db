# TODO: Validate
"""Contains the Title class."""

from __future__ import annotations

import json
from logging import NullHandler, getLogger

from i_am_the_db.base_api_endpoint import BaseEndpoint
from i_am_the_db.exceptions import TitleNotFoundError
from i_am_the_db.title.models import TitleModel, model_validate_json

logger = getLogger(__name__)
logger.addHandler(NullHandler())

QUERY = """
query Title($id: ID!) {
  title(id: $id) {
    id
    titleText { text }
    originalTitleText { text }
    titleType { id text isSeries isEpisode }
    releaseYear { year endYear }
    releaseDate { day month year }
    runtime { seconds }
    ratingsSummary { aggregateRating voteCount }
    meterRanking { currentRank rankChange { changeDirection difference } }
    metacritic { metascore { score } }
    certificate { rating }
    genres { genres { id text } }
    plot { plotText { plainText } }
    primaryImage { url width height }
    countriesOfOrigin { countries { id text } }
    spokenLanguages { spokenLanguages { id text } }
    episodes {
      seasons { number }
      totalEpisodes: episodes(first: 0) { total }
    }
  }
}
"""
"""The main details of a movie or show."""


# TODO: Validate
class Title(BaseEndpoint):
    """Contains a movie or show.

    A title is looked up by its IMDb id, e.g. tt0386676 in
    https://www.imdb.com/title/tt0386676/.

    Source: https://caching.graphql.imdb.com/

    Example request:
        - POST / HTTP/2
        - Host: caching.graphql.imdb.com
        - Accept: application/json
        - Content-Type: application/json
        - x-imdb-client-name: imdb-web-next-localized
        - x-imdb-user-country: US
        - x-imdb-user-language: en-US
    """

    # TODO: Validate
    def __call__(self, title_id: str) -> TitleModel:
        """Download and parse the title file."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(self.download(title_id), log_id)

    # TODO: Validate
    def download(self, title_id: str) -> str:
        """Download the title file.

        Raises:
            TitleNotFoundError: If no title is under that id.
        """
        log_id = self.get_log_id(self.download, locals())
        response = self._client.download(
            QUERY,
            variables={"id": title_id},
            log_id=log_id,
        )
        return self._validate_download(response, title_id)

    # TODO: Validate
    @staticmethod
    def _validate_download(response: str, title_id: str) -> str:
        # A missing title comes back as a title with every field null, and an id
        # that is not a title id comes back as an error with no title at all.
        title = (json.loads(response).get("data") or {}).get("title") or {}
        if title.get("id") != title_id or title.get("titleText") is None:
            raise TitleNotFoundError(title_id, response)
        return response

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> TitleModel:
        """Load a title file into its model."""
        return model_validate_json(data, log_id or self.default_log_id)
