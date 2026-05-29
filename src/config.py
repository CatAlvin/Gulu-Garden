from pathlib import Path

# =========================
# Basic Game Information
# =========================

GAME_TITLE = "Gulu Garden - 咕噜小菜园"
GAME_VERSION = "0.1.0"

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