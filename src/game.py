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

from models.inventory import Inventory
from models.player import Player
from models.plot import Plot

from systems.shop_system import ShopSystem

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
        self.shop_items = self.load_shop_items()
        self.shop_system = ShopSystem(self.shop_items)

        self.selected_crop_id = CROP_STARBUBBLE_RADISH
        self.player = Player(coins=50)
        self.inventory = Inventory(
            seeds={
                CROP_STARBUBBLE_RADISH: 0,
            }
        )

        self.message = "Version 0.5: Press B to buy seeds. Click empty plots to plant."

        self.plots = self.create_plots()
    
    def load_crop_data(self) -> dict:
        """Load crop data from data/crops.json."""
        crops_path = DATA_DIR / "crops.json"

        with crops_path.open("r", encoding="utf-8") as file:
            return json.load(file)
    
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
    
    def load_shop_items(self) -> dict:
        """Load shop item data from data/shop_items.json."""
        shop_items_path = DATA_DIR / "shop_items.json"

        with shop_items_path.open("r", encoding="utf-8") as file:
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

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    self.buy_starbubble_seed()

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

                if plot.status == PLOT_MATURE:
                    self.harvest_plot(plot)
                    return

                if plot.status in (PLOT_PLANTED, PLOT_GROWING):
                    crop_name = self.get_crop_name(plot.crop_id)
                    stage_label = self.get_crop_stage_label(plot)
                    self.message = f"Plot {plot.plot_id}: {plot.status} {crop_name} ({stage_label})"
                    print(self.message)
                    print("This crop is still growing.")
                    return

                self.message = f"Plot {plot.plot_id}: {plot.status}"
                print(self.message)
                return

        self.message = "Clicked outside farm plots."
        print(self.message)
        
    def plant_selected_crop(self, plot: Plot) -> None:
        """Plant the currently selected crop on a plot."""
        crop_name = self.get_crop_name(self.selected_crop_id)

        if not self.inventory.consume_seed(self.selected_crop_id, amount=1):
            self.message = f"No {crop_name} seeds left. Buy seeds later in the shop."
            print(self.message)
            return

        planted_at = time.time()
        plot.plant(self.selected_crop_id, planted_at)

        seed_count = self.inventory.get_seed_count(self.selected_crop_id)
        self.message = (
            f"Plot {plot.plot_id}: planted {crop_name}. "
            f"Seeds left: {seed_count}"
        )
        print(self.message)
    
    def harvest_plot(self, plot: Plot) -> None:
        """Harvest a mature crop and add coins to the player."""
        harvested_crop_id = plot.harvest()

        if harvested_crop_id is None:
            self.message = f"Plot {plot.plot_id}: nothing to harvest"
            print(self.message)
            return

        crop = self.crop_data.get(harvested_crop_id)

        if crop is None:
            self.message = f"Plot {plot.plot_id}: harvested unknown crop"
            print(self.message)
            return

        crop_name = crop["name_en"]
        sell_price = crop["sell_price"]

        self.player.add_coins(sell_price)

        self.message = (
            f"Harvested {crop_name} from Plot {plot.plot_id}. "
            f"+{sell_price} coins."
        )
        print(self.message)
        print(f"Current coins: {self.player.coins}")

    def buy_starbubble_seed(self) -> None:
        """Buy one Starbubble Radish seed from the temporary shop."""
        success, message = self.shop_system.buy_seed(
            item_id="starbubble_radish_seed",
            player=self.player,
            inventory=self.inventory,
        )

        self.message = message
        print(message)

        seed_count = self.inventory.get_seed_count(CROP_STARBUBBLE_RADISH)
        print(f"Coins: {self.player.coins}, Starbubble Seeds: {seed_count}")
    
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

        self.draw_hud()
        self.draw_message()
        self.draw_plots()

        pygame.display.flip()
    
    def draw_hud(self) -> None:
        """Draw basic HUD information."""
        coin_text = f"Coins: {self.player.coins}"
        coin_surface = self.font.render(coin_text, True, TEXT_COLOR)
        self.screen.blit(coin_surface, (40, 28))

        seed_count = self.inventory.get_seed_count(CROP_STARBUBBLE_RADISH)
        seed_text = f"Starbubble Seeds: {seed_count}"
        seed_surface = self.font.render(seed_text, True, TEXT_COLOR)
        self.screen.blit(seed_surface, (220, 28))

    def draw_message(self) -> None:
        """Draw current status message."""
        text_surface = self.font.render(self.message, True, TEXT_COLOR)
        self.screen.blit(text_surface, (40, 68))

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