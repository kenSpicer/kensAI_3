import os
from dotenv import load_dotenv
from google import genai
import argparse
from google.genai import types




load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")


parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

# Now we can access `args.user_prompt`
messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]


client = genai.Client(api_key=api_key)
response = client.models.generate_content(
    model='gemini-2.5-flash', contents='Why are episodes 7-9 so much worse than 1-6? Use one paragraph.'
    )

if not response.usage_metadata:
    raise RuntimeError("Gemini API response appears to be malformed")

if args.verbose:
    print("User prompt:", args.user_prompt)
    print("Prompt tokens:", response.usage_metadata.prompt_token_count)
    print("Response tokens:", response.usage_metadata.candidates_token_count)

print(response.text)
