import random
import time
import os

from rich import print
from rich.highlighter import Highlighter
from pygame import mixer
from pyfiglet import Figlet
f = Figlet (font = "slant")

# Dictionnaire principal pour notre jeu, contenant des listes pour les réponses
questions_dictionnary = {
    "Je suis toujours affamé, je dois manger pour vivre, et pourtant je n'ai pas de bouche.Qui suis-je ?": {
        "propositions": ["Un feu", "Un animal", "Une plante", "Un robot"],
        "good_response": "Un feu"
    },
    "Je suis toujours en mouvement, je suis partout et pourtant je suis immobile.Qui suis-je ?": {
        "propositions": ["Le temps", "La lumière", "Le vent", "L'eau"],
        "good_response": "Le temps"
    },
    "Je suis invisible, mais je peux être entendu, Je peux être capturé, mais je ne peux être touché. Qui suis-je ?": {
        "propositions": ["Un souffle", "Un rêve", "Un fantôme", "Un son"],
        "good_response": "Un son"
    },
    "Je peux être vu, mais je ne peux pas être touché. Je peux être senti. Qui suis-je ?": {
        "propositions": ["Une ombre", "Un souvenir", "Une émotion", "Une image"],
        "good_response": "Une ombre"
    },
    "Je suis un objet commun, mais je peux être difficile à utiliser. Je peux être utilisé pour des choses simples et compliquées. Qui suis-je ?": {
        "propositions": ["Un livre", "Une clé", "Un puzzle", "Un outil"],
        "good_response": "Un outil"
    },
    "Je suis toujours caché, mais je peux être découvert. Je suis précieux, mais je ne peux pas être acheté. Qui suis-je ?": {
    "propositions": ["Un trésor", "Un secret", "Un ami", "Une idée"],
    "good_response": "Un trésor"
    },
    "Je suis toujours en haut, mais je ne peux pas être touché. Je suis un symbole de force et de pouvoir. Qui suis-je ?": {
    "propositions": ["Un aigle", "Un drapeau", "Un roi", "Une montagne"],
    "good_response": "Un drapeau"
    },
    "Je suis toujours en bas, mais je peux être gravi. Je suis un défi et une aventure. Qui suis-je ?": {
    "propositions": ["Une colline", "Une échelle", "Une montagne", "Une grotte"],
    "good_response": "Une montagne"
    },
    "Je suis toujours vide, mais je peux être rempli. Je suis un moyen de transport et de stockage. Qui suis-je ?": {
    "propositions": ["Un sac", "Un bateau", "Un réservoir", "Une bouteille"],
    "good_response": "Un sac"
    },
    "Je suis toujours en mouvement, mais je ne vais nulle part. Je suis utilisé pour se divertir et pour l'exercice. Qui suis-je ?": {
    "propositions": ["Un vélo", "Un ballon", "Une balançoire", "Une roue"],
    "good_response": "Une balançoire"
    },
    "Je suis toujours présent, mais je ne peux pas être vu. Je suis l'air que nous respirons. Qui suis-je ?": {
    "propositions": ["L'air", "Le vent", "L'oxygène", "La vapeur d'eau"],
    "good_response": "L'air"
    },
    "Je suis toujours en mouvement, mais je ne peux pas être touché. Je suis un son. Qui suis-je ?": {
    "propositions": ["Un son", "Une onde", "Une musique", "Un écho"],
    "good_response": "Un son"
    },
    "Je suis toujours présent, mais je ne peux pas être entendu. Je suis le silence. Qui suis-je ?": {
    "propositions": ["Le silence", "La solitude", "Le vide", "L'invisibilité"],
    "good_response": "Le silence"
    },
    "Je suis toujours en mouvement, mais je ne peux pas être vu. Je suis un courant d'eau. Qui suis-je ?": {
    "propositions": ["Un courant d'eau", "Une rivière", "Une cascade", "Un ruisseau"],
    "good_response": "Un courant d'eau"
    },
    "Je suis toujours en haut, mais je peux être utilisé. Je suis un élément de la nature. Qui suis-je ?": {
    "propositions": ["Un nuage", "Une pluie", "Une neige", "Un orage"],
    "good_response": "Un nuage"
    },
    "Je suis toujours caché, mais je peux être découvert. Je suis un indice. Qui suis-je ?": {
    "propositions": ["Un indice", "Une piste", "Un signe", "Une preuve"],
    "good_response": "Un indice"
    },
    "Je suis toujours en haut, mais je peux être atteint. Je suis un but à atteindre. Qui suis-je ?": {
    "propositions": ["Un sommet", "Une cime", "Un pic", "Un faîte"],
    "good_response": "Un sommet"
    },
    "Je suis toujours en mouvement, mais je ne peux pas être touché. Je suis un flux. Qui suis-je ?": {
    "propositions": ["Un flux", "Un courant", "Une circulation", "Un écoulement"],
    "good_response": "Un flux"
    },
    "Je suis toujours présent, mais je ne peux pas être vu. Je suis une force. Qui suis-je ?": {
    "propositions": ["La gravité", "L'électricité", "Le magnétisme", "La pression"],
    "good_response": "La gravité"
    },
    "Je suis toujours en mouvement, mais je ne peux pas être vu. Je suis un processus. Qui suis-je ?": {
    "propositions": ["Une réaction chimique", "Une digestion", "Une fermentation", "Une photosynthèse"],
    "good_response": "Une réaction chimique"
    }

}

