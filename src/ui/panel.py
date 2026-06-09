import pygame


def draw_rounded_rect(
    screen: pygame.Surface,
    x: int,
    y: int,
    width: int,
    height: int,
    background_color: tuple[int, int, int, int],
    border_color: tuple[int, int, int, int] | None = None,
    border_radius: int = 16,
    border_width: int = 0,
) -> None:
    """Draw a transparent rounded rectangle."""
    surface = pygame.Surface((width, height), pygame.SRCALPHA)
    rect = surface.get_rect()

    pygame.draw.rect(
        surface,
        background_color,
        rect,
        border_radius=border_radius,
    )

    if border_color is not None and border_width > 0:
        pygame.draw.rect(
            surface,
            border_color,
            rect,
            width=border_width,
            border_radius=border_radius,
        )

    screen.blit(surface, (x, y))


def draw_rounded_panel(
    screen: pygame.Surface,
    x: int,
    y: int,
    width: int,
    height: int,
    background_color: tuple[int, int, int, int],
    border_color: tuple[int, int, int, int] | None,
    border_radius: int,
    border_width: int = 2,
    shadow_color: tuple[int, int, int, int] | None = None,
    shadow_offset_x: int = 0,
    shadow_offset_y: int = 0,
) -> None:
    """Draw a rounded panel with optional shadow."""
    if shadow_color is not None:
        draw_rounded_rect(
            screen=screen,
            x=x + shadow_offset_x,
            y=y + shadow_offset_y,
            width=width,
            height=height,
            background_color=shadow_color,
            border_color=None,
            border_radius=border_radius,
            border_width=0,
        )

    draw_rounded_rect(
        screen=screen,
        x=x,
        y=y,
        width=width,
        height=height,
        background_color=background_color,
        border_color=border_color,
        border_radius=border_radius,
        border_width=border_width,
    )