This small project is a simple system for tracking basic player events in a game such as install and purchase.

***Overview:***
1. SDK simulates what a game client would do:
    - Creates an event (install or purchase)

    - Sends it to the backend API via HTTP request

2. API receives that event:

    - Parses and structures it

    - Serializes it to json

    - Sends it to AWS Firehose

3. Firehose:

    - Normally would batch and deliver json events to S3

***How to run:***
1. Install dependencies:
    
    Create a python virtual environment and run the following
    ```
   pip install -r requirements.txt
    ```


2. Start the Flask API:
    ```
    python -m api.main
    ```

3. Send events:
    ```
    python -m sdk.client
    ```

4. Run tests:

    ```
    python -m tests.test_sdk
    python -m tests.test_api
    ```

***Design decisions:***

**Simplicity and modularity:**

I wanted this to be as easy as possible to understand, so everything is split into small, clear modules:

- events.py: Defines what an event looks like
- client.py: Handles sending events
- utils.py: A seperate module for helper functions tat can be used across all other modules
- main.py: Handles incoming API requests
- models.py: Converts data into Firehose and Snowflake-friendly format
- firehose_client.py: AWS logic

Each file does one simple job. If I added more events or destinations later, I could just create new modules without changing everything.

**Why Flask:**

Flask is quite lightweight and easy to use with just a few lines to make a REST API.
In a real production setup, I might switch to FastAPI becuase it is:
- Better performance with async support 
- it has built-in validation
- it has features to auto-generate docs for API

**Configurations and setup:**

Right now, I’ve hardcoded things like:
- The backend URL in client.py
- Stream name in main.py
- AWS credentials

In productio, these should never be hardcoded

Production example: 
- .env files or environment variables
- A config module (config.py)
- AWS secret manager or vault for saving secrets that could also be frtched on the run

**Data flow overview:**

Event SDK  ->  Flask API  -> Load to Firehose  -> Load to S3  ->  Load to Snowflake
- SDK: Creates and sends events as json
- Flask API: Receives and validates event data  
- Firehose: Batches and stores even json in S3
- Snowflake: Loads json data into a table using COPY INTO 

**Future improvemnts:**

1. Retires and error handling:
    If sending fails, the SDK could retry a few times 
2. Batching:
    Instead of sending every event immediately, batch multiple events and send them together this reduces network overhead.(Depending on need though, if realtime not necessary)
3. Config:
    Move all configurations to one config.py file. This makes it easier to have differnet environments like dev stage and prod
4. Validation
    Use better and more modularised schema valdiation solution. integrate something like great expecatations for example
5. Logging 
    Use a logging module instead of prints   
6. Event handling
    - Large volumes of events could be handles using a worker queue instead or kafka that the API or firehose could subscrie to
    - Asynchronous processing would allow independent services to consume event data without api dependence
    - A queue in the middle could help with scalability as well
7. Currency handling:      
    - store both original and converted amount in some base currency using a daily exchange rate table
9. To be productionready:
    - containarise the API (kubernetes or docker)
    - laod balancer needed
    - cicd and orchestration
    - health checkks, logging, and hardcodign of conffigs need to be removed 



