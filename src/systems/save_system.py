import json
from datetime import datetime
from pathlib import Path


class SaveSystem:
    """Save and load game progress as JSON files."""

    def __init__(self, saves_dir: Path) -> None:
        self.saves_dir = saves_dir
        self.saves_dir.mkdir(parents=True, exist_ok=True)

    def save_game(self, save_path: Path, save_data: dict) -> None:
        """Save game data to a JSON file."""
        save_path.parent.mkdir(parents=True, exist_ok=True)

        with save_path.open("w", encoding="utf-8") as file:
            json.dump(save_data, file, ensure_ascii=False, indent=2)

    @staticmethod
    def current_time_iso() -> str:
        """Return current local time as ISO string."""
        return datetime.now().isoformat(timespec="seconds")

    @staticmethod
    def timestamp_to_iso(timestamp: float | None) -> str | None:
        """Convert a Unix timestamp to ISO string."""
        if timestamp is None:
            return None

        return datetime.fromtimestamp(timestamp).isoformat(timespec="seconds")