"""
This modeúle connects to AWS Firehose and loads the event straem data

In production:
- The Firehose stream batches incoming json events.
- Data is delivered to an S3 bucket.
- Snowflake ingests this data via Snowpipe or COPY INTO.

"""

from api.models import serialize_event
import boto3

def send_to_firehose(stream_name, event, aws_connections = None):
    """
    Send events from a given stream to firehose

    Args:
        stream_name (str): The Firehose delivery stream name.
        event (dict): The event dictionary to send.
        aws_connections (dict): A dict with aws connection detials. (Set to none in this case jsut o make things work)

    Returns:
        response (dict):  Now just a simple print just to mae things work but ideally the response from firehose put_record call
    """
    try:
        # convert event payload to json string
        serialized = serialize_event(event)

        # exqample of loading the event to firehose 
        '''session = boto3.Session(
            aws_access_key_id=aws_connections["secret_key_id"], 
            aws_secret_access_key=aws_connections["secret_key"], 
            region_name=aws_connections["region"])

        firehose = session.client("firehose")
        response = firehose.put_record(
            DeliveryStreamName=stream_name,
            Record={"Data": ...})
        '''

        # Just to make this work
        print(f"Sending {serialized} to stream '{stream_name}'")
        return {"ok": True, "message": "Event sent to AWS Firehose successfully"}

    except Exception as e:
        print(e)
        return {"ok": False, "error": str(e)}

'''
Example flow to snowflake:
- Events are sent to firehose
- Firehose writes to an s3 bucket
- Data can be loaded to snowflake using for exmaple snowflake stage tables or COPY INTO 
- This can be orchestrated usign tools such as dbt, airflow, etc..
'''
