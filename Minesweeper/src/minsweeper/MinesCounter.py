## @file MinesCounter.py
#  @author Guiye Wu, Shuying Chen, Ziyang Huang
#  @brief remaining mines number counter
#  @date 30/11/208
import pygame
from pygame.locals import *

## @brief A class that defines the mines counter
class MinesCounter:
    ## @brief initaite the counter color
    #  @details initialte the color, white and blue, for the use of shows.
    def __init__(self):
        self.white = (255,255,255)
        self.BLUE = (0,0,255)
    ## @brief set up the counter
    #  @details set the position of the counter, and fill with the initiate color
    #   then set the size of the edge and display it on the board
    #  @param screen the screen the needs the counter to be insert in
    #  @param mines the total number of mines of a specific level that should be
    #   shown as the beginning of the game, on the counter.
    def show_counter(self,screen,mines):
        r = Rect(50,15,100,25)
        screen.fill(self.white,r)
        font = pygame.font.Font(None, 25)
        output_string = "Mines: {0:02}".format(mines)
        text = font.render(output_string, True, self.BLUE)
        screen.blit(text, [60, 20])
        pygame.display.flip()
