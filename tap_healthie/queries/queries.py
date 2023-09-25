APPOINTMENT_TYPES_QUERY = """
    query ($offset: Int) {
        appointmentTypesCount
        appointmentTypes(
            with_deleted_appt_types: true,
            offset: $offset
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
    }
"""

CHARTING_ITEMS_QUERY = """
    query ($user_id: String) {
        chartingItemsCount(user_id: $user_id)
        chartingItems(user_id: $user_id) {
            created_at
            custom_module_form_name
            filler_id
            form_answer_group {
                appointment {
                    id
                }
                autoscored_sections {
                    section_key
                    section_title
                    value
                }
                charting_note_addendums {
                    content
                    created_at
                    id
                    user {
                        id
                    }
                }
                created_at
                deleted_at
                filler {
                    id
                }
                finished
                form_answer_group_signings {
                    created_at
                    form_answer_group_id
                    id
                    user {
                        id
                    }
                }
                form_answers {
                    answer
                    created_at
                    custom_module_id
                    displayed_answer
                    id
                    label
                    user_id
                }
                group_appointment_attendees {
                    id
                }
                id
                individual_client_notes {
                    content
                    id
                    user {
                        id
                    }
                }
                is_group_appt_note
                locked_at
                locked_by {
                    id
                }
                name
                updated_at
                user {
                    id
                }
            }
            form_answer_group_id
            id
            is_document
            name
            provider_name
            signed
            use_for_charting
            use_for_program
        }
    }
"""

USERS_QUERY = """
    query ($offset: Int) {
        usersCount
        users(offset: $offset) {
            id
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
            policies {
                id
                effective_end
                effective_start
                insurance_plan {
                    id
                    is_accepted
                    name_and_id
                    payer_id
                    payer_name
                }
                insurance_plan_id
                priority_type
                name
                num
                group_num
                same_address_as_client
                holder_relationship
                holder_first
                holder_mi
                holder_last
                holder_gender
                holder_dob
                holder_location {
                    id
                    line1
                    line2
                    city
                    state
                    zip
                }
                updated_at
                user_id
            }
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
    }
"""

ORGANIZATION_MEMBERS_QUERY = """
    query ($offset: Int) {
        organizationMembersCount
        organizationMembers(offset: $offset) {
            id
            active
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
    }
"""

CPT_CODES_QUERY = """
    query ($offset: Int) {
        cptCodesCount
        cptCodes(offset: $offset, should_paginate: true) {
            code
            created_at
            description
            display_name
            id
            is_favorite
            updated_at
        }
    }
"""

ICD10_CODES_QUERY = """
    query ($offset: Int) {
        icdCodesCount
        icdCodes(offset: $offset, should_paginate: true) {
            code
            created_at
            description
            display_name
            id
            is_favorite
            updated_at
        }
    }
"""
