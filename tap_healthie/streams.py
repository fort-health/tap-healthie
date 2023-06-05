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

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


class AppointmentTypesStream(HealthieStream):
    """Appointment Types stream."""

    name = "appointment_types"
    # schema_filepath = SCHEMAS_DIR / "appointment_types.json"
    schema = PropertiesList(
        Property("id", StringType),
        Property("is_group", BooleanType),
        Property("length", IntegerType),
        Property("name", StringType),
        Property("pricing", StringType),
        Property("pricing_option", StringType),
        Property("time_on_label", StringType),
        Property("user_group_id", StringType),
        Property("user_id", IntegerType),
    ).to_dict()
    primary_keys = ["id"]
    records_jsonpath = "$.data.appointmentTypes[*]"
    query = """
        appointmentTypes(
            should_paginate: false,
            with_deleted_appt_types: true
        ) {
            id
            is_group
            length
            name
            pricing
            pricing_option
            time_on_label
            user_group_id
            user_id
        }
    """


class UsersStream(HealthieStream):
    """Users stream."""

    name = "users"
    # schema_filepath = SCHEMAS_DIR / "users.json"
    schema = PropertiesList(
        Property("active", BooleanType),
        Property(
            "appointments",
            ArrayType(
                ObjectType(
                    Property("actual_duration", StringType),
                    Property("appointment_category", StringType),
                    Property("appointment_inclusions_count", IntegerType),
                    Property("appointment_label", StringType),
                    Property("appointment_location_id", StringType),
                    Property("appointment_type_id", IntegerType),
                    Property(
                        "assigned_groups",
                        ArrayType(
                            ObjectType(
                                Property("id", StringType),
                                Property("name", StringType),
                            )
                        )
                    ),
                    Property(
                        "attended_clients",
                        ArrayType(
                            ObjectType(
                                Property("id", StringType),
                                Property("user_id", StringType),
                                Property("attended", BooleanType),
                                Property("cancelled", BooleanType),
                                Property("confirmed", BooleanType),
                            )
                        )
                    ),
                    Property(
                        "attendees",
                        ArrayType(
                            ObjectType(
                                Property("id", StringType),
                            )
                        )
                    ),
                    Property("confirmed", BooleanType),
                    Property("created_at", StringType),
                    Property("current_position_in_recurring_series", IntegerType),
                    Property("date", StringType),
                    Property("deleted_at", StringType),
                    Property("end", StringType),
                    Property("id", StringType),
                    Property("initiator_id", StringType),
                    Property("is_blocker", BooleanType),
                    Property("is_group", BooleanType),
                    Property("is_zoom_chat", BooleanType),
                    Property("last_client_conversation_id", StringType),
                    Property("length", IntegerType),
                    Property("location", StringType),
                    Property("notes", StringType),
                    Property("other_party_id", IntegerType),
                    Property("patient_reschedule_count", IntegerType),
                    Property("pm_status", StringType),
                    Property("pm_status_changed_at", StringType),
                    Property(
                        "provider",
                        ObjectType(
                            Property("id", StringType),
                        )
                    ),
                    Property("provider_name", StringType),
                    Property(
                        "providers",
                        ArrayType(
                            ObjectType(
                                Property("id", StringType),
                            )
                        )
                    ),
                    Property("reason", StringType),
                    Property(
                        "recurring_appointment",
                        ObjectType(
                            Property("id", StringType),
                        )
                    ),
                    Property("scheduled_by", StringType),
                    Property("start", StringType),
                    Property("title", StringType),
                    Property("updated_at", StringType),
                    Property("use_zoom", BooleanType),
                    Property("user_id", IntegerType),
                    Property(
                        "zoom_cloud_recording_urls",
                        ArrayType(
                            StringType
                        )
                    ),
                )
            )
        ),
        Property("created_at", StringType),
        Property("dietitian_id", StringType),
        Property("first_name", StringType),
        Property("full_legal_name", StringType),
        Property("full_name", StringType),
        Property("gender", StringType),
        Property("gender_identity", StringType),
        Property("gender_identity_code", StringType),
        Property("group_name", StringType),
        Property("human_id", StringType),
        Property("id", StringType, required=True),
        Property("is_active_provider", BooleanType),
        Property("is_first_time_provider", BooleanType),
        Property("is_org", BooleanType),
        Property("is_org_admin", BooleanType),
        Property("is_org_with_multiple_users", BooleanType),
        Property("is_owner", BooleanType),
        Property("is_patient", BooleanType),
        Property("is_super_admin", BooleanType),
        Property("is_trialing", BooleanType),
        Property("last_activity", StringType),
        Property("last_name", BooleanType),
        Property("last_sign_in_at", StringType),
        Property("next_appt_date", StringType),
        Property("patients_count", IntegerType),
        Property("pronouns", StringType),
        Property(
            "providers",
            ArrayType(
                ObjectType(
                    Property("id", StringType)
                )
            )
        ),
        Property("record_identifier", StringType),
        Property("referring_provider_name", StringType),
        Property("referring_provider_npi", StringType),
        Property("true_human_id", StringType),
        Property("updated_at", StringType),
    ).to_dict()
    primary_keys = ["id"]
    records_jsonpath = "$.data.users[*]"
    query = """
        usersCount
        users {
            active
            appointments {
                actual_duration
                appointment_category
                appointment_inclusions_count
                appointment_label
                appointment_location_id
                appointment_type_id
                assigned_groups {
                    id
                    name
                }
                attended_clients {
                    id
                    user_id
                    attended
                    cancelled
                    confirmed
                }
                attendees {
                    id
                }
                confirmed
                created_at
                current_position_in_recurring_series
                date
                deleted_at
                end
                id
                initiator_id
                is_blocker
                is_group
                is_zoom_chat
                last_client_conversation_id
                length
                location
                notes
                other_party_id
                patient_reschedule_count
                pm_status
                pm_status_changed_at
                provider {
                    id
                }
                provider_name
                providers {
                    id
                }
                reason
                recurring_appointment {
                    id
                }
                scheduled_by
                start
                title
                updated_at
                use_zoom
                user_id
                zoom_cloud_recording_urls
            }
            created_at
            dietitian_id
            first_name
            full_legal_name
            full_name
            gender
            gender_identity
            gender_identity_code
            group_name
            human_id
            id
            is_active_provider
            is_first_time_provider
            is_org
            is_org_admin
            is_org_with_multiple_users
            is_owner
            is_patient
            is_super_admin
            is_trialing
            last_activity
            last_name
            last_sign_in_at
            next_appt_date
            patients_count
            pronouns
            providers {
                id
            }
            record_identifier
            referring_provider_name
            referring_provider_npi
            true_human_id
            updated_at
        }
        """
