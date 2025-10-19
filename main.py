import sys
import pygame
from constants import *
from player import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


    clock = pygame.time.Clock()
    dt = 0

   
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    

    Shot.containers = (shots,updatable,drawable)
    player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = updatable
    play = player(SCREEN_WIDTH / 2 , SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    

    while True:
          for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


          updatable.update(dt)

          for asteroid in asteroids:
              if asteroid.check_collision(play):     
                 print("Game over!")
                 sys.exit()   


          for asteroid in asteroids:
              for bullet in shots:
                  if bullet.check_collision(play):
                     bullet.kill() 
                     asteroid.split()
                     
                         
     

          screen.fill((0,0,0)) 
          

          for obj in drawable:
            obj.draw(screen)

          pygame.display.flip()


          dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
