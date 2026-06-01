# docs/asset-guide.md

# 《咕噜小菜园》Gulu Garden 素材规范文档 v0.2

## 1. 文档目的

本文档用于规范《咕噜小菜园》（Gulu Garden）的美术素材、音频素材、文件命名、目录结构和 AI 生成素材流程。

从本版本开始，除完整背景图以外，所有需要后期抠图并在游戏中以透明 PNG 使用的素材，统一采用：

> 纯绿色背景抠图版

也就是说，AI 生成阶段不再优先要求 true transparent background，而是要求模型生成纯绿色背景。后期通过图像处理工具把纯绿色背景抠掉，再导出真正带 alpha 通道的 PNG 文件供 Pygame 使用。

本项目最终美术风格确定为：

> 高清可爱卡通风

不是像素风。

虽然游戏使用 Pygame 开发，但视觉目标不是粗糙实验项目，而是尽量做成一个画面舒服、界面清晰、适合 GitHub 展示和朋友试玩的可爱休闲小游戏。

---

# 2. 美术总方向

## 2.1 风格关键词

游戏整体美术风格应符合以下关键词：

* 高清
* 可爱
* 卡通
* 柔和
* 治愈
* 温暖
* 轻松
* 明亮
* 童话感
* 奇幻小菜园
* 干净边缘
* 适合后期抠图

英文关键词可用于 AI 生成素材：

!!!text
high-resolution, cute cartoon style, cozy farming game, soft pastel colors, whimsical fantasy garden, clean game UI, warm lighting, adorable vegetables, casual farming game style, clean silhouette, crisp cutout edge, no text, no watermark
!!!

## 2.2 不采用的风格

本项目不采用以下方向作为主风格：

* 像素风
* 黑暗奇幻风
* 写实农场风
* 低清网页小游戏风
* 复杂厚涂风
* 赛博朋克风
* 恐怖风
* 过度幼儿化风格
* 过度发光风
* 复杂粒子特效风
* 真实摄影素材风

## 2.3 视觉参考方向

整体观感应接近：

* 可爱农场小游戏
* 童话小菜园
* 治愈系放置游戏
* 轻量级移动端经营游戏
* 高清卡通 UI 游戏

视觉重点不是炫技，而是：

1. 玩家一眼能看懂操作。
2. 作物状态清晰。
3. 色彩温暖舒服。
4. UI 不拥挤。
5. 素材风格统一。
6. 抠图后边缘干净，不出现绿色残边。

---

# 3. 纯绿色背景抠图版规范

## 3.1 为什么统一使用纯绿色背景

AI 直接生成透明 PNG 时，常见问题包括：

* 透明背景不稳定。
* 输出看似透明，实际带棋盘格背景。
* 素材边缘有半透明脏边。
* 光晕、阴影、发光效果与透明区域混在一起，后期很难清理。
* 多张素材透明边缘不一致，放进 Pygame 后显得风格不统一。

因此，当前项目统一采用：

> AI 生成纯绿色背景图 → 本地扣除纯绿色 → 输出透明 PNG → 接入 Pygame

这条流程更稳定，也更方便批处理。

## 3.2 纯绿色背景标准

所有需要抠图的素材，提示词中必须明确写：

!!!text
solid pure chroma key green background, background color must be exactly RGB(0,255,0) / HEX #00FF00, not transparent, no checkerboard pattern, no fake transparency
!!!

要求：

* 背景必须是纯绿色。
* 背景颜色必须是 `RGB(0,255,0)`。
* 背景颜色必须是 `HEX #00FF00`。
* 不能要求透明背景。
* 不能出现棋盘格背景。
* 不能出现假透明背景。
* 不能出现渐变绿色背景。
* 不能出现草地、土壤、光影等背景元素。

## 3.3 哪些素材使用纯绿色背景

以下素材必须使用纯绿色背景抠图版：

| 类型 | 是否使用纯绿色背景 | 原因 |
| --- | --- | --- |
| 作物成长阶段图 | 是 | 后期要叠加到土地上 |
| 作物图标 | 是 | 后期用于 UI、背包、商店 |
| 土地格子 | 是 | 需要叠加到背景图上 |
| UI 按钮 | 是 | 需要在 Pygame 中绘制文字 |
| UI 面板 | 是 | 需要叠加在游戏界面上 |
| 金币图标 | 是 | HUD 常驻图标 |
| 商店图标 | 是 | UI 图标 |
| 背包图标 | 是 | UI 图标 |
| 图鉴图标 | 是 | UI 图标 |
| 装饰物 | 是 | 未来需要摆放到地图上 |
| 角色 / 宠物 | 是 | 未来需要叠加到界面中 |
| 特效帧 | 视情况 | 如有半透明特效，后期可单独处理 |
| 完整背景图 | 否 | 背景图本身不需要抠图 |

