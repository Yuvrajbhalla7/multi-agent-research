

import os
from groq import Groq

# Reads GROQ_API_KEY from your environment. Set it before running, e.g.
#   setx GROQ_API_KEY "your-key-here"   (Windows, then restart terminal)
from dotenv import load_dotenv
load_dotenv()
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

MODEL = "llama-3.3-70b-versatile"  # good balance of speed and quality


def call_llm(system_prompt: str, user_prompt: str) -> str:
    """Send a system + user prompt to Groq and return the text response."""
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.3,
    )
    return response.choices[0].message.content