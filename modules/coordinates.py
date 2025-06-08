import json
import re
from subprocess import Popen, PIPE
from config import USE_ROUNDED_COORDINATES
from exceptions import CantGetCoordinates
from name_tuples.nt_coordinates import NtCoordinates


def get_gps_coordinates() -> NtCoordinates:
    """Return gps coordinates using whereami by node js"""
    output_lines = _get_whereami_output()
    coordinates: NtCoordinates = _get_coordinates_from_list(output_lines)
    return _round_coordinates(coordinates)


def _get_whereami_output() -> list[str]:
    # Assuming 'whereami' is a command-line tool that returns GPS coordinates
    process = Popen(['whereami', '-f', 'json'], stdout=PIPE, stderr=PIPE)
    # Capture the output and error streams
    (output, error) = process.communicate()
    # Check if the command was successful
    exit_code = process.wait()
    if error is not None and exit_code != 0:
        raise CantGetCoordinates(
            f"Error getting coordinates: {error.decode().strip()}")

    return output.decode(errors='ignore').splitlines()


def _get_coordinates_from_list(output_lines: list[str]) -> NtCoordinates:
    json_pattern = re.compile(r'{.*"latitude".*"longitude".*}')
    for line in output_lines:
        match = json_pattern.search(line)
        if match:
            try:
                coords = json.loads(match.group())
                latitude = coords.get('latitude')
                longitude = coords.get('longitude')
                if USE_ROUNDED_COORDINATES:
                    latitude = round(latitude, 1)
                    longitude = round(longitude, 1)
                return NtCoordinates(
                    latitude=latitude,
                    longitude=longitude
                )
            except json.JSONDecodeError as e:
                raise CantGetCoordinates(f"Failed to decode JSON: {e}")
    raise CantGetCoordinates("No valid GPS coordinates found in output.")


def _round_coordinates(coordinates: NtCoordinates):
    """Round coordinates if USE_ROUNDED_COORDINATES is True."""
    if USE_ROUNDED_COORDINATES:
        return NtCoordinates(
            latitude=round(coordinates.latitude, 1),
            longitude=round(coordinates.longitude, 1)
        )
    return coordinates
