from api.firehose_client import send_to_firehose

def test_send_to_firehose():
    event = {
        "event_id": "1234-abcd",
        "event_type": "Install",
        "user_id": "user001",
        "timestamp": "2025-11-04T12:00:00",
        "currency": "SEK",
        "amount": "12",
        "product_id": "1234-efgh"
    }

    result = send_to_firehose("test-stream", event)
    assert result["ok"] is True
    print("Sent event data to firehose successfully", result)

if __name__ == "__main__":
    test_send_to_firehose()
    print("API testing passed")