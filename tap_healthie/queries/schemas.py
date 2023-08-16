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

APPOINTMENT_TYPES_SCHEMA = PropertiesList(
    Property("id", StringType),
    Property("is_group", BooleanType),
    Property("length", IntegerType),
    Property("name", StringType),
    Property("pricing", StringType),
    Property("pricing_option", StringType),
    Property("time_on_label", StringType),
    Property("user_group_id", StringType),
    Property("user_id", IntegerType),
)

CHARTING_ITEMS_SCHEMA = PropertiesList(
    Property("created_at", StringType),
    Property("custom_module_form_name", StringType),
    Property("filler_id", StringType),
    Property("form_answer_group_id", StringType),
    Property("id", StringType, required=True),
    Property("is_document", BooleanType),
    Property("name", StringType),
    Property("provider_name", StringType),
    Property("signed", BooleanType),
    Property("use_for_charting", BooleanType),
    Property("use_for_program", BooleanType),
    Property("user_id", StringType, required=True),
)

FORM_ANSWER_GROUPS_SCHEMA = PropertiesList(
    Property("appointment_id", StringType),
    Property(
        "autoscored_sections",
        ArrayType(
            ObjectType(
                Property("section_key", StringType),
                Property("section_title", StringType),
                Property("value", NumberType)
            )
        )
    ),
    Property(
        "charting_note_addendums",
        ArrayType(
            ObjectType(
                Property("content", StringType),
                Property("created_at", StringType),
                Property("id", StringType),
                Property("user_id", StringType),
            ),
        ),
    ),
    # Property("cms1500", ObjectType(...)) TODO: if needed one day
    Property("created_at", StringType),
    # Property("custom_module_form", ObjectType(...)) TODO: if needed one day
    Property("deleted_at", StringType),
    Property("filler_id", StringType),
    Property("finished", BooleanType),
    Property(
        "form_answer_group_signings",
        ArrayType(
            ObjectType(
                Property("created_at", StringType),
                Property("form_answer_group_id", StringType),
                Property("id", StringType),
                Property("user_id", StringType)
            )
        )
    ),
    # Property("form_answer_group_users_connections", ArrayType(ObjectType(...))) TODO: if needed one day
    Property(
        "form_answers",
        ArrayType(
            ObjectType(
                Property("answer", StringType),
                Property("created_at", StringType),
                Property("custom_module_id", StringType),
                Property("displayed_answer", StringType),
                Property("form_answer_group_id", StringType),
                Property("id", StringType),
                Property("label", StringType),
                Property("user_id", StringType)
            )
        )
    ),
    Property("group_appointment_attendees", ArrayType(StringType)),
    Property("id", StringType),
    Property(
        "individual_client_notes",
        ArrayType(
            ObjectType(
                Property("content", StringType),
                Property("id", StringType),
                Property("user_id", StringType)
            )
        )
    ),
    Property("is_group_appt_note", BooleanType),
    Property("locked_at", StringType),
    Property("locked_by_id", StringType),
    Property("name", StringType),
    Property("updated_at", StringType),
    Property("user_id", StringType)
)

USERS_SCHEMA = PropertiesList(
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
        "policies",
        ArrayType(
            ObjectType(
                Property("id", StringType),
                Property("effective_end", StringType),
                Property("effective_start", StringType),
                Property(
                    "insurance_plan",
                    ObjectType(
                        Property("id", StringType),
                        Property("is_accepted", BooleanType),
                        Property("name_and_id", StringType),
                        Property("payer_id", StringType),
                        Property("payer_name", StringType),
                    ),
                ),
                Property("insurance_plan_id", StringType),
                Property("name", StringType),
                Property("priority_type", StringType),
                Property("updated_at", StringType),
                Property("user_id", StringType),
            ),
        )
    ),
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
)
