class CodexSystem:
    """Basic codex system for Gulu Garden.

    Version 1.2 scope:
    - Track whether a crop has been planted.
    - Track whether a crop has been harvested.
    - Keep best planting method locked for now.
    - Provide simple text lines for temporary display.
    """

    def __init__(self, crop_data: dict) -> None:
        """Initialize codex progress from crop data."""
        self.crop_data = crop_data
        self.progress = self.create_default_progress()

    def create_default_progress(self) -> dict:
        """Create default codex progress for all configured crops."""
        progress = {}

        for crop_id in self.crop_data:
            progress[crop_id] = {
                "has_planted": False,
                "has_harvested": False,
                "has_perfect_quality": False,
                "best_method_unlocked": False,
            }

        return progress

    def load_progress(self, saved_progress: dict | None) -> None:
        """Load codex progress from save data.

        Missing crops will be filled with default progress.
        This keeps old saves compatible when new crops are added.
        """
        default_progress = self.create_default_progress()

        if not isinstance(saved_progress, dict):
            self.progress = default_progress
            return

        for crop_id, default_crop_progress in default_progress.items():
            saved_crop_progress = saved_progress.get(crop_id)

            if not isinstance(saved_crop_progress, dict):
                continue

            default_crop_progress["has_planted"] = bool(
                saved_crop_progress.get(
                    "has_planted",
                    default_crop_progress["has_planted"],
                )
            )
            default_crop_progress["has_harvested"] = bool(
                saved_crop_progress.get(
                    "has_harvested",
                    default_crop_progress["has_harvested"],
                )
            )
            default_crop_progress["has_perfect_quality"] = bool(
                saved_crop_progress.get(
                    "has_perfect_quality",
                    default_crop_progress["has_perfect_quality"],
                )
            )
            default_crop_progress["best_method_unlocked"] = bool(
                saved_crop_progress.get(
                    "best_method_unlocked",
                    default_crop_progress["best_method_unlocked"],
                )
            )

        self.progress = default_progress

    def to_save_data(self) -> dict:
        """Return codex progress data for saving."""
        return self.progress

    def record_planted(self, crop_id: str) -> str | None:
        """Record that a crop has been planted."""
        crop_progress = self.progress.get(crop_id)

        if crop_progress is None:
            return None

        if crop_progress["has_planted"]:
            return None

        crop_progress["has_planted"] = True

        crop_name = self.get_crop_display_name(crop_id)
        return f"Codex updated: planted {crop_name}."

    def record_harvested(self, crop_id: str) -> str | None:
        """Record that a crop has been harvested."""
        crop_progress = self.progress.get(crop_id)

        if crop_progress is None:
            return None

        if crop_progress["has_harvested"]:
            return None

        crop_progress["has_harvested"] = True

        crop_name = self.get_crop_display_name(crop_id)
        return f"Codex updated: harvested {crop_name}."

    def get_crop_display_name(self, crop_id: str) -> str:
        """Return crop display name."""
        crop = self.crop_data.get(crop_id)

        if crop is None:
            return crop_id

        name_cn = crop.get("name_cn")
        name_en = crop.get("name_en")

        if name_cn and name_en:
            return f"{name_cn} / {name_en}"

        return name_en or name_cn or crop_id

    def get_codex_lines(self, crop_id: str) -> list[str]:
        """Return codex display lines for one crop."""
        crop = self.crop_data.get(crop_id)
        crop_progress = self.progress.get(crop_id)

        if crop is None or crop_progress is None:
            return ["Codex entry not found."]

        name_cn = crop.get("name_cn", crop_id)
        name_en = crop.get("name_en", crop_id)
        description = crop.get("description", "No description.")

        planted_text = "已种植" if crop_progress["has_planted"] else "未种植"
        harvested_text = "已收获" if crop_progress["has_harvested"] else "未收获"

        if crop_progress["best_method_unlocked"]:
            best_method_text = "已解锁"
        else:
            best_method_text = "未解锁"

        return [
            "========== Codex ==========",
            f"名称：{name_cn}",
            f"英文名：{name_en}",
            f"描述：{description}",
            f"种植记录：{planted_text}",
            f"收获记录：{harvested_text}",
            f"最佳种植方式：{best_method_text}",
            "===========================",
        ]