## 3.4 纯绿色不能出现在主体上

因为后期会扣除 `#00FF00`，所以素材主体内部不能使用接近纯绿色的颜色。

尤其注意：

* 叶子不能使用高饱和亮绿色。
* 草、藤蔓、绿宝石、绿色 UI 装饰不能接近 `#00FF00`。
* 如果需要绿色元素，应使用柔和薄荷绿、灰绿、浅橄榄绿等低饱和颜色。

推荐写法：

!!!text
leaf color should be soft muted mint green and must not match the pure green background
!!!

不推荐写法：

!!!text
bright green leaves
!!!

## 3.5 发光、光晕与阴影限制

为了保证抠图干净，所有抠图素材默认不使用外部发光、光晕、泛光和大面积投影。

提示词中建议统一写：

!!!text
no glow, no aura, no bloom, no light halo, no external shadow, clean outer silhouette, crisp cutout edge
!!!

允许的效果：

* 素材内部的柔和高光。
* 物体表面的轻微亮面。
* UI 按钮内部的柔和内阴影。
* 金币表面的高光。
* 叶片、果实、按钮自身内部的颜色层次。

不推荐的效果：

* 物体外圈光晕。
* 大范围发光粒子。
* 模糊半透明阴影。
* 漂浮的发光点。
* 背景上的辉光。
* 和纯绿色背景混在一起的半透明边缘。

## 3.6 素材位置规范

除非某个素材有特殊构图要求，所有可抠图素材统一要求居中：

!!!text
centered object, the object must be centered both horizontally and vertically
!!!

统一居中的好处：

1. 后续在 Pygame 里更容易用代码控制位置。
2. 批量缩放时不容易产生偏移。
3. 作物、图标、按钮的视觉中心更稳定。
4. 如果需要贴地、靠边或偏移，可以在 Pygame 绘制阶段调整，而不是让 AI 直接固定死。

## 3.7 抠图后最终文件要求

AI 生成阶段使用纯绿色背景，但最终接入游戏的文件应当是透明 PNG。

最终接入 Pygame 的图片应满足：

* 文件格式：PNG
* 背景：透明
* alpha 通道：存在
* 边缘：干净
* 无绿色残边
* 无棋盘格
* 无文字
* 无水印

建议工作文件命名：

| 阶段 | 示例文件名 | 是否提交 GitHub |
| --- | --- | --- |
| AI 原始绿底图 | stage_0_seed_raw_green.png | 可不提交 |
| 抠图后正式图 | stage_0_seed.png | 提交 |
| 废稿 | stage_0_seed_test_01.png | 不建议提交 |

正式游戏路径仍然使用规范文件名，例如：

!!!text
assets/images/crops/starbubble_radish/stage_0_seed.png
!!!

---

# 4. 初始分辨率与适配原则

## 4.1 初始窗口大小

第一阶段窗口大小固定为：

!!!text
1280 × 720
!!!

这是 16:9 横屏比例，适合桌面 Pygame 项目，也方便录屏展示。

## 4.2 后续扩展目标

未来可能扩展到：

!!!text
2560 × 1440
!!!

或全屏模式。

但第一阶段不处理复杂适配，只保证 1280 × 720 下界面清晰。

## 4.3 素材分辨率原则

由于后续可能适配更高分辨率，建议 AI 生成素材时不要太小。

推荐原则：

| 素材类型 | 推荐生成尺寸 | 背景策略 |
| --- | ---: | --- |
| 背景图 | 2560 × 1440 | 正常不透明背景 |
| 单个作物图标 | 512 × 512 | 纯绿色背景抠图版 |
| 作物成长阶段图 | 512 × 512 | 纯绿色背景抠图版 |
| UI 图标 | 256 × 256 或 512 × 512 | 纯绿色背景抠图版 |
| 土地格子 | 512 × 512 | 纯绿色背景抠图版 |
| UI 按钮 | 512 × 160 | 纯绿色背景抠图版 |
| 装饰物 | 512 × 512 或 1024 × 1024 | 纯绿色背景抠图版 |
| 宠物角色 | 1024 × 1024 | 纯绿色背景抠图版 |
| 商店物品图标 | 512 × 512 | 纯绿色背景抠图版 |

在游戏中可以缩放显示，但原始素材应尽量高清，方便后期适配。

---

# 5. 素材目录结构

推荐素材目录如下：

!!!text
assets/
├─ images/
│  ├─ backgrounds/
│  ├─ crops/
│  │  └─ starbubble_radish/
│  ├─ tiles/
│  ├─ ui/
│  ├─ icons/
│  ├─ decorations/
│  ├─ characters/
│  └─ effects/
├─ audio/
│  ├─ bgm/
│  └─ sfx/
└─ fonts/
!!!

## 5.1 backgrounds/

