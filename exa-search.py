from exa_py import Exa
from dotenv import load_dotenv
from openai import api_key
import os

load_dotenv()

api_key = os.environ.get("EXA_API_KEY")
if api_key is None:
    raise ValueError("EXA_API_KEY not found in environment variables.")
exa = Exa(api_key=api_key)

response = exa.answer(
    "Who has the third most contributions to ActivityWatch?",
    text=True
)
print(response.answer)
# Brayo has the third most contributions to ActivityWatch. ([activitywatch.net](https://activitywatch.net/contributors))