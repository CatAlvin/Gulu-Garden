# docs/save-format.md

# 《咕噜小菜园》Gulu Garden 存档格式文档 v0.1

## 1. 文档目的

本文档用于设计《咕噜小菜园》的 JSON 存档结构。

由于本游戏需要支持现实时间流逝和离线成长，因此存档系统是项目最核心的系统之一。

存档系统必须保证：

1. 游戏关闭后，玩家进度不会丢失。
2. 作物可以根据现实经过时间继续成长。
3. 多块土地的状态可以正确恢复。
4. 后续可以扩展任务、图鉴、背包、装饰和成就。
5. 存档结构清晰，方便调试。

---

## 2. 存档基本原则

### 2.1 使用 JSON

第一阶段使用 JSON 作为存档格式。

理由：

* 方便阅读
* 方便调试
* 适合小型单机项目
* Python 原生支持
* 方便放在 GitHub 文档中说明

### 2.2 真实存档不提交 GitHub

真实存档文件不应提交到 GitHub。

可以提交：

* `saves/.gitkeep`
* `docs/save-format.md`
* `docs/example-save.json`

不建议提交：

* 玩家真实存档
* 自动生成的运行时存档
* 临时备份存档

### 2.3 存档应当可扩展

即使第一阶段只需要金币、种子、土地和作物，也应预留未来字段。

例如：

* 任务进度
* 图鉴进度
* 完美品质记录
* 装饰数据
* 设置项
* 统计数据

---

## 3. 存档文件命名

### 3.1 单存档阶段

第一阶段可以使用：

```text
saves/save_1.json
```

### 3.2 多存档阶段

多存档阶段建议使用：

```text
saves/save_1.json
saves/save_2.json
saves/save_3.json
```

### 3.3 存档元信息

未来可以增加一个存档索引文件：

```text
saves/save_index.json
```

用于记录每个存档槽的显示信息，例如：

* 存档名称
* 创建时间
* 最后保存时间
* 当前金币
* 已解锁土地数量
* 游戏版本

---

## 4. 时间字段设计

时间字段建议统一使用 ISO 8601 字符串。

例如：

```text
2026-05-29T18:30:00
```

### 4.1 为什么要记录时间

作物离线成长需要知道：

1. 作物什么时候种下。
2. 当前什么时候重新进入游戏。
3. 两者之间经过了多久。

### 4.2 关键时间字段

| 字段              | 说明           |
| --------------- | ------------ |
| created_at      | 存档创建时间       |
| last_saved_at   | 上一次保存时间      |
| planted_at      | 某块土地上作物的种植时间 |
| last_watered_at | 上一次浇水时间      |
| harvested_at    | 后续可记录最近收获时间  |

---

## 5. 顶层存档结构

推荐顶层结构：

```text
{
  "save_version": "0.1",
  "game_version": "0.1.0",
  "slot_id": 1,
  "created_at": "...",
  "last_saved_at": "...",
  "player": {},
  "time": {},
  "inventory": {},
  "plots": [],
  "tasks": {},
  "codex": {},
  "settings": {},
  "statistics": {}
}
```

说明：

| 字段            | 说明     | 第一阶段是否需要 |
| ------------- | ------ | -------- |
| save_version  | 存档结构版本 | 需要       |
| game_version  | 游戏版本   | 需要       |
| slot_id       | 存档槽编号  | 多存档阶段需要  |
| created_at    | 创建时间   | 需要       |
| last_saved_at | 最后保存时间 | 需要       |
| player        | 玩家数据   | 需要       |
| time          | 时间相关数据 | 需要       |
| inventory     | 背包数据   | 需要       |
| plots         | 土地数据   | 需要       |
| tasks         | 任务数据   | 后续       |
| codex         | 图鉴数据   | 后续       |
| settings      | 设置数据   | 后续       |
| statistics    | 统计数据   | 后续       |

---

## 6. 玩家数据 player

### 6.1 第一阶段字段

```text
"player": {
  "name": "Player",
  "coins": 50
}
```

### 6.2 字段说明

| 字段    | 说明                    |
| ----- | --------------------- |
| name  | 玩家名称，第一阶段可以固定为 Player |
| coins | 当前金币数量                |

### 6.3 后续可扩展字段

```text
"player": {
  "name": "Player",
  "coins": 50,
  "total_earned_coins": 0,
  "total_spent_coins": 0
}
```

暂时不设计等级系统，因为当前项目决定金币是主要解锁途径。

---

## 7. 时间数据 time

### 7.1 推荐结构

```text
"time": {
  "use_real_world_time": true,
  "current_day_phase": "daytime",
  "last_calculated_at": "2026-05-29T18:30:00"
}
```

### 7.2 字段说明

