# Gulu Garden AI Prompts

本文档记录《咕噜小菜园》（Gulu Garden）当前使用或计划使用的 AI 生成素材提示词。

统一风格要求：

```text
high-resolution, cute cartoon style, cozy farming game, soft pastel colors, whimsical fantasy garden, clean game UI, warm lighting, adorable vegetables, casual farming game style, no text, no watermark
```

---

## 1. 主背景：farm_daytime.png

保存路径：

```text
assets/images/backgrounds/farm_daytime.png
```

图片要求：

- 尺寸：2560 × 1440
- 比例：16:9 横屏
- 背景：不透明
- 用途：游戏主界面白日背景
- 注意：中央区域要干净，方便放置农田
- 不要生成文字
- 不要出现人物
- 不要出现复杂建筑遮挡中间农田区域

英文提示词：

```text
A cozy cute fantasy vegetable garden background for a casual farming game, 2560x1440, 16:9 horizontal game background, high-resolution cartoon style, soft warm daylight, light top-down or front-facing 2D game perspective, very gentle perspective, large flat open central area reserved for placing a rectangular farm plot grid, clean and unobstructed middle ground, soft green grass, small wooden fences around the sides, tiny flowers near the edges, a charming cottage in the far background, blue sky and fluffy clouds, whimsical fantasy garden, clear composition for game UI overlay, no characters, no text, no watermark, not pixel art, not realistic, avoid dramatic perspective, avoid curved ground, avoid diagonal field direction
```

中文理解：

```text
一张高清可爱卡通风的小菜园白日背景图，16:9 横屏，柔和阳光、草地、小木栅栏、小花、远处小屋和云朵。中间区域要干净，方便放农田。不要人物、不要文字、不要水印，不要像素风。
```

---

## 2. 空土地：plot_empty.png

保存路径：

```text
assets/images/tiles/plot_empty.png
```

图片要求：

- 尺寸：512 × 512
- 背景：透明
- 用途：可播种空土地
- 视角：轻微俯视或正交俯视
- 风格：圆角、柔和、可爱
- 不能带文字

英文提示词：

```text
A single empty farm plot tile for a cute fantasy farming game, 512x512, transparent background, high-resolution cartoon style, soft rounded square soil patch, warm brown soil, slightly raised soft edges, gentle highlights, cozy casual game asset, clean outline, centered object, no text, no watermark, not pixel art, not realistic
```

---

## 3. 锁定土地：plot_locked.png

保存路径：

```text
assets/images/tiles/plot_locked.png
```

图片要求：

- 尺寸：512 × 512
- 背景：透明
- 用途：locked 土地
- 视觉：灰蓝色、稍暗、不能播种的感觉
- 可包含轻微锁链或小木牌，但不要文字

英文提示词：

```text
A locked farm plot tile for a cute fantasy farming game, 512x512, transparent background, high-resolution cartoon style, rounded square soil patch covered with soft gray-blue stones, subtle locked feeling, small cute wooden sign without text or tiny chain detail, clean outline, centered object, cozy casual game asset, no text, no watermark, not pixel art, not realistic
```

---

## 4. 星泡萝卜种子阶段：stage_0_seed.png

保存路径：

```text
assets/images/crops/starbubble_radish/stage_0_seed.png
```

图片要求：

- 尺寸：512 × 512
- 背景：透明
- 用途：作物 stage 0
- 形象：小小发光种子
- 颜色：奶白、淡粉、淡紫
- 不带文字

英文提示词：

```text
A cute fantasy crop growth stage asset, Starbubble Radish seed stage, 512x512, transparent background, high-resolution cute cartoon style, tiny glowing seed with soft pastel pink and lavender tones, small star pattern, gentle magical glow, centered object, clean outline, cozy farming game asset, no soil base, no text, no watermark, not pixel art, not realistic
```

---

## 5. 星泡萝卜幼苗阶段：stage_1_sprout.png

保存路径：

```text
assets/images/crops/starbubble_radish/stage_1_sprout.png
```

