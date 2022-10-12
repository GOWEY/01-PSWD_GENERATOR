from cgi import print_environ
from cmath import rect
from operator import truediv
import random
import string
import pygame
from pygame.locals import *
import sys

nb_lettres = 12
nb_chiffres = 2
majuscules = 1


def gen_mdp(nb_lettres,nb_chiffres,majuscules):
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

    mdp_final = ''.join(mot_de_passe)

    return mdp_final


pygame.init()

Size = 100
blue = ( 100, 177, 255 )
flag_mdp = 0

font = pygame.font.Font('freesansbold.ttf', 32)

running = True
while running:

    ecran = pygame.display.set_mode((Size*6,Size*8))
    ecran.fill((150,150,150))
    bouton = pygame.draw.ellipse(ecran, blue, Rect(2*Size, 6*Size, 2*Size, Size))

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False    

        if event.type == pygame.MOUSEBUTTONDOWN:
            if bouton.collidepoint(event.pos):
                mdp_final = gen_mdp(12,2,1)
                flag_mdp = 1

    
    if flag_mdp != 0:
        # create a text surface object,
        # on which text is drawn on it.
        text = font.render(mdp_final,True,(255,255,255))
        
        # create a rectangular object for the
        # text surface object
        textRect = text.get_rect()
        ecran.blit(text,(150,300))

    pygame.display.update()