# this allows us to use code from
# the open-source pygame library
# throughout this file
from asteroid import *
import sys
import pygame # type: ignore
from AsteroidField import AsteroidField
from constants import *
from player import *
from shot import Shot

def __prog_init__():
    # pygame.init()
    # screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # figure out how to init the screen here rather than main fuction
    pass

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    game_delta = 0

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    all_shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = updateable
    Shot.containers = (all_shots, updateable, drawable)


    main_player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    game_asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        updateable.update(game_delta)
        
        for test_asteroid in asteroids:
            if main_player.is_colliding(test_asteroid):
                print("Game over!")
                sys.exit()
        
            for bullet in all_shots:
                if test_asteroid.is_colliding(bullet):
                    bullet.kill()
                    test_asteroid.split()

        for obj_draw in drawable:
            obj_draw.draw(screen)
        pygame.display.flip()        
        game_delta = game_clock.tick(60) / 1000



if __name__ == "__main__":
    main()