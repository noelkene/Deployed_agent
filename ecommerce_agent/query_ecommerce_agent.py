import vertexai
from vertexai import agent_engines
from google.genai import types


transcript_summary_agent = vertexai.agent_engines.get('projects/17485694024/locations/us-central1/reasoningEngines/4615213251729293312')

# Run the agent with this hard-coded input
events = transcript_summary_agent.run(
    session_id="new_user_session",
    message=types.Content(
        parts=[types.Part(text="""
            Virtual Agent: I'm an ecommerce Agent how can I help you?
            User: i have an issue with my order can I cancel it?
        """)],
        role="user",
    ).model_dump_json())

# Print the response
print("Agent Response:")
for event in events:
    for part in event['parts']:
        if 'text' in part:
            print(part['text'])
