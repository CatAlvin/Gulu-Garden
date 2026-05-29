from datetime import datetime


class TimeSystem:
    """Real-world time system for Gulu Garden."""

    def get_current_datetime(self) -> datetime:
        """Return current local datetime."""
        return datetime.now()

    def get_day_phase(self, current_time: datetime | None = None) -> str:
        """Return current day phase based on local real-world time."""
        if current_time is None:
            current_time = self.get_current_datetime()

        hour = current_time.hour

        if 5 <= hour <= 8:
            return "morning"

        if 9 <= hour <= 16:
            return "daytime"

        if 17 <= hour <= 20:
            return "evening"

        return "midnight"

    def get_day_phase_label(self, phase: str) -> str:
        """Return display label for a day phase."""
        labels = {
            "morning": "Morning",
            "daytime": "Daytime",
            "evening": "Evening",
            "midnight": "Midnight",
        }

        return labels.get(phase, "Unknown")

    def get_current_time_text(self) -> str:
        """Return current time as HH:MM text."""
        return self.get_current_datetime().strftime("%H:%M")