from exceptions import ApiServiceError
from modules.coordinates import get_gps_coordinates
from modules.weather_api_service import get_weather
from modules.weather_formatter import format_weather
from utils import errorPrint


def main():
    coordinates = get_gps_coordinates()
    try:
        weather = get_weather(coordinates)
    except ApiServiceError as e:
        errorPrint(f"Error fetching weather data: {e}")
        return
    print(f"weather: {weather}")
    format_weather(weather)


if __name__ == "__main__":
    main()
