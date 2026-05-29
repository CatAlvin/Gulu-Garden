# Gulu Garden Version 1.0 Release Checklist

## 1. Basic Run Check

- [x] `python src/main.py` can start the game.
- [x] The game window size is 1280 × 720.
- [x] The window title displays Gulu Garden / 咕噜小菜园.
- [x] The game can be closed normally.
- [x] No error appears in the terminal during normal play.

## 2. Core Gameplay Check

- [x] The player can see 8 farm plots.
- [x] The first 4 plots are usable.
- [x] The last 4 plots are locked.
- [x] Locked plots cannot be planted.
- [x] The player can buy Starbubble Radish seeds.
- [x] Buying seeds costs coins.
- [x] Seeds are added to the inventory after purchase.
- [x] Empty plots can be planted when seeds are available.
- [x] Planting consumes 1 seed.
- [x] Planting fails when there are no seeds.
- [x] Crops grow over real elapsed time.
- [x] Crops eventually become mature.
- [x] Mature crops can be harvested.
- [x] Harvesting gives coins.
- [x] Harvested plots return to empty.

## 3. Save and Load Check

- [x] Pressing `S` saves the game.
- [x] Closing the game saves the game automatically.
- [x] Restarting the game loads the saved progress.
- [x] Coins are restored correctly.
- [x] Seed inventory is restored correctly.
- [x] Plot states are restored correctly.
- [x] Planted crops are restored correctly.
- [x] Real save files are not committed to GitHub.

## 4. Offline Growth Check

- [x] Plant a crop and save.
- [x] Close the game before the crop matures.
- [x] Wait more than the growth time.
- [x] Restart the game.
- [x] The crop becomes mature.
- [x] The game shows an offline growth message.

## 5. Day Phase Check

- [x] HUD displays current real-world time.
- [x] HUD displays current day phase.
- [x] Day phase can be Morning / Daytime / Evening / Midnight.
- [x] Background color changes according to day phase.

## 6. GitHub Project Check

- [x] `README.md` explains what the game is.
- [x] `README.md` explains how to install dependencies.
- [x] `README.md` explains how to run the game.
- [x] `README.md` lists current implemented features.
- [x] `README.md` lists future plans.
- [x] `requirements.txt` contains pygame.
- [x] `.gitignore` ignores `.venv/`.
- [x] `.gitignore` ignores `saves/*.json`.
- [x] Project structure is clear.
- [x] Development log is updated.

## 7. Version 1.0 Decision

Version 1.0 can be marked complete only when all critical gameplay, save/load, and README checks pass.
