from pathlib import Path

# =========================
# Basic Game Information
# =========================

GAME_TITLE = "Gulu Garden - 咕噜小菜园"
GAME_VERSION = "0.9.0"

# =========================
# Screen Settings
# =========================

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60

# =========================
# Project Paths
# =========================

PROJECT_ROOT = Path(__file__).resolve().parents[1]
ASSETS_DIR = PROJECT_ROOT / "assets"
DATA_DIR = PROJECT_ROOT / "data"
SAVES_DIR = PROJECT_ROOT / "saves"

# =========================
# Image Asset Paths
# =========================

BACKGROUNDS_DIR = ASSETS_DIR / "images" / "backgrounds"
TILES_DIR = ASSETS_DIR / "images" / "tiles"
CROPS_DIR = ASSETS_DIR / "images" / "crops"
UI_IMAGES_DIR = ASSETS_DIR / "images" / "ui"
ICONS_DIR = ASSETS_DIR / "images" / "icons"

BACKGROUND_DAYTIME_IMAGE = BACKGROUNDS_DIR / "farm_daytime.png"

PLOT_EMPTY_IMAGE = TILES_DIR / "plot_empty.png"
PLOT_LOCKED_IMAGE = TILES_DIR / "plot_locked.png"

STARBUBBLE_RADISH_IMAGE_DIR = CROPS_DIR / "starbubble_radish"
STARBUBBLE_RADISH_STAGE_IMAGES = {
    0: STARBUBBLE_RADISH_IMAGE_DIR / "stage_0_seed.png",
    1: STARBUBBLE_RADISH_IMAGE_DIR / "stage_1_sprout.png",
    2: STARBUBBLE_RADISH_IMAGE_DIR / "stage_2_growing.png",
    3: STARBUBBLE_RADISH_IMAGE_DIR / "stage_3_mature.png",
}

SHOP_BUTTON_NORMAL_IMAGE = UI_IMAGES_DIR / "button_shop_normal.png"
SHOP_BUTTON_HOVER_IMAGE = UI_IMAGES_DIR / "button_shop_hover.png"
ICON_COIN_IMAGE = ICONS_DIR / "icon_coin.png"

# =========================
# Colors
# =========================
# 暂时使用柔和背景色，后续再替换成 farm_daytime.png 背景图。

BACKGROUND_COLOR = (188, 224, 170)

# =========================
# Farm Plot Layout Settings
# =========================

# 使用交错式农田布局：
# 第 1 行：6 块
# 第 2 行：8 块
# 第 3 行：6 块
# 中间行更宽，适合后续接入圆角/圆形土地贴图。
PLOT_ROW_COUNTS = [6, 8, 6]

PLOT_ROWS = len(PLOT_ROW_COUNTS)
PLOT_COLUMNS = max(PLOT_ROW_COUNTS)
PLOT_TOTAL = sum(PLOT_ROW_COUNTS)

# 仍然只开放前 4 块，避免视觉优化影响当前经济节奏。
# 后续做土地解锁系统时再逐步开放更多土地。
PLOT_UNLOCKED_COUNT = 4

# 后续接入土地贴图时，这个尺寸会作为贴图显示尺寸。
PLOT_SIZE = 96

PLOT_GAP_X = 20
PLOT_GAP_Y = 20

# 农田区域用于承载 6-8-6 交错布局。
# 区域宽度需要覆盖中间 8 块地，整体略微下移，避开顶部 HUD。
FARM_AREA_X = 180
FARM_AREA_Y = 300
FARM_AREA_WIDTH = 920
FARM_AREA_HEIGHT = 330

# =========================
# Plot Colors
# =========================

PLOT_EMPTY_COLOR = (196, 142, 85)
PLOT_LOCKED_COLOR = (130, 145, 150)
PLOT_PLANTED_COLOR = (156, 112, 76)
PLOT_BORDER_COLOR = (92, 76, 60)
PLOT_GROWING_COLOR = (118, 154, 92)
PLOT_MATURE_COLOR = (235, 196, 82)

TEXT_COLOR = (45, 55, 45)
PLOT_PLANTED_TEXT_COLOR = (245, 235, 205)
PLOT_GROWING_TEXT_COLOR = (235, 245, 220)
PLOT_MATURE_TEXT_COLOR = (80, 60, 25)

# =========================
# Shop Button Settings
# =========================

SHOP_BUTTON_X = 40
SHOP_BUTTON_Y = 620
SHOP_BUTTON_WIDTH = 220
SHOP_BUTTON_HEIGHT = 56

BUTTON_NORMAL_COLOR = (248, 224, 168)
BUTTON_HOVER_COLOR = (255, 236, 188)
BUTTON_BORDER_COLOR = (130, 96, 55)
BUTTON_TEXT_COLOR = (70, 52, 35)

# =========================
# Day Phase Background Colors
# =========================

BACKGROUND_MORNING_COLOR = (205, 230, 190)
BACKGROUND_DAYTIME_COLOR = (188, 224, 170)
BACKGROUND_EVENING_COLOR = (230, 184, 128)
BACKGROUND_MIDNIGHT_COLOR = (74, 91, 130)