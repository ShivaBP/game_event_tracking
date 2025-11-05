"""
This module receives events from the SDK,
structures and serialises the data that can then be loaded to AWS Firehose and snowflake
them to a mocked AWS Firehose client.
"""

from flask import Flask, request, jsonify
from api.firehose_client import send_to_firehose

app = Flask(__name__)

@app.route("/events", methods=["POST"])
def handle_event():
    """
    Handle incoming event POST requests in json 
    """
    event = request.get_json()

    if not event:
        return jsonify({"error": "no data provided"})

    print(f"Received event: {event}")

    # Send event to Firehose 
    result = send_to_firehose("game-events-stream", event)

    return jsonify(result)


if __name__ == "__main__":
    print("API running on http://localhost:8000")
    app.run(port=8000)
