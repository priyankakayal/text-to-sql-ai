# text_to_sql_v2.py — Adds multi-turn conversation memory

import os
from openai import OpenAI
from dotenv import load_dotenv
from schema import DATABASE_SCHEMA

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = f"""You are an expert SQL analyst. Convert questions to SQL.
Schema: {DATABASE_SCHEMA}
Rules: Return SQL first, then EXPLANATION: on a new line. Temperature: precise SQL only."""

def chat_sql_session():
    """Interactive multi-turn SQL chat session"""

    # conversation_history stores ALL previous messages.
    # This is how the LLM "remembers" what was asked before.
    conversation_history = []

    print("\n🤖 Multi-Turn SQL Assistant")
    print("Ask a question, then ask follow-ups! (e.g., 'Now filter to US only')")
    print("Type 'new' to start a fresh conversation. Type 'quit' to exit.\n")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == 'quit':
            break

        if user_input.lower() == 'new':
            conversation_history = []   # Clear memory, start fresh
            print("\n✨ New conversation started.\n")
            continue

        # Add user's message to history
        conversation_history.append({
            "role": "user",
            "content": user_input
        })

        # Send system prompt + FULL history to the API
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            temperature=0,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT}
            ] + conversation_history    # Full history included!
        )

        assistant_reply = response.choices[0].message.content.strip()

        # Add AI's reply to history (so it can reference it next turn)
        conversation_history.append({
            "role": "assistant",
            "content": assistant_reply
        })

        print(f"\nAI:\n{assistant_reply}\n")
        print(f"[Tokens: {response.usage.total_tokens} | History: {len(conversation_history)} messages]\n")


if __name__ == "__main__":
    chat_sql_session()