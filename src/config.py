from pathlib import Path

# =========================
# Basic Game Information
# =========================

GAME_TITLE = "Gulu Garden - 咕噜小菜园"
GAME_VERSION = "1.2.0"

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

BACKGROUND_MORNING_IMAGE = BACKGROUNDS_DIR / "farm_morning.png"
BACKGROUND_DAYTIME_IMAGE = BACKGROUNDS_DIR / "farm_daytime.png"
BACKGROUND_EVENING_IMAGE = BACKGROUNDS_DIR / "farm_evening.png"
BACKGROUND_MIDNIGHT_IMAGE = BACKGROUNDS_DIR / "farm_midnight.png"

DAY_PHASE_BACKGROUND_IMAGES = {
    "morning": BACKGROUND_MORNING_IMAGE,
    "daytime": BACKGROUND_DAYTIME_IMAGE,
    "evening": BACKGROUND_EVENING_IMAGE,
    "midnight": BACKGROUND_MIDNIGHT_IMAGE,
}

PLOT_EMPTY_IMAGE = TILES_DIR / "plot_empty.png"
PLOT_LOCKED_IMAGE = TILES_DIR / "plot_locked.png"

# =========================
# Crop Image Asset Paths
# =========================

STARBUBBLE_RADISH_IMAGE_DIR = CROPS_DIR / "starbubble_radish"

CROP_STAGE_IMAGE_PATHS = {
    "starbubble_radish": {
        0: STARBUBBLE_RADISH_IMAGE_DIR / "stage_0_seed.png",
        1: STARBUBBLE_RADISH_IMAGE_DIR / "stage_1_sprout.png",
        2: STARBUBBLE_RADISH_IMAGE_DIR / "stage_2_growing.png",
        3: STARBUBBLE_RADISH_IMAGE_DIR / "stage_3_mature.png",
    }
}

# =========================
# Crop Image Drawing Settings
# =========================

CROP_STAGE_IMAGE_SIZE = 96

# 作物底部对齐到土地内部的“种植线”。
# 正数表示更靠下，负数表示更靠上。
CROP_BASE_OFFSET_Y = 4

SHOP_BUTTON_NORMAL_IMAGE = UI_IMAGES_DIR / "button_shop_normal.png"
SHOP_BUTTON_HOVER_IMAGE = UI_IMAGES_DIR / "button_shop_hover.png"
ICON_COIN_IMAGE = ICONS_DIR / "icon_coin.png"
ICON_SEED_STARBUBBLE_RADISH_IMAGE = ICONS_DIR / "icon_seed_starbubble_radish.png"

# =========================
# Colors
# =========================
# 暂时使用柔和背景色，后续再替换成 farm_daytime.png 背景图。

BACKGROUND_COLOR = (188, 224, 170)

# =========================
# Farm Plot Layout Settings
# =========================

PLOT_ROW_COUNTS = [6, 8, 6]

PLOT_ROWS = len(PLOT_ROW_COUNTS)
PLOT_COLUMNS = max(PLOT_ROW_COUNTS)
PLOT_TOTAL = sum(PLOT_ROW_COUNTS)

PLOT_UNLOCKED_COUNT = 4

PLOT_SIZE = 128

PLOT_GAP_X = 1
PLOT_GAP_Y = 2

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
# HUD Icon Settings
# =========================

HUD_ICON_SIZE = 34

HUD_COIN_ICON_X = 36
HUD_COIN_ICON_Y = 22
HUD_COIN_TEXT_X = 78
HUD_COIN_TEXT_Y = 26

HUD_SEED_ICON_X = 180
HUD_SEED_ICON_Y = 22
HUD_SEED_TEXT_X = 222
HUD_SEED_TEXT_Y = 26

HUD_TIME_TEXT_X = 560
HUD_TIME_TEXT_Y = 26

HUD_SEED_TEXT_MAX_WIDTH = HUD_TIME_TEXT_X - HUD_SEED_TEXT_X - 24

# =========================
# HUD Panel Settings
# =========================

HUD_PANEL_X = 24
HUD_PANEL_Y = 14
HUD_PANEL_WIDTH = 1040
HUD_PANEL_HEIGHT = 92
HUD_PANEL_BORDER_RADIUS = 18

# 半透明奶油色背板，保证文字可读，但不完全挡住背景。
HUD_PANEL_BACKGROUND_COLOR = (255, 246, 220, 110)

# 柔和棕色边框。
HUD_PANEL_BORDER_COLOR = (132, 96, 58, 85)

# 轻微阴影，增加层次感。
HUD_PANEL_SHADOW_COLOR = (0, 0, 0, 28)
HUD_PANEL_SHADOW_OFFSET_X = 3
HUD_PANEL_SHADOW_OFFSET_Y = 3

# =========================
# Day Phase Background Colors
# =========================

BACKGROUND_MORNING_COLOR = (205, 230, 190)
BACKGROUND_DAYTIME_COLOR = (188, 224, 170)
BACKGROUND_EVENING_COLOR = (230, 184, 128)
BACKGROUND_MIDNIGHT_COLOR = (74, 91, 130)

# =========================
# Day Phase Scene Tint Settings
# =========================

# 用于土地、作物等场景素材的简易昼夜调色。
# 背景图本身不使用这套调色，因为背景已经是不同时间段的完整图。
SCENE_TINT_SETTINGS = {
    "morning": {
        "multiply": (255, 248, 235),
        "overlay": (255, 230, 170, 8),
    },
    "daytime": {
        "multiply": (255, 255, 255),
        "overlay": (255, 255, 255, 0),
    },
    "evening": {
        "multiply": (248, 222, 190),
        "overlay": (255, 150, 70, 14),
    },
    "midnight": {
        "multiply": (145, 165, 215),
        "overlay": (35, 70, 140, 18),
    },
}

# =========================
# Debug Settings
# =========================

# 开发调试用：允许用数字键临时预览不同昼夜阶段。
# 0 = 恢复真实时间
# 1 = morning
# 2 = daytime
# 3 = evening
# 4 = midnight
ENABLE_DAY_PHASE_PREVIEW_KEYS = True