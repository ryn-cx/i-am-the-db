# TODO: Validate
"""Contains the TitleList class."""

from __future__ import annotations

import json
from logging import NullHandler, getLogger

from i_am_the_db.base_api_endpoint import BaseEndpoint
from i_am_the_db.exceptions import TitleListNotFoundError
from i_am_the_db.title_list.models import TitleListModel, model_validate_json

logger = getLogger(__name__)
logger.addHandler(NullHandler())

QUERY = """
query TitleList($id: ID!, $first: Int!, $after: ID) {
  list(id: $id) {
    id
    name { originalText }
    description { originalText { plainText } }
    listType { id }
    items(first: $first, after: $after) {
      total
      pageInfo { hasNextPage endCursor }
      edges {
        node {
          listItem {
            ... on Title {
              id
              titleText { text }
              titleType { id text isSeries isEpisode }
              releaseYear { year endYear }
            }
          }
        }
      }
    }
  }
}
"""
"""One page of the titles on a list."""

PAGE_SIZE = 250


# TODO: Validate
class TitleList(BaseEndpoint):
    """Contains the titles on a user's list.

    A list is looked up by its IMDb id, e.g. ls504392170 in
    https://www.imdb.com/list/ls504392170/.

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
    def __call__(
        self,
        list_id: str,
        first: int = PAGE_SIZE,
        after: str | None = None,
    ) -> TitleListModel:
        """Download and parse one page of the list."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(self.download(list_id, first, after), log_id)

    # TODO: Validate
    def download(
        self,
        list_id: str,
        first: int = PAGE_SIZE,
        after: str | None = None,
    ) -> str:
        """Download one page of the list.

        Raises:
            TitleListNotFoundError: If no list of titles is under that id.
        """
        log_id = self.get_log_id(self.download, locals())
        response = self._client.download(
            QUERY,
            variables={"id": list_id, "first": first, "after": after},
            log_id=log_id,
        )
        return self._validate_download(response, list_id)

    # TODO: Validate
    def download_all(self, list_id: str) -> list[str]:
        """Download every page of the list."""
        pages: list[str] = []
        after: str | None = None
        while True:
            page = self.download(list_id, after=after)
            pages.append(page)
            page_info = json.loads(page)["data"]["list"]["items"]["pageInfo"]
            if not page_info["hasNextPage"]:
                return pages
            after = page_info["endCursor"]

    # TODO: Validate
    @staticmethod
    def _validate_download(response: str, list_id: str) -> str:
        # A missing list comes back as an error with a list holding only its id,
        # and an id that is not a list id comes back as an error with no list.
        # A list of people or images has an item for each entry that is not a title.
        title_list = (json.loads(response).get("data") or {}).get("list") or {}
        if (
            title_list.get("id") != list_id
            or (title_list.get("listType") or {}).get("id") != "TITLES"
        ):
            raise TitleListNotFoundError(list_id, response)
        return response

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> TitleListModel:
        """Load a list file into its model."""
        return model_validate_json(data, log_id or self.default_log_id)
