import os
import requests

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")


@tool
def get_weather(city: str) -> str:
    """Get the current weather for a city."""

    url = "https://api.weatherapi.com/v1/current.json"

    params = {
        "key": API_KEY,
        "q": city,
        "aqi": "no"
    }

    response = requests.get(url, params=params)
    data = response.json()

    current = data["current"]
    location = data["location"]

    return f"""
Weather in {location["name"]}, {location["country"]}
Temperature: {current["temp_c"]}°C
Feels like: {current["feelslike_c"]}°C
Condition: {current["condition"]["text"]}
Humidity: {current["humidity"]}%
Wind: {current["wind_kph"]} km/h
"""


agent = create_agent(
    model="google_genai:gemini-3.5-flash-lite",
    tools=[get_weather]
)


# question = input("Ask me about the weather: ")

# result = agent.invoke({
#     "messages": [
#         {
#             "role": "user",
#             "content": question
#         }
#     ]
# })


# response = result["messages"][-1]

# for block in response.content:
#     if block["type"] == "text":
#         print(block["text"])