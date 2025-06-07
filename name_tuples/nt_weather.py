from typing import NamedTuple
from enum import Enum

Celsius = int


class WeatherType(Enum):
    THUNDERSTORM = "Thunderstorm"
    DRIZZLE = "Drizzle"
    RAIN = "Rain"
    SNOW = "Snow"
    CLEAR = "Clear"
    FOG = "Fog"
    CLOUDS = "Clouds"


class Weather(NamedTuple):
    temperature: Celsius
    weather_type: WeatherType
    sunrise: str
    sunset: str
    city: str
