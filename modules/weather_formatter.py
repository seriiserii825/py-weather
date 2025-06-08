from name_tuples.nt_weather import NtWeather


def format_weather(weather: NtWeather) -> str:
    """ Formats the weather data for display."""
    return "Current weather in {weather.city}:\n"
