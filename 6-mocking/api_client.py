
def fetch_weather_data(city):
    return {
        "city": city,
        "temp": 25,
        "condition": "Sunny",
        "humidity": 40,
    }

def fetch_forecast(city, days=3):
    return [
        {"day": "Monday", "temp": 25, "condition": "Sunny"},
        {"day": "Tuesday", "temp": 22, "condition": "Cloudy"},
        {"day": "Wednesday", "temp": 20, "condition": "Rainy"},
    ][:days]


def get_current_hour():
    return 12
