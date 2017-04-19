import pygame
# Creamos el fondo con movimiento.
class Espacio (pygame.sprite.Sprite):
	def __init__(self):
		self.image = pygame.image.load("imagenes/fondo.gif")
		
		self.rect = self.image.get_rect()
		self.rect.x = 0
		self.rect.y = 1024
		self.ancho = 512
		self.alto = 512
	def update(self,pantalla):
		self.rect.y -= 4
		
		if self.rect.y <= 0:
			self.rect.y = 1024
			
		self.superficie = self.image.subsurface(self.rect.x,self.rect.y,self.ancho,self.alto)	
		pantalla.blit(self.superficie,(0,0))

