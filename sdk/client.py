
"""
This module  client to send events to the  backend API
"""

import requests
from sdk import events

# API URL
BACKEND_URL = "http://localhost:8000"

def send_event(event):
    """
    Send a event dictionary request to the API

    Args:
        event (dict): Event payload
    """
    try:
        res = requests.post(BACKEND_URL + "/events", json=event)
        print("Sent", event["event_type"], "status:", res.status_code)
    except Exception as e:
        print("Failed to send", event["event_type"], e)

def send_install(user_id):
    """
    Create and send an install event for a given user

    Args:
        user_id (string): Unique identifier of the user
    """
    event = events.install_event(user_id)
    send_event(event)

def send_purchase(user_id, currency, amount, product_id=None):
    """
    Create and send a purchase event for a given user

    Args:
        user_id (string): Unique identifier of the user
        currency (string): Purchase currency
        amount (float): Purchased amoutn
        product_id (string) optional: Unique identifier of the purchased procuct
    """
    event = events.purchase_event(user_id, currency, amount, product_id)
    send_event(event)

if __name__ == "__main__":
    print("Sending sample events for demo")

    send_install("user123")
    send_purchase("user123", "SEK", 5, "item001")

    print("Sent")