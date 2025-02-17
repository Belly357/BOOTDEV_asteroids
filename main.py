# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame # type: ignore
from constants import *
from player import *

def __prog_init__():
    # pygame.init()
    # screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # figure out how to init the screen here rather than main fuction
    pass

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    game_delta = 0
    main_player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        main_player.update(game_delta)
        main_player.draw(screen)
        pygame.display.flip()        
        game_delta = game_clock.tick(60) / 1000



if __name__ == "__main__":
    main()