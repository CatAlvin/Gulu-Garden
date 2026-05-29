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
            return False, "Shop item not found."

        if item.get("item_type") != "seed":
            return False, "This item is not a seed."

        price = item["price"]
        crop_id = item["crop_id"]
        amount = item.get("amount", 1)
        item_name = item["name_en"]

        if not player.spend_coins(price):
            return False, f"Not enough coins to buy {item_name}."

        inventory.add_seed(crop_id, amount)

        return True, f"Bought {amount} {item_name} for {price} coins."