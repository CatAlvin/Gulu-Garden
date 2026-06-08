class ShopSystem:
    """Shop logic for buying items."""

    def __init__(self, shop_items: dict) -> None:
        """Initialize shop with item data."""
        self.shop_items = shop_items

    def buy_seed(self, item_id: str, player, inventory) -> tuple[bool, str]:
        """Buy a seed item.

        Return:
            (success, message)
        """
        item = self.shop_items.get(item_id)

        if item is None:
            return False, "商店中没有找到该商品。"

        if item.get("item_type") != "seed":
            return False, "该商品不是种子。"

        price = int(item.get("price", 0))
        crop_id = item.get("crop_id")
        amount = int(item.get("amount", 1))
        item_name = item.get("name_cn", item.get("name_en", item_id))

        if crop_id is None:
            return False, "该种子商品缺少作物 ID。"

        if not player.spend_coins(price):
            return False, f"金币不足，无法购买{item_name}。需要 {price} 金币。"

        inventory.add_seed(crop_id, amount)

        return (
            True,
            f"已购买 {amount} 个{item_name}，花费 {price} 金币。"
            f"当前金币：{player.coins}"
        )