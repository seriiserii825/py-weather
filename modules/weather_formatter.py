from name_tuples.nt_weather import NtWeather


def format_weather(weather: NtWeather) -> str:
    """Formats the weather data for display."""
    return (
        f"{weather.city}, температура {weather.temperature}°C, "
        f"{weather.weather_type.value}\n"
        f"Восход: {weather.sunrise}\n"
        f"Закат: {weather.sunset}\n"
    )
