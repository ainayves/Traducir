import os
import openai
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def davinci_translate(sentence):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=f"Translate this into 1. English, 2. Spanish and 3. Japanese:\n\n{sentence}\n\n1.",
    temperature=0.3,
    max_tokens=100,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
    )
    print(response)

    return response