import pygame
from constants import *
from player import Player


def main():
    print("Starting Asteroids!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player_one = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player_one.draw(screen)
        pygame.display.flip()

        # limit framerate to 120 fps
        dt = clock.tick(120) / 1000


if __name__ == "__main__":
    main()