用于存放背景图。

背景图不使用纯绿色背景抠图版，因为它本身就是完整画面。

例如：

!!!text
assets/images/backgrounds/farm_morning.png
assets/images/backgrounds/farm_daytime.png
assets/images/backgrounds/farm_evening.png
assets/images/backgrounds/farm_midnight.png
!!!

第一阶段可以只使用一张背景图：

!!!text
assets/images/backgrounds/farm_daytime.png
!!!

## 5.2 crops/

用于存放作物素材。

每种作物单独一个文件夹。

例如：

!!!text
assets/images/crops/starbubble_radish/
├─ stage_0_seed.png
├─ stage_1_sprout.png
├─ stage_2_growing.png
├─ stage_3_mature.png
├─ icon_seed.png
├─ icon_crop.png
└─ perfect.png
!!!

注意：

* AI 生成原图可以是绿底图。
* 最终放入该目录的正式图应是抠图后的透明 PNG。
* 文件名不需要写 `transparent` 或 `green`。

## 5.3 tiles/

用于存放土地、地块、网格等素材。

例如：

!!!text
assets/images/tiles/plot_empty.png
assets/images/tiles/plot_locked.png
assets/images/tiles/plot_watered.png
assets/images/tiles/plot_need_water.png
assets/images/tiles/plot_mature_highlight.png
!!!

土地素材同样先用纯绿色背景生成，后期抠图为透明 PNG。

## 5.4 ui/

用于存放 UI 面板、按钮、边框等素材。

例如：

!!!text
assets/images/ui/button_normal.png
assets/images/ui/button_hover.png
assets/images/ui/button_pressed.png
assets/images/ui/panel_main.png
assets/images/ui/panel_shop.png
assets/images/ui/panel_inventory.png
assets/images/ui/panel_codex.png
!!!

UI 按钮和面板默认不直接生成文字，文字由 Pygame 绘制。

## 5.5 icons/

用于存放通用图标。

例如：

!!!text
assets/images/icons/icon_coin.png
assets/images/icons/icon_shop.png
assets/images/icons/icon_inventory.png
assets/images/icons/icon_codex.png
assets/images/icons/icon_water.png
assets/images/icons/icon_fertilizer.png
!!!

图标全部采用纯绿色背景抠图版流程。

## 5.6 decorations/

用于后期装饰系统。

例如：

!!!text
assets/images/decorations/wooden_fence.png
assets/images/decorations/tiny_lamp.png
assets/images/decorations/flower_pot.png
!!!

第一阶段只建立目录，不需要实现装饰系统。

## 5.7 characters/

用于后期 AI 聊天宠物或 NPC。

例如：

!!!text
assets/images/characters/gulu_pet_idle.png
assets/images/characters/gulu_pet_happy.png
assets/images/characters/gulu_pet_sleepy.png
!!!

第一阶段不实现宠物系统，只预留目录。

## 5.8 effects/

用于后期特效动画帧。

例如：

!!!text
assets/images/effects/star_bubble_01.png
assets/images/effects/star_bubble_02.png
assets/images/effects/coin_popup.png
assets/images/effects/water_drop.png
!!!

特效帧是否使用绿底，需要根据特效类型决定。若是普通实心图形或图标式特效，可以使用绿底抠图；若是半透明粒子、烟雾、光效，则不建议使用绿底粗暴抠图，应单独设计透明 alpha 特效流程。

---

# 6. 文件命名规范

## 6.1 基本规则

所有文件名使用：

* 小写英文
* 下划线 `_`
* 不使用中文
* 不使用空格
* 不使用特殊符号
* 文件名表达清楚用途

推荐：

!!!text
starbubble_radish_stage_0_seed.png
plot_empty.png
button_shop_normal.png
icon_coin.png
!!!

不推荐：

!!!text
星泡萝卜.png
new image.png
素材1.png
button-final-final2.png
!!!

## 6.2 作物命名规则

作物素材命名格式：

!!!text
作物id_stage_阶段编号_阶段名.png
!!!

例如：

!!!text
starbubble_radish_stage_0_seed.png
starbubble_radish_stage_1_sprout.png
starbubble_radish_stage_2_growing.png
starbubble_radish_stage_3_mature.png
!!!

当前实际项目中也可以采用阶段短名：

!!!text
stage_0_seed.png
stage_1_sprout.png
stage_2_growing.png
stage_3_mature.png
!!!

前提是每种作物都放在自己的独立文件夹中。

## 6.3 UI 命名规则

UI 按钮命名格式：

!!!text
button_功能_状态.png
!!!

例如：

!!!text
button_shop_normal.png
button_shop_hover.png
button_shop_pressed.png
button_inventory_normal.png
button_codex_normal.png
!!!

## 6.4 图标命名规则

图标命名格式：

!!!text
icon_功能.png
!!!

