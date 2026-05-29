from dataclasses import dataclass

from utils.constants import (
    CROP_STAGE_SEED,
    PLOT_EMPTY,
    PLOT_LOCKED,
    PLOT_PLANTED,
)


@dataclass
class Plot:
    """A single farm plot in Gulu Garden."""

    plot_id: int
    x: int
    y: int
    width: int
    height: int
    is_unlocked: bool
    status: str
    crop_id: str | None = None
    planted_at: float | None = None
    current_stage: int | None = None

    def contains_point(self, position: tuple[int, int]) -> bool:
        """Check whether a mouse position is inside this plot."""
        mouse_x, mouse_y = position

        return (
            self.x <= mouse_x <= self.x + self.width
            and self.y <= mouse_y <= self.y + self.height
        )

    def can_plant(self) -> bool:
        """Return whether this plot can be planted."""
        return self.is_unlocked and self.status == PLOT_EMPTY and self.crop_id is None

    def plant(self, crop_id: str, planted_at: float) -> None:
        """Plant a crop on this plot."""
        if not self.can_plant():
            return

        self.crop_id = crop_id
        self.planted_at = planted_at
        self.current_stage = CROP_STAGE_SEED
        self.status = PLOT_PLANTED

    def is_locked(self) -> bool:
        """Return whether this plot is locked."""
        return (not self.is_unlocked) or self.status == PLOT_LOCKED