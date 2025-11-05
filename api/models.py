"""
This module handles the event data. It structures event data so that they can be loaded on to snowflake
as well as serializing them into json to be loaded in firehose.
"""

import json

def parse_event_payload(event):
    """
    Parse event payload. This rebuilding of the payload is to 
    define the schema to be expected by for example snowflake as well as enforcing data type and filed name constriants.

    Args:
        event (dict): Raw event payload

    Returns:
        parsed event (dict): Normalized event data
    """
    parsed = {
        "event_id": str(event["event_id"]),
        "event_type": str(event["event_type"]),
        "user_id": str(event["user_id"]),
        "timestamp": str(event["timestamp"]),   # Stored as TIMESTAMP in Snowflake
        "currency": str(event["currency"]) if event["currency"] else None,
        "amount": float(event["amount"]) if event["amount"] else None,
        "product_id": str(event["product_id"]) if event["product_id"] else None,
        "raw_data": json.dumps(event)  # Keep the full event record
    }
    return parsed


def serialize_event(event):
    """
    Convert the event dict to json to be loaded to firehose.

    Args:
        event (dict): Parsed event data

    Returns:
        event string (string): json string representation of the event payload
    """
    parsed_event = parse_event_payload(event)
    return json.dumps(parsed_event)