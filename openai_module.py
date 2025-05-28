import os
from azure_open_ai import openAi


def generate_text_basic(
    prompt: str,
    model=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    system_prompt: str = "You are a helpful bot that answers with max 3 lines.",
):
    response = openAi.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ],
    )
    return response.choices[0].message.content
