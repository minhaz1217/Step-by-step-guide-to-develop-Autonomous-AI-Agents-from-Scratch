import os
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv(override=True)

openAi = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_VERSION"),
)


def test_azure_open_ai():
    response = openAi.chat.completions.create(
        model=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),  # model = "deployment_name".
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": "Does Azure OpenAI support customer managed keys?",
            },
            {
                "role": "assistant",
                "content": "Yes, customer managed keys are supported by Azure OpenAI.",
            },
            {"role": "user", "content": "Do other Azure services support this too?"},
        ],
    )
    print(response.choices[0].message.content)
