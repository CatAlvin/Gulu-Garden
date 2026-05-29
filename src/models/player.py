from dataclasses import dataclass


@dataclass
class Player:
    """Player data for Gulu Garden."""

    coins: int = 50

    def add_coins(self, amount: int) -> None:
        """Add coins to the player."""
        if amount <= 0:
            return

        self.coins += amount

    def spend_coins(self, amount: int) -> bool:
        """Spend coins if the player has enough.

        Return True if spending succeeds.
        """
        if amount <= 0:
            return False

        if self.coins < amount:
            return False

        self.coins -= amount
        return True