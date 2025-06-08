import json
import re
from subprocess import Popen, PIPE
from exceptions import CantGetCoordinates
from name_tuples.nt_coordinates import NtCoordinates


def get_gps_coordinates() -> NtCoordinates:
    """Return gps coordinates using whereami by node js"""
    # Assuming 'whereami' is a command-line tool that returns GPS coordinates
    process = Popen(['whereami', '-f', 'json'], stdout=PIPE, stderr=PIPE)
    # Capture the output and error streams
    (output, error) = process.communicate()
    # Check if the command was successful
    exit_code = process.wait()
    if error is not None and exit_code != 0:
        raise CantGetCoordinates(
            f"Error getting coordinates: {error.decode().strip()}")

    output_lines = output.decode(errors='ignore').splitlines()
    json_pattern = re.compile(r'{.*"latitude".*"longitude".*}')

    for line in output_lines:
        match = json_pattern.search(line)
        if match:
            try:
                coords = json.loads(match.group())
                return NtCoordinates(
                    latitude=coords['latitude'],
                    longitude=coords['longitude']
                )
            except json.JSONDecodeError as e:
                raise CantGetCoordinates(f"Failed to decode JSON: {e}")
    raise CantGetCoordinates("No valid GPS coordinates found in output.")
