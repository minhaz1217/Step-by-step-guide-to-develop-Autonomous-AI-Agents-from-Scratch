# react agent with function

# so that we can use packages from one folder above
import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)


from sample_functions import get_weather
from openai_module import generate_text_with_conversation
from prompts import react_system_prompt_json_action
from json_helpers import extract_json

# Available actions are:

available_actions = {"get_weather": get_weather}

city = "Dhaka"
current_weather = get_weather(city)

prompt = f"""
Should I take an umbrella when going out today in {city}?
"""

prompt = f"""
Is it a good day to store water in {city}?
"""

messages = [
    {"role": "system", "content": react_system_prompt_json_action},
    {"role": "user", "content": prompt},
]


turn_count = 1
max_turns = 3
while turn_count < max_turns:
    print(f"Loop: {turn_count}")
    print("-----------------------")
    turn_count += 1

    response = generate_text_with_conversation(messages)
    print(f"Response from the model: {response}")


    # instruct model to call the function
    json_function = extract_json(response)
    print(f"Extracted JSON functions {json_function}")

    if json_function:
        function_name = json_function[0]["function_name"]
        function_params = json_function[0]["function_params"]
        if function_name not in available_actions:
            raise Exception(f"Unknown action: {function_name}: {function_params}")
        print(f" -- running {function_name}: {function_params}")
        action_function = available_actions[function_name]

        result = action_function(**function_params)
        function_result_message = f"Action_Response: {result}"
        messages.append({"role": "user", "content": function_result_message})
        print(function_result_message)
