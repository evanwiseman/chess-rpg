import pygame

from src.backend.foundation.constants import SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_FRAMERATE
from src.game import Player


def main():
    pygame.init()
    print("Starting Chess-RPG")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player("Player1")

    # Time
    clock = pygame.time.Clock()
    dt = 0

    while True:
        # Check for exit condition
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.display.flip()
        dt = clock.tick(SCREEN_FRAMERATE) / 1000 


if __name__ == "__main__":
    main()
