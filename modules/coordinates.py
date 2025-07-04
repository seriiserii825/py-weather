from subprocess import PIPE, Popen

from config import USE_ROUNDED_COORDINATES
from exceptions import CantGetCoordinates
from name_tuples.nt_coordinates import NtCoordinates


def get_gps_coordinates() -> NtCoordinates:
    """Return gps coordinates using whereami by node js"""
    coordinates = _get_whereami_output()
    return _round_coordinates(coordinates)


def _get_whereami_output() -> NtCoordinates:
    # process = Popen(['whereami', '-f', 'json'], stdout=PIPE, stderr=PIPE)
    process = Popen(["curl", "-s", "ipinfo.io/loc"], stdout=PIPE, stderr=PIPE)
    # Capture the output and error streams
    (output, error) = process.communicate()
    # Check if the command was successful
    exit_code = process.wait()
    if error is not None and exit_code != 0:
        raise CantGetCoordinates(f"Error getting coordinates: {error.decode().strip()}")

    output = output.strip()
    decoded = output.decode().strip()

    coord_list = [float(coord) for coord in decoded.split(",")]
    if len(coord_list) != 2:
        raise CantGetCoordinates("Invalid coordinates format received.")
    if not all(isinstance(coord, float) for coord in coord_list):
        raise CantGetCoordinates("Coordinates must be floats.")
    return NtCoordinates(latitude=coord_list[0], longitude=coord_list[1])


def _round_coordinates(coordinates: NtCoordinates):
    """Round coordinates if USE_ROUNDED_COORDINATES is True."""
    if USE_ROUNDED_COORDINATES:
        return NtCoordinates(
            latitude=round(coordinates.latitude, 1),
            longitude=round(coordinates.longitude, 1),
        )
    return coordinates
