import pygame
import sys
from constants import SCREEN_WIDTH,SCREEN_HEIGHT,PLAYER_SHOOT_COOLDOWN
from logger import log_state,log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
	print(f"""Starting Asteroids with pygame version: {pygame.version.ver}
Screen width: {SCREEN_WIDTH}
Screen height: {SCREEN_HEIGHT}""")
	pygame.init()
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	Player.containers = (updatable,drawable)
	Shot.containers = (shots,updatable,drawable)
	Asteroid.containers = (asteroids,updatable,drawable)
	AsteroidField.containers = (updatable)
	clock = pygame.time.Clock() 
	field = AsteroidField()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,PLAYER_SHOOT_COOLDOWN)
	while True:
		log_state()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill("black")
		dt = (clock.tick(60) /1000)
		updatable.update(dt)
		for object in asteroids:
			if object.collides_with(player):
				log_event("player_hit")
				print("Game over!")
				sys.exit()
			for shot in shots:
				if object.collides_with(shot):
					log_event("asteroid_shot")
					object.split()
					shot.kill()
		for object in drawable:
			object.draw(screen)
		pygame.display.flip()

if __name__ == "__main__":
	main()
