"""Healthie tap class."""

from __future__ import annotations

from singer_sdk import Tap
from singer_sdk import typing as th  # JSON schema typing helpers

# TODO: Import your custom stream types here:
from tap_healthie import streams


class TapHealthie(Tap):
    """Healthie tap class."""

    name = "tap-healthie"

    # TODO: Update this section with the actual config values you expect:
    config_jsonschema = th.PropertiesList(
        th.Property(
            "environment",
            th.StringType,
            description="The name of the environment, 'Sandbox' or 'Production'",
        ),
        th.Property(
            "sandbox_api_key",
            th.StringType,
            secret=True,
            description="The Sandbox API Key for authenticating to Healthie's API service",
        ),
        th.Property(
            "production_api_key",
            th.StringType,
            secret=True,
            description="The Production API Key for authenticating to Healthie's API service",
        ),
        th.Property(
            "start_date",
            th.DateTimeType,
            description="The earliest record date to sync",
        ),
    ).to_dict()

    def discover_streams(self) -> list[streams.HealthieStream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """
        return [
            streams.AppointmentTypesStream(self),
            streams.UsersStream(self),
        ]


if __name__ == "__main__":
    TapHealthie.cli()
