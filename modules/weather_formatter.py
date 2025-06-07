from name_tuples.nt_weather import Weather


def format_weather(weather: Weather) -> str:
    """ Formats the weather data for display."""
    return "Current weather in {weather.city}:\n"
