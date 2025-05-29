# hard coded agent

# so that we can use packages from one folder above
import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))


from sample_functions import get_weather
from openai_module import generate_text_basic


city = "Dhaka"
current_weather = get_weather(city)

prompt = f"""
Should I take an umbrella when going out today in {city} based on the following weather conditions: {current_weather}?
"""

response = generate_text_basic(prompt)
print(response)