| 字段                  | 说明           |
| ------------------- | ------------ |
| use_real_world_time | 是否使用现实时间     |
| current_day_phase   | 当前昼夜阶段       |
| last_calculated_at  | 上一次计算作物状态的时间 |

### 7.3 昼夜阶段取值

| 值        | 说明 |
| -------- | -- |
| morning  | 清晨 |
| daytime  | 白日 |
| evening  | 傍晚 |
| midnight | 午夜 |

---

## 8. 背包数据 inventory

### 8.1 第一阶段结构

第一阶段只记录种子数量。

```text
"inventory": {
  "seeds": {
    "starbubble_radish": 3
  },
  "crops": {},
  "tools": {},
  "fertilizers": {},
  "decorations": {}
}
```

### 8.2 字段说明

| 字段          | 说明    | 第一阶段是否使用 |
| ----------- | ----- | -------- |
| seeds       | 种子数量  | 是        |
| crops       | 收获的作物 | 后续       |
| tools       | 工具    | 后续       |
| fertilizers | 肥料    | 后续       |
| decorations | 装饰    | 后续       |

### 8.3 第一阶段简化规则

第一阶段可以采用：

> 收获作物后直接转化为金币，不进入 crops 背包。

后续如果加入“作物背包 + 手动出售”，再启用 crops 字段。

---

## 9. 土地数据 plots

### 9.1 土地数组结构

每块土地是 `plots` 数组中的一个对象。

推荐结构：

```text
"plots": [
  {
    "plot_id": 1,
    "status": "empty",
    "is_unlocked": true,
    "unlock_cost": 0,
    "crop": null
  }
]
```

### 9.2 土地字段说明

| 字段          | 说明                  |
| ----------- | ------------------- |
| plot_id     | 土地编号                |
| status      | 土地状态                |
| is_unlocked | 是否已解锁               |
| unlock_cost | 解锁价格                |
| crop        | 当前种植的作物，如果没有则为 null |

### 9.3 土地状态取值

| 值          | 说明      |
| ---------- | ------- |
| locked     | 被锁定     |
| empty      | 空地      |
| planted    | 已播种     |
| growing    | 生长中     |
| need_water | 需要浇水    |
| mature     | 已成熟     |
| withered   | 枯萎，后续版本 |

---

## 10. 土地中的作物 crop

### 10.1 作物结构

当土地上有作物时，`crop` 字段记录作物信息。

```text
"crop": {
  "crop_id": "starbubble_radish",
  "planted_at": "2026-05-29T18:30:00",
  "growth_time_seconds": 30,
  "current_stage": 0,
  "is_watered": false,
  "last_watered_at": null,
  "is_mature": false,
  "quality": "normal"
}
```

### 10.2 字段说明

| 字段                  | 说明     | 第一阶段是否需要 |
| ------------------- | ------ | -------- |
| crop_id             | 作物 ID  | 是        |
| planted_at          | 种植时间   | 是        |
| growth_time_seconds | 成熟所需秒数 | 是        |
| current_stage       | 当前成长阶段 | 是        |
| is_watered          | 是否已浇水  | 是        |
| last_watered_at     | 上次浇水时间 | 是        |
| is_mature           | 是否成熟   | 是        |
| quality             | 作物品质   | 后续       |

### 10.3 成长阶段 current_stage

星泡萝卜第一阶段建议使用 4 个阶段：

| current_stage | 阶段  |
| ------------: | --- |
|             0 | 种子  |
|             1 | 幼苗  |
|             2 | 生长期 |
|             3 | 成熟  |

### 10.4 阶段计算规则

根据已经经过的时间计算阶段。

例如星泡萝卜成熟时间为 30 秒：

| 已经过时间     | 阶段  |
| --------- | --- |
| 0 - 9 秒   | 种子  |
| 10 - 19 秒 | 幼苗  |
| 20 - 29 秒 | 生长期 |
| 30 秒及以上   | 成熟  |

---

## 11. 离线成长计算规则

### 11.1 基础逻辑

读取存档时：

1. 获取当前真实时间。
2. 遍历每块土地。
3. 如果土地上有作物，读取 planted_at。
4. 计算当前时间与 planted_at 的差值。
5. 根据差值更新作物阶段。
6. 如果差值大于等于 growth_time_seconds，则作物成熟。

### 11.2 第一阶段规则

第一阶段只处理成熟，不处理枯萎。

也就是说：

* 离线时间短：作物继续成长
* 离线时间超过成熟时间：作物成熟
* 离线时间非常长：作物仍然保持成熟，不会死亡

### 11.3 后续枯萎规则

后续如果加入枯萎，可以增加字段：

```text
"wither_time_seconds": 86400
```

