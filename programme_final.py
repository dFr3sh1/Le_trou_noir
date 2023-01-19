from pygame import mixer
import time, pygame
import random
import wave
import numpy as np
from functions_questions_and_logs import question_launcher, save_logs


# Script de départ du jeu
start_string = """
Hello soldier welcome to the black hole Game.
your spaceship was lost in space, to get back to earth you have to answer some questions.
At each level we'll give you a question to answer.
If you can't answer our question you'll lose points.
To start you'll be given 3 chances respresenting your life.
You have also some bonus points hidden in the levels.
You'll get them for each correct answer.
"""



# Dictionnaire principal pour notre jeu, contenant des listes pour les réponses
questions_dictionnary = {
    "Bonjour ?": {
        "propositions": ["Oui", "Non", "Peut-être", "Jaune"],
         "good_response": "Oui"
    },
    "À quoi était consacré ce temple ?": {
        "propositions": ["A toi", "A moi", "Aux autres", "A une divinité"],
        "good_response": "A toi"
    },
    "Quand a été construit ce temple ?": {
        "propositions": ["Il y à des millénaires", "Il y à quelques siècles", "Il y a des décennies", "Il vient d'être construit"],
        "good_response": "Il vient d'être construit"
    },
    "Qui était l'architecte ou le constructeur principal de ce temple ?": {
        "propositions": ["Un roi", "Un groupuscule", "Un architecte", "Un peuple indigène"],
        "good_response": "Un roi"
    }
}

# On définit les bonnes réponses aux questions dans un autre dictionnaire.
response_dictionnary = {
    "Bonjour ?": "Oui",
    "À quoi était consacré ce temple ?": "A toi",
    "Quand a été construit ce temple ?": "Il vient d'être construit",
    "Qui était l'architecte ou le constructeur principal de ce temple ?": "Un roi"
}

# Liste de mots pour la réussite du joueur
felicitations_quotes = ['Bravo !', 'Excellent !', 'Quel génie !', 'Quel talent !',
                        "C'est une prouesse incroyable, tu es un véritable érudit"]

# Un dictionnaire pour sauvegarder les réponses du joueur
save_player_answer = {}

# Définition des attributs du joueur
score = 0
health = 40



while True:
    # sélectionne une question aléatoirement
    random_question = random.choice(list(questions_dictionnary.keys()))
    # On lance alors le jeu qui va lancer des questions aléatoirement
    question_launcher(random_question)

    # On sauvegarde les actions du joueur
    save_logs()

#save_logs()