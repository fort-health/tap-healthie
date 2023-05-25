"""GraphQL client handling, including HealthieStream base class."""

from __future__ import annotations

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
    def url_base(self) -> str:
        """Return the API URL root, configurable via tap settings."""
        if self.config.get("environment").lower() == "sandbox":
            url = "https://staging-api.gethealthie.com/graphql"
        else:
            url = "https://api.gethealthie.com/graphql"
        return url

    @property
    def http_headers(self) -> dict:
        """Return the http headers needed.

        Returns:
            A dictionary of HTTP headers.
        """
        headers = {}
        if self.config.get("environment").lower() == "sandbox":
            environment = "sandbox"
        else:
            environment = "production"
        api_key_name = f"{environment}_api_key"
        if api_key_name in self.config:
            api_key = self.config.get(api_key_name)
            headers["Authorization"] = f"Basic {api_key}"
        headers["AuthorizationSource"] = "API"
        return headers

    # def get_new_paginator(self, response, object, count_object):
    #     count = response.get(count_object)
    #     length = response.get(object).length()
    #     return length if count > length else 0

    # def parse_response(self, response: requests.Response) -> Iterable[dict]:
    #     """Parse the response and return an iterator of result records.

    #     Args:
    #         response: The HTTP ``requests.Response`` object.

    #     Yields:
    #         Each record from the source.
    #     """
    #     # TODO: Parse response body and return a set of records.
    #     resp_json = response.json()
    #     yield from resp_json.get("<TODO>")

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
