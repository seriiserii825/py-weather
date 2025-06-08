import os
import requests
from pathlib import Path
from dotenv import load_dotenv
from name_tuples.nt_coordinates import NtCoordinates


def get_weather(coordinates: NtCoordinates):
    """ Requests weather from openweather API and returns it as a string."""
    api_key = _get_api_key_from_env()
    info = _get_weather_info(api_key, coordinates)
    print(f"info: {info}")
    return info


def _get_api_key_from_env() -> str:
    """ Retrieves the API key from environment variables."""
    current_script_path = Path(__file__).resolve()
    print(f"current_script_path: {current_script_path}")
    # .env is 2 up levels
    dotenv_path = current_script_path.parents[1] / '.env'
    load_dotenv(dotenv_path)

    if not os.getenv("OPEN_WEATHER_API_KEY"):
        raise EnvironmentError(
            "OPEN_WEATHER_API_KEY environment variable not set,or not found .env.")
    api_key = os.getenv("OPEN_WEATHER_API_KEY")
    if not api_key:
        raise ValueError("API key not found in environment variables.")
    return api_key


def _get_weather_info(API_KEY: str, coordinates: NtCoordinates) -> dict:
    """ Fetches weather information from OpenWeather API"""
    """using the provided API key and coordinates."""
    lat = coordinates.latitude
    lon = coordinates.longitude

    try:
        url = (
            f"https://api.openweathermap.org/data/2.5/weather"
            f"?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
        )
        response = requests.get(url)
        data = response.json()
        return data
    except requests.RequestException as e:
        raise RuntimeError(f"Failed to fetch weather data: {e}")
