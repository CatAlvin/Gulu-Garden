# 咕噜小菜园 Gulu Garden

《咕噜小菜园》（Gulu Garden）是一款使用 Python + Pygame 开发的可爱休闲种菜经营游戏。

玩家将在自己的小菜园中购买种子、播种、浇水、等待作物成熟、收获并获得金币。项目长期目标是做成一个可试玩、可展示、可扩展的个人 Pygame 游戏作品集项目。

当前项目处于早期开发阶段，第一目标是先完成稳定、清晰、可运行的基础版本。

---

## 当前版本

Version 0.6.0 — 单存档系统

当前已完成：

- 创建基础项目结构
- 创建 Pygame 窗口
- 设置窗口大小为 1280 × 720
- 支持正常关闭窗口
- 显示 8 块基础土地
- 前 4 块土地为 empty 状态
- 后 4 块土地为 locked 状态
- 支持鼠标点击土地
- 添加星泡萝卜 Starbubble Radish 数据
- 支持点击 empty 土地播种星泡萝卜
- 作物会根据真实经过时间成长
- 作物成熟后土地状态变为 mature
- 添加玩家金币
- 初始金币为 50
- 成熟作物可以被点击收获
- 收获星泡萝卜后获得 20 金币
- 收获后土地恢复为 empty
- 添加种子背包
- 播种会消耗 1 个星泡萝卜种子
- 种子不足时不能播种
- 添加星泡萝卜种子商品数据
- 点击商店按钮可以购买星泡萝卜种子
- 购买种子消耗 10 金币
- 金币不足时不能购买
- 顶部 HUD 显示金币和种子数量
- 添加 JSON 单存档系统
- 退出游戏时自动保存进度
- 按 `S` 可以手动保存进度
- 启动游戏时自动读取已有存档
- 可以恢复金币、种子、土地和作物状态

当前暂未实现：

- 多存档槽
- 存档选择界面
- 离线成长总结提示
- 正式商店面板
- 正式背包界面
- 正式作物素材
- 浇水系统
- 任务系统
- 图鉴系统
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

下一版本为 Version 0.7 — 离线成长提示。

Version 0.7 目标：

- 启动游戏时检查作物是否在离线期间成长
- 如果作物在离线期间成熟，显示提示信息
- 告诉玩家哪些土地上的作物已经成熟
- 保持当前基础成长逻辑
- 暂不做复杂离线收益总结
- 暂不做作物枯萎
- 暂不做系统时间作弊检测

---

## 开发说明

本项目遵循小版本迭代原则：

- 每个版本只解决一个核心问题
- 每个版本都要能运行和测试
- 不提前加入复杂功能
- 优先保证结构清晰和长期可维护