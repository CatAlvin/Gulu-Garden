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
    BACKGROUND_DAYTIME_COLOR,
    BACKGROUND_EVENING_COLOR,
    BACKGROUND_MIDNIGHT_COLOR,
    BACKGROUND_MORNING_COLOR,
    SHOP_BUTTON_HEIGHT,
    SHOP_BUTTON_WIDTH,
    SHOP_BUTTON_X,
    SHOP_BUTTON_Y,
    DATA_DIR,
    FPS,
    GAME_TITLE,
    PLOT_COLUMNS,
    PLOT_ROWS,
    PLOT_EMPTY_COLOR,
    PLOT_ROW_COUNTS,
    PLOT_GAP_X,
    PLOT_GAP_Y,
    FARM_AREA_X,
    FARM_AREA_Y,
    FARM_AREA_WIDTH,
    FARM_AREA_HEIGHT,
    PLOT_LOCKED_COLOR,
    PLOT_PLANTED_COLOR,
    PLOT_PLANTED_TEXT_COLOR,
    PLOT_BORDER_COLOR,
    PLOT_SIZE,
    PLOT_UNLOCKED_COUNT,
    FARM_AREA_X,
    FARM_AREA_Y,
    FARM_AREA_WIDTH,
    FARM_AREA_HEIGHT,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    TEXT_COLOR,
    PLOT_GROWING_COLOR,
    PLOT_GROWING_TEXT_COLOR,
    PLOT_MATURE_COLOR,
    PLOT_MATURE_TEXT_COLOR,
    DAY_PHASE_BACKGROUND_IMAGES,
    SCENE_TINT_SETTINGS,
    PLOT_EMPTY_IMAGE,
    PLOT_LOCKED_IMAGE,
    CROP_BASE_OFFSET_Y,
    CROP_STAGE_IMAGE_PATHS,
    CROP_STAGE_IMAGE_SIZE,
    ENABLE_DAY_PHASE_PREVIEW_KEYS,
    SHOP_BUTTON_NORMAL_IMAGE,
    SHOP_BUTTON_HOVER_IMAGE,
    ICON_COIN_IMAGE,
    HUD_ICON_SIZE,
    HUD_COIN_ICON_X,
    HUD_COIN_ICON_Y,
    HUD_COIN_TEXT_X,
    HUD_COIN_TEXT_Y,
    HUD_SEED_TEXT_X,
    HUD_SEED_TEXT_Y,
    HUD_TIME_TEXT_X,
    HUD_TIME_TEXT_Y,
    ICON_SEED_STARBUBBLE_RADISH_IMAGE,
    HUD_SEED_ICON_X,
    HUD_SEED_ICON_Y,
    HUD_PANEL_X,
    HUD_PANEL_Y,
    HUD_PANEL_WIDTH,
    HUD_PANEL_HEIGHT,
    HUD_PANEL_BORDER_RADIUS,
    HUD_PANEL_BACKGROUND_COLOR,
    HUD_PANEL_BORDER_COLOR,
    HUD_PANEL_SHADOW_COLOR,
    HUD_PANEL_SHADOW_OFFSET_X,
    HUD_PANEL_SHADOW_OFFSET_Y,
    HUD_SEED_TEXT_MAX_WIDTH,
)

from models.inventory import Inventory
from models.player import Player
from models.plot import Plot

from systems.codex_system import CodexSystem
from systems.save_system import SaveSystem
from systems.shop_system import ShopSystem
from systems.task_system import TaskSystem
from systems.time_system import TimeSystem

from ui.button import Button

from utils.constants import (
    CROP_IDS,
    CROP_STARBUBBLE_RADISH,
    CROP_CLOUD_SUGAR_PUMPKIN,
    CROP_MOONDEW_MUSHROOM,
    PLOT_EMPTY,
    PLOT_LOCKED,
    PLOT_PLANTED,
    PLOT_GROWING,
    PLOT_MATURE,
)
from utils.asset_loader import AssetLoader


