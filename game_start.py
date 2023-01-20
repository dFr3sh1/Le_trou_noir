import time
from pygame import mixer


# Script de départ du jeu
start_string = """
Vous êtes devant votre bol de céréales, 
soudainement, vous êtes aspiré dans un trou noir que forme vos chocapics,
vous tombez sans cesse,
l'ennui vous gagne, 
heureusement qu'une voix vous donne des énigmes pour passer le temps...
Mais peut-être que tout ça à un sens...




"""

def game_start(start_string):
    """
    :param start_string: Prend une variable string.
    :type start_string: str
    :return: Retourne une string d'introduction au jeu.
    :rtype: str
    """

    mixer.init()
    mixer.music.load("Dossier_tools/typewriterSoundEffect.mp3")
    mixer.music.play(loops=2)
    
            
    for char in start_string:
        print(char, end="")
        time.sleep(0.03)
    
    mixer.music.stop()