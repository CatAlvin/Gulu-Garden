from pathlib import Path

import pygame


class AssetLoader:
    """Load and cache game image assets."""

    def __init__(self) -> None:
        self.image_cache: dict[Path, pygame.Surface] = {}

    def load_image(
        self,
        image_path: Path,
        size: tuple[int, int] | None = None,
        use_alpha: bool = True,
    ) -> pygame.Surface | None:
        """Load an image from disk.

        Return None if the image does not exist or cannot be loaded.
        """
        if not image_path.exists():
            return None

        cache_key = image_path

        if cache_key not in self.image_cache:
            try:
                image = pygame.image.load(str(image_path))

                if use_alpha:
                    image = image.convert_alpha()
                else:
                    image = image.convert()

                self.image_cache[cache_key] = image
            except pygame.error:
                return None

        image = self.image_cache[cache_key]

        if size is not None:
            return pygame.transform.smoothscale(image, size)

        return image