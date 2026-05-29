# 咕噜小菜园 Gulu Garden

《咕噜小菜园》（Gulu Garden）是一款使用 Python + Pygame 开发的可爱休闲种菜经营游戏。

玩家可以在自己的小菜园中购买种子、播种、等待作物成长、收获并获得金币。游戏使用现实时间驱动作物成长，即使关闭游戏，作物也会根据真实经过时间继续成长。

本项目是一个长期个人游戏开发项目，目标是练习 Python / Pygame、积累 GitHub 作品集，并逐步扩展为可以打包分享给朋友试玩的可爱休闲小游戏。

---

## 当前版本

Version 1.0.0 — 第一个可试玩版本

当前版本已经完成基础种菜闭环：

* 打开 Pygame 游戏窗口
* 显示 8 块农田
* 前 4 块土地可使用
* 后 4 块土地为 locked 状态
* 点击商店按钮购买星泡萝卜种子
* 购买种子消耗金币
* 播种消耗 1 个种子
* 星泡萝卜根据真实时间成长
* 成熟后可以点击收获
* 收获后获得金币
* 土地恢复为空地
* 游戏可以保存和读取进度
* 关闭游戏期间作物继续成长
* 重新打开游戏后显示离线成长提示
* 根据现实时间显示 Morning / Daytime / Evening / Midnight
* 不同昼夜阶段显示不同背景色

---

## 游戏截图

![Gulu Garden Main Window](docs/images/gulu_garden_v1_0_main_window.png)

当前截图展示了 Version 1.0 候选版本的基础界面，包括金币、种子数量、现实时间阶段、农田格子、商店按钮和作物成长状态。

---

## 核心玩法

当前基础循环：

1. 玩家进入游戏。
2. 查看金币和种子数量。
3. 点击 `Shop: Buy Seed` 购买星泡萝卜种子。
4. 点击空地播种。
5. 等待星泡萝卜成长。
6. 作物成熟后点击收获。
7. 获得金币。
8. 继续购买种子并扩展后续玩法。

当前作物：

| 作物   | 英文名               | 种子价格 | 收获金币 | 成熟时间 |
| ---- | ----------------- | ---: | ---: | ---: |
| 星泡萝卜 | Starbubble Radish |   10 |   20 | 30 秒 |

---

## 操作说明

| 操作                  | 说明               |
| ------------------- | ---------------- |
| 鼠标左键点击土地            | 播种、查看状态或收获       |
| 点击 `Shop: Buy Seed` | 购买 1 个星泡萝卜种子     |
| 按 `B`               | 临时测试快捷键：购买 1 个种子 |
| 按 `S`               | 手动保存游戏           |
| 点击窗口关闭按钮            | 自动保存并退出游戏        |

土地显示说明：

| 显示   | 含义          |
| ---- | ----------- |
| 数字编号 | 空地或锁定土地     |
| P    | 已播种 planted |
| G    | 生长中 growing |
| M    | 已成熟 mature  |

---

## 技术栈

* Python 3.12
* Pygame
* JSON 本地存档
* Git / GitHub 项目管理

---

## 安装与运行

### 1. 克隆项目

```powershell
git clone https://github.com/CatAlvin/Gulu-Garden.git
cd Gulu-Garden
```

### 2. 创建虚拟环境

```powershell
py -3.12 -m venv .venv
```

### 3. 激活虚拟环境

Windows PowerShell：

```powershell
..venv\Scripts\Activate.ps1
```

### 4. 安装依赖

```powershell
python -m pip install -r requirements.txt
```

### 5. 启动游戏

```powershell
python src/main.py
```

运行成功后，应打开一个 1280 × 720 的 Pygame 窗口。

---

## 项目结构

```text
Gulu-Garden/
├─ README.md
├─ requirements.txt
├─ .gitignore
├─ docs/
│  ├─ game-design.md
│  ├─ version-roadmap.md
│  ├─ asset-guide.md
│  ├─ save-format.md
│  ├─ project-structure.md
│  ├─ development-log.md
│  ├─ version-1.0-release-checklist.md
│  └─ images/
├─ data/
│  ├─ crops.json
│  └─ shop_items.json
├─ assets/
│  ├─ images/
│  ├─ audio/
│  └─ fonts/
├─ saves/
│  └─ .gitkeep
├─ src/
│  ├─ main.py
│  ├─ config.py
│  ├─ game.py
│  ├─ models/
│  │  ├─ inventory.py
│  │  ├─ player.py
│  │  └─ plot.py
│  ├─ systems/
│  │  ├─ save_system.py
│  │  ├─ shop_system.py
│  │  └─ time_system.py
│  ├─ ui/
│  │  └─ button.py
│  └─ utils/
│     └─ constants.py
└─ tests/
```

---

## 已实现版本

| 版本          | 内容        | 状态  |
| ----------- | --------- | --- |
| Version 0.1 | 项目骨架与基础窗口 | 已完成 |
| Version 0.2 | 农田网格与鼠标点击 | 已完成 |
| Version 0.3 | 星泡萝卜播种与成长 | 已完成 |
| Version 0.4 | 收获与金币循环   | 已完成 |
| Version 0.5 | 商店与种子背包   | 已完成 |
| Version 0.6 | 单存档系统     | 已完成 |
| Version 0.7 | 离线成长提示    | 已完成 |
| Version 0.9 | 昼夜系统基础版   | 已完成 |

---

## 当前未实现内容

当前版本暂未实现：

* 多存档槽
* 存档选择界面
* 正式商店面板
* 正式背包界面
* 正式作物图片素材
* 浇水系统
* 任务系统
* 图鉴系统
* 多作物系统
* 动画系统
* 音效系统
* exe 打包发布

---

## 后续计划

下一阶段建议进入 Version 1.1 — 简单任务系统。

计划加入：

* 第一次播种任务
* 第一次收获任务
* 收获 3 个星泡萝卜任务
* 任务进度记录
* 任务完成奖励
* 任务数据保存

更长期计划：

* 图鉴系统
* 更多奇幻作物
* 完美品质系统
* 知识锁图鉴
* 高清素材替换
* 基础动画与音效
* exe 打包发布

---

## 存档说明

游戏使用本地 JSON 存档。

默认存档路径：

```text
saves/save_1.json
```

真实存档文件不会提交到 GitHub。仓库中只保留：

```text
saves/.gitkeep
```

---

## 素材说明

当前版本主要使用 Pygame 绘制的占位图形和颜色块。

项目最终美术方向为：

* 高清
* 可爱
* 卡通
* 柔和
* 治愈
* 奇幻小菜园风格

后续会逐步替换为正式图片素材。

---

## 开发日志

详细版本记录见：

```text
docs/development-log.md
```

Version 1.0 发布检查清单见：

```text
docs/version-1.0-release-checklist.md
```
