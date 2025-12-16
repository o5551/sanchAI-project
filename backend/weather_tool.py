import requests

def get_weather(city: str):
    url = f"https://wttr.in/{city}?format=j1"
    response = requests.get(url)

    if response.status_code != 200:
        return "Unable to fetch weather."

    data = response.json()
    current = data["current_condition"][0]

    temp = current["temp_C"]
    desc = current["weatherDesc"][0]["value"]

    return f"It is {temp}°C in {city}. Weather is {desc}."
