import pygame


def apply_scene_tint(
    image: pygame.Surface,
    multiply: tuple[int, int, int],
    overlay: tuple[int, int, int, int],
) -> pygame.Surface:
    """Return a tinted copy of an image for a day phase.

    This function only changes RGB color channels.
    It keeps the original alpha channel unchanged, so transparent pixels
    remain transparent after tinting.
    """
    tinted_image = image.copy().convert_alpha()
    width, height = tinted_image.get_size()

    # 1. Multiply RGB channels only.
    # Use BLEND_RGB_MULT instead of BLEND_RGBA_MULT to preserve alpha.
    multiply_surface = pygame.Surface((width, height)).convert()
    multiply_surface.fill(multiply)
    tinted_image.blit(
        multiply_surface,
        (0, 0),
        special_flags=pygame.BLEND_RGB_MULT,
    )

    # 2. Apply a soft RGB overlay while preserving alpha.
    # Formula:
    # result_rgb = original_rgb * (1 - a) + overlay_rgb * a
    overlay_r, overlay_g, overlay_b, overlay_alpha = overlay
    overlay_alpha = max(0, min(255, overlay_alpha))

    if overlay_alpha > 0:
        keep_ratio = 255 - overlay_alpha

        keep_surface = pygame.Surface((width, height)).convert()
        keep_surface.fill((keep_ratio, keep_ratio, keep_ratio))
        tinted_image.blit(
            keep_surface,
            (0, 0),
            special_flags=pygame.BLEND_RGB_MULT,
        )

        add_surface = pygame.Surface((width, height)).convert()
        add_surface.fill(
            (
                overlay_r * overlay_alpha // 255,
                overlay_g * overlay_alpha // 255,
                overlay_b * overlay_alpha // 255,
            )
        )
        tinted_image.blit(
            add_surface,
            (0, 0),
            special_flags=pygame.BLEND_RGB_ADD,
        )

    return tinted_image