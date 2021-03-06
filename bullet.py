import pygame, time
from pygame.sprite import Sprite

class Bullet(Sprite):
	'''A class to manage the bullets fired from the ship'''
	
	def __init__(self, ai_game):
		'''Create a bullet object at the ship's current position'''
		
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.color = self.settings.bullet_color
		
		#Creating a timer for every bullet
		self.clock = pygame.time.Clock()
		self.current = time.time()
		
		#Create a bullet rect at (0,0) and then set correct position
		self.rect = pygame.Rect(0,0,self.settings.bullet_width, self.settings.bullet_height)
		self.rect.midtop = ai_game.ship.rect.midtop
		
		#Store the bullet's position as a decimal value
		self.y = float(self.rect.y)
		
	def update(self):
		'''Move the bullet up the screen'''
		
		#Update the decimal position of the bullet every 0.5 milliseconds
		if (time.time() - self.current) > 0.0005:	
			self.y -= self.settings.bullet_speed
			self.current = time.time()
		
		#Update the rect position.
		self.rect.y = self.y
		
	def draw_bullet(self):
		'''Draw the bullet to the screen'''
		
		pygame.draw.rect(self.screen, self.color, self.rect)

class LeftBullet(Sprite):
	'''A class to manage the bullets fired from the ship'''
	
	def __init__(self, ai_game):
		'''Create a bullet object at the ship's current position'''
		
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.color = self.settings.bullet_color
		
		#Creating a timer for every bullet
		self.clock = pygame.time.Clock()
		self.current = time.time()
		
		#Create a bullet rect at (0,0) and then set correct position
		self.rect = pygame.Rect(0,0,self.settings.bullet_width, self.settings.bullet_height)
		self.rect.midtop = ai_game.ship.rect.midtop
		
		#Store the bullet's position as a decimal value
		self.y = float(self.rect.y)
		self.x = float(self.rect.x)
		
	def update(self):
		'''Move the bullet up the screen'''
		
		#Update the decimal position of the bullet every 0.5 milliseconds
		if (time.time() - self.current) > 0.0005:	
			self.y -= self.settings.bullet_speed
			self.x -= (self.settings.bullet_speed/2)
			self.current = time.time()
		
		#Update the rect position.
		self.rect.y = self.y
		self.rect.x = self.x
		
	def draw_bullet(self):
		'''Draw the bullet to the screen'''
		
		pygame.draw.rect(self.screen, self.color, self.rect)

class RightBullet(Sprite):
	'''A class to manage the bullets fired from the ship'''
	
	def __init__(self, ai_game):
		'''Create a bullet object at the ship's current position'''
		
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.color = self.settings.bullet_color
		
		#Creating a timer for every bullet
		self.clock = pygame.time.Clock()
		self.current = time.time()
		
		#Create a bullet rect at (0,0) and then set correct position
		self.rect = pygame.Rect(0,0,self.settings.bullet_width, self.settings.bullet_height)
		self.rect.midtop = ai_game.ship.rect.midtop
		
		#Store the bullet's position as a decimal value
		self.y = float(self.rect.y)
		self.x = float(self.rect.x)
		
	def update(self):
		'''Move the bullet up the screen'''
		
		#Update the decimal position of the bullet every 0.5 milliseconds
		if (time.time() - self.current) > 0.0005:	
			self.y -= self.settings.bullet_speed
			self.x += (self.settings.bullet_speed/2)
			self.current = time.time()
		
		#Update the rect position.
		self.rect.y = self.y
		self.rect.x = self.x
		
	def draw_bullet(self):
		'''Draw the bullet to the screen'''
		
		pygame.draw.rect(self.screen, self.color, self.rect)
