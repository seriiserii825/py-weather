from name_tuples.nt_coordinates import NtCoordinates
from name_tuples.nt_weather import EWeatherType, NtWeather


def get_weather(coordinates: NtCoordinates) -> NtWeather:
    """ Requests weather from openweather API and returns it as a string."""
    # This is a placeholder implementation.
    # In a real application, you would make an API call to OpenNtWeather
    # or another weather service.
    return NtWeather(
        temperature=20,
        weather_type=EWeatherType.CLEAR,
        sunrise="06:00 AM",
        sunset="08:00 PM",
        city="Sample City"
    )
