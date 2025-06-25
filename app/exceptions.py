class PartNotFoundError(Exception):
    """Exception raised when a part is not found in the database."""

    def __init__(self, part_serial: str):
        super().__init__(f"Part with ID {part_serial} not found.")