例如：

!!!text
icon_coin.png
icon_shop.png
icon_inventory.png
icon_codex.png
icon_water.png
icon_fertilizer.png
!!!

## 6.5 音效命名规则

音效命名格式：

!!!text
sfx_动作名.wav
!!!

例如：

!!!text
sfx_click.wav
sfx_plant.wav
sfx_water.wav
sfx_harvest.wav
sfx_coin.wav
!!!

背景音乐命名格式：

!!!text
bgm_场景名.mp3
!!!

例如：

!!!text
bgm_main_farm.mp3
bgm_midnight_garden.mp3
!!!

---

# 7. 第一阶段最低素材清单

第一阶段目标是实现基础可玩闭环，因此素材需求不要太大。

## 7.1 必需图像素材

| 类型 | 文件名 | 说明 | 生成阶段背景 | 最终游戏文件 |
| --- | --- | --- | --- | --- |
| 背景 | farm_daytime.png | 主界面背景 | 不透明完整背景 | 不透明 PNG |
| 土地 | plot_empty.png | 空地 | 纯绿色背景 | 透明 PNG |
| 土地 | plot_locked.png | 锁定土地 | 纯绿色背景 | 透明 PNG |
| 土地 | plot_need_water.png | 需要浇水 | 纯绿色背景 | 透明 PNG |
| 土地 | plot_watered.png | 已浇水 | 纯绿色背景 | 透明 PNG |
| 作物 | stage_0_seed.png | 种子阶段 | 纯绿色背景 | 透明 PNG |
| 作物 | stage_1_sprout.png | 幼苗阶段 | 纯绿色背景 | 透明 PNG |
| 作物 | stage_2_growing.png | 生长期 | 纯绿色背景 | 透明 PNG |
| 作物 | stage_3_mature.png | 成熟阶段 | 纯绿色背景 | 透明 PNG |
| 图标 | icon_coin.png | 金币 | 纯绿色背景 | 透明 PNG |
| 图标 | icon_shop.png | 商店 | 纯绿色背景 | 透明 PNG |
| 图标 | icon_inventory.png | 背包 | 纯绿色背景 | 透明 PNG |
| 图标 | icon_codex.png | 图鉴 | 纯绿色背景 | 透明 PNG |
| 图标 | icon_water.png | 浇水 | 纯绿色背景 | 透明 PNG |

## 7.2 可先占位的素材

以下素材第一阶段可以用简单色块或临时图代替：

* 背包按钮
* 图鉴按钮
* 商店面板
* 任务栏面板
* 状态提示面板
* 背景音乐
* 点击音效
* 收获音效

## 7.3 暂时不需要的素材

第一阶段不需要：

* 多种作物素材
* 宠物素材
* 好友农场素材
* 装饰素材
* 完美品质素材
* 大量动画帧
* 天气素材
* 季节素材

---

# 8. 星泡萝卜素材设定

## 8.1 基础视觉描述

星泡萝卜是一种可爱的新手奇幻作物。

视觉特征：

* 主体像圆滚滚的小萝卜。
* 颜色以浅粉、淡紫、奶白为主。
* 叶子柔软，但不要使用接近 `#00FF00` 的高饱和绿色。
* 星星泡泡应优先设计成实心装饰形状，而不是发光粒子。
* 表情可选，但不要太复杂。
* 整体应当可爱、干净、适合新手作物定位。
* 抠图后边缘必须干净。

## 8.2 四个成长阶段

### stage_0_seed

种子阶段：

* 一个小小的奇幻种子。
* 可以带一点星星纹路。
* 颜色以奶白、淡粉、淡紫为主。
* 不使用外部发光或光晕。

### stage_1_sprout

幼苗阶段：

* 长出两片小叶子。
* 叶尖可以有扁平小星星纹样。
* 体积较小。
* 叶色使用柔和薄荷绿或灰绿，不能接近纯绿色背景。

### stage_2_growing

生长期：

* 萝卜主体开始露出。
* 叶子更大。
* 周围可以有少量实心星泡装饰。
* 不要生成土壤底座，不要生成土地格子。

### stage_3_mature

成熟阶段：

* 圆滚滚的星泡萝卜明显露出。
* 颜色更饱满。
* 周围有小星星泡泡装饰。
* 玩家一眼能看出“可以收获”。
* 不要使用发光光晕来表达成熟，应靠体积、颜色、星泡装饰表达。

## 8.3 星泡萝卜通用提示词模板

可用于生成完整作物概念图：

