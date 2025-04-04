import os
import uuid # Import uuid to generate session IDs
from google.genai import types
import vertexai
from vertexai import agent_engines

# --- Initialization ---

ecommerce_agent = vertexai.agent_engines.get('projects/17485694024/locations/us-central1/reasoningEngines/4615213251729293312')
print(f"Found deployed agent: {ecommerce_agent.name}")
print(f"Display Name: {ecommerce_agent.display_name}")

# --- Session Details ---
# Define a user ID (optional, depends if your agent logic specifically uses it via session state)
# user_id = "deployed_user_001"
# Generate a unique session ID for this specific chat instance
session_id = str(uuid.uuid4())

print(f"--- Starting Chat with Deployed Agent ---")
# print(f"User ID: {user_id}") # User ID isn't directly passed to deployed run()
print(f"Session ID: {session_id}")
print(f"Agent Name: {ecommerce_agent.display_name}")
print("Type 'quit' to end the chat.")
print("-" * 20)


# --- Chat Loop ---
while True:
    try:
        # 1. Get user input
        user_message = input("""
        You: """)

        # 2. Check for exit command
        if user_message.lower() == 'quit':
            print("--- Ending Chat ---")
            # Note: There's no direct 'delete_session' on the deployed agent resource object.
            # Sessions typically expire based on configuration or inactivity.
            break

        # 3. Prepare the message content for the deployed agent
        content = types.Content(
            parts=[types.Part(text=user_message)],
            role="user",
        )
        # The deployed agent's run method often expects the message payload as JSON string
        message_payload = content.model_dump_json()

        # 4. Send message to deployed agent and get response(s)
        print("Agent: ", end="", flush=True) # Print "Agent: " prefix, stay on the same line

        # The run method yields response chunks (events)
        full_response = ""
        # Note: The deployed ecommerce_agent.run() signature might primarily use session_id and message.
        # If user_id needs to be tracked, it's often done implicitly via session state
        # or needs to be included in the message/prompt structure if the agent needs it explicitly.
        events = ecommerce_agent.run(
            session_id=session_id, # Use the SAME session_id every time
            message=message_payload
            # user_id=user_id # user_id might not be a direct parameter here
        )

        # Process the stream of response events
        for event in events:
            # Check if the event dictionary has 'parts'
            if isinstance(event, dict) and 'parts' in event:
                 for part in event['parts']:
                    # Check if the part is a dictionary and has 'text'
                    if isinstance(part, dict) and 'text' in part:
                        text = part['text']
                        print(text, end="", flush=True) # Print agent response parts as they arrive
                        full_response += text
            # Handle potential other formats if necessary (e.g., direct string response)
            # elif isinstance(event, str):
            #    print(event, end="", flush=True)
            #    full_response += event


        print() # Add a newline after the agent's full response

    except EOFError:
        # Handle Ctrl+D or other EOF signals
        print("\n--- Chat ended by user (EOF) ---")
        break
    except KeyboardInterrupt:
        # Handle Ctrl+C
        print("\n--- Chat interrupted by user ---")
        break
    except Exception as e:
        print(f"\n--- An error occurred: {e} ---")
        # Optionally add more specific error handling for API errors
        # Decide if you want to break or continue on error
        break

# Optional: Indicate script has finished
print("--- Script finished ---")
