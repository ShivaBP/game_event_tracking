"""
This module defines the folwoing game events: install, purchase
Each function returns its corresponding event payload as a dictionary
"""

from sdk.utils import current_timestamp, generate_event_id

def install_event(user_id):
    """
    Create a install event
    
    Args:
        user_id (string): Unique identifier of the user
        
    Returns:
        event (dict): Install event payload
    """
    return {
        "event_id": generate_event_id(), 
        "event_type": "Install",
        "user_id": user_id,
        "timestamp": current_timestamp()
    }

def purchase_event(user_id, currency, amount, product_id=None):
    """
    Create a purchase event
    
    Args:
        user_id (string): Unique identifier of the user
        currency (string): Purchase currency
        amount (float): Purchased amoutn
        product_id (string) optional: Unique identifier of the purchased procuct
        
    Returns:
        event (dict): Purchase event payload
    """
    return {
        "event_id": generate_event_id(),
        "event_type": "Purchase",
        "user_id": user_id,
        "timestamp": current_timestamp(),
        "currency": currency,
        "amount": amount,
        "product_id": product_id
    }