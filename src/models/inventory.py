from dataclasses import dataclass, field


@dataclass
class Inventory:
    """Player inventory for seeds and future items."""

    seeds: dict[str, int] = field(default_factory=dict)

    def get_seed_count(self, crop_id: str) -> int:
        """Return how many seeds the player has for a crop."""
        return self.seeds.get(crop_id, 0)

    def add_seed(self, crop_id: str, amount: int = 1) -> None:
        """Add seeds for a crop."""
        if amount <= 0:
            return

        current_count = self.get_seed_count(crop_id)
        self.seeds[crop_id] = current_count + amount

    def consume_seed(self, crop_id: str, amount: int = 1) -> bool:
        """Consume seeds if enough are available.

        Return True if consumption succeeds.
        """
        if amount <= 0:
            return False

        current_count = self.get_seed_count(crop_id)

        if current_count < amount:
            return False

        self.seeds[crop_id] = current_count - amount
        return True