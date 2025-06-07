class CantGetCoordinates(Exception):
    """Exception raised when coordinates cannot be retrieved."""
    def __init__(self, message="Cannot get coordinates."):
        self.message = message
        super().__init__(self.message)
