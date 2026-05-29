import pygame

from config import (
    BACKGROUND_COLOR,
    FPS,
    GAME_TITLE,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
)


class Game:
    """Main game controller for Gulu Garden."""

    def __init__(self) -> None:
        """Initialize pygame, window, clock, and basic running state."""
        pygame.init()

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(GAME_TITLE)

        self.clock = pygame.time.Clock()
        self.running = True

    def run(self) -> None:
        """Run the main game loop."""
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

        self.quit()

    def handle_events(self) -> None:
        """Handle user input and window events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self) -> None:
        """Update game state.

        Version 0.1 has no gameplay logic yet.
        This method is reserved for future systems.
        """
        pass

    def draw(self) -> None:
        """Draw everything on the screen."""
        self.screen.fill(BACKGROUND_COLOR)
        pygame.display.flip()

    def quit(self) -> None:
        """Cleanly quit pygame."""
        pygame.quit()