但第一阶段不建议加入，避免玩家压力过大。

---

## 12. 任务数据 tasks

### 12.1 后续结构

任务系统加入后，可以使用：

```text
"tasks": {
  "first_plant": {
    "status": "completed",
    "progress": 1,
    "target": 1,
    "reward_claimed": true
  },
  "harvest_3_starbubble_radish": {
    "status": "active",
    "progress": 2,
    "target": 3,
    "reward_claimed": false
  }
}
```

### 12.2 任务状态

| 值         | 说明    |
| --------- | ----- |
| inactive  | 未激活   |
| active    | 进行中   |
| completed | 已完成   |
| claimed   | 已领取奖励 |

---

## 13. 图鉴数据 codex

### 13.1 后续结构

图鉴系统加入后，可以使用：

```text
"codex": {
  "starbubble_radish": {
    "has_planted": true,
    "has_harvested": true,
    "has_perfect_quality": false,
    "best_method_unlocked": false
  }
}
```

### 13.2 字段说明

| 字段                   | 说明         |
| -------------------- | ---------- |
| has_planted          | 是否种植过      |
| has_harvested        | 是否收获过      |
| has_perfect_quality  | 是否获得过完美品质  |
| best_method_unlocked | 是否解锁最佳种植方式 |

---

## 14. 设置数据 settings

### 14.1 后续结构

```text
"settings": {
  "music_volume": 0.8,
  "sfx_volume": 0.8,
  "fullscreen": false,
  "resolution": "1280x720"
}
```

### 14.2 第一阶段处理

第一阶段可以暂时不提供设置界面，但可以预留 settings 字段。

---

## 15. 统计数据 statistics

### 15.1 后续结构

```text
"statistics": {
  "total_planted": 0,
  "total_harvested": 0,
  "total_starbubble_radish_harvested": 0,
  "total_perfect_crops": 0
}
```

统计数据可用于：

* 成就系统
* 任务系统
* 图鉴记录
* 玩家回顾

---

## 16. 第一阶段完整存档示例

以下是第一阶段推荐存档结构示例。

```text
{
  "save_version": "0.1",
  "game_version": "0.1.0",
  "slot_id": 1,
  "created_at": "2026-05-29T18:00:00",
  "last_saved_at": "2026-05-29T18:30:00",

  "player": {
    "name": "Player",
    "coins": 50
  },

  "time": {
    "use_real_world_time": true,
    "current_day_phase": "evening",
    "last_calculated_at": "2026-05-29T18:30:00"
  },

  "inventory": {
    "seeds": {
      "starbubble_radish": 3
    },
    "crops": {},
    "tools": {},
    "fertilizers": {},
    "decorations": {}
  },

  "plots": [
    {
      "plot_id": 1,
      "status": "empty",
      "is_unlocked": true,
      "unlock_cost": 0,
      "crop": null
    },
    {
      "plot_id": 2,
      "status": "growing",
      "is_unlocked": true,
      "unlock_cost": 0,
      "crop": {
        "crop_id": "starbubble_radish",
        "planted_at": "2026-05-29T18:29:40",
        "growth_time_seconds": 30,
        "current_stage": 2,
        "is_watered": true,
        "last_watered_at": "2026-05-29T18:29:45",
        "is_mature": false,
        "quality": "normal"
      }
    }
  ],

  "tasks": {},
  "codex": {},
  "settings": {
    "music_volume": 0.8,
    "sfx_volume": 0.8,
    "fullscreen": false,
    "resolution": "1280x720"
  },
  "statistics": {
    "total_planted": 1,
    "total_harvested": 0,
    "total_perfect_crops": 0
  }
}
```

---

## 17. 存档损坏处理原则

如果存档文件不存在：

* 创建新存档。

如果存档文件存在但无法读取：

* 不要直接崩溃。
* 显示提示。
* 可以创建新存档或读取备份。

如果某些字段缺失：

* 使用默认值补齐。

例如：

| 缺失字段  | 默认值  |
| ----- | ---- |
| coins | 50   |
| seeds | 空字典  |
| plots | 默认土地 |
| tasks | 空字典  |
| codex | 空字典  |

---

## 18. 当前待确认问题

以下问题会影响后续存档设计，需要在正式实现前确认：

1. 玩家是否可以自己命名存档？
2. 多存档数量是否固定为 3 个？
3. 收获作物是否第一阶段直接卖钱，还是先进入作物背包再手动出售？
4. 是否需要防止玩家通过修改系统时间加速作物成长？
5. 是否需要自动备份存档文件？

在这些问题确认前，第一阶段可以先按最简单方案推进：

* 固定 3 个存档槽
* 第一阶段收获直接变金币
* 暂时不防系统时间修改
* 后续再加入备份机制
