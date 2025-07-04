import ast
import json
import os
from datetime import datetime
from json.decoder import JSONDecodeError
from pathlib import Path
from typing import Literal, TypeAlias

import requests
from dotenv import load_dotenv

from exceptions import ApiServiceError
from name_tuples.nt_coordinates import NtCoordinates
from name_tuples.nt_weather import EWeatherType, NtWeather

Celsius: TypeAlias = int


def get_weather(coordinates: NtCoordinates):
    """Requests weather from openweather API and returns it as a string."""
    api_key = _get_api_key_from_env()
    info = _get_weather_json_from_api(api_key, coordinates)
    json_str = _prepare_to_json(str(info))
    result = _parse_json_to_dict(json_str)
    return result


def _get_api_key_from_env() -> str:
    """Retrieves the API key from environment variables."""
    current_script_path = Path(__file__).resolve()
    # .env is 2 up levels
    dotenv_path = current_script_path.parents[1] / ".env"
    load_dotenv(dotenv_path)

    if not os.getenv("OPEN_WEATHER_API_KEY"):
        raise ApiServiceError("OPEN_WEATHER_API_KEY not found in .env file.")
    api_key = os.getenv("OPEN_WEATHER_API_KEY")
    if not api_key:
        raise ApiServiceError("API key is empty in .env file.")
    return api_key


def _get_weather_json_from_api(API_KEY: str, coordinates: NtCoordinates) -> str:
    """Fetches weather information from OpenWeather API"""
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
        raise ApiServiceError(f"Error fetching weather data: {e}")


def _prepare_to_json(str_from_api: str):
    data = ast.literal_eval(str_from_api)
    return json.dumps(data, indent=2, ensure_ascii=False)


def _parse_json_to_dict(openweather_response: str) -> NtWeather:
    """Parses JSON string to a dictionary."""
    try:
        openweather_dict = json.loads(openweather_response)
    except JSONDecodeError:
        raise ApiServiceError("Invalid JSON response from OpenWeather API.")
    return NtWeather(
        temperature=_parse_temperature(openweather_dict),
        weather_type=_parse_weather_type(openweather_dict),
        sunrise=_parse_sun_time(openweather_dict, "sunrise"),
        sunset=_parse_sun_time(openweather_dict, "sunset"),
        city=_parse_city(openweather_dict),
    )


def _parse_temperature(openweather_dict: dict) -> Celsius:
    return round(openweather_dict["main"]["temp"])


def _parse_weather_type(openweather_dict: dict) -> EWeatherType:
    try:
        weather_type_id = str(openweather_dict["weather"][0]["id"])
    except (IndexError, KeyError):
        raise ApiServiceError("Weather type ID not found in response.")
    weather_types = {
        "1": EWeatherType.THUNDERSTORM,
        "3": EWeatherType.DRIZZLE,
        "5": EWeatherType.RAIN,
        "6": EWeatherType.SNOW,
        "7": EWeatherType.FOG,
        "800": EWeatherType.CLEAR,
        "80": EWeatherType.CLOUDS,
    }
    for _id, _weather_type in weather_types.items():
        if weather_type_id.startswith(_id):
            return _weather_type
    raise ApiServiceError(f"Unknown weather type ID: {weather_type_id}")


def _parse_sun_time(
    openweather_dict: dict, time: Literal["sunrise"] | Literal["sunset"]
) -> str:
    formated_time = datetime.fromtimestamp(openweather_dict["sys"][time])
    return formated_time.strftime("%H:%M:%S")


def _parse_city(openweather_dict: dict) -> str:
    try:
        return openweather_dict["name"]
    except KeyError:
        raise ApiServiceError("City name not found in response.")
