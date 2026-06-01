import pygame


class Button:
    """Simple UI button with optional image skins."""

    def __init__(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        text: str,
    ) -> None:
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text

    def is_hovered(self, mouse_pos: tuple[int, int]) -> bool:
        """Return whether the mouse is over the button."""
        return self.rect.collidepoint(mouse_pos)

    def is_clicked(self, mouse_pos: tuple[int, int]) -> bool:
        """Return whether the button is clicked."""
        return self.is_hovered(mouse_pos)

    def draw(
        self,
        screen: pygame.Surface,
        font: pygame.font.Font,
        normal_color: tuple[int, int, int],
        hover_color: tuple[int, int, int],
        border_color: tuple[int, int, int],
        text_color: tuple[int, int, int],
        normal_image: pygame.Surface | None = None,
        hover_image: pygame.Surface | None = None,
    ) -> None:
        """Draw the button.

        Use image skins if available. Otherwise, draw the old rectangle button.
        """
        mouse_pos = pygame.mouse.get_pos()
        hovered = self.is_hovered(mouse_pos)

        button_image = None

        if hovered and hover_image is not None:
            button_image = hover_image
        elif normal_image is not None:
            button_image = normal_image

        if button_image is not None:
            screen.blit(button_image, self.rect)
        else:
            if hovered:
                color = hover_color
            else:
                color = normal_color

            pygame.draw.rect(screen, color, self.rect, border_radius=14)
            pygame.draw.rect(
                screen,
                border_color,
                self.rect,
                width=3,
                border_radius=14,
            )

        text_surface = font.render(self.text, True, text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)