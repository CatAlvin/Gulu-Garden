# docs/asset-guide.md

# 《咕噜小菜园》Gulu Garden 素材规范文档 v0.1

## 1. 文档目的

本文档用于规范《咕噜小菜园》（Gulu Garden）的美术素材、音频素材、文件命名、目录结构和 AI 生成素材流程。

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

英文关键词可用于 AI 生成素材：

```text
high-resolution, cute cartoon style, cozy farming game, soft colors, whimsical fantasy garden, clean game UI, warm lighting, adorable vegetables, casual mobile game style
```

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

---

# 3. 初始分辨率与适配原则

## 3.1 初始窗口大小

第一阶段窗口大小固定为：

```text
1280 × 720
```

这是 16:9 横屏比例，适合桌面 Pygame 项目，也方便录屏展示。

## 3.2 后续扩展目标

未来可能扩展到：

```text
2560 × 1440
```

或全屏模式。

但第一阶段不处理复杂适配，只保证 1280 × 720 下界面清晰。

## 3.3 素材分辨率原则

由于后续可能适配更高分辨率，建议 AI 生成素材时不要太小。

推荐原则：

| 素材类型    |                  推荐生成尺寸 |
| ------- | ----------------------: |
| 背景图     |             2560 × 1440 |
| 单个作物图标  |               512 × 512 |
| 作物成长阶段图 |               512 × 512 |
| UI 图标   |   256 × 256 或 512 × 512 |
| 土地格子    |               512 × 512 |
| 装饰物     | 512 × 512 或 1024 × 1024 |
| 宠物角色    |             1024 × 1024 |
| 商店物品图标  |               512 × 512 |

在游戏中可以缩放显示，但原始素材应尽量高清，方便后期适配。

---

# 4. 素材目录结构

推荐素材目录如下：

```text
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
```

## 4.1 backgrounds/

用于存放背景图。

例如：

```text
assets/images/backgrounds/farm_morning.png
assets/images/backgrounds/farm_daytime.png
assets/images/backgrounds/farm_evening.png
assets/images/backgrounds/farm_midnight.png
```

第一阶段可以只使用一张背景图：

```text
assets/images/backgrounds/farm_daytime.png
```

后续昼夜系统完善后，再加入其他时间段背景。

## 4.2 crops/

用于存放作物素材。

每种作物单独一个文件夹。

例如：

```text
assets/images/crops/starbubble_radish/
├─ stage_0_seed.png
├─ stage_1_sprout.png
├─ stage_2_growing.png
├─ stage_3_mature.png
├─ icon_seed.png
├─ icon_crop.png
└─ perfect.png
```

## 4.3 tiles/

用于存放土地、地块、网格等素材。

例如：

```text
assets/images/tiles/plot_empty.png
assets/images/tiles/plot_locked.png
assets/images/tiles/plot_watered.png
assets/images/tiles/plot_need_water.png
assets/images/tiles/plot_mature_highlight.png
```

## 4.4 ui/

用于存放 UI 面板、按钮、边框等素材。

例如：

```text
assets/images/ui/button_normal.png
assets/images/ui/button_hover.png
assets/images/ui/button_pressed.png
assets/images/ui/panel_main.png
assets/images/ui/panel_shop.png
assets/images/ui/panel_inventory.png
assets/images/ui/panel_codex.png
```

## 4.5 icons/

用于存放通用图标。

例如：

```text
assets/images/icons/coin.png
assets/images/icons/shop.png
assets/images/icons/bag.png
assets/images/icons/codex.png
assets/images/icons/task.png
assets/images/icons/water.png
assets/images/icons/fertilizer.png
```

## 4.6 decorations/

用于后期装饰系统。

例如：

```text
assets/images/decorations/wooden_fence.png
assets/images/decorations/tiny_lamp.png
assets/images/decorations/flower_pot.png
```

第一阶段只建立目录，不需要实现装饰系统。

## 4.7 characters/

用于后期 AI 聊天宠物或 NPC。

例如：

```text
assets/images/characters/gulu_pet_idle.png
assets/images/characters/gulu_pet_happy.png
assets/images/characters/gulu_pet_sleepy.png
```

第一阶段不实现宠物系统，只预留目录。

## 4.8 effects/

用于后期特效动画帧。

例如：

```text
assets/images/effects/star_bubble_01.png
assets/images/effects/star_bubble_02.png
assets/images/effects/coin_popup.png
assets/images/effects/water_drop.png
```

---

# 5. 文件命名规范

## 5.1 基本规则

所有文件名使用：

* 小写英文
* 下划线 `_`
* 不使用中文
* 不使用空格
* 不使用特殊符号
* 文件名表达清楚用途

推荐：

```text
starbubble_radish_stage_0_seed.png
plot_empty.png
button_shop_normal.png
coin_icon.png
```

