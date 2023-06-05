"""GraphQL client handling, including HealthieStream base class."""

from __future__ import annotations

from singer_sdk.helpers.jsonpath import extract_jsonpath
from singer_sdk.streams import GraphQLStream
from singer_sdk.pagination import BaseOffsetPaginator


class Paginator(BaseOffsetPaginator):
    def has_more(self, response):
        data = response.json()
        return data.get("userCount") > self.current_value

    def get_next(self, response):
        data = response.json()
        return self._value + data.get("users").length()


class HealthieStream(GraphQLStream):
    """Healthie stream class."""

    @property
    def environment(self) -> str:
        """Return the environment based on API key format"""
        if self.config.get("api_key").startswith("gh_sbox"):
            return "sandbox"
        else:
            return "production"

    @property
    def url_base(self) -> str:
        """Return the API URL root, configurable via tap settings."""
        if self.environment == "sandbox":
            return "https://staging-api.gethealthie.com/graphql"
        else:
            return "https://api.gethealthie.com/graphql"

    @property
    def http_headers(self) -> dict:
        """Return the http headers needed.

        Returns:
            A dictionary of HTTP headers.
        """
        headers = {}
        if "api_key" in self.config:
            headers["Authorization"] = f"Basic {self.config.get('api_key')}"
        headers["AuthorizationSource"] = "API"
        return headers

    # def get_new_paginator(self, response, object, count_object):
    #     count = response.get(count_object)
    #     length = response.get(object).length()
    #     return length if count > length else 0

    def parse_response(self, response: requests.Response) -> Iterable[dict]:
        """Parse the response and return an iterator of result records.

        Args:
            response: The HTTP ``requests.Response`` object.

        Yields:
            Each record from the source.
        """
        yield from extract_jsonpath(self.records_jsonpath, input=response.json())

    # def post_process(
    #     self,
    #     row: dict,
    #     context: dict | None = None,  # noqa: ARG002
    # ) -> dict | None:
    #     """As needed, append or transform raw data to match expected structure.

    #     Args:
    #         row: An individual record from the stream.
    #         context: The stream context.

    #     Returns:
    #         The updated record dictionary, or ``None`` to skip the record.
    #     """
    #     # TODO: Delete this method if not needed.
    #     return row
