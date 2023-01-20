import random
import time
import os
from game_start import game_start, start_string
from functions_questions_and_logs import question_launcher, save_logs, questions_dictionnary
from initiate_game import loading_game
from loading_main_system import loading_main_question

from pyfiglet import Figlet
from pygame import mixer


mon_score = 0
ma_health = 50
line = "\n*\---------------------------------------------------------------/*\n"

os.system("clear")
loading_game()
game_start(start_string)
time.sleep(1)
os.system("clear")
loading_main_question()


while True:
    f = Figlet(font="slant")
    print(f.renderText("BLACK HOLE"))

    mixer.init()
    mixer.music.load("Dossier_tools/power-down-7103.mp3")
    mixer.music.play(1, 0, 0)

    for characters in line:
        print(characters, end=" ")
        time.sleep(0.03)

    mon_score, ma_health = question_launcher(random.choice(list(questions_dictionnary.keys())), mon_score, ma_health)

    save_logs(mon_score, ma_health)