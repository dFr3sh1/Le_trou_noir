import random

from game_start import game_start, start_string
from functions_questions_and_logs import question_launcher, save_logs, questions_dictionnary


game_start(start_string)

while True:
    
    # sélectionne une question aléatoirement
    random_question = random.choice(list(questions_dictionnary.keys()))
    # On lance alors le jeu qui va lancer des questions aléatoirement
    question_launcher(random_question)

    # On sauvegarde les actions du joueur
    save_logs()