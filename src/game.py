import json
import time

import pygame

from config import (
    BACKGROUND_COLOR,
    DATA_DIR,
    FPS,
    GAME_TITLE,
    PLOT_BORDER_COLOR,
    PLOT_COLUMNS,
    PLOT_EMPTY_COLOR,
    PLOT_GAP,
    PLOT_LOCKED_COLOR,
    PLOT_PLANTED_COLOR,
    PLOT_PLANTED_TEXT_COLOR,
    PLOT_SIZE,
    PLOT_START_X,
    PLOT_START_Y,
    PLOT_TOTAL,
    PLOT_UNLOCKED_COUNT,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    TEXT_COLOR,
    PLOT_GROWING_COLOR,
    PLOT_GROWING_TEXT_COLOR,
    PLOT_MATURE_COLOR,
    PLOT_MATURE_TEXT_COLOR,
)
from models.plot import Plot
from utils.constants import (
    CROP_STARBUBBLE_RADISH,
    PLOT_EMPTY,
    PLOT_LOCKED,
    PLOT_PLANTED,
    PLOT_GROWING,
    PLOT_MATURE,
)


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
        self.crop_data = self.load_crop_data()
        self.selected_crop_id = CROP_STARBUBBLE_RADISH

        self.message = "Version 0.3: Click an empty plot to plant Starbubble Radish."

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

            if plot_id <= PLOT_UNLOCKED_COUNT:
                is_unlocked = True
                status = PLOT_EMPTY
            else:
                is_unlocked = False
                status = PLOT_LOCKED

            plot = Plot(
                plot_id=plot_id,
                x=x,
                y=y,
                width=PLOT_SIZE,
                height=PLOT_SIZE,
                is_unlocked=is_unlocked,
                status=status,
            )

            plots.append(plot)

        return plots
    
    def load_crop_data(self) -> dict:
        """Load crop data from data/crops.json."""
        crops_path = DATA_DIR / "crops.json"

        with crops_path.open("r", encoding="utf-8") as file:
            return json.load(file)

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
                if plot.is_locked():
                    self.message = f"Plot {plot.plot_id}: locked"
                    print(self.message)
                    print("This plot is locked.")
                    return

                if plot.can_plant():
                    self.plant_selected_crop(plot)
                    return

                if plot.status in (PLOT_PLANTED, PLOT_GROWING, PLOT_MATURE):
                    crop_name = self.get_crop_name(plot.crop_id)
                    stage_label = self.get_crop_stage_label(plot)
                    self.message = f"Plot {plot.plot_id}: {plot.status} {crop_name} ({stage_label})"
                    print(self.message)

                    if plot.status == PLOT_MATURE:
                        print("This crop is mature. Harvesting will be added in Version 0.4.")
                    else:
                        print("This crop is still growing.")

                    return

                self.message = f"Plot {plot.plot_id}: {plot.status}"
                print(self.message)
                return

        self.message = "Clicked outside farm plots."
        print(self.message)
        
    def plant_selected_crop(self, plot: Plot) -> None:
        """Plant the currently selected crop on a plot."""
        planted_at = time.time()
        plot.plant(self.selected_crop_id, planted_at)

        crop_name = self.get_crop_name(self.selected_crop_id)
        self.message = f"Plot {plot.plot_id}: planted {crop_name}"
        print(self.message)

    def get_crop_name(self, crop_id: str | None) -> str:
        """Get crop English name by crop id."""
        if crop_id is None:
            return "None"

        crop = self.crop_data.get(crop_id)

        if crop is None:
            return crop_id

        return crop["name_en"]
    
    def get_crop_stage_label(self, plot: Plot) -> str:
        """Get current crop stage label."""
        if plot.crop_id is None or plot.current_stage is None:
            return "None"

        crop = self.crop_data.get(plot.crop_id)
        if crop is None:
            return "Unknown"

        growth_stages = crop.get("growth_stages", [])

        for stage_data in growth_stages:
            if stage_data["stage"] == plot.current_stage:
                return stage_data["name"]

        return "Unknown"

    def update(self) -> None:
        """Update game state."""
        current_time = time.time()

        for plot in self.plots:
            if plot.crop_id is None:
                continue

            crop = self.crop_data.get(plot.crop_id)
            if crop is None:
                continue

            growth_time_seconds = crop["growth_time_seconds"]
            plot.update_growth(current_time, growth_time_seconds)

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
            elif plot.status == PLOT_LOCKED:
                color = PLOT_LOCKED_COLOR
            elif plot.status == PLOT_PLANTED:
                color = PLOT_PLANTED_COLOR
            elif plot.status == PLOT_GROWING:
                color = PLOT_GROWING_COLOR
            elif plot.status == PLOT_MATURE:
                color = PLOT_MATURE_COLOR
            else:
                color = PLOT_EMPTY_COLOR

            pygame.draw.rect(self.screen, color, rect, border_radius=14)
            pygame.draw.rect(self.screen, PLOT_BORDER_COLOR, rect, width=4, border_radius=14)

            if plot.status == PLOT_PLANTED:
                label_text = "P"
                label_color = PLOT_PLANTED_TEXT_COLOR
            elif plot.status == PLOT_GROWING:
                label_text = "G"
                label_color = PLOT_GROWING_TEXT_COLOR
            elif plot.status == PLOT_MATURE:
                label_text = "M"
                label_color = PLOT_MATURE_TEXT_COLOR
            else:
                label_text = str(plot.plot_id)
                label_color = TEXT_COLOR

            label_surface = self.font.render(label_text, True, label_color)
            label_rect = label_surface.get_rect(center=rect.center)
            self.screen.blit(label_surface, label_rect)

    def quit(self) -> None:
        """Cleanly quit pygame."""
        pygame.quit()