!!!text
A cute fantasy radish crop called Starbubble Radish, 512x512, solid pure chroma key green background, background color must be exactly RGB(0,255,0) / HEX #00FF00, not transparent, no checkerboard pattern, no fake transparency, high-resolution cute cartoon style, soft pastel colors, round chubby radish body, pastel pink, lavender, and creamy white colors, soft muted mint green leaves that must not match the pure green background, small solid star-bubble ornaments, centered object, the object must be centered both horizontally and vertically, clean outer silhouette, crisp cutout edge, no glow, no aura, no bloom, no light halo, no external shadow, cozy whimsical farming game asset, no text, no watermark, not pixel art, not realistic
!!!

中文理解：

> 一种叫星泡萝卜的可爱奇幻萝卜作物，512×512，纯绿色背景，背景必须是 #00FF00，不透明、不棋盘格、不假透明。主体是高清可爱卡通风，柔和粉紫奶白色，叶子使用低饱和薄荷绿，不能接近纯绿背景。周围可以有实心星泡装饰，但不要发光、不要光晕、不要外部阴影。主体居中，边缘干净，无文字无水印。

## 8.4 成长阶段提示词模板

!!!text
A cute fantasy farming game crop asset, Starbubble Radish, [growth stage], 512x512, solid pure chroma key green background, background color must be exactly RGB(0,255,0) / HEX #00FF00, not transparent, no checkerboard pattern, no fake transparency, high-resolution cute cartoon style, soft pastel colors, centered object, the object must be centered both horizontally and vertically, clean outer silhouette, crisp cutout edge, no glow, no aura, no bloom, no light halo, no external shadow, no text, no watermark, not pixel art, not realistic
!!!

将 `[growth stage]` 替换为：

!!!text
stage 0 seed, tiny magical seed with printed star pattern
stage 1 sprout, small sprout with two soft rounded leaves
stage 2 growing, chubby radish body partially visible, larger leaves, a few solid star-bubble ornaments
stage 3 mature, fully mature round chubby radish, clearly harvestable, several solid star-bubble ornaments
!!!

---

# 9. 背景素材设定

## 9.1 主背景方向

主背景应表现一个温暖、干净、可爱的小菜园。

视觉元素可以包括：

* 柔和草地
* 小木栅栏
* 远处小屋
* 云朵
* 蓝天
* 小花
* 圆润可爱的农田区域
* 轻微奇幻感

背景图不是抠图素材，因此不使用纯绿色背景。

第一阶段主背景建议用白日版本：

!!!text
farm_daytime.png
!!!

## 9.2 背景 AI 生成提示词

!!!text
A cozy cute fantasy vegetable garden background for a casual farming game, 2560x1440, 16:9 horizontal game background, high-resolution cartoon style, soft warm daylight, light top-down or front-facing 2D game perspective, very gentle perspective, large flat open central area reserved for placing a rectangular farm plot grid, clean and unobstructed middle ground, soft green grass, small wooden fences around the sides, tiny flowers near the edges, a charming cottage in the far background, blue sky and fluffy clouds, whimsical fantasy garden, clear composition for game UI overlay, no characters, no text, no watermark, not pixel art, not realistic, avoid dramatic perspective, avoid curved ground, avoid diagonal field direction
!!!

## 9.3 昼夜背景扩展

后续可以扩展：

!!!text
farm_morning.png
farm_daytime.png
farm_evening.png
farm_midnight.png
!!!

### 清晨 Morning

关键词：

!!!text
soft morning light, pale blue sky, gentle golden sunrise, fresh dew
!!!

### 白日 Daytime

关键词：

!!!text
bright warm daylight, clear blue sky, cozy green garden
!!!

### 傍晚 Evening

关键词：

!!!text
warm orange sunset, soft golden light, peaceful evening garden
!!!

### 午夜 Midnight

关键词：

!!!text
deep blue night, moonlight, tiny stars, magical garden atmosphere
!!!

注意：背景图可以有光照氛围，但不要让中央农田区域过亮、过暗或过复杂。

---

# 10. 土地素材设定

## 10.1 土地总风格

土地素材应符合：

* 圆角
* 柔和
* 可爱
* 轻微俯视或正交俯视
* 状态清晰
* 边缘干净
* 抠图后能自然叠加在背景上

土地素材使用纯绿色背景抠图版。

## 10.2 空土地 prompt 模板

!!!text
A single empty farm plot tile for a cute fantasy farming game, 512x512, solid pure chroma key green background, background color must be exactly RGB(0,255,0) / HEX #00FF00, not transparent, no checkerboard pattern, no fake transparency, high-resolution cute cartoon style, soft rounded square soil patch, warm brown soil, slightly raised soft clay edges, gentle painted highlights on the soil only, centered object, the object must be centered both horizontally and vertically, object should occupy about 82% to 90% of the canvas width and height, clean outer silhouette, crisp cutout edge, no glow, no aura, no bloom, no light halo, no external shadow, top-down or very light top-down 2D game asset, cozy casual farming game style, no text, no watermark, not pixel art, not realistic
!!!

## 10.3 锁定土地 prompt 模板