# Liste de mots pour la réussite du joueur
felicitations_quotes = ['[bold green]Bravo ![/bold green]', '[bold green]Excellent ![/bold green]', '[bold green]Quel génie ![/bold green]', '[bold green]Quel talent ![/bold green]',"[bold green]C'est une prouesse incroyable, tu es un véritable érudit[/bold green]"]

jokes_quotes = ["[bold red]AH! AH! AH! ![/bold red]", "[bold red]MAIS NON! ![/bold red]", "[bold red]PPPFFFF ![/bold red]", "[bold red]VOUS DORMEZ ?[/bold red]", "[bold red]QUELLE MISERE ![/bold red]","[bold red]MON PAUVRE[/bold red]","[bold red]SORTEZ ![/bold red]"]


# Un dictionnaire pour sauvegarder les réponses du joueur
save_player_answer = {}


def question_launcher(question_key, score, health):
    """
    :param question_key: Take the keys from the dictionary questions.
    :type question_key: dict & str
    :return: The player's result.
    :rtype:
    """

    mixer.init()
    mixer.music.load("Dossier_tools/Yoga_Outer_Space_Nature_Sounds.mp3")
    mixer.music.play(10, 0, 0)

    time.sleep(2)
    question = questions_dictionnary[question_key]
    print(question_key)
    for i, propositions in enumerate(question["propositions"]):
        print(f"{i + 1}. {propositions}")
    user_answer = input("Entrez le chiffre associé à la proposition de votre choix : ")

    if question["propositions"][int(user_answer) - 1] == question["good_response"]:

        print(felicitations_quotes[random.randrange(0, 4)])
        score += random.randint(2, 5)

        if score >= 50:
            mixer.init()
            mixer.music.load("Dossier_tools/success-fanfare-trumpets-6185.mp3")
            print("\n*\------------------------------------------------------------/*\n")
            print(f.renderText("B R A V O !"))
            print("\n*/------------------------------------------------------------\*\n")
            mixer.music.play(1, 0, 0)

            time.sleep(8)
            exit()

        mixer.init()
        mixer.music.load("Dossier_tools/youpi-87023.mp3")
        mixer.music.play(1, 0, 0)
        time.sleep(1)
        print(f"[italic green]Votre score est de {score} et votre santé est de {health}[/italic green]")

        time.sleep(3)
        os.system("clear")

    elif question["propositions"][int(user_answer) - 1] != question["good_response"]:

        print(jokes_quotes[random.randrange(0, 7)])
        health -= random.randint(4, 11)

        mixer.init()
        mixer.music.load("Dossier_tools/karate-chop-6357.mp3")
        mixer.music.play(1, 0, 0)
        time.sleep(1)

        if health <= 0:
            mixer.init()
            mixer.music.load("Dossier_tools/gorgonlaff.mp3")
            # module figlet, titre en ascii
            print("\n*\------------------------------------------------------------/*\n")
            print(f.renderText("LOOOOOSER !"))
            print("\n*/------------------------------------------------------------\*\n")
            # joue un mp3 lorsque la vie est a 0
            mixer.music.play(1, 0, 0)
            #mixer.get_init()
            time.sleep(8)
            exit()

        print(f"[italic red]Votre score est de {score} et votre santé est à {health}.[/italic red]")

        time.sleep(3)
        os.system("clear")


    save_player_answer[question_key] = user_answer
    return score, health

def save_logs(score, health):
    """
    :return: Création d'un fichier qui va contenir toutes les actions du joueur.
    :rtype: file
    """
    with open("game_log.txt", "a") as fichier:
        fichier.write(f"Score: {score}\n")
        fichier.write(f"Santé: {health}\n")
        for question_key, user_answer in save_player_answer.items():
            if questions_dictionnary[question_key]["good_response"] == questions_dictionnary[question_key]["propositions"][int(user_answer) - 1]:
                fichier.write(f"\n[/!\---Bonne réponse---/!\] --> {question_key} {questions_dictionnary[question_key]['good_response']}\n*\------------------------------/*")

            else:
                fichier.write(f"\n[/!\---Mauvaise réponse---/!\] --> {question_key} votre réponse : {questions_dictionnary[question_key]['propositions'][int(user_answer) - 1]} \nLa bonne réponse était: {questions_dictionnary[question_key]['good_response']}\n*\------------------------------/*\n")
