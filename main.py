from cgi import print_environ
import random
import string
import tkinter

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




def do_something():
    print("Clicked")

window = Tk()

# On injecte un premier label dans la fenêtre
label = Label(window, text="Hello Tk")
label.pack()

# Puis, on injecte un bouton dans la fenêtre. Il est connecté à la
# fonction do_something qui déclenchera au clic sur le bouton.
button = Button(window, text="Push me !", command=do_something)
button.pack()

window.mainloop