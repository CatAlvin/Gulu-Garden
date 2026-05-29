# docs/project-structure.md

# 《咕噜小菜园》Gulu Garden 项目结构说明 v0.1

## 1. 文档目的

本文档用于说明《咕噜小菜园》（Gulu Garden）的项目目录结构、各文件职责、模块之间的关系，以及第一阶段需要优先创建和维护的文件。

本项目是一个长期单人开发的 Pygame 游戏项目，因此目录结构需要同时满足：

1. 初期开发简单清晰。
2. 后续功能容易扩展。
3. GitHub 展示时结构专业。
4. 文件职责明确，避免所有代码堆在 `main.py` 中。
5. 美术、音频、数据、存档和源码分离。

---

## 2. 推荐项目结构

项目根目录建议命名为：

```text
gulu-garden/
```

完整结构如下：

```text
gulu-garden/
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
│  ├─ crops.json
│  ├─ shop_items.json
│  └─ tasks.json
├─ assets/
│  ├─ images/
│  │  ├─ backgrounds/
│  │  ├─ crops/
│  │  ├─ tiles/
│  │  └─ ui/
│  ├─ audio/
│  │  ├─ bgm/
│  │  └─ sfx/
│  └─ fonts/
├─ saves/
│  └─ .gitkeep
├─ src/
│  ├─ main.py
│  ├─ config.py
│  ├─ game.py
│  ├─ models/
│  │  ├─ crop.py
│  │  ├─ plot.py
│  │  ├─ inventory.py
│  │  └─ player.py
│  ├─ systems/
│  │  ├─ time_system.py
│  │  ├─ save_system.py
│  │  ├─ shop_system.py
│  │  └─ task_system.py
│  ├─ ui/
│  │  ├─ button.py
│  │  ├─ panel.py
│  │  └─ hud.py
│  └─ utils/
│     ├─ asset_loader.py
│     └─ constants.py
└─ tests/
   └─ test_save_system.py
```

---

# 3. 根目录文件说明

## 3.1 README.md

`README.md` 是项目首页说明文件，也是 GitHub 展示中最重要的文档。

它应该说明：

* 游戏名称
* 游戏简介
* 当前版本
* 已实现功能
* 项目截图
* 如何安装依赖
* 如何运行游戏
* 项目结构
* 操作说明
* 版本路线
* 素材说明
* 开发日志链接

第一阶段 README 不需要非常长，但必须让别人知道：

> 这个项目是什么，怎么运行，目前做到哪里。

---

## 3.2 requirements.txt

`requirements.txt` 用于记录项目依赖。

第一阶段最少只需要：

```text
pygame
```

后续可能加入：

```text
pytest
python-dotenv
requests
```

说明：

* `pygame`：游戏开发核心库。
* `pytest`：后期用于测试存档系统等逻辑。
* `python-dotenv`：后期如果接入 DeepSeek API，可用于读取 `.env`。
* `requests`：后期如果接入 API，可用于网络请求。

第一阶段不需要提前安装过多库。

---

## 3.3 .gitignore

`.gitignore` 用于告诉 Git 哪些文件不应该上传。

本项目不应上传：

* Python 缓存
* 虚拟环境
* 本地存档
* `.env`
* 打包产物
* 日志文件
* 临时素材
* 编辑器缓存

但应保留：

* 源代码
* 文档
* 数据配置文件
* 必要的正式素材
* `.gitkeep`

---

# 4. docs/ 文档目录

`docs/` 用于保存项目设计文档。

文档目录是本项目长期维护的重要部分，因为这是一个作品集项目，不只是本地小游戏。

## 4.1 docs/game-design.md

游戏设计文档。

记录内容包括：

* 游戏定位
* 核心玩法
* 作物系统
* 土地系统
* 金币系统
* 背包系统
* 商店系统
* 任务系统
* 图鉴系统
* UI 设计
* 第一阶段做什么
* 第一阶段不做什么

它回答的问题是：

> 这个游戏怎么玩？为什么这样设计？

---

## 4.2 docs/version-roadmap.md

版本路线文档。

记录内容包括：

* Version 0.1 做什么
* Version 0.2 做什么
* Version 1.0 之前的目标
* 哪些功能后期再做
* 每个版本的验收标准

它回答的问题是：

> 这个项目按什么顺序开发？

---

## 4.3 docs/asset-guide.md

素材规范文档。

记录内容包括：

* 美术风格
* AI 生成素材规范
* 文件命名规则
* 图片尺寸建议
* 素材目录结构
* 第一阶段最低素材清单
* 音效和字体规范

它回答的问题是：

> 素材应该怎么生成、命名、放置和管理？

---

## 4.4 docs/save-format.md

存档格式文档。

记录内容包括：

