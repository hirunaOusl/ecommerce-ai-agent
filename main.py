
import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

# Connect to Gemini
client = genai.Client(api_key=api_key)

# Send a message
response = client.models.generate_content(
    model="gemini-3.5-flash-lite",  
    contents="Hello! Introduce yourself as an AI shopping assistant."
)

# Display AI response
print("AI Agent:")
print(response.text)