不推荐：

```text
星泡萝卜.png
new image.png
素材1.png
button-final-final2.png
```

## 5.2 作物命名规则

作物素材命名格式：

```text
作物id_stage_阶段编号_阶段名.png
```

例如：

```text
starbubble_radish_stage_0_seed.png
starbubble_radish_stage_1_sprout.png
starbubble_radish_stage_2_growing.png
starbubble_radish_stage_3_mature.png
```

## 5.3 UI 命名规则

UI 按钮命名格式：

```text
button_功能_状态.png
```

例如：

```text
button_shop_normal.png
button_shop_hover.png
button_shop_pressed.png
button_inventory_normal.png
button_codex_normal.png
```

## 5.4 图标命名规则

图标命名格式：

```text
icon_功能.png
```

例如：

```text
icon_coin.png
icon_shop.png
icon_inventory.png
icon_codex.png
icon_water.png
icon_fertilizer.png
```

## 5.5 音效命名规则

音效命名格式：

```text
sfx_动作名.wav
```

例如：

```text
sfx_click.wav
sfx_plant.wav
sfx_water.wav
sfx_harvest.wav
sfx_coin.wav
```

背景音乐命名格式：

```text
bgm_场景名.mp3
```

例如：

```text
bgm_main_farm.mp3
bgm_midnight_garden.mp3
```

---

# 6. 第一阶段最低素材清单

第一阶段目标是实现基础可玩闭环，因此素材需求不要太大。

## 6.1 必需图像素材

| 类型 | 文件名                                   | 说明    |
| -- | ------------------------------------- | ----- |
| 背景 | farm_daytime.png                      | 主界面背景 |
| 土地 | plot_empty.png                        | 空地    |
| 土地 | plot_locked.png                       | 锁定土地  |
| 土地 | plot_need_water.png                   | 需要浇水  |
| 土地 | plot_watered.png                      | 已浇水   |
| 作物 | starbubble_radish_stage_0_seed.png    | 种子阶段  |
| 作物 | starbubble_radish_stage_1_sprout.png  | 幼苗阶段  |
| 作物 | starbubble_radish_stage_2_growing.png | 生长期   |
| 作物 | starbubble_radish_stage_3_mature.png  | 成熟阶段  |
| 图标 | icon_coin.png                         | 金币    |
| 图标 | icon_shop.png                         | 商店    |
| 图标 | icon_inventory.png                    | 背包    |
| 图标 | icon_codex.png                        | 图鉴    |
| 图标 | icon_water.png                        | 浇水    |

## 6.2 可先占位的素材

以下素材第一阶段可以用简单色块或临时图代替：

* 背包按钮
* 图鉴按钮
* 商店面板
* 任务栏面板
* 状态提示面板
* 背景音乐
* 点击音效
* 收获音效

## 6.3 暂时不需要的素材

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

# 7. 星泡萝卜素材设定

## 7.1 基础视觉描述

星泡萝卜是一种可爱的新手奇幻作物。

视觉特征：

* 主体像圆滚滚的小萝卜
* 颜色以浅粉、淡紫、奶白为主
* 叶子柔软，略带星光
* 成熟后周围有小小星星泡泡
* 表情可选，但不要太复杂
* 整体应当可爱、干净、适合新手作物定位

## 7.2 四个成长阶段

### stage_0_seed

种子阶段：

* 一个小小的发光种子
* 可以带一点星星纹路
* 看起来像刚埋进土里的奇幻种子

### stage_1_sprout

幼苗阶段：

* 长出两片小叶子
* 叶尖有微弱星光
* 体积较小

### stage_2_growing

生长期：

* 萝卜主体开始露出地面
* 叶子更大
* 周围有少量淡淡泡泡

### stage_3_mature

成熟阶段：

* 圆滚滚的星泡萝卜明显露出
* 颜色更亮
* 周围有星星泡泡
* 玩家一眼能看出“可以收获”

## 7.3 星泡萝卜 AI 生成提示词

可用于生成完整作物概念图：

```text
A cute fantasy radish crop called Starbubble Radish, high-resolution cartoon style, soft pastel colors, round chubby radish body, tiny glowing star bubbles floating around it, adorable farming game asset, clean transparent background, cozy whimsical garden style, game icon, no text
```

中文理解：

> 一种叫星泡萝卜的可爱奇幻萝卜作物，高清卡通风，柔和粉紫色，圆滚滚，周围漂浮小星星泡泡，适合休闲农场游戏素材，透明背景，无文字。

## 7.4 成长阶段提示词模板

```text
A cute fantasy farming game crop asset, Starbubble Radish, [growth stage], high-resolution cartoon style, soft pastel colors, transparent background, clean outline, cozy casual game style, no text
```