* JSON 存档结构
* 玩家金币
* 种子数量
* 土地状态
* 作物种植时间
* 离线成长计算
* 多存档设计
* 图鉴、任务、设置的后续扩展字段

它回答的问题是：

> 游戏如何保存进度？关闭游戏后作物如何继续成长？

---

## 4.5 docs/project-structure.md

项目结构说明文档。

也就是本文档。

它回答的问题是：

> 每个文件和文件夹负责什么？

---

# 5. data/ 数据配置目录

`data/` 用于保存游戏配置数据。

原则：

> 能用 JSON 配置的内容，就尽量不要硬编码在 Python 文件中。

这样后续新增作物、商品、任务时，不需要大规模修改代码。

---

## 5.1 data/crops.json

作物数据文件。

用于记录所有作物的基础配置。

第一阶段只需要星泡萝卜。

示例字段包括：

```text
id
name_cn
name_en
description
seed_price
sell_price
growth_time_seconds
growth_stages
need_water
can_wither
preferred_time
perfect_chance
```

第一阶段重点字段：

* `id`
* `name_cn`
* `name_en`
* `description`
* `seed_price`
* `sell_price`
* `growth_time_seconds`
* `growth_stages`
* `need_water`

---

## 5.2 data/shop_items.json

商店商品数据文件。

用于记录商店里能购买的物品。

第一阶段只需要：

* 星泡萝卜种子

后续可以扩展：

* 其他种子
* 肥料
* 水壶
* 工具
* 装饰
* 特殊道具

---

## 5.3 data/tasks.json

任务数据文件。

用于记录任务配置。

第一阶段可以先创建空结构，或者只写简单任务。

例如：

* 第一次播种
* 第一次收获
* 收获 3 个星泡萝卜

如果第一阶段还没实现任务系统，`tasks.json` 可以先保留但不读取。

---

# 6. assets/ 素材目录

`assets/` 用于保存游戏素材。

包括：

* 图片
* 音频
* 字体

素材目录不应混入 Python 代码。

---

## 6.1 assets/images/

图片资源目录。

### backgrounds/

存放背景图。

例如：

```text
farm_daytime.png
farm_morning.png
farm_evening.png
farm_midnight.png
```

第一阶段只需要：

```text
farm_daytime.png
```

### crops/

存放作物图片。

每种作物建议单独一个文件夹。

例如：

```text
assets/images/crops/starbubble_radish/
```

里面可以放：

```text
stage_0_seed.png
stage_1_sprout.png
stage_2_growing.png
stage_3_mature.png
icon_seed.png
icon_crop.png
```

### tiles/

存放土地格子图片。

例如：

```text
plot_empty.png
plot_locked.png
plot_need_water.png
plot_watered.png
```

### ui/

存放 UI 相关图片。

例如：

```text
button_normal.png
button_hover.png
panel_shop.png
panel_inventory.png
icon_coin.png
```

---

## 6.2 assets/audio/

音频资源目录。

### bgm/

存放背景音乐。

例如：

```text
bgm_main_farm.mp3
```

### sfx/

存放音效。

例如：

```text
sfx_click.wav
sfx_plant.wav
sfx_water.wav
sfx_harvest.wav
sfx_coin.wav
```

第一阶段可以只预留目录，不急着加入音频。

---

## 6.3 assets/fonts/

字体目录。

用于保存游戏字体。

注意：

* 字体必须支持中文。
* 不要随便上传版权不明确的商业字体。
* 如果使用免费字体，应在 README 或文档中说明来源和授权。

---

# 7. saves/ 存档目录

`saves/` 用于保存玩家本地存档。

第一阶段或多存档阶段建议使用：

```text
save_1.json
save_2.json
save_3.json
```

但是这些真实存档不应该提交到 GitHub。

因此目录中保留：

```text
.gitkeep
```

`.gitkeep` 的作用是：

> 让 Git 记录这个空文件夹。

`.gitignore` 中应忽略真实存档，但保留 `.gitkeep`。

---

# 8. src/ 源码目录

`src/` 是项目核心代码目录。

所有 Python 游戏代码都应放在这里。

---

## 8.1 src/main.py

程序入口文件。

职责：

* 初始化项目
* 创建游戏对象
* 启动游戏主循环

它应该尽量短。

不建议在 `main.py` 中写大量游戏逻辑。

推荐理解：

> main.py 只负责“启动游戏”，不负责“实现游戏”。

---

## 8.2 src/config.py

配置文件。

职责：

* 窗口宽度
* 窗口高度
* FPS
* 项目根目录
* assets 路径
* data 路径
* saves 路径
* 默认字体
* 默认颜色

例如：

```text
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60
```

配置集中管理的好处是：

> 后续改分辨率或路径时，不需要到处找代码。

---

## 8.3 src/game.py

