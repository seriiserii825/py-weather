from name_tuples.nt_coordinates import NtCoordinates
from name_tuples.nt_weather import Weather, WeatherType


def get_weather(coordinates: NtCoordinates) -> Weather:
    """ Requests weather from openweather API and returns it as a string."""
    # This is a placeholder implementation.
    # In a real application, you would make an API call to OpenWeather
    # or another weather service.
    return Weather(
        temperature=20,
        weather_type=WeatherType.CLEAR,
        sunrise="06:00 AM",
        sunset="08:00 PM",
        city="Sample City"
    )