class Game:
    """Main game controller for Gulu Garden."""

    def __init__(self) -> None:
        """Initialize pygame, window, clock, and basic running state."""
        pygame.init()

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(GAME_TITLE)

        self.clock = pygame.time.Clock()
        self.running = True
        
        self.asset_loader = AssetLoader()
        self.background_images = self.load_background_images()
    
        self.crop_stage_images = self.load_crop_stage_images()

        self.shop_button_normal_image = self.asset_loader.load_image(
            SHOP_BUTTON_NORMAL_IMAGE,
            size=(SHOP_BUTTON_WIDTH, SHOP_BUTTON_HEIGHT),
            use_alpha=True,
        )

        self.shop_button_hover_image = self.asset_loader.load_image(
            SHOP_BUTTON_HOVER_IMAGE,
            size=(SHOP_BUTTON_WIDTH, SHOP_BUTTON_HEIGHT),
            use_alpha=True,
        )

        self.coin_icon_image = self.asset_loader.load_image(
            ICON_COIN_IMAGE,
            size=(HUD_ICON_SIZE, HUD_ICON_SIZE),
            use_alpha=True,
        )
        
        self.seed_icon_image = self.asset_loader.load_image(
            ICON_SEED_STARBUBBLE_RADISH_IMAGE,
            size=(HUD_ICON_SIZE, HUD_ICON_SIZE),
            use_alpha=True,
        )

        self.font = pygame.font.SysFont("Microsoft YaHei", 24)
        self.crop_data = self.load_crop_data()
        self.shop_items = self.load_shop_items()
        self.shop_system = ShopSystem(self.shop_items)

        self.task_data = self.load_task_data()
        self.task_system = TaskSystem(self.task_data)
        
        self.codex_system = CodexSystem(self.crop_data)

        self.save_system = SaveSystem(SAVES_DIR)
        self.save_path = SAVES_DIR / "save_1.json"
        self.created_at = self.save_system.current_time_iso()
        self.time_system = TimeSystem()
        self.current_day_phase = self.time_system.get_day_phase()
        self.day_phase_preview_override: str | None = None

        self.selected_crop_id = CROP_STARBUBBLE_RADISH
        self.player = Player(coins=50)

        self.inventory = Inventory(
            seeds={
                crop_id: 0
                for crop_id in CROP_IDS
            }
        )

        self.message = "Version 1.2: Basic codex system."
        
        self.show_codex_panel = False
        
        self.plots = self.create_plots()

        self.shop_button = Button(
            x=SHOP_BUTTON_X,
            y=SHOP_BUTTON_Y,
            width=SHOP_BUTTON_WIDTH,
            height=SHOP_BUTTON_HEIGHT,
            text="买星泡萝卜种子",
        )

        self.select_crop(self.selected_crop_id)

        self.load_existing_save()

    def ensure_inventory_seed_keys(self) -> None:
        """Ensure inventory has seed entries for all configured crop ids."""
        for crop_id in CROP_IDS:
            if crop_id not in self.inventory.seeds:
                self.inventory.seeds[crop_id] = 0
    
    def load_crop_data(self) -> dict:
        """Load crop data from data/crops.json."""
        crops_path = DATA_DIR / "crops.json"

        with crops_path.open("r", encoding="utf-8") as file:
            return json.load(file)

    def load_background_images(self) -> dict[str, pygame.Surface]:
        """Load day phase background images."""
        background_images: dict[str, pygame.Surface] = {}

        for phase, image_path in DAY_PHASE_BACKGROUND_IMAGES.items():
            image = self.asset_loader.load_image(
                image_path=image_path,
                size=(SCREEN_WIDTH, SCREEN_HEIGHT),
                use_alpha=False,
            )

            if image is not None:
                background_images[phase] = image

        return background_images
    
    def get_crop_stage_image(
    self,
        crop_id: str | None,
        current_stage: int | None,
    ) -> pygame.Surface | None:
        """Return crop image for current crop stage."""
        if crop_id is None or current_stage is None:
            return None

        return self.crop_stage_images.get(crop_id, {}).get(current_stage)
    
    def get_plot_empty_image(self) -> pygame.Surface | None:
        """Return tinted empty plot image for current day phase."""
        return self.asset_loader.load_tinted_image(
            image_path=PLOT_EMPTY_IMAGE,
            size=(PLOT_SIZE, PLOT_SIZE),
            phase=self.current_day_phase,
            tint_settings=SCENE_TINT_SETTINGS,
            use_alpha=True,
        )

    def get_plot_locked_image(self) -> pygame.Surface | None:
        """Return tinted locked plot image for current day phase."""
        return self.asset_loader.load_tinted_image(
            image_path=PLOT_LOCKED_IMAGE,
            size=(PLOT_SIZE, PLOT_SIZE),
            phase=self.current_day_phase,
            tint_settings=SCENE_TINT_SETTINGS,
            use_alpha=True,
        )
    
    def create_plots(self) -> list[Plot]:
        """Create farm plots with a staggered row layout."""
        plots: list[Plot] = []

        grid_height = PLOT_ROWS * PLOT_SIZE + (PLOT_ROWS - 1) * PLOT_GAP_Y
        start_y = FARM_AREA_Y + (FARM_AREA_HEIGHT - grid_height) // 2

        plot_id = 1

        for row, row_count in enumerate(PLOT_ROW_COUNTS):
            row_width = row_count * PLOT_SIZE + (row_count - 1) * PLOT_GAP_X

            start_x = FARM_AREA_X + (FARM_AREA_WIDTH - row_width) // 2
            y = start_y + row * (PLOT_SIZE + PLOT_GAP_Y)

            for col in range(row_count):
                x = start_x + col * (PLOT_SIZE + PLOT_GAP_X)

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
                plot_id += 1

        return plots

    def load_shop_items(self) -> dict:
        """Load shop item data from data/shop_items.json."""
        shop_items_path = DATA_DIR / "shop_items.json"
        if not shop_items_path.exists():
            return {}
        try:
            with shop_items_path.open("r", encoding="utf-8") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return {}
 
    def load_task_data(self) -> dict:
        """Load task data from data/tasks.json."""
        tasks_path = DATA_DIR / "tasks.json"

        if not tasks_path.exists():
            return {}

        try:
            with tasks_path.open("r", encoding="utf-8") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return {}

        
    def load_crop_stage_images(self) -> dict[str, dict[int, pygame.Surface]]:
        """Load crop stage images for all configured crops."""
        crop_images: dict[str, dict[int, pygame.Surface]] = {}

        for crop_id, stage_paths in CROP_STAGE_IMAGE_PATHS.items():
            crop_images[crop_id] = {}

            for stage, image_path in stage_paths.items():
                image = self.asset_loader.load_image(
                    image_path,
                    size=(CROP_STAGE_IMAGE_SIZE, CROP_STAGE_IMAGE_SIZE),
                    use_alpha=True,
                )

                if image is not None:
                    crop_images[crop_id][stage] = image

        return crop_images

    def get_tinted_crop_stage_image(
        self,
        crop_id: str | None,
        current_stage: int | None,
    ) -> pygame.Surface | None:
        """Return tinted crop stage image for current day phase."""
        if crop_id is None or current_stage is None:
            return None

        crop_stage_paths = CROP_STAGE_IMAGE_PATHS.get(crop_id)

        if crop_stage_paths is None:
            return None

        image_path = crop_stage_paths.get(current_stage)

        if image_path is None:
            return None

        return self.asset_loader.load_tinted_image(
            image_path=image_path,
            size=(CROP_STAGE_IMAGE_SIZE, CROP_STAGE_IMAGE_SIZE),
            phase=self.current_day_phase,
            tint_settings=SCENE_TINT_SETTINGS,
            use_alpha=True,
        )
        
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
            "time": {
                "use_real_world_time": True,
                "current_day_phase": self.time_system.get_day_phase(),
                "last_calculated_at": self.save_system.current_time_iso(),
            },
            "inventory": {
                "seeds": self.inventory.seeds,
            },
            "plots": plots_data,
            "tasks": self.task_system.to_save_data(),
            "codex": self.codex_system.to_save_data(),
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
        self.ensure_inventory_seed_keys()
        
        self.restore_plots(save_data.get("plots", []))
        
        self.task_system.load_progress(save_data.get("tasks"))
        self.codex_system.load_progress(save_data.get("codex"))
        self.sync_codex_from_existing_plots()

        offline_messages = self.apply_offline_growth()

        if offline_messages:
            self.message = offline_messages[0]
            for message in offline_messages:
                print(message)
        else:
            self.message = "Loaded save_1.json."

        print(f"Game loaded from {self.save_path}")

    def sync_codex_from_existing_plots(self) -> None:
        """Sync codex planted records from currently loaded plots.

        This is mainly for old saves created before Version 1.2.
        If a crop already exists on a plot, the codex should know that
        this crop has been planted before.
        """
        for plot in self.plots:
            if plot.crop_id is None:
                continue

            codex_message = self.codex_system.record_planted(plot.crop_id)

            if codex_message:
                print(codex_message)
    
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
            
    def apply_offline_growth(self) -> list[str]:
        """Apply growth after loading save data and report offline changes."""
        current_time = time.time()
        offline_messages: list[str] = []

        for plot in self.plots:
            if plot.crop_id is None:
                continue

            old_status = plot.status
            old_stage = plot.current_stage

            crop = self.crop_data.get(plot.crop_id)
            if crop is None:
                continue

            growth_time_seconds = crop["growth_time_seconds"]
            plot.update_growth(current_time, growth_time_seconds)

            became_mature = old_status != PLOT_MATURE and plot.status == PLOT_MATURE

            if became_mature:
                crop_name = self.get_crop_name(plot.crop_id)
                message = (
                    f"Plot {plot.plot_id}: {crop_name} became mature "
                    f"while you were away."
                )
                offline_messages.append(message)

            elif old_stage != plot.current_stage:
                crop_name = self.get_crop_name(plot.crop_id)
                stage_label = self.get_crop_stage_label(plot)
                message = (
                    f"Plot {plot.plot_id}: {crop_name} grew to "
                    f"{stage_label} while you were away."
                )
                offline_messages.append(message)

        return offline_messages

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
                    self.buy_selected_seed()

                elif event.key == pygame.K_s:
                    self.save_game()
                    self.message = "Game saved."

                elif event.key == pygame.K_t:
                    self.print_task_summary()
                    
                elif event.key == pygame.K_c:
                    self.toggle_codex_panel()
                
                elif event.key == pygame.K_i:
                    self.print_inventory_summary()

                elif event.key == pygame.K_ESCAPE:
                    if self.show_codex_panel:
                        self.show_codex_panel = False
                        self.message = "Codex closed."
                
                elif event.key == pygame.K_q:
                    self.select_crop(CROP_STARBUBBLE_RADISH)

                elif event.key == pygame.K_w:
                    self.select_crop(CROP_CLOUD_SUGAR_PUMPKIN)

                elif event.key == pygame.K_e:
                    self.select_crop(CROP_MOONDEW_MUSHROOM)

                elif ENABLE_DAY_PHASE_PREVIEW_KEYS and event.key == pygame.K_0:
                    self.set_day_phase_preview(None)

                elif ENABLE_DAY_PHASE_PREVIEW_KEYS and event.key == pygame.K_1:
                    self.set_day_phase_preview("morning")

                elif ENABLE_DAY_PHASE_PREVIEW_KEYS and event.key == pygame.K_2:
                    self.set_day_phase_preview("daytime")

                elif ENABLE_DAY_PHASE_PREVIEW_KEYS and event.key == pygame.K_3:
                    self.set_day_phase_preview("evening")

                elif ENABLE_DAY_PHASE_PREVIEW_KEYS and event.key == pygame.K_4:
                    self.set_day_phase_preview("midnight")

    def handle_mouse_click(self, position: tuple[int, int]) -> None:
        """Handle left mouse click on farm plots."""
        
        # handle shop button click
        if self.shop_button.is_clicked(position):
            self.buy_selected_seed()
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

        task_messages = self.task_system.handle_event(
            event_type="plant_crop",
            crop_id=self.selected_crop_id,
            player=self.player,
        )
        codex_message = self.codex_system.record_planted(self.selected_crop_id)

        seed_count = self.inventory.get_seed_count(self.selected_crop_id)
        self.message = (
            f"Plot {plot.plot_id}: planted {crop_name}. "
            f"Seeds left: {seed_count}"
        )
        print(self.message)

        for task_message in task_messages:
            self.message = task_message
            print(task_message)
        
        if codex_message:
            self.message = codex_message
            print(codex_message)
    
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

        task_messages = self.task_system.handle_event(
            event_type="harvest_crop",
            crop_id=harvested_crop_id,
            player=self.player,
        )
        
        codex_message = self.codex_system.record_harvested(harvested_crop_id)

        self.message = (
            f"Harvested {crop_name} from Plot {plot.plot_id}. "
            f"+{sell_price} coins."
        )
        print(self.message)

        for task_message in task_messages:
            self.message = task_message
            print(task_message)

        if codex_message:
            self.message = codex_message
            print(codex_message)

        print(f"Current coins: {self.player.coins}")

    def buy_selected_seed(self) -> None:
        """Buy one seed for the currently selected crop."""
        item_id = self.get_seed_item_id_by_crop_id(self.selected_crop_id)

        if item_id is None:
            crop_name = self.get_crop_name(self.selected_crop_id)
            self.message = f"No shop item found for {crop_name}."
            print(self.message)
            return

        success, message = self.shop_system.buy_seed(
            item_id=item_id,
            player=self.player,
            inventory=self.inventory,
        )

        self.message = message
        print(message)

        seed_count = self.inventory.get_seed_count(self.selected_crop_id)
        crop_name = self.get_crop_name(self.selected_crop_id)

        print(
            f"Coins: {self.player.coins}, "
            f"{crop_name} Seeds: {seed_count}"
        )

    def select_crop(self, crop_id: str) -> None:
        """Select a crop for planting and buying seeds."""
        if crop_id not in self.crop_data:
            self.message = f"Crop not found: {crop_id}"
            print(self.message)
            return

        self.selected_crop_id = crop_id

        crop_name_cn = self.get_crop_name_cn(crop_id)
        seed_count = self.inventory.get_seed_count(crop_id)

        self.shop_button.text = f"买{crop_name_cn}种子"

        self.message = f"Selected {crop_name_cn}. Seeds: {seed_count}"
        print(self.message)

    def print_task_summary(self) -> None:
        """Print current task progress for Version 1.1 debugging."""
        print("========== Task Progress ==========")

        for line in self.task_system.get_task_summary_lines():
            print(line)

        print("===================================")

        self.message = "Task progress printed in terminal."

    def print_inventory_summary(self) -> None:
        """Print current seed inventory for Version 1.3 debugging."""
        print("========== Seed Inventory ==========")

        for crop_id in CROP_IDS:
            crop_name_cn = self.get_crop_name_cn(crop_id)
            seed_count = self.inventory.get_seed_count(crop_id)
            print(f"{crop_name_cn}种子: {seed_count}")

        print("====================================")

        self.message = "Seed inventory printed in terminal."
    
    def print_codex_entry(self) -> None:
        """Print selected crop codex entry for debugging."""
        for line in self.codex_system.get_codex_lines(self.selected_crop_id):
            print(line)

        crop_name = self.get_crop_name(self.selected_crop_id)
        self.message = f"Codex entry printed: {crop_name}"
        
    def toggle_codex_panel(self) -> None:
        """Toggle the simple codex panel."""
        self.show_codex_panel = not self.show_codex_panel

        if self.show_codex_panel:
            self.print_codex_entry()
            self.message = "Codex opened. Press C or Esc to close."
        else:
            self.message = "Codex closed."
    
    def get_crop_name(self, crop_id: str | None) -> str:
        """Get crop English name by crop id."""
        if crop_id is None:
            return "None"

        crop = self.crop_data.get(crop_id)

        if crop is None:
            return crop_id

        return crop["name_en"]

    def get_crop_name_cn(self, crop_id: str | None) -> str:
        """Get crop Chinese name by crop id."""
        if crop_id is None:
            return "未知作物"

        crop = self.crop_data.get(crop_id)

        if crop is None:
            return crop_id

        return crop.get("name_cn", crop.get("name_en", crop_id))

    def get_crop_short_label(self, crop_id: str | None) -> str:
        """Return a short Chinese label for fallback crop display."""
        if crop_id is None:
            return "?"

        crop_short_labels = {
            CROP_STARBUBBLE_RADISH: "萝",
            CROP_CLOUD_SUGAR_PUMPKIN: "瓜",
            CROP_MOONDEW_MUSHROOM: "菇",
        }

        if crop_id in crop_short_labels:
            return crop_short_labels[crop_id]

        crop_name_cn = self.get_crop_name_cn(crop_id)

        if crop_name_cn:
            return crop_name_cn[0]

        return "?"

    def get_plot_stage_letter(self, plot: Plot) -> str:
        """Return a short stage letter for fallback plot display."""
        if plot.status == PLOT_PLANTED:
            return "P"

        if plot.status == PLOT_GROWING:
            return "G"

        if plot.status == PLOT_MATURE:
            return "M"

        return ""

    def get_plot_fallback_text(self, plot: Plot) -> str:
        """Return fallback text when crop image is missing."""
        if plot.crop_id is None:
            return str(plot.plot_id)

        crop_label = self.get_crop_short_label(plot.crop_id)
        stage_letter = self.get_plot_stage_letter(plot)

        if stage_letter:
            return f"{crop_label}{stage_letter}"

        return crop_label
    
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
    
    def get_seed_item_id_by_crop_id(self, crop_id: str) -> str | None:
        """Find seed shop item id by crop id."""
        for item_id, item in self.shop_items.items():
            if item.get("item_type") != "seed":
                continue

            if item.get("crop_id") == crop_id:
                return item_id

        return None

    def get_background_color(self) -> tuple[int, int, int]:
        """Return background color for current day phase."""
        if self.current_day_phase == "morning":
            return BACKGROUND_MORNING_COLOR

        if self.current_day_phase == "daytime":
            return BACKGROUND_DAYTIME_COLOR

        if self.current_day_phase == "evening":
            return BACKGROUND_EVENING_COLOR

        if self.current_day_phase == "midnight":
            return BACKGROUND_MIDNIGHT_COLOR

        return BACKGROUND_COLOR

    def update(self) -> None:
        """Update game state."""
        if self.day_phase_preview_override is None:
            self.current_day_phase = self.time_system.get_day_phase()
        else:
            self.current_day_phase = self.day_phase_preview_override

        current_time = time.time()

        for plot in self.plots:
            if plot.crop_id is None:
                continue

            crop = self.crop_data.get(plot.crop_id)
            if crop is None:
                continue

            growth_time_seconds = crop["growth_time_seconds"]
            plot.update_growth(current_time, growth_time_seconds)

    def set_day_phase_preview(self, phase: str | None) -> None:
        """Set or clear day phase preview override."""
        self.day_phase_preview_override = phase

        if phase is None:
            self.current_day_phase = self.time_system.get_day_phase()
            phase_label = self.time_system.get_day_phase_label(self.current_day_phase)
            self.message = f"Preview disabled. Using real day phase: {phase_label}."
            print(self.message)
            return

        self.current_day_phase = phase
        phase_label = self.time_system.get_day_phase_label(phase)
        self.message = f"Preview day phase: {phase_label}. Press 0 to return to real time."
        print(self.message)
    

    def draw(self) -> None:
        """Draw everything on the screen."""
        self.draw_background()
        self.draw_hud_panel()
        self.draw_hud()
        self.draw_message()
        self.draw_plots()
        self.draw_buttons()

        if self.show_codex_panel:
            self.draw_codex_panel()

        pygame.display.flip()
    
    def draw_background(self) -> None:
        """Draw current day phase background image or fallback color."""
        background_image = self.background_images.get(self.current_day_phase)

        if background_image is not None:
            self.screen.blit(background_image, (0, 0))
            return

        daytime_background = self.background_images.get("daytime")

        if daytime_background is not None:
            self.screen.blit(daytime_background, (0, 0))
            return

        self.screen.fill(self.get_background_color())

    def draw_transparent_rounded_rect(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        background_color: tuple[int, int, int, int],
        border_color: tuple[int, int, int, int],
        border_radius: int,
        border_width: int = 2,
    ) -> None:
        """Draw a transparent rounded rectangle on the screen."""
        panel_surface = pygame.Surface((width, height), pygame.SRCALPHA)

        panel_rect = pygame.Rect(0, 0, width, height)

        pygame.draw.rect(
            panel_surface,
            background_color,
            panel_rect,
            border_radius=border_radius,
        )

        if border_width > 0:
            pygame.draw.rect(
                panel_surface,
                border_color,
                panel_rect,
                width=border_width,
                border_radius=border_radius,
            )

        self.screen.blit(panel_surface, (x, y))

    def draw_hud_panel(self) -> None:
        """Draw a soft transparent panel behind HUD text."""
        shadow_x = HUD_PANEL_X + HUD_PANEL_SHADOW_OFFSET_X
        shadow_y = HUD_PANEL_Y + HUD_PANEL_SHADOW_OFFSET_Y

        self.draw_transparent_rounded_rect(
            x=shadow_x,
            y=shadow_y,
            width=HUD_PANEL_WIDTH,
            height=HUD_PANEL_HEIGHT,
            background_color=HUD_PANEL_SHADOW_COLOR,
            border_color=(0, 0, 0, 0),
            border_radius=HUD_PANEL_BORDER_RADIUS,
            border_width=0,
        )

        self.draw_transparent_rounded_rect(
            x=HUD_PANEL_X,
            y=HUD_PANEL_Y,
            width=HUD_PANEL_WIDTH,
            height=HUD_PANEL_HEIGHT,
            background_color=HUD_PANEL_BACKGROUND_COLOR,
            border_color=HUD_PANEL_BORDER_COLOR,
            border_radius=HUD_PANEL_BORDER_RADIUS,
            border_width=2,
        )
    
    def draw_hud(self) -> None:
        """Draw basic HUD information."""
        if self.coin_icon_image is not None:
            self.screen.blit(
                self.coin_icon_image,
                (HUD_COIN_ICON_X, HUD_COIN_ICON_Y),
            )

        coin_text = f"{self.player.coins}"
        coin_surface = self.font.render(coin_text, True, TEXT_COLOR)
        self.screen.blit(coin_surface, (HUD_COIN_TEXT_X, HUD_COIN_TEXT_Y))

        selected_crop_name = self.get_crop_name_cn(self.selected_crop_id)
        selected_seed_count = self.inventory.get_seed_count(self.selected_crop_id)

        if self.seed_icon_image is not None:
            self.screen.blit(
                self.seed_icon_image,
                (HUD_SEED_ICON_X, HUD_SEED_ICON_Y),
            )

        seed_text = f"{selected_crop_name}种子: {selected_seed_count}"
        seed_text = self.fit_text_to_width(
            text=seed_text,
            font=self.font,
            max_width=HUD_SEED_TEXT_MAX_WIDTH,
        )
        seed_surface = self.font.render(seed_text, True, TEXT_COLOR)
        seed_surface = self.font.render(seed_text, True, TEXT_COLOR)
        self.screen.blit(seed_surface, (HUD_SEED_TEXT_X, HUD_SEED_TEXT_Y))

        current_time_text = self.time_system.get_current_time_text()
        phase_label = self.time_system.get_day_phase_label(self.current_day_phase)

        if self.day_phase_preview_override is None:
            time_text = f"{current_time_text} | {phase_label}"
        else:
            time_text = f"{current_time_text} | {phase_label} (Preview)"

        time_surface = self.font.render(time_text, True, TEXT_COLOR)
        self.screen.blit(time_surface, (HUD_TIME_TEXT_X, HUD_TIME_TEXT_Y))

    def fit_text_to_width(
        self,
        text: str,
        font: pygame.font.Font,
        max_width: int,
    ) -> str:
        """Shorten text so it does not exceed max rendered width."""
        if font.size(text)[0] <= max_width:
            return text

        ellipsis = "..."
        result = ""

        for char in text:
            test_text = result + char + ellipsis

            if font.size(test_text)[0] > max_width:
                break

            result += char

        return result + ellipsis

    def wrap_text_by_width(
        self,
        text: str,
        font: pygame.font.Font,
        max_width: int,
    ) -> list[str]:
        """Wrap text by rendered pixel width.

        This character-based wrapping works better for Chinese text.
        """
        lines = []
        current_line = ""

        for char in text:
            test_line = current_line + char

            if font.size(test_line)[0] <= max_width:
                current_line = test_line
            else:
                if current_line:
                    lines.append(current_line)
                current_line = char

        if current_line:
            lines.append(current_line)

        return lines

    def draw_codex_panel(self) -> None:
        """Draw a simple in-game codex panel."""
        panel_width = 760
        panel_height = 430
        panel_x = (SCREEN_WIDTH - panel_width) // 2
        panel_y = (SCREEN_HEIGHT - panel_height) // 2

        panel_surface = pygame.Surface((panel_width, panel_height), pygame.SRCALPHA)
        panel_surface.fill((255, 248, 220, 225))

        panel_rect = panel_surface.get_rect(topleft=(panel_x, panel_y))
        pygame.draw.rect(
            panel_surface,
            (255, 248, 220, 225),
            panel_surface.get_rect(),
            border_radius=24,
        )
        pygame.draw.rect(
            panel_surface,
            (130, 96, 55, 255),
            panel_surface.get_rect(),
            width=4,
            border_radius=24,
        )

        self.screen.blit(panel_surface, panel_rect)

        title_font = pygame.font.SysFont("Microsoft YaHei", 30, bold=True)
        body_font = pygame.font.SysFont("Microsoft YaHei", 22)

        selected_crop = self.crop_data.get(self.selected_crop_id, {})
        selected_crop_name = selected_crop.get(
            "name_cn",
            self.get_crop_name(self.selected_crop_id),
        )

        title_surface = title_font.render(
            f"图鉴 Codex - {selected_crop_name}",
            True,
            TEXT_COLOR,
        )
        self.screen.blit(title_surface, (panel_x + 32, panel_y + 24))

        hint_surface = body_font.render("Press C or Esc to close", True, TEXT_COLOR)
        self.screen.blit(hint_surface, (panel_x + panel_width - 270, panel_y + 32))

        codex_lines = self.codex_system.get_codex_lines(self.selected_crop_id)

        text_x = panel_x + 36
        text_y = panel_y + 82
        max_text_width = panel_width - 72
        line_height = 30

        for line in codex_lines:
            if line.startswith("="):
                continue

            wrapped_lines = self.wrap_text_by_width(
                text=line,
                font=body_font,
                max_width=max_text_width,
            )

            for wrapped_line in wrapped_lines:
                text_surface = body_font.render(wrapped_line, True, TEXT_COLOR)
                self.screen.blit(text_surface, (text_x, text_y))
                text_y += line_height

            text_y += 6

    def draw_message(self) -> None:
        """Draw current status message."""
        text_surface = self.font.render(self.message, True, TEXT_COLOR)
        self.screen.blit(text_surface, (40, 68))
        
    # TODO: 临时的农田区域调试边框，后续接入背景图和土地贴图后可以去掉。
    def draw_farm_area_debug(self) -> None:
        """Draw the farm area rectangle for layout debugging."""
        debug_rect = pygame.Rect(
            FARM_AREA_X,
            FARM_AREA_Y,
            FARM_AREA_WIDTH,
            FARM_AREA_HEIGHT,
        )
        pygame.draw.rect(self.screen, (255, 0, 0), debug_rect, width=2)

    def draw_plots(self) -> None:
        """Draw all farm plots."""
        for plot in self.plots:
            rect = pygame.Rect(plot.x, plot.y, plot.width, plot.height)

            if plot.is_locked():
                plot_image = self.get_plot_locked_image()
            else:
                plot_image = self.get_plot_empty_image()

            if plot_image is not None:
                self.screen.blit(plot_image, rect)
            else:
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
                pygame.draw.rect(
                    self.screen,
                    PLOT_BORDER_COLOR,
                    rect,
                    width=4,
                    border_radius=14,
                )

            crop_image_drawn = False

            if plot.crop_id is not None:
                crop_image_drawn = self.draw_crop_on_plot(plot, rect)

            if crop_image_drawn:
                continue

            if plot.status == PLOT_PLANTED:
                label_text = self.get_plot_fallback_text(plot)
                label_color = PLOT_PLANTED_TEXT_COLOR
            elif plot.status == PLOT_GROWING:
                label_text = self.get_plot_fallback_text(plot)
                label_color = PLOT_GROWING_TEXT_COLOR
            elif plot.status == PLOT_MATURE:
                label_text = self.get_plot_fallback_text(plot)
                label_color = PLOT_MATURE_TEXT_COLOR
            else:
                label_text = str(plot.plot_id)
                label_color = TEXT_COLOR

            label_surface = self.font.render(label_text, True, label_color)
            label_rect = label_surface.get_rect(center=rect.center)
            self.screen.blit(label_surface, label_rect)

    def draw_crop_on_plot(self, plot: Plot, plot_rect: pygame.Rect) -> bool:
        """Draw crop image on a plot.

        Return True if a crop image is drawn.
        """
        crop_image = self.get_tinted_crop_stage_image(
            crop_id=plot.crop_id,
            current_stage=plot.current_stage,
        )

        if crop_image is None:
            return False

        crop_rect = crop_image.get_rect(
            midbottom=(
                plot_rect.centerx,
                plot_rect.centery + CROP_BASE_OFFSET_Y,
            )
        )

        self.screen.blit(crop_image, crop_rect)
        return True
            
    def draw_buttons(self) -> None:
        """Draw game buttons."""
        self.shop_button.draw(
            screen=self.screen,
            font=self.font,
            normal_color=BUTTON_NORMAL_COLOR,
            hover_color=BUTTON_HOVER_COLOR,
            border_color=BUTTON_BORDER_COLOR,
            text_color=BUTTON_TEXT_COLOR,
            normal_image=self.shop_button_normal_image,
            hover_image=self.shop_button_hover_image,
        )

    def quit(self) -> None:
        """Save progress and cleanly quit pygame."""
        self.save_game()
        pygame.quit()