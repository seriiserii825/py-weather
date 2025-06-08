from typing import NamedTuple
from enum import Enum

Celsius = int


class EWeatherType(Enum):
    THUNDERSTORM = "Thunderstorm"
    DRIZZLE = "Drizzle"
    RAIN = "Rain"
    SNOW = "Snow"
    CLEAR = "Clear"
    FOG = "Fog"
    CLOUDS = "Clouds"


class NtWeather(NamedTuple):
    temperature: Celsius
    weather_type: EWeatherType
    sunrise: str
    sunset: str
    city: str
