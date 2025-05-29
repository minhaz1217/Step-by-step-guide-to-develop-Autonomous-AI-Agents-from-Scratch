import os
from azure_open_ai import openAi


model = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
def generate_text_basic(
    prompt: str,
    model=model,
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

def generate_text_with_conversation(messages, model = model):
    response = openAi.chat.completions.create(
        model=model,
        messages=messages
    )
    return response.choices[0].message.content