from dataclasses import dataclass

from utils.constants import PLOT_EMPTY, PLOT_LOCKED


@dataclass
class Plot:
    """A single farm plot in Gulu Garden."""

    plot_id: int
    x: int
    y: int
    width: int
    height: int
    is_unlocked: bool

    @property
    def status(self) -> str:
        """Return current plot status."""
        if self.is_unlocked:
            return PLOT_EMPTY
        return PLOT_LOCKED

    def contains_point(self, position: tuple[int, int]) -> bool:
        """Check whether a mouse position is inside this plot."""
        mouse_x, mouse_y = position

        return (
            self.x <= mouse_x <= self.x + self.width
            and self.y <= mouse_y <= self.y + self.height
        )