将 `[growth stage]` 替换为：

```text
tiny glowing seed stage
small sprout stage with two leaves
growing radish partially above soil
fully mature chubby radish with star bubbles
```

---

# 8. 背景素材设定

## 8.1 主背景方向

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

第一阶段主背景建议用白日版本：

```text
farm_daytime.png
```

## 8.2 背景 AI 生成提示词

```text
A cozy cute fantasy vegetable garden background for a casual farming game, high-resolution cartoon style, soft warm daylight, small wooden fence, green grass, tiny flowers, charming little farm, clean composition, 16:9 horizontal game background, no characters, no text
```

## 8.3 昼夜背景扩展

后续可以扩展：

```text
farm_morning.png
farm_daytime.png
farm_evening.png
farm_midnight.png
```

### 清晨 Morning

关键词：

```text
soft morning light, pale blue sky, gentle golden sunrise, fresh dew
```

### 白日 Daytime

关键词：

```text
bright warm daylight, clear blue sky, cozy green garden
```

### 傍晚 Evening

关键词：

```text
warm orange sunset, soft golden light, peaceful evening garden
```

### 午夜 Midnight

关键词：

```text
deep blue night, moonlight, tiny stars, magical glowing plants
```

---

# 9. UI 素材设定

## 9.1 UI 总风格

UI 应符合：

* 圆角
* 柔和阴影
* 可爱但清晰
* 按钮较大
* 信息层级明确
* 不使用过细字体
* 不使用过暗颜色
* 避免复杂纹理

## 9.2 UI 色彩方向

推荐色彩：

| 用途   | 色彩方向        |
| ---- | ----------- |
| 主背景  | 柔和绿色、浅蓝色    |
| 按钮   | 奶油色、浅绿色、浅橙色 |
| 强调   | 金黄色、粉紫色     |
| 警告   | 柔和红色        |
| 锁定   | 灰蓝色         |
| 成熟提示 | 亮黄色或星光色     |

## 9.3 UI 生成提示词

```text
Cute cartoon farming game UI button set, rounded corners, soft pastel colors, clean readable design, high-resolution, cozy casual game style, transparent background, no text
```

注意：
按钮素材尽量不要直接生成文字，因为 AI 生成文字容易出错。文字应在 Pygame 中用字体绘制。

---

# 10. 字体规范

## 10.1 字体需求

游戏需要支持：

* 中文
* 英文
* 数字
* 标点

因此字体选择必须支持中文显示。

## 10.2 字体原则

字体应：

* 清晰
* 圆润
* 不过度花哨
* 适合可爱游戏
* 支持中文

## 10.3 字体文件管理

字体可以放在：

```text
assets/fonts/
```

例如：

```text
assets/fonts/main_font.ttf
assets/fonts/title_font.ttf
```

注意：
字体文件通常有版权要求。使用前必须确认授权，不要随便把商业字体上传 GitHub。

---

# 11. 音频素材规范

## 11.1 音频目录

```text
assets/audio/
├─ bgm/
└─ sfx/
```

## 11.2 背景音乐方向

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

## 11.3 音效方向

音效应短、轻、可爱。

推荐音效：

| 动作   | 音效方向    |
| ---- | ------- |
| 点击   | 轻快 pop  |
| 播种   | 柔和 drop |
| 浇水   | 小水滴     |
| 收获   | 亮晶晶     |
| 金币   | 清脆 coin |
| 任务完成 | 小铃铛     |

## 11.4 第一阶段音频策略

第一阶段可以先不加入真实音频。

建议只预留接口和目录。

等核心种菜闭环稳定后，再加入音效。

---

# 12. AI 生成素材工作流

## 12.1 推荐流程

每个素材建议按照以下流程制作：

1. 明确素材用途
   例如：星泡萝卜成熟阶段。

2. 写出提示词
   包含风格、对象、背景要求、是否透明背景。

3. 生成多张候选图
   不要只生成一张。

4. 选择最统一的一张
   优先选择风格与已有素材一致的图。

5. 去背景或生成透明背景
   作物、图标、UI 元素最好是透明背景。

6. 统一尺寸
   例如统一裁成 512 × 512。

7. 按命名规范保存
   例如 `starbubble_radish_stage_3_mature.png`。

8. 放入正确目录。

9. 在素材清单中记录。

## 12.2 生成作物时必须注意

作物素材最好满足：

* 正面或 3/4 视角统一
* 光照方向统一
* 画风统一
* 大小比例统一
* 背景透明
* 不带文字
* 不带水印
* 边缘干净
* 一眼能看出成长阶段差异

## 12.3 生成 UI 时必须注意

UI 素材最好满足：

* 不要自带乱码文字
* 按钮留出文字区域
* 圆角统一
* 阴影方向统一
* 状态变化清晰
* normal / hover / pressed 风格一致

