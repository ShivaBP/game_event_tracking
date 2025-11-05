"""
This module includes helper functions for the SDK
"""

import random
import string
import time

def current_timestamp():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())

def generate_event_id():
    """
    Generate a unique event ID by combining:
    - current timestamp in seconds
    - 4-character random alphanumeric UID
    """
    timestamp_part = str(int(time.time()))
    uid_part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    return f"{timestamp_part}-{uid_part}"