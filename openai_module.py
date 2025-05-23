from openai import OpenAI
import os
from dotenv import load_dotenv


load_dotenv(override=True)

openai = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_text_basic(
    prompt: str,
    model="gpt-3.5-turbo",
    system_prompt: str = "You are a helpful bot that answers with max 3 lines.",
):
    response = openai.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ],
    )
    return response.choices[0].message.content
