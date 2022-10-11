from cgi import print_environ
from cmath import rect
import random
import string
import pygame
from pygame.locals import *
import sys

nb_lettres = 12
nb_chiffres = 2
majuscules = 1

mot_de_passe = []

for i in range(nb_lettres):
    randnum = random.randint(0,len(string.ascii_lowercase)-1)
    piece = random.randint(0,1)
    if majuscules == 1:
        if piece == 1:
            randlet = string.ascii_lowercase[randnum]
        elif piece == 0:
            randlet = string.ascii_uppercase[randnum]
    elif majuscules == 0:
        randlet = string.ascii_lowercase[randnum]
    mot_de_passe.append(randlet)

for i in range(nb_chiffres):    
    randnum = random.randint(1,9)
    mot_de_passe.append(str(randnum))
    
random.shuffle(mot_de_passe)

str = ''.join(mot_de_passe)




pygame.init()

Size = 100
blue = ( 100, 177, 255 )

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    ecran = pygame.display.set_mode((Size*6,Size*8))
    ecran.fill((150,150,150))
    pygame.draw.ellipse(ecran, blue, Rect(2*Size, 6*Size, 2*Size, Size))

    pygame.display.update()