!!!text
A locked farm plot tile for a cute fantasy farming game, 512x512, solid pure chroma key green background, background color must be exactly RGB(0,255,0) / HEX #00FF00, not transparent, no checkerboard pattern, no fake transparency, high-resolution cute cartoon style, rounded square soil patch covered with soft gray-blue stones, subtle locked feeling, small cute wooden sign without text or tiny chain detail, centered object, the object must be centered both horizontally and vertically, object should occupy about 82% to 90% of the canvas width and height, clean outer silhouette, crisp cutout edge, no glow, no aura, no bloom, no light halo, no external shadow, cozy casual game asset, no text, no watermark, not pixel art, not realistic
!!!

---

# 11. UI 素材设定

## 11.1 UI 总风格

UI 应符合：

* 圆角
* 柔和阴影
* 可爱但清晰
* 按钮较大
* 信息层级明确
* 不使用过细字体
* 不使用过暗颜色
* 避免复杂纹理
* 不直接生成文字
* 抠图后边缘干净

## 11.2 UI 色彩方向

推荐色彩：

| 用途 | 色彩方向 |
| --- | --- |
| 主背景 | 柔和绿色、浅蓝色 |
| 按钮 | 奶油色、浅绿色、浅橙色 |
| 强调 | 金黄色、粉紫色 |
| 警告 | 柔和红色 |
| 锁定 | 灰蓝色 |
| 成熟提示 | 亮黄色或星星装饰色 |

注意：如果 UI 内部使用绿色装饰，不能接近 `#00FF00`。

## 11.3 UI 生成提示词模板

!!!text
A cute cartoon farming game UI button, [button purpose], 512x160, solid pure chroma key green background, background color must be exactly RGB(0,255,0) / HEX #00FF00, not transparent, no checkerboard pattern, no fake transparency, high-resolution cozy casual game UI asset, rounded rectangle button, soft cream color, subtle pastel orange and muted green accents, clean readable design, empty center area reserved for text, centered object, the button must be centered both horizontally and vertically, the button should occupy about 85% to 92% of the canvas width and about 70% to 78% of the canvas height, rounded corners must be fully visible, soft inner shadow and very subtle attached contact shadow only, no external glow, no aura, no bloom, no light halo, no text, no letters, no symbols, no watermark, not pixel art
!!!

将 `[button purpose]` 替换为：

!!!text
shop button normal state
shop button hover state
inventory button normal state
codex button normal state
!!!

注意：
按钮素材尽量不要直接生成文字，因为 AI 生成文字容易出错。文字应在 Pygame 中用字体绘制。

---

# 12. 图标素材设定

## 12.1 图标总规则

图标素材应符合：

* 单个主体
* 轮廓清楚
* 颜色明快但不过饱和
* 中心构图
* 无文字
* 无水印
* 无外部发光
* 无外部阴影
* 纯绿色背景抠图版

## 12.2 金币图标 prompt 模板

!!!text
A cute cartoon gold coin icon for a cozy farming game, 512x512, solid pure chroma key green background, background color must be exactly RGB(0,255,0) / HEX #00FF00, not transparent, no checkerboard pattern, no fake transparency, high-resolution game icon, round shiny golden coin, slightly chubby shape, soft painted highlights on the coin surface only, warm cheerful style, clean outline, centered object, the coin must be centered both horizontally and vertically, the coin should occupy about 70% to 80% of the canvas width and height, crisp cutout edge, no glow, no aura, no bloom, no light halo, no external shadow, no text, no numbers, no letters, no watermark, not pixel art, not realistic
!!!

---

# 13. 字体规范

## 13.1 字体需求

游戏需要支持：

* 中文
* 英文
* 数字
* 标点

因此字体选择必须支持中文显示。

## 13.2 字体原则

字体应：

* 清晰
* 圆润
* 不过度花哨
* 适合可爱游戏
* 支持中文

## 13.3 字体文件管理

字体可以放在：

!!!text
assets/fonts/
!!!

例如：

!!!text
assets/fonts/main_font.ttf
assets/fonts/title_font.ttf
!!!

注意：
字体文件通常有版权要求。使用前必须确认授权，不要随便把商业字体上传 GitHub。

---

# 14. 音频素材规范

## 14.1 音频目录

!!!text
assets/audio/
├─ bgm/
└─ sfx/
!!!

## 14.2 背景音乐方向

背景音乐应符合：

* 轻松
* 治愈
* 温暖
* 循环播放不烦
* 不抢注意力

推荐类型：

* 轻音乐
* 木琴
* 钢琴
* 轻快拨弦
* 温柔合成器

## 14.3 音效方向

音效应短、轻、可爱。

推荐音效：

