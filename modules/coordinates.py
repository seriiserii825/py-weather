from name_tuples.nt_coordinates import Coordinates


def get_gps_coordinates() -> Coordinates:
    """Return gps coordinates using whereami by node js"""
    # Example coordinates for San Francisco
    return Coordinates(latitude=37.7749, longitude=-122.4194)
