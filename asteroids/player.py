import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
	def __init__(self,x,y,shoot_cd):
		super().__init__(x,y,PLAYER_RADIUS)
		self.rotation = 0
		self.cooldown = shoot_cd

	def triangle(self):
		forward = pygame.Vector2(0,1).rotate(self.rotation)
		right = pygame.Vector2(0,1).rotate(self.rotation +90) *self.radius/1.5
		a = self.position + forward * self.radius
		b = self.position - forward * self.radius - right
		c = self.position - forward * self.radius + right
		return [a,b,c]

	def draw(self,screen):
		pygame.draw.polygon(screen, "white", self.triangle(),LINE_WIDTH)

	def rotate(self,dt):
		self.rotation += PLAYER_TURN_SPEED * dt

	def update(self,dt):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_a]:
			self.rotate(dt)
		if keys[pygame.K_d]:
			self.rotate(dt * -1)
		if keys[pygame.K_w]:
			self.move(dt)
		if keys[pygame.K_s]:
			self.move(dt * -1)
		if keys[pygame.K_SPACE]:
			self.shoot(dt)
		self.cooldown -= dt

	def move(self,dt):
		unit_vector = pygame.Vector2(0, 1)
		rotated_vector = unit_vector.rotate(self.rotation)
		rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
		self.position += rotated_with_speed_vector

	def shoot(self,dt):
		if self.cooldown > 0:
			return
		else:
			bullet = Shot(self.position[0],self.position[1],SHOT_RADIUS)
			bullet.velocity = (pygame.Vector2(0,1) * PLAYER_SHOOT_SPEED).rotate(self.rotation)
			self.cooldown = 0.3
