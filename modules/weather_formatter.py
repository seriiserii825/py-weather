from name_tuples.nt_weather import NtWeather


def format_weather(weather: NtWeather) -> str:
    """ Formats the weather data for display."""
    wt = weather.weather_type
    print(f"wt: {wt}")
    print(f'wt.value: {wt.value}')
    return (f"{weather.city}, температура {weather.temperature}°C, "
            f"{weather.weather_type}\n"
            f"Восход: {weather.sunrise}\n"
            f"Закат: {weather.sunset}\n")
