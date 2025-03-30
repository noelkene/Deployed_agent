# Agent Engine A2A Test

This brief documentation is for the test of connecting to Agent Engine.


### Install dependencies

Install dependencies with:

```
python3 -m pip install --upgrade -r requirements.txt
```


### Authenticate


Point your application default env variable to the credential file:

```
export GOOGLE_APPLICATION_CREDENTIALS=platinum-banner-303105-7d0d2ba2a783.json
```


### Run agent one: Transcript Summarizer

"""Summarizes a transcript provided in plain text."""

Example input (hardcoded into query file):
"""
Virtual Agent: Hi, I am a vehicle sales agent. How can I help you?
User: I'd like to buy a boat.
Virtual Agent: A big boat, or a small boat?
User: How much boat will $50,000 get me?
Virtual Agent: That will get you a very nice boat.
User: Let's do it!
"""

Run with:
```
python3 query_transcript_summarizer.py
```

Should return:
```
Agent Response:
The virtual agent introduces itself as a vehicle sales agent. The user states they want to buy a boat and asks what kind of boat $50,000 will buy. The virtual agent responds that it will buy a very nice boat, and the user says "Let's do it!".

```

