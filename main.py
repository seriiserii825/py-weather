from exceptions import ApiServiceError, CantGetCoordinates
from modules.coordinates import get_gps_coordinates
from modules.weather_api_service import get_weather
from modules.weather_formatter import format_weather
from utils import errorPrint


def main():
    try:
        coordinates = get_gps_coordinates()
    except CantGetCoordinates as e:
        errorPrint(e)
        return
    try:
        weather = get_weather(coordinates)
    except ApiServiceError as e:
        errorPrint(f"Error fetching weather data: {e}")
        return
    formatted_weather = format_weather(weather)
    print(formatted_weather)


if __name__ == "__main__":
    main()
