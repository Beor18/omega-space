#-*- coding: UTF-8 -*-

import pygame
import sys, os

from pygame.locals import *

x = 280
y = 100
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

# Variables para la ventana
ancho = 512
alto = 512
pantalla = pygame.display.set_mode((ancho,alto))
pygame.display.set_caption("Omega Space")


reloj = pygame.time.Clock()
FPS = 30

#repeticion de teclas
pygame.key.set_repeat(200,50)

# Import el Fondo y Nave.
from prueba import Espacio
from nave_jugador import NaveJugador
nave_jugador = NaveJugador()


# Metemos dentro de un objeto para poder llamar en el bucle
espacio = Espacio()

# Bucle
while True:
	for evento in pygame.event.get():
		if evento.type == QUIT: 
			sys.exit()
				
				
	
	#
	espacio.update(pantalla)
	nave_jugador.update(pantalla)
	#nave_jugador.movimiento()

	print pygame.time.get_ticks()/1000
	#print reloj
	
	pygame.display.update()
	#print "FPS: ", reloj.tick(FPS)

