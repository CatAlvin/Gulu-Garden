import pygame

from config import (
    BACKGROUND_COLOR,
    FPS,
    GAME_TITLE,
    PLOT_BORDER_COLOR,
    PLOT_COLUMNS,
    PLOT_EMPTY_COLOR,
    PLOT_GAP,
    PLOT_LOCKED_COLOR,
    PLOT_SIZE,
    PLOT_START_X,
    PLOT_START_Y,
    PLOT_TOTAL,
    PLOT_UNLOCKED_COUNT,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    TEXT_COLOR,
)
from models.plot import Plot
from utils.constants import PLOT_EMPTY, PLOT_LOCKED


class Game:
    """Main game controller for Gulu Garden."""

    def __init__(self) -> None:
        """Initialize pygame, window, clock, and basic running state."""
        pygame.init()

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(GAME_TITLE)

        self.clock = pygame.time.Clock()
        self.running = True

        self.font = pygame.font.SysFont("Microsoft YaHei", 24)
        self.message = "Version 0.2: Click a plot to check its status."

        self.plots = self.create_plots()

    def create_plots(self) -> list[Plot]:
        """Create the initial 8 farm plots."""
        plots: list[Plot] = []

        for index in range(PLOT_TOTAL):
            row = index // PLOT_COLUMNS
            col = index % PLOT_COLUMNS

            x = PLOT_START_X + col * (PLOT_SIZE + PLOT_GAP)
            y = PLOT_START_Y + row * (PLOT_SIZE + PLOT_GAP)

            plot_id = index + 1
            is_unlocked = plot_id <= PLOT_UNLOCKED_COUNT

            plot = Plot(
                plot_id=plot_id,
                x=x,
                y=y,
                width=PLOT_SIZE,
                height=PLOT_SIZE,
                is_unlocked=is_unlocked,
            )

            plots.append(plot)

        return plots

    def run(self) -> None:
        """Run the main game loop."""
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

        self.quit()

    def handle_events(self) -> None:
        """Handle user input and window events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.handle_mouse_click(event.pos)

    def handle_mouse_click(self, position: tuple[int, int]) -> None:
        """Handle left mouse click on farm plots."""
        for plot in self.plots:
            if plot.contains_point(position):
                self.message = f"Plot {plot.plot_id}: {plot.status}"
                print(self.message)

                if plot.status == PLOT_LOCKED:
                    print("This plot is locked.")
                elif plot.status == PLOT_EMPTY:
                    print("This plot is empty and can be planted later.")

                return

        self.message = "Clicked outside farm plots."
        print(self.message)

    def update(self) -> None:
        """Update game state.

        Version 0.2 only handles plot display and click detection.
        """
        pass

    def draw(self) -> None:
        """Draw everything on the screen."""
        self.screen.fill(BACKGROUND_COLOR)

        self.draw_message()
        self.draw_plots()

        pygame.display.flip()

    def draw_message(self) -> None:
        """Draw current status message."""
        text_surface = self.font.render(self.message, True, TEXT_COLOR)
        self.screen.blit(text_surface, (40, 40))

    def draw_plots(self) -> None:
        """Draw all farm plots."""
        for plot in self.plots:
            rect = pygame.Rect(plot.x, plot.y, plot.width, plot.height)

            if plot.status == PLOT_EMPTY:
                color = PLOT_EMPTY_COLOR
            else:
                color = PLOT_LOCKED_COLOR

            pygame.draw.rect(self.screen, color, rect, border_radius=14)
            pygame.draw.rect(self.screen, PLOT_BORDER_COLOR, rect, width=4, border_radius=14)

            label_surface = self.font.render(str(plot.plot_id), True, TEXT_COLOR)
            label_rect = label_surface.get_rect(center=rect.center)
            self.screen.blit(label_surface, label_rect)

    def quit(self) -> None:
        """Cleanly quit pygame."""
        pygame.quit()