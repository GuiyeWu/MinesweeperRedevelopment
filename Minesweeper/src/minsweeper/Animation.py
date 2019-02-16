## @file Animation.py
#  @author Guiye Wu, Shuying Chen, Ziyang Huang
#  @brief Animation
#  @date 30/11/2018
import pygame
import random
from sound import *

## @brief An set up for the win/lose animation
class Animation:
    ## @brief animation constructor
    #  @details setup the background pictures, the dynamic animation pictures,
    #  transfer them into proper size, with win/lose, respectively. Then assign
    #  the win/lose animation pictures randomly among the blocks of the boad.
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Winning Animation")
        self.rainloose = pygame.image.load("pics/loseanimation.jpg")
        self.rainloose = pygame.transform.scale(self.rainloose,(30,30))
        self.rainwin = pygame.image.load("pics/winningannimation.jpg")
        self.rainwin = pygame.transform.scale(self.rainwin,(40,40))
        self.backgroundwin = pygame.image.load("pics/win.jpg")
        self.backgroundwin = pygame.transform.scale(self.backgroundwin,(600,320))
        self.backgroundloose = pygame.image.load("pics/Gameover.jpg")
        self.backgroundloose = pygame.transform.scale(self.backgroundloose,(600,320))
        self.rain_list = []
        for i in range(100):
            x = random.randrange(0, 600)
            y = random.randrange(50, 320)
            self.rain_list.append([x, y])
     
        self.clock = pygame.time.Clock()
    ## @brief win animation setup
    #  @details randomly appen the number of the animation pictures into the board,
    #  then make the rain animation
    #  @param screen assign the winning animation to the screen on which it is needed
    def win(self,screen):
        screen.blit(self.backgroundwin,(0,50))
        for item in self.rain_list:
            item[1] += 2
            screen.blit(self.rainwin,item)
            if item[1] > 370:
                item[1] = 50
                item[0] = random.randrange(0, 600)
    
        pygame.display.flip()
        self.clock.tick(20)
    ## @brief lose animation setup
    #  @details randomly appen the number of the animation pictures into the board,
    #  then make the rain animation
    #  @param screen assign the lose animation to the screen on which it is needed
    def loose(self,screen):
        screen.blit(self.backgroundloose,(0,50))
        for item in self.rain_list:
            item[1] += 2
            screen.blit(self.rainloose,item)
            if item[1] > 370:
                item[1] = 50
                item[0] = random.randrange(0, 600)
        
        pygame.display.flip()
        self.clock.tick(20)
