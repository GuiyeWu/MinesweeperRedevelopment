## @file Minesweeper.py
#  @author Guiye Wu, Shuying Chen, Ziyang Huang
#  @biref Minesweeper
#  @date 30/11/2018
import pygame
from pygame.locals import *

## @brief exception when given index is not in bounds
class InvalidIndex(Exception):
  pass

## @brief Set up the basic operations of the cell
class Cell:
    ## @brief initiate some variables
    #  @details initiate the variables that would be used through the entire class
    #  @param isbomb check if ther is bomb, and return the boolean value
    #  @param row the variable of row
    #  @param col the variable of column
    def __init__(self,isBomb, row, col):
        if row < 0 or col < 0:
            raise InvalidIndex
        self.unlocked = False
        self.flagged = False
        self.isB = isBomb
        self.r = row
        self.c = col
        self.nBN = 0
    ## @brief unlock number behavior
    #  @details when click on the cell, the matching picture should display base on the preset, from blank to eight.
    #  @param r row position
    #  @param c column position
    #  @param w width of the cell
    #  @param h height of the cell
    def unlock(self,screen,r,c,w,h):
        if r < 0 or c < 0 or w < 0 or h < 0:
            raise InvalidIndex
        self.unlocked = True
        if self.nBN == 0:
            num = pygame.image.load("pics/zero.png")
            num = pygame.transform.scale(num,(w,h))
            screen.blit(num,(c*w,r*h+50))
            pygame.display.flip()
        elif self.nBN == 1:
            num = pygame.image.load("pics/one.png")
            num = pygame.transform.scale(num,(w,h))
            screen.blit(num,(c*w,r*h+50))
            pygame.display.flip()
        elif self.nBN == 2:
            num = pygame.image.load("pics/two.png")
            num = pygame.transform.scale(num,(w,h))
            screen.blit(num,(c*w,r*h+50))
            pygame.display.flip()
        elif self.nBN == 3:
            num = pygame.image.load("pics/three.png")
            num = pygame.transform.scale(num,(w,h))
            screen.blit(num,(c*w,r*h+50))
            pygame.display.flip()
        elif self.nBN == 4:
            num = pygame.image.load("pics/four.png")
            num = pygame.transform.scale(num,(w,h))
            screen.blit(num,(c*w,r*h+50))
            pygame.display.flip()
        elif self.nBN == 5:
            num = pygame.image.load("pics/five.png")
            num = pygame.transform.scale(num,(w,h))
            screen.blit(num,(c*w,r*h+50))
            pygame.display.flip()
        elif self.nBN == 6:
            num = pygame.image.load("pics/six.png")
            num = pygame.transform.scale(num,(w,h))
            screen.blit(num,(c*w,r*h+50))
            pygame.display.flip()
        elif self.nBN == 7:
            num = pygame.image.load("pics/seven.png")
            num = pygame.transform.scale(num,(w,h))
            screen.blit(num,(c*w,r*h+50))
            pygame.display.flip()
        elif self.nBN == 8:
            num = pygame.image.load("pics/eight.png")
            num = pygame.transform.scale(num,(w,h))
            screen.blit(num,(c*w,r*h+50))
            pygame.display.flip()
    ## @brief set the setting flag behavior
    #  @details set the flag behavior and its picture when click on the flag
    #  @param r row position
    #  @param c column position
    #  @param w width of the cell
    #  @param h height of the cell
    def flag(self,screen,r,c,w,h):
        if r < 0 or c < 0 or w < 0 or h < 0:
            raise InvalidIndex
        self.flagged = True
        flg = pygame.image.load("pics/flag.jpg")
        flg =  pygame.transform.scale(flg,(w,h))
        screen.blit(flg,(c*w,r*h+50))
        pygame.display.flip()
    ## @brief set the setting unflag behavior
    #  @details set the unflag behavior and its picture when right-click on the flag
    #  @param r row position
    #  @param c column position
    #  @param w width of the cell
    #  @param h height of the cell
    def unflag(self,screen,r,c,w,h):
        if r < 0 or c < 0 or w < 0 or h < 0:
            raise InvalidIndex
        self.flagged = False
        blanckcell = pygame.image.load("pics/blankcell.jpg")
        blanckcell = pygame.transform.scale(blanckcell,(w,h))
        screen.blit(blanckcell,(c*w,r*h+50))
        pygame.display.flip()
    ## @brief set the clicking on bomb behavior
    #  @details set the clicking on bomb behavior and its picture when click on the cell
    #  @param r row position
    #  @param c column position
    #  @param w width of the cell
    #  @param h height of the cell
    def clickExplode(self,screen,r,c,w,h):
        if r < 0 or c < 0 or w < 0 or h < 0:
            raise InvalidIndex
        hitmine = pygame.image.load("pics/hitmine.jpg")
        hitmine = pygame.transform.scale(hitmine,(w,h))
        screen.blit(hitmine,(c*w,r*h+50))
        pygame.display.flip()
    ## @brief return a boolean value if this is bomb
    #  @details return a boolean value if this is bomb
    #  @return boolean value
    def isBomb(self):
        return self.isB
      
    ## @brief return a boolean value if unlocked
    #  @details return a boolean value if unlocked
    #  @return boolean value
    def isUnlocked(self):
        return self.unlocked
      
    ## @brief return a boolean value if isflagged
    #  @details return a boolean value if isflagged
    #  @return boolean value
    def isFlagged(self):
        return self.flagged

    ## @brief return the row value
    #  @details return the row value
    #  @return row value
    def getRow(self):
        return self.r
      
    ## @brief return the column value
    #  @details return the column value
    #  @return row value
    def getCol(self):
        return self.c
    ## @brief set the neighboring bombs
    #  @details set the neighboring bombs as the number matching to the cell.
    #  @param numBombNeighbors the number of the neighboring bombs
    def setNumBombNeighbors(self,numBombNeighbors):
        if numBombNeighbors < 0 or numBombNeighbors > 8:
            raise InvalidIndex
        self.nBN = numBombNeighbors
    ## @brief set the isunlocked variable to the self variable
    #  @details set the isunlocked variable to the self variable
    #  @param inUnlocked isUnlocked variable
    def setIsUnlocked(self,isUnlocked):
        self.unlocked = isUnlocked
    ## @brief get the number of neighboring bombs 
    #  @details get the number of neighboring bombs 
    #  @return number of neighboring bombs 
    def getNumBombNeighbors(self):
        return self.nBN


