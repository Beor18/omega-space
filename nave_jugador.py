#-*- coding: UTF-8 -*-
import pygame
# Creamos la Nave.
class NaveJugador (pygame.sprite.Sprite):
	def __init__ (self):
		self.image = pygame.image.load("imagenes/nave_verde.png")
		self.rect = self.image.get_rect()
		self.rect.y = 400
		self.rect.centerx = 256
		self.velocidadx = 10
		self.velocidady = 10
	def update (self,pantalla):
		pantalla.blit(self.image,self.rect)
			
		self.movimiento()
	def movimiento(self):
		teclado = pygame.key.get_pressed()
		# if teclado [pygame.K_UP]:
			# print "Arriba"
			# self.rect.y -= self.velocidady
		# if teclado [pygame.K_DOWN]:
			# print "Abajo"
			# self.rect.y += self.velocidady
		if teclado [pygame.K_LEFT]:
			print "Izquierda"
			self.rect.x -= self.velocidadx
		if teclado [pygame.K_RIGHT]:
			
			print "Derecha"
			self.rect.x += self.velocidady