游戏主控制文件。

职责：

* 初始化 Pygame
* 创建窗口
* 管理主循环
* 处理事件
* 更新游戏状态
* 绘制画面
* 调用各系统

可以理解为游戏的“大脑”。

它通常会包含类似这些方法：

```text
run()
handle_events()
update()
draw()
quit()
```

但具体代码后续再写。

---

# 9. src/models/ 数据模型目录

`models/` 用于保存游戏中的核心对象。

这些类主要表示“游戏里有什么东西”。

---

## 9.1 src/models/crop.py

作物模型。

职责：

* 表示一种作物
* 保存作物 ID
* 保存成长时间
* 保存当前阶段
* 判断是否成熟
* 计算成长阶段

第一阶段主要服务于星泡萝卜。

后续扩展到所有作物。

---

## 9.2 src/models/plot.py

土地模型。

职责：

* 表示一块土地
* 保存土地编号
* 保存土地状态
* 保存是否解锁
* 保存当前作物
* 处理播种、浇水、收获等操作

土地是第一阶段最重要的模型之一。

---

## 9.3 src/models/inventory.py

背包模型。

职责：

* 保存种子数量
* 保存作物数量
* 保存工具
* 保存肥料
* 保存装饰

第一阶段只需要实现：

```text
种子数量管理
```

例如：

* 增加星泡萝卜种子
* 消耗星泡萝卜种子
* 检查种子是否足够

---

## 9.4 src/models/player.py

玩家模型。

职责：

* 保存玩家金币
* 处理金币增加
* 处理金币减少
* 判断金币是否足够

第一阶段不做等级系统。

金币是主要成长资源。

---

# 10. src/systems/ 系统逻辑目录

`systems/` 用于保存跨对象的系统逻辑。

这些文件通常不代表某个具体物体，而是负责一类功能。

---

## 10.1 src/systems/time_system.py

时间系统。

职责：

* 获取当前现实时间
* 判断当前昼夜阶段
* 计算作物已经成长多久
* 支持离线成长
* 后期可检测异常时间变化

这是本项目最重要的系统之一。

第一阶段必须保证时间逻辑清晰。

---

## 10.2 src/systems/save_system.py

存档系统。

职责：

* 创建新存档
* 读取 JSON 存档
* 写入 JSON 存档
* 处理存档不存在
* 处理存档损坏
* 固定支持 3 个存档槽

这是本项目另一个核心系统。

---

## 10.3 src/systems/shop_system.py

商店系统。

职责：

* 读取商品数据
* 判断金币是否足够
* 购买商品
* 扣除金币
* 增加背包物品

第一阶段只需要支持购买星泡萝卜种子。

---

## 10.4 src/systems/task_system.py

任务系统。

职责：

* 读取任务数据
* 记录任务进度
* 判断任务是否完成
* 发放任务奖励

第一阶段可以先创建文件，但不一定实现完整功能。

---

# 11. src/ui/ 界面目录

`ui/` 用于保存界面组件代码。

界面组件应尽量和游戏逻辑分离。

---

## 11.1 src/ui/button.py

按钮组件。

职责：

* 保存按钮位置
* 判断鼠标是否悬停
* 判断鼠标是否点击
* 绘制按钮
* 显示按钮文字或图标

第一阶段可以先做简单矩形按钮。

后期再换成高清 UI 图片按钮。

---

## 11.2 src/ui/panel.py

面板组件。

职责：

* 绘制 UI 面板
* 显示商店面板
* 显示背包面板
* 显示图鉴面板
* 显示提示框

第一阶段可以先做简单半透明矩形面板。

---

## 11.3 src/ui/hud.py

HUD 是 Head-Up Display 的缩写，指游戏主界面的常驻信息栏。

职责：

* 显示金币
* 显示当前时间
* 显示当前昼夜阶段
* 显示当前选中的种子
* 显示操作提示
* 显示任务摘要

第一阶段 HUD 应优先实现金币和提示文本。

---

# 12. src/utils/ 工具目录

`utils/` 用于保存通用工具函数。

这些函数不属于某个具体系统，但很多地方都会用到。

---

## 12.1 src/utils/asset_loader.py

素材加载工具。

职责：

* 加载图片
* 加载音频
* 缓存素材
* 处理素材不存在的情况
* 返回占位素材

设计这个文件的原因是：

> 不希望每个模块都自己写一遍 pygame.image.load。

后期换素材路径或加缓存时，也只需要改这里。

---

## 12.2 src/utils/constants.py

常量文件。

职责：

* 土地状态常量
* 作物状态常量
* 昼夜阶段常量
* UI 状态常量
* 颜色常量

例如：

```text
PLOT_EMPTY = "empty"
PLOT_LOCKED = "locked"
PLOT_MATURE = "mature"
```

