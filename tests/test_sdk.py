from sdk import events

def test_install_event():
    e = events.install_event("user123")
    assert "event_id" in e
    assert e["event_type"] == "Install"
    print("install_event test success:", e)

def test_purchase_event():
    e = events.purchase_event("user123", "SEK", 5.99, "product01")
    assert e["event_type"] == "Purchase"
    print("purchase_event test success:", e)

if __name__ == "__main__":
    test_install_event()
    test_purchase_event()
    print("All SDK tests passed")