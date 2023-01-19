import time, pygame
from pygame import mixer


start_string = """Hello soldier welcome to the black hole Game.
your spaceship was lost in space, to get back to earth you have to answer some questions.
At each level we'll give you a question to answer.
If you can't answer our question you'll lose points.
To start you'll be given 3 chances respresenting your life.
You have also some bonus points hidden in the levels.
You'll get them for each correct answer.
press P to Play
Press Q to Quit
Press H to get a hint
This game has 5 levels
Press S to Start"""

def game_start(start_string):
    mixer.init()
    mixer.music.load("Dossier_tools/typewriterSoundEffect.mp3")
    mixer.music.play(loops=2)
    
            
    for char in start_string:
        print(char, end="")
        time.sleep(0.07)
    
    mixer.music.stop()
        
print(game_start(start_string))