| 动作 | 音效方向 |
| --- | --- |
| 点击 | 轻快 pop |
| 播种 | 柔和 drop |
| 浇水 | 小水滴 |
| 收获 | 亮晶晶 |
| 金币 | 清脆 coin |
| 任务完成 | 小铃铛 |

## 14.4 第一阶段音频策略

第一阶段可以先不加入真实音频。

建议只预留接口和目录。

等核心种菜闭环稳定后，再加入音效。

---

# 15. AI 生成素材工作流

## 15.1 推荐流程

每个素材建议按照以下流程制作：

1. 明确素材用途。
   例如：星泡萝卜成熟阶段。

2. 先更新 `docs/ai-prompts.md`。
   记录素材名、保存路径、尺寸、用途和英文提示词。

3. 写出纯绿色背景抠图版提示词。
   必须包含 `RGB(0,255,0)` 和 `HEX #00FF00`。

4. 生成多张候选图。
   不要只生成一张。

5. 选择最统一的一张。
   优先选择风格与已有素材一致、边缘清晰、主体居中的图。

6. 本地抠除纯绿色背景。
   将 `#00FF00` 背景转为 alpha 透明。

7. 检查边缘。
   确认没有绿色残边、半透明脏边、棋盘格残留。

8. 统一尺寸。
   例如统一裁成 512 × 512。

9. 按命名规范保存。
   例如 `stage_3_mature.png`。

10. 放入正确目录。

11. 在素材清单中记录。

## 15.2 生成作物时必须注意

作物素材最好满足：

* 正面或 3/4 视角统一。
* 光照方向统一。
* 画风统一。
* 大小比例统一。
* AI 生成阶段使用纯绿色背景。
* 最终游戏文件是透明 PNG。
* 不带文字。
* 不带水印。
* 边缘干净。
* 主体居中。
* 一眼能看出成长阶段差异。
* 不使用外部发光、光晕、泛光。
* 叶子等绿色元素不能接近 `#00FF00`。

## 15.3 生成 UI 时必须注意

UI 素材最好满足：

* 不要自带乱码文字。
* 按钮留出文字区域。
* 圆角统一。
* 阴影方向统一。
* 状态变化清晰。
* normal / hover / pressed 风格一致。
* AI 生成阶段使用纯绿色背景。
* 最终游戏文件是透明 PNG。
* 不使用外部发光或大范围阴影。

## 15.4 生成图标时必须注意

图标素材最好满足：

* 主体居中。
* 轮廓简单。
* 小尺寸下仍然能看懂。
* 不生成文字、数字、字母。
* 不生成背景装饰。
* 不使用外部光晕。
* 最终抠图后能直接放入 HUD 或按钮区域。

## 15.5 生成背景时必须注意

背景素材最好满足：

* 不使用纯绿色背景。
* 不要太复杂。
* 中央农田区域不要被复杂物体遮挡。
* 留出 UI 放置空间。
* 不要生成文字。
* 不要出现真实人物。
* 画面不要过暗。
* 远景元素不要抢作物视觉焦点。

## 15.6 后处理检查清单

每张绿底素材抠图后应检查：

| 检查项 | 标准 |
| --- | --- |
| 背景是否已透明 | 是 |
| 是否还有绿色残边 | 否 |
| 是否误删主体绿色部分 | 否 |
| 是否出现棋盘格 | 否 |
| 是否有文字或水印 | 否 |
| 是否有外部光晕残留 | 否 |
| 主体是否居中 | 是 |
| 尺寸是否正确 | 是 |
| 文件名是否规范 | 是 |
| 路径是否正确 | 是 |

---

# 16. 素材清单记录表

建议在 `docs/asset-list.md` 或本文件后续版本中记录素材状态。

| 素材名 | 路径 | 类型 | 生成背景 | 最终状态 | 备注 |
| --- | --- | --- | --- | --- | --- |
| 白日菜园背景 | assets/images/backgrounds/farm_daytime.png | 背景 | 不透明完整背景 | 待生成 | 第一阶段需要 |
| 空地 | assets/images/tiles/plot_empty.png | 土地 | 纯绿色背景 | 待抠图 / 待生成 | 第一阶段需要 |
| 锁定土地 | assets/images/tiles/plot_locked.png | 土地 | 纯绿色背景 | 待抠图 / 待生成 | 第一阶段需要 |
| 需要浇水土地 | assets/images/tiles/plot_need_water.png | 土地 | 纯绿色背景 | 待抠图 / 待生成 | 第一阶段需要 |
| 已浇水土地 | assets/images/tiles/plot_watered.png | 土地 | 纯绿色背景 | 待抠图 / 待生成 | 第一阶段需要 |
| 星泡萝卜种子阶段 | assets/images/crops/starbubble_radish/stage_0_seed.png | 作物 | 纯绿色背景 | 待抠图 / 待生成 | 第一阶段需要 |
| 星泡萝卜幼苗阶段 | assets/images/crops/starbubble_radish/stage_1_sprout.png | 作物 | 纯绿色背景 | 待抠图 / 待生成 | 第一阶段需要 |
| 星泡萝卜生长期 | assets/images/crops/starbubble_radish/stage_2_growing.png | 作物 | 纯绿色背景 | 待抠图 / 待生成 | 第一阶段需要 |
| 星泡萝卜成熟阶段 | assets/images/crops/starbubble_radish/stage_3_mature.png | 作物 | 纯绿色背景 | 待抠图 / 待生成 | 第一阶段需要 |
| 金币图标 | assets/images/icons/icon_coin.png | 图标 | 纯绿色背景 | 待抠图 / 待生成 | 第一阶段需要 |
| 商店图标 | assets/images/icons/icon_shop.png | 图标 | 纯绿色背景 | 待抠图 / 待生成 | 第一阶段需要 |
| 背包图标 | assets/images/icons/icon_inventory.png | 图标 | 纯绿色背景 | 待抠图 / 待生成 | 第一阶段需要 |

