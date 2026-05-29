from pathlib import Path

# =========================
# Basic Game Information
# =========================

GAME_TITLE = "Gulu Garden - 咕噜小菜园"
GAME_VERSION = "0.6.0"

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
# Colors
# =========================
# 暂时使用柔和背景色，后续再替换成 farm_daytime.png 背景图。

BACKGROUND_COLOR = (188, 224, 170)

# =========================
# Farm Plot Settings
# =========================

PLOT_COLUMNS = 4
PLOT_ROWS = 2
PLOT_TOTAL = PLOT_COLUMNS * PLOT_ROWS
PLOT_UNLOCKED_COUNT = 4

PLOT_SIZE = 120
PLOT_GAP = 28

PLOT_START_X = 340
PLOT_START_Y = 230

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