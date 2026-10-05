# TODO: Validate
"""Exceptions."""

from __future__ import annotations

from typing import Any


# TODO: Validate
class IAmTheDBError(Exception):
    """Base exception for IAmTheDB."""

    response: str | dict[str, Any] | None = None
    """The data that caused the error, or None if there was none."""


# TODO: Validate
class HTTPError(IAmTheDBError):
    """Raised when HTTP request fails with unexpected status code."""

    # TODO: Validate
    def __init__(
        self,
        status_code: int,
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize the HTTPError with the status code and response body."""
        self.status_code = status_code
        self.response = response
        super().__init__(f"Unexpected response status code: {status_code}")


# TODO: Validate
class TitleNotFoundError(IAmTheDBError):
    """Raised when the requested title does not exist or the id is not a title id."""

    # TODO: Validate
    def __init__(self, title_id: str, response: str) -> None:
        """Initialize with the title id and the originating response."""
        self.title_id = title_id
        self.response = response
        super().__init__(f"No title found for {title_id}")


# TODO: Validate
class TitleListNotFoundError(IAmTheDBError):
    """Raised when the requested list does not exist or is not a list of titles."""

    # TODO: Validate
    def __init__(self, list_id: str, response: str) -> None:
        """Initialize with the list id and the originating response."""
        self.list_id = list_id
        self.response = response
        super().__init__(f"No title list found for {list_id}")
