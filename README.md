# 咕噜小菜园 Gulu Garden

《咕噜小菜园》（Gulu Garden）是一款使用 Python + Pygame 开发的可爱休闲种菜经营游戏。

玩家将在自己的小菜园中购买种子、播种、浇水、等待作物成熟、收获并获得金币。项目长期目标是做成一个可试玩、可展示、可扩展的个人 Pygame 游戏作品集项目。

当前项目处于早期开发阶段，第一目标是先完成稳定、清晰、可运行的基础版本。

---

## 当前版本

Version 0.2.0 — 农田网格与鼠标点击

当前已完成：

- 创建基础项目结构
- 创建 Pygame 窗口
- 设置窗口大小为 1280 × 720
- 设置窗口标题
- 设置基础 FPS
- 支持正常关闭窗口
- 显示基础背景色
- 显示 8 块基础土地
- 前 4 块土地为 empty 状态
- 后 4 块土地为 locked 状态
- 支持鼠标点击土地
- 点击土地后可以显示土地编号和状态

当前暂未实现：

- 播种系统
- 作物成长系统
- 商店系统
- 存档系统
- 背包系统
- 动画系统
- 音效系统

## 技术栈

- Python 3.12.1
- Pygame

---

## 安装与运行

### 1. 进入项目目录

```powershell
cd "D:\Programming\Python\python_workspace\project\Gulu-Garden"
```

### 2. 创建并激活虚拟环境

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. 安装依赖

```powershell
python -m pip install -r requirements.txt
```

### 4. 启动游戏

```powershell
python src/main.py
```

运行成功后，应打开一个标题为 `Gulu Garden - 咕噜小菜园` 的 1280 × 720 Pygame 窗口。

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
│  └─ project-structure.md
├─ data/
├─ assets/
├─ saves/
├─ src/
│  ├─ main.py
│  ├─ config.py
│  └─ game.py
└─ tests/
```

---

## 后续计划

下一版本为 Version 0.3 — 星泡萝卜播种与成长。

Version 0.3 目标：

- 添加星泡萝卜基础数据
- 支持选择星泡萝卜种子
- 点击空地可以播种
- 土地状态从 empty 变为 planted / growing
- 作物根据时间成长
- 成熟后状态变为 mature
- UI 显示作物状态

---

## 开发说明

本项目遵循小版本迭代原则：

- 每个版本只解决一个核心问题
- 每个版本都要能运行和测试
- 不提前加入复杂功能
- 优先保证结构清晰和长期可维护