from modules.coordinates import get_gps_coordinates
from modules.weather_api_service import get_weather
from modules.weather_formatter import format_weather


def main():
    coordinates = get_gps_coordinates()
    weather = get_weather(coordinates)
    format_weather(weather)


if __name__ == "__main__":
    main()
