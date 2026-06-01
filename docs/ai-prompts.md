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
A single empty farm plot tile for a cute fantasy farming game, 512x512, true  true transparent background, PNG with alpha channel, PNG with alpha channel, high-resolution cute cartoon style, soft rounded square soil patch, warm brown soil, slightly raised soft clay edges, gentle highlights, clean soft outline, centered object, enough empty transparent padding around the object, top-down or very light top-down 2D game asset, cozy casual farming game style, no text, no watermark, not pixel art, not realistic, no checkerboard background, do not draw a transparency grid, background must be fully transparent
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
A locked farm plot tile for a cute fantasy farming game, 512x512, true  true transparent background, PNG with alpha channel, PNG with alpha channel, high-resolution cartoon style, rounded square soil patch covered with soft gray-blue stones, subtle locked feeling, small cute wooden sign without text or tiny chain detail, clean outline, centered object, cozy casual game asset, no text, no watermark, not pixel art, not realistic
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
A cute fantasy crop growth stage asset, Starbubble Radish seed stage, stage 0, 512x512, solid pure chroma key green background, background color must be exactly RGB(0,255,0) / HEX #00FF00, not transparent, no checkerboard pattern, no fake transparency, high-resolution cute cartoon style, tiny magical seed, soft pastel pink, lavender, creamy white colors, small star patterns printed on the seed body, glossy but not glowing, centered object, the object must be centered both horizontally and vertically, object should occupy about 30% to 40% of the canvas height, clean outer silhouette, crisp cutout edge, no glow, no aura, no bloom, no light halo, no floating sparkles, no shadow outside the object, no soil base, no ground, no platform, cozy farming game asset, no text, no watermark, not pixel art, not realistic
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
A cute fantasy crop growth stage asset, Starbubble Radish sprout stage, stage 1, 512x512, solid pure chroma key green background, background color must be exactly RGB(0,255,0) / HEX #00FF00, not transparent, no checkerboard pattern, no fake transparency, high-resolution cute cartoon style, small sprout with two soft rounded leaves, leaf color should be soft muted mint green and must not match the pure green background, tiny flat star-shaped marks on the leaf tips, pastel pink-lavender seed base barely visible, centered object, the object must be centered both horizontally and vertically, object should occupy about 40% to 50% of the canvas height, clean outer silhouette, crisp cutout edge, no glow, no aura, no bloom, no light halo, no floating sparkles, no shadow outside the object, no soil base, no ground, no platform, cozy whimsical farming game asset, no text, no watermark, not pixel art, not realistic
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
A cute fantasy crop growth stage asset, Starbubble Radish growing stage, stage 2, 512x512, solid pure chroma key green background, background color must be exactly RGB(0,255,0) / HEX #00FF00, not transparent, no checkerboard pattern, no fake transparency, high-resolution cute cartoon style, chubby radish body partially visible above the planting line but without any soil tile, pastel pink, lavender, and creamy white radish body, larger soft rounded leaves, leaf color should be soft muted mint green and must not match the pure green background, a few small solid star-bubble ornaments around the radish, the star-bubbles must be flat decorative shapes, not glowing particles, centered object, the object must be centered both horizontally and vertically, object should occupy about 55% to 65% of the canvas height, clean outer silhouette, crisp cutout edge, no glow, no aura, no bloom, no light halo, no sparkle effects, no shadow outside the object, no soil base, no ground, no platform, cozy whimsical farming game asset, no text, no watermark, not pixel art, not realistic
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
A cute fantasy crop growth stage asset, fully mature Starbubble Radish, stage 3, 512x512, solid pure chroma key green background, background color must be exactly RGB(0,255,0) / HEX #00FF00, not transparent, no checkerboard pattern, no fake transparency, high-resolution cute cartoon style, round chubby harvestable radish body, pastel pink, lavender, and creamy white colors, soft rounded leaves, leaf color should be soft muted mint green and must not match the pure green background, several small solid star-bubble ornaments around the radish, the star-bubbles must look like cute decorative flat shapes, not glowing effects, clearly harvestable, centered object, the object must be centered both horizontally and vertically, object should occupy about 70% to 80% of the canvas height, clean outer silhouette, crisp cutout edge, no glow, no aura, no bloom, no light halo, no sparkle effects, no shadow outside the object, no soil base, no ground, no platform, adorable cozy farming game asset, no text, no watermark, not pixel art, not realistic
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
A cute cartoon farming game UI button, shop button normal state, 512x160, solid pure chroma key green background, background color must be exactly RGB(0,255,0) / HEX #00FF00, not transparent, no checkerboard pattern, no fake transparency, high-resolution cozy casual game UI asset, rounded rectangle button, soft cream color, subtle pastel orange and muted green accents, clean readable design, empty center area reserved for text, centered object, the button must be centered both horizontally and vertically, the button should occupy about 85% to 92% of the canvas width and about 70% to 78% of the canvas height, rounded corners must be fully visible, soft inner shadow and very subtle attached contact shadow only, no external glow, no aura, no bloom, no light halo, no text, no letters, no symbols, no watermark, not pixel art
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
A cute cartoon farming game UI button, shop button hover state, 512x160, solid pure chroma key green background, background color must be exactly RGB(0,255,0) / HEX #00FF00, not transparent, no checkerboard pattern, no fake transparency, high-resolution cozy casual game UI asset, rounded rectangle button, slightly brighter warm cream color than the normal state, subtle pastel orange and muted green accents, clean readable design, empty center area reserved for text, centered object, the button must be centered both horizontally and vertically, the button should occupy about 85% to 92% of the canvas width and about 70% to 78% of the canvas height, rounded corners must be fully visible, soft inner shadow and very subtle attached contact shadow only, no external glow, no aura, no bloom, no light halo, no text, no letters, no symbols, no watermark, not pixel art
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
A cute cartoon gold coin icon for a cozy farming game, 512x512, solid pure chroma key green background, background color must be exactly RGB(0,255,0) / HEX #00FF00, not transparent, no checkerboard pattern, no fake transparency, high-resolution game icon, round shiny golden coin, slightly chubby shape, soft painted highlights on the coin surface only, warm cheerful style, clean outline, centered object, the coin must be centered both horizontally and vertically, the coin should occupy about 70% to 80% of the canvas width and height, crisp cutout edge, no glow, no aura, no bloom, no light halo, no external shadow, no text, no numbers, no letters, no watermark, not pixel art, not realistic
```
