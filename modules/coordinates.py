from name_tuples.Coordinates import Coordinates


def get_gps_coordinates() -> Coordinates:
    """Return gps coordinates using whereami by node js"""
    return Coordinates(latitude=37.7749, longitude=-122.4194)  # Example coordinates for San Francisco