图片要求：

- 尺寸：512 × 512
- 背景：透明
- 用途：作物 stage 1
- 形象：两片小叶子，叶尖有微弱星光
- 不带文字

英文提示词：

```text
A cute fantasy crop growth stage asset, Starbubble Radish sprout stage, 512x512, transparent background, high-resolution cute cartoon style, small sprout with two soft green leaves, tiny glowing star sparkle on leaf tips, pastel pink-lavender seed base barely visible, centered object, clean outline, cozy whimsical farming game asset, no text, no watermark, not pixel art, not realistic
```

---

## 6. 星泡萝卜生长期：stage_2_growing.png

保存路径：

```text
assets/images/crops/starbubble_radish/stage_2_growing.png
```

图片要求：

- 尺寸：512 × 512
- 背景：透明
- 用途：作物 stage 2
- 形象：萝卜主体部分露出，叶子更大，有少量泡泡
- 不带文字

英文提示词：

```text
A cute fantasy crop growth stage asset, Starbubble Radish growing stage, 512x512, transparent background, high-resolution cute cartoon style, chubby radish body partially emerging from the ground shape but without a soil tile, pastel pink and creamy white radish, larger soft green leaves, a few tiny glowing star bubbles floating around, centered object, clean outline, cozy whimsical farming game asset, no text, no watermark, not pixel art, not realistic
```

---

## 7. 星泡萝卜成熟阶段：stage_3_mature.png

保存路径：

```text
assets/images/crops/starbubble_radish/stage_3_mature.png
```

图片要求：

- 尺寸：512 × 512
- 背景：透明
- 用途：作物 stage 3
- 形象：圆滚滚成熟萝卜，明显可收获
- 成熟时有星星泡泡
- 不带文字

英文提示词：

```text
A cute fantasy crop growth stage asset, fully mature Starbubble Radish, 512x512, transparent background, high-resolution cute cartoon style, round chubby radish body, pastel pink lavender and creamy white colors, soft green leaves, tiny glowing star bubbles floating around it, clearly harvestable, adorable cozy farming game asset, centered object, clean outline, no text, no watermark, not pixel art, not realistic
```

---

## 8. 商店按钮底图：button_shop_normal.png

保存路径：

```text
assets/images/ui/button_shop_normal.png
```

图片要求：

- 尺寸：512 × 160
- 背景：透明
- 用途：商店按钮普通状态
- 不要自带文字，文字由 Pygame 绘制
- 圆角、奶油色、柔和阴影

英文提示词：

```text
A cute cartoon farming game UI button, normal state, 512x160, transparent background, rounded rectangle, soft cream color, gentle warm shadow, subtle green and orange accents, clean readable design, high-resolution cozy casual game UI asset, empty center area for text, no text, no watermark, not pixel art
```

---

## 9. 商店按钮悬停底图：button_shop_hover.png

保存路径：

```text
assets/images/ui/button_shop_hover.png
```

图片要求：

- 尺寸：512 × 160
- 背景：透明
- 用途：商店按钮 hover 状态
- 比 normal 更亮一点
- 不带文字

英文提示词：

```text
A cute cartoon farming game UI button, hover state, 512x160, transparent background, rounded rectangle, slightly brighter warm cream color than normal state, gentle glow, soft shadow, subtle green and orange accents, clean readable design, high-resolution cozy casual game UI asset, empty center area for text, no text, no watermark, not pixel art
```

---

## 10. 金币图标：icon_coin.png

保存路径：

```text
assets/images/icons/icon_coin.png
```

图片要求：

- 尺寸：512 × 512
- 背景：透明
- 用途：HUD 金币图标
- 形象：圆润金币，可爱游戏图标
- 不带文字

英文提示词：

```text
A cute cartoon gold coin icon for a cozy farming game, 512x512, transparent background, high-resolution, round shiny golden coin, soft highlights, slightly chubby shape, warm cheerful style, clean outline, centered object, no text, no watermark, not pixel art, not realistic
```
