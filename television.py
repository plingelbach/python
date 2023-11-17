class Television:
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """Initialize the Television object with default values."""

    def power(self) -> None:
        """Turn the TV on and off by changing the value of the status variable."""

    def mute(self) -> None:
        """Mute and unmute the TV when it's on by changing the value of the muted variable."""
        # Implementation

    def __str__(self) -> str:
        """Return the formatted string representation of the TV object."""
