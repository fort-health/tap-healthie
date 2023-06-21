"""Stream type classes for tap-healthie."""

from __future__ import annotations

from pathlib import Path

from singer_sdk.typing import (
    ArrayType,
    BooleanType,
    DateTimeType,
    IntegerType,
    NumberType,
    ObjectType,
    PropertiesList,
    Property,
    StringType,
    JSONTypeHelper,
)

from tap_healthie.client import HealthieStream
from tap_healthie.queries import (
    queries,
    schemas,
)

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


class AppointmentTypesStream(HealthieStream):
    """Appointment Types stream."""

    name = "appointment_types"
    query_name = "appointmentTypes"
    # schema_filepath = SCHEMAS_DIR / "appointment_types.json"
    schema = schemas.APPOINTMENT_TYPES_SCHEMA.to_dict()
    primary_keys = ["id"]
    records_jsonpath = f"$.data.{query_name}[*]"
    query = queries.APPOINTMENT_TYPES_QUERY


class UsersStream(HealthieStream):
    """Users stream."""

    name = "users"
    query_name = "users"
    schema = schemas.USERS_SCHEMA.to_dict()
    primary_keys = ["id"]
    records_jsonpath = f"$.data.{query_name}[*]"
    query = queries.USERS_QUERY


class OrganizationMembersStream(HealthieStream):
    """Organization Members stream."""

    name = "organization_members"
    query_name = "organizationMembers"
    schema = schemas.USERS_SCHEMA.to_dict()
    primary_keys = ["id"]
    records_jsonpath = f"$.data.{query_name}[*]"
    query = queries.ORGANIZATION_MEMBERS_QUERY
