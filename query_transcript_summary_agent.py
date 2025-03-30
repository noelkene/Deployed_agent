import vertexai
from vertexai import agent_engines
from google.genai import types


transcript_summary_agent = vertexai.agent_engines.get('projects/17485694024/locations/us-central1/reasoningEngines/8391059326814388224')

# Run the agent with this hard-coded input
events = transcript_summary_agent.run(
    session_id="new_user_session",
    message=types.Content(
        parts=[types.Part(text="""
            Virtual Agent: Hi, I am a vehicle sales agent. How can I help you?
            User: I'd like to buy a boat.
            Virtual Agent: A big boat, or a small boat?
            User: How much boat will $50,000 get me?
            Virtual Agent: That will get you a very nice boat.
            User: Let's do it!
        """)],
        role="user",
    ).model_dump_json())

# Print the response
print("Agent Response:")
for event in events:
    for part in event['parts']:
        if 'text' in part:
            print(part['text'])

