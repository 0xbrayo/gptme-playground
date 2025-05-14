from urllib import response
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

openrouter_header =  {
    "HTTP-Referer": "https://github.com/gptme/gptme",
    "X-Title": "gptme",
}

api_key = os.environ.get("OPENROUTER_API_KEY")
if api_key is None:
    raise ValueError("OPENROUTER_API_KEY not found in environment variables.")

client = OpenAI(
    # This is the default and can be omitted
    api_key=api_key,
    )

response = client.responses.create(
    model="gpt-3.5-turbo",
    instructions="You are a coding assistant that talks like a pirate.",
    input="How do I check if a Python object is an instance of a class?",
)
print(response.choices[0].message.content)