使用常量可以减少拼写错误。

---

# 13. tests/ 测试目录

`tests/` 用于保存测试代码。

第一阶段可以先只测试存档系统。

## 13.1 tests/test_save_system.py

用于测试：

* 新存档是否能创建
* 存档是否能写入
* 存档是否能读取
* 缺失字段是否能补默认值
* 损坏存档是否不会导致程序直接崩溃

虽然 Pygame 画面部分不容易自动测试，但存档、时间、数据读取这些逻辑很适合写测试。

---

# 14. 第一阶段必须创建的文件

第一阶段建议优先创建：

```text
README.md
requirements.txt
.gitignore

docs/game-design.md
docs/version-roadmap.md
docs/asset-guide.md
docs/save-format.md
docs/project-structure.md

data/crops.json
data/shop_items.json

saves/.gitkeep

src/main.py
src/config.py
src/game.py
src/models/crop.py
src/models/plot.py
src/models/inventory.py
src/models/player.py
src/systems/time_system.py
src/systems/save_system.py
src/systems/shop_system.py
src/ui/button.py
src/ui/hud.py
src/utils/asset_loader.py
src/utils/constants.py
```

第一阶段可以暂时不重点实现：

```text
src/systems/task_system.py
src/ui/panel.py
tests/test_save_system.py
```

但可以先创建空文件，方便保持结构完整。

---

# 15. 模块依赖关系建议

为了避免代码混乱，建议遵守以下依赖方向：

```text
main.py
  ↓
game.py
  ↓
models / systems / ui / utils
```

更具体地说：

* `main.py` 可以导入 `Game`
* `game.py` 可以导入 models、systems、ui、utils
* `systems` 可以操作 models
* `ui` 尽量只负责显示，不直接修改复杂游戏数据
* `models` 尽量不要依赖 ui
* `utils` 尽量不依赖具体游戏逻辑

不推荐出现：

```text
crop.py 导入 game.py
plot.py 导入 hud.py
button.py 直接修改 save_system.py
```

这样容易造成循环依赖和调试困难。

---

# 16. 第一阶段开发顺序建议

建议按照以下顺序开发：

## Step 1：创建项目结构

先创建所有文件夹和基础文件。

重点是让项目看起来像一个正式项目。

## Step 2：写 README 和文档

先把项目目标、结构和运行方式写清楚。

这会帮助后续开发不跑偏。

## Step 3：实现 Pygame 窗口

先让 `src/main.py` 能打开窗口。

## Step 4：显示背景和土地

让玩家能看到农田。

## Step 5：实现土地点击

让玩家点击土地时能看到状态反馈。

## Step 6：实现星泡萝卜数据

从 `data/crops.json` 读取星泡萝卜配置。

## Step 7：实现播种和成长

作物能从种子阶段成长到成熟阶段。

## Step 8：实现收获金币

成熟后可以收获，玩家金币增加。

## Step 9：实现商店和种子背包

玩家必须先购买种子，才能播种。

## Step 10：实现存档和离线成长

关闭游戏再打开，状态仍然正确。

---

# 17. 常见错误与避免方式

## 17.1 不要把所有代码写进 main.py

错误做法：

```text
main.py 中包含窗口、土地、作物、商店、存档、UI 所有逻辑
```

后果：

* 代码越来越长
* 很难调试
* 后续无法扩展
* GitHub 展示效果差

正确做法：

```text
main.py 只启动游戏
game.py 管理主循环
models 表示对象
systems 处理系统逻辑
ui 负责显示
utils 负责工具函数
```

---

## 17.2 不要一开始做太多功能

第一阶段不要同时做：

* 多作物
* 完美品质
* 宠物
* 好友
* 成就
* 装饰
* 天气
* 复杂动画

否则项目容易失控。

当前最重要的是：

> 星泡萝卜的种植、成长、收获、卖钱、存档和离线成长。

---

## 17.3 不要把数据写死在代码里

不推荐：

```text
在 crop.py 里直接写死星泡萝卜价格和成熟时间
```

推荐：

```text
在 data/crops.json 中配置作物数据
Python 代码负责读取和使用数据
```

这样后期新增作物更方便。

---

## 17.4 不要提交真实存档和临时文件

真实存档会不断变化，不适合提交到 GitHub。

推荐：

```text
提交 saves/.gitkeep
忽略 saves/*.json
```

---

# 18. 当前结论

《咕噜小菜园》的项目结构采用工程化但不过度复杂的方式。

核心思想是：

> 文档、数据、素材、存档、源码分开管理；主循环、模型、系统、UI、工具分层组织。

第一阶段最重要的不是把所有文件都写满，而是让结构清晰、核心闭环稳定，并为后续版本留下合理扩展空间。
