"""Stream type classes for tap-healthie."""

from __future__ import annotations

from pathlib import Path

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_healthie.client import HealthieStream

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


class AppointmentTypesStream(HealthieStream):
    """Appointment Types stream."""

    name = "appointment_types"
    schema_filepath = SCHEMAS_DIR / "appointment_types.json"
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
    schema_filepath = SCHEMAS_DIR / "users.json"
    primary_keys = ["id"]
    records_jsonpath = "$.data.users[*]"
    query = """
        usersCount
        users {
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
