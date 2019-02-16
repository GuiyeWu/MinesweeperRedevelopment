## @file timer.py
#  @author Guiye Wu, Shuying Chen, Ziyang Huang
#  @brief Timer
#  @date 30/11/2018
import pygame
from pygame.locals import *

## @brief The construction of the timer
class Timer:
    ## @brief initiate the timer/preset values
    #  @details initiate the preset color, the clock and some preset values
    def __init__(self):
        self.white = (255, 255, 255)
        self.clock = pygame.time.Clock()
        self.count = 0
        self.rate = 60
        self.total_seconds = 0
        self.BLUE = (0, 0, 255)
        self.minutes = 0
        self.seconds = 0
    ## @brief make the timer present on the screen
    #  @details set up the position of where the timer should be located in,
    #  the format of the timer display, the text color and sytle and the minute/
    #  second and the rate.
    #  @param screen the screen which need the timer to be insert in
    def show_time(self,screen):
        r = Rect(440,15,115,25)
        screen.fill(self.white,r)
        font = pygame.font.Font(None, 25)
        output_string = "Time: {0:02}:{1:02}".format(self.minutes, self.seconds)
        text = font.render(output_string, True, self.BLUE)
        screen.blit(text, [450, 20])
        self.total_seconds = self.count // self.rate
        self.minutes = self.total_seconds // 60
        self.seconds = self.total_seconds % 60
        self.count += 1
        self.clock.tick(self.rate)
        pygame.display.flip()

            
