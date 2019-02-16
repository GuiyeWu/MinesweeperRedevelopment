## @file Sound.py
#  @author Guiye Wu, Shuying Chen, Ziyang Huang
#  @brief sound
#  @date 30/11/208
import gtts
import pygame

## @brief An implementation of the sound class that load/play all the sounds from the local files
class sound:

    ## @brief the sound of leftclick
    #  @details import the sound of left click and play it.
    def lclick():
        pygame.mixer.music.load("music/leftclick.mp3")
        pygame.mixer.music.play()
    ## @brief the sound of click-the-bomb
    #  @details import the sound of left click if click on the bomb and play it.
    def cbomb():
        pygame.mixer.music.load("music/clickbomb.mp3")
        pygame.mixer.music.play()
    ## @brief the sound of rightclick
    #  @details import the sound of right click and play it.
    def rclick():
        pygame.mixer.music.load("music/rightclick.mp3")
        pygame.mixer.music.play()
    ## @brief the sound of winning
    #  @details import the sound of winning animation.
    def win():
        pygame.mixer.music.load("music/Victory.mp3")
        pygame.mixer.music.play()
    ## @brief the sound of losing
    #  @details import the sound of losing animation.
    def lose():
        pygame.mixer.music.load("music/Lose.mp3")
        pygame.mixer.music.play()