---

# 17. GitHub 素材提交规则

## 17.1 可以提交

可以提交：

* 自己生成且允许使用的正式素材。
* 自己绘制的正式素材。
* 免费授权素材。
* 占位素材。
* 素材说明文档。
* AI 生成提示词记录。
* 抠图后的透明 PNG 正式图。

## 17.2 不建议提交

不建议提交：

* 版权不明确的素材。
* 商业字体。
* 大量未使用素材。
* 重复生成的废稿。
* 体积过大的原始文件。
* 临时 PSD 或工程源文件。
* 大量 AI 生成绿底原图。
* 批处理过程中的临时备份文件。

## 17.3 推荐保留

推荐保留：

!!!text
docs/asset-guide.md
docs/asset-list.md
docs/ai-prompts.md
!!!

其中：

* `asset-guide.md` 记录素材规范。
* `asset-list.md` 记录素材状态。
* `ai-prompts.md` 记录重要素材的生成提示词。

---

# 18. 第一阶段素材完成标准

第一阶段不要求素材全部完美。

只要满足以下标准即可：

1. 主背景可用。
2. 土地状态能看清。
3. 星泡萝卜四个成长阶段能区分。
4. 金币、商店、背包等图标能看懂。
5. 所有素材路径规范。
6. 素材尺寸基本统一。
7. 替换素材时不需要大改代码。
8. 抠图后没有明显绿色残边。
9. 素材主体没有被误删。
10. Pygame 中加载后边缘干净。

第一阶段的目标是：

> 画面足够清楚，风格初步统一，能支撑核心玩法测试。

不是：

> 一开始就做成完整商业游戏美术品质。

---

# 19. 后续扩展素材规划

未来可以逐步加入：

## 19.1 更多作物

例如：

!!!text
moondew_mushroom/
cloud_sugar_pumpkin/
gulu_bean/
nightglow_lily/
!!!

每种作物都应有：

* 种子阶段
* 幼苗阶段
* 生长期
* 成熟阶段
* 种子图标
* 作物图标
* 完美品质图标

这些素材默认采用纯绿色背景抠图版流程。

## 19.2 装饰系统

可以加入：

* 小木栅栏
* 小路
* 花盆
* 路灯
* 风车
* 小水池
* 魔法蘑菇灯

装饰素材默认采用纯绿色背景抠图版流程。

## 19.3 宠物系统

可以加入：

* 待机表情
* 开心表情
* 困倦表情
* 惊讶表情
* 提醒表情

宠物素材默认采用纯绿色背景抠图版流程。由于宠物可能需要较柔和边缘，抠图后要重点检查毛边。

## 19.4 昼夜系统

可以加入：

* 清晨背景
* 白日背景
* 傍晚背景
* 午夜背景
* 光照遮罩
* 星星装饰

昼夜背景不使用纯绿色背景。光照遮罩和半透明特效不建议使用简单绿底抠图流程，应单独处理 alpha。

---

# 20. 当前结论

《咕噜小菜园》的素材路线确定为：

> 高清可爱卡通风，以 AI 生成素材为主。除完整背景图外，作物、土地、UI、图标、装饰、角色等需要叠加到游戏画面上的素材，统一采用纯绿色背景抠图版流程。

第一阶段不追求大量素材，而是先完成：

1. 一张主背景图。
2. 几张土地状态图。
3. 星泡萝卜四阶段图。
4. 几个基础 UI 图标。

后续生成或接入任何新素材前，应先更新 `docs/ai-prompts.md` 中对应素材的 AI 提示词，再进行生成、抠图、接入代码和提交。

最终接入游戏的图片仍应是透明 PNG。纯绿色背景只是 AI 生成与后期处理的中间流程，不是游戏内最终显示效果。