## 12.4 生成背景时必须注意

背景素材最好满足：

* 不要太复杂
* 中央农田区域不要被复杂物体遮挡
* 留出 UI 放置空间
* 不要生成文字
* 不要出现真实人物
* 画面不要过暗
* 远景元素不要抢作物视觉焦点

---

# 13. 素材清单记录表

建议在 `docs/asset-list.md` 或本文件后续版本中记录素材状态。

| 素材名      | 路径                                                        | 类型 | 状态  | 备注     |
| -------- | --------------------------------------------------------- | -- | --- | ------ |
| 白日菜园背景   | assets/images/backgrounds/farm_daytime.png                | 背景 | 待生成 | 第一阶段需要 |
| 空地       | assets/images/tiles/plot_empty.png                        | 土地 | 待生成 | 第一阶段需要 |
| 锁定土地     | assets/images/tiles/plot_locked.png                       | 土地 | 待生成 | 第一阶段需要 |
| 星泡萝卜种子阶段 | assets/images/crops/starbubble_radish/stage_0_seed.png    | 作物 | 待生成 | 第一阶段需要 |
| 星泡萝卜幼苗阶段 | assets/images/crops/starbubble_radish/stage_1_sprout.png  | 作物 | 待生成 | 第一阶段需要 |
| 星泡萝卜生长期  | assets/images/crops/starbubble_radish/stage_2_growing.png | 作物 | 待生成 | 第一阶段需要 |
| 星泡萝卜成熟阶段 | assets/images/crops/starbubble_radish/stage_3_mature.png  | 作物 | 待生成 | 第一阶段需要 |
| 金币图标     | assets/images/icons/icon_coin.png                         | 图标 | 待生成 | 第一阶段需要 |
| 商店图标     | assets/images/icons/icon_shop.png                         | 图标 | 待生成 | 第一阶段需要 |
| 背包图标     | assets/images/icons/icon_inventory.png                    | 图标 | 待生成 | 第一阶段需要 |

---

# 14. GitHub 素材提交规则

## 14.1 可以提交

可以提交：

* 自己生成且允许使用的素材
* 自己绘制的素材
* 免费授权素材
* 占位素材
* 素材说明文档
* AI 生成提示词记录

## 14.2 不建议提交

不建议提交：

* 版权不明确的素材
* 商业字体
* 大量未使用素材
* 重复生成的废稿
* 体积过大的原始文件
* 临时 PSD 或工程源文件

## 14.3 推荐保留

推荐保留：

```text
docs/asset-guide.md
docs/asset-list.md
docs/ai-prompts.md
```

其中：

* `asset-guide.md` 记录素材规范
* `asset-list.md` 记录素材状态
* `ai-prompts.md` 记录重要素材的生成提示词

---

# 15. 第一阶段素材完成标准

第一阶段不要求素材全部完美。

只要满足以下标准即可：

1. 主背景可用。
2. 土地状态能看清。
3. 星泡萝卜四个成长阶段能区分。
4. 金币、商店、背包等图标能看懂。
5. 所有素材路径规范。
6. 素材尺寸基本统一。
7. 替换素材时不需要大改代码。

第一阶段的目标是：

> 画面足够清楚，风格初步统一，能支撑核心玩法测试。

不是：

> 一开始就做成完整商业游戏美术品质。

---

# 16. 后续扩展素材规划

未来可以逐步加入：

## 16.1 更多作物

例如：

```text
moondew_mushroom/
cloud_sugar_pumpkin/
gulu_bean/
nightglow_lily/
```

每种作物都应有：

* 种子阶段
* 幼苗阶段
* 生长期
* 成熟阶段
* 种子图标
* 作物图标
* 完美品质图标

## 16.2 装饰系统

可以加入：

* 小木栅栏
* 小路
* 花盆
* 路灯
* 风车
* 小水池
* 魔法蘑菇灯

## 16.3 宠物系统

可以加入：

* 待机表情
* 开心表情
* 困倦表情
* 惊讶表情
* 提醒表情

## 16.4 昼夜系统

可以加入：

* 清晨背景
* 白日背景
* 傍晚背景
* 午夜背景
* 光照遮罩
* 星光粒子

---

# 17. 当前结论

《咕噜小菜园》的素材路线确定为：

> 高清可爱卡通风，以 AI 生成素材为主，第一阶段只准备最小必要素材，优先保证风格统一、状态清晰、路径规范和后续可替换。

第一阶段不追求大量素材，而是先完成：

1. 一张主背景图。
2. 几张土地状态图。
3. 星泡萝卜四阶段图。
4. 几个基础 UI 图标。

等核心玩法稳定后，再逐步加入动画、音效、装饰、宠物和更多奇幻作物。
