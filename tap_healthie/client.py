"""GraphQL client handling, including HealthieStream base class."""

from __future__ import annotations

from singer_sdk.helpers.jsonpath import extract_jsonpath
from singer_sdk.streams import GraphQLStream
from singer_sdk.pagination import BaseOffsetPaginator


class OffsetPaginator(BaseOffsetPaginator):
    def __init__(self, start_value: int, page_size: int, query_name, records_jsonpath, *args: t.Any, **kwargs: t.Any):
        super().__init__(start_value, page_size, *args, **kwargs)
        self.count_jsonpath = f'$.data.{query_name}Count'
        self.records_jsonpath = records_jsonpath

    def has_more(self, response):
        data = response.json()
        return next(extract_jsonpath(self.count_jsonpath, data)) > self._value

    def get_next(self, response):
        data = response.json()
        self._page_size = len(list(extract_jsonpath(self.records_jsonpath, data)))
        return self._value + self._page_size


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

    @property
    def query_name(self) -> str:
        """Return the name of the object being queried in camelCase"""
        first, *others = self.name.split('_')
        return ''.join([first.lower(), *map(str.title, others)])

    def get_new_paginator(self):
        return OffsetPaginator(start_value=0, page_size=30, query_name = self.query_name, records_jsonpath=self.records_jsonpath)

    def get_url_params(self, context, next_page_token):
        params = {}
        if next_page_token:
            params["offset"] = next_page_token
        return params

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
