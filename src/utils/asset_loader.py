from pathlib import Path

import pygame

from utils.image_tint import apply_scene_tint


class AssetLoader:
    """Load, scale, tint, and cache game image assets."""

    def __init__(self) -> None:
        self.image_cache: dict[tuple[Path, tuple[int, int] | None, bool], pygame.Surface] = {}
        self.tinted_image_cache: dict[
            tuple[Path, tuple[int, int] | None, str, bool],
            pygame.Surface,
        ] = {}

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

        cache_key = (image_path, size, use_alpha)

        if cache_key in self.image_cache:
            return self.image_cache[cache_key]

        try:
            image = pygame.image.load(str(image_path))

            if use_alpha:
                image = image.convert_alpha()
            else:
                image = image.convert()

            if size is not None:
                image = pygame.transform.smoothscale(image, size)

            self.image_cache[cache_key] = image
            return image

        except pygame.error:
            return None

    def load_tinted_image(
        self,
        image_path: Path,
        size: tuple[int, int] | None,
        phase: str,
        tint_settings: dict[str, dict],
        use_alpha: bool = True,
    ) -> pygame.Surface | None:
        """Load a tinted image for a day phase.

        The tinted result is cached, so it is not recalculated every frame.
        """
        if phase == "daytime":
            return self.load_image(
                image_path=image_path,
                size=size,
                use_alpha=use_alpha,
            )

        cache_key = (image_path, size, phase, use_alpha)

        if cache_key in self.tinted_image_cache:
            return self.tinted_image_cache[cache_key]

        base_image = self.load_image(
            image_path=image_path,
            size=size,
            use_alpha=use_alpha,
        )

        if base_image is None:
            return None

        phase_tint = tint_settings.get(phase)

        if phase_tint is None:
            return base_image

        tinted_image = apply_scene_tint(
            image=base_image,
            multiply=phase_tint["multiply"],
            overlay=phase_tint["overlay"],
        )

        self.tinted_image_cache[cache_key] = tinted_image
        return tinted_image