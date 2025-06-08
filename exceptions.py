class CantGetCoordinates(Exception):
    """Exception raised when coordinates cannot be retrieved."""

    def __init__(self, message="Cannot get coordinates."):
        self.message = message
        super().__init__(self.message)


class ApiServiceError(Exception):
    """Exception raised for errors in the API service."""

    def __init__(self, message="API service error occurred."):
        self.message = message
        super().__init__(self.message)
