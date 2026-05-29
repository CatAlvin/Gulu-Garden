import json
import time

import pygame

from config import (
    GAME_VERSION,
    SAVES_DIR,
    BACKGROUND_COLOR,
    BUTTON_BORDER_COLOR,
    BUTTON_HOVER_COLOR,
    BUTTON_NORMAL_COLOR,
    BUTTON_TEXT_COLOR,
    SHOP_BUTTON_HEIGHT,
    SHOP_BUTTON_WIDTH,
    SHOP_BUTTON_X,
    SHOP_BUTTON_Y,
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
from systems.save_system import SaveSystem

from ui.button import Button

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

        self.save_system = SaveSystem(SAVES_DIR)
        self.save_path = SAVES_DIR / "save_1.json"
        self.created_at = self.save_system.current_time_iso()

        self.selected_crop_id = CROP_STARBUBBLE_RADISH
        self.player = Player(coins=50)

        self.inventory = Inventory(
            seeds={
                CROP_STARBUBBLE_RADISH: 0,
            }
        )

        self.message = "Version 0.6: Save and load game progress."

        self.plots = self.create_plots()

        self.shop_button = Button(
            x=SHOP_BUTTON_X,
            y=SHOP_BUTTON_Y,
            width=SHOP_BUTTON_WIDTH,
            height=SHOP_BUTTON_HEIGHT,
            text="Shop: Buy Seed",
        )

        self.load_existing_save()
    
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
        
    def build_save_data(self) -> dict:
        """Build current game state as JSON-serializable data."""
        plots_data = []

        for plot in self.plots:
            plot_data = {
                "plot_id": plot.plot_id,
                "status": plot.status,
                "is_unlocked": plot.is_unlocked,
                "crop": None,
            }

            if plot.crop_id is not None:
                plot_data["crop"] = {
                    "crop_id": plot.crop_id,
                    "planted_at": self.save_system.timestamp_to_iso(plot.planted_at),
                    "current_stage": plot.current_stage,
                }

            plots_data.append(plot_data)

        return {
            "save_version": "0.1",
            "game_version": GAME_VERSION,
            "slot_id": 1,
            "created_at": self.created_at,
            "last_saved_at": self.save_system.current_time_iso(),
            "player": {
                "coins": self.player.coins,
            },
            "inventory": {
                "seeds": self.inventory.seeds,
            },
            "plots": plots_data,
        }
        
    def save_game(self) -> None:
        """Save current game progress."""
        save_data = self.build_save_data()
        self.save_system.save_game(self.save_path, save_data)
        print(f"Game saved to {self.save_path}")
    
    def load_existing_save(self) -> None:
        """Load existing save data if available."""
        save_data = self.save_system.load_game(self.save_path)

        if save_data is None:
            self.message = "No save found. Started a new game."
            print(self.message)
            return

        self.created_at = save_data.get(
            "created_at",
            self.save_system.current_time_iso(),
        )

        player_data = save_data.get("player", {})
        self.player.coins = int(player_data.get("coins", 50))

        inventory_data = save_data.get("inventory", {})
        seeds_data = inventory_data.get("seeds", {})
        self.inventory.seeds = {
            str(crop_id): int(count)
            for crop_id, count in seeds_data.items()
        }

        self.restore_plots(save_data.get("plots", []))

        self.message = "Loaded save_1.json."
        print(f"Game loaded from {self.save_path}")
    
    def restore_plots(self, plots_data: list[dict]) -> None:
        """Restore plot states from save data."""
        plots_by_id = {
            plot.plot_id: plot
            for plot in self.plots
        }

        for plot_data in plots_data:
            plot_id = plot_data.get("plot_id")
            plot = plots_by_id.get(plot_id)

            if plot is None:
                continue

            plot.status = plot_data.get("status", plot.status)
            plot.is_unlocked = bool(plot_data.get("is_unlocked", plot.is_unlocked))

            crop_data = plot_data.get("crop")

            if crop_data is None:
                plot.crop_id = None
                plot.planted_at = None
                plot.current_stage = None
                continue

            plot.crop_id = crop_data.get("crop_id")
            plot.planted_at = self.save_system.iso_to_timestamp(
                crop_data.get("planted_at")
            )
            plot.current_stage = crop_data.get("current_stage")

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

                elif event.key == pygame.K_s:
                    self.save_game()
                    self.message = "Game saved."

    def handle_mouse_click(self, position: tuple[int, int]) -> None:
        """Handle left mouse click on farm plots."""
        
        # handle shop button click
        if self.shop_button.is_clicked(position):
            self.buy_starbubble_seed()
            return
        
        # handle farm plot clicks
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
        self.draw_buttons()

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
            
    def draw_buttons(self) -> None:
        """Draw game buttons."""
        self.shop_button.draw(
            screen=self.screen,
            font=self.font,
            normal_color=BUTTON_NORMAL_COLOR,
            hover_color=BUTTON_HOVER_COLOR,
            border_color=BUTTON_BORDER_COLOR,
            text_color=BUTTON_TEXT_COLOR,
        )

    def quit(self) -> None:
        """Save progress and cleanly quit pygame."""
        self.save_game()
        pygame.quit()