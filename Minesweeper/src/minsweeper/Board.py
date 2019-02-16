## @file Minesweeper.py
#  @author Guiye Wu, Shuying Chen, Ziyang Huang
#  @biref Minesweeper
#  @date 30/11/2018
import random
import pygame
from pygame.locals import *
from Cell import *
from timer import *
from sound import *

## @brief The settings and operations on the board
class Board:
    ## @brief initiate the board
    #  @details set up the size of the board, number of rows and colums, that split
    #  the cells in the board, and load each picture that need to be on the board. Then
    #  set the inital win/lose state to the board
    #  @param rows the number value of the row
    #  @param cols the number value of the column
    #  @param numBombs the number value of the bombs
    #  @param width the width of the cell
    #  @param height the height of the cell
    def __init__(self,rows,cols,numBombs,width,height):
        if rows < 0 or cols < 0 or width < 0 or height < 0:
            raise InvalidIndex
        self.rs = rows
        self.cs = cols
        self.w = width
        self.h = height
        self.nBs = numBombs
        self.numCells = rows*cols
        self.numCellsToUncover = 0
        self.cells=[]
        pygame.init()
        self.screen = pygame.display.set_mode((cols*width,rows*height+50),pygame.DOUBLEBUF)
        blanckcell = pygame.image.load("pics/blankcell.jpg")
        blanckcell = pygame.transform.scale(blanckcell,(width,height))
        for r in range(rows):
            for c in range(cols):
                self.screen.blit(blanckcell,(c*width,r*height+50))
        topPanel = pygame.image.load("pics/zero.png")
        topPanel = pygame.transform.scale(topPanel,(cols*width,50))
        self.screen.blit(topPanel,(0,0))
        smile = pygame.image.load("pics/reset.jpg")
        smile = pygame.transform.scale(smile,(50,50))
        self.screen.blit(smile,(cols*width/2-50/2,0))
        self.win = False
        self.loose = False
        pygame.display.flip()
        
    ## @brief refresh the cell
    #  @details refresh the cell to the matching presets while the cell is clicked.
    #  If the cell does not contain the bomb, the chain of neighboring cell will also
    #  to be refreshing, until there are bombs nearby.
    def refreshCells(self):
        self.numCellsToUncover = self.numCells - self.nBs
        List = []
        for i in range(self.numCells):
            List.append(i)
        random.shuffle(List)
        self.cells = []
        position = 0
        for i in range(self.rs):
            tempCells = []
            for j in range(self.cs):
                tempCells.append(Cell(List[position]<self.nBs,i,j))
                position+=1
            self.cells.append(tempCells)

        for i in range(self.rs):
            for j in range(self.cs):
                cell = self.cells[i][j]
                if (not cell.isBomb()):
                    cell.setNumBombNeighbors(self.getNumBombNeighbors(i,j))
    ## @brief get the number of neighboring bombs
    #  @details count the number of neighboring bombs from cell to cell
    #  @param i the current row number
    #  @param j the current cloumn number
    #  @return the value of the number of bombs
    def getNumBombNeighbors(self,i,j):
        if not (0 <= i and i <= self.rs) or not (0 <= j and j <= self.cs):
            raise InvalidIndex
        counter = 0
        startK = -1 if i > 0 else 0
        endK = 2 if i < self.rs-1 else 1
        startM = -1 if j > 0 else 0
        endM = 2 if j < self.cs-1 else 1

        for k in range(startK,endK):
            for m in range(startM,endM):
                centerBox = k==0 and m==0
                cell = self.cells[i+k][j+m]
                if (not centerBox and cell.isBomb()):
                    counter+=1
        return counter
    
    ## @brief set the behavior of right click
    #  @details set the behavior of the right click, if the cell is unflagged, then do the flag action. If
    #  the cell is currently flagged, then do the unflag action
    #  @param r row number of the cell
    #  @param c column number of the cell
    def rightClick(self,r,c):
        if not (0 <= r and r <= self.rs) or not (0 <= c and c <= self.cs):
            raise InvalidIndex
        sound.rclick()
        cell = self.cells[r][c]
        if not cell.isUnlocked():
            if cell.isFlagged():
                cell.unflag(self.screen,cell.getRow(),cell.getCol(),self.w,self.h)
                self.nBs += 1
            elif not cell.isFlagged():
                cell.flag(self.screen,cell.getRow(),cell.getCol(),self.w,self.h)
                self.nBs -= 1
                
    ## @brief set the behavior of left click
    #  @details set the behavior of the left click, if the cell is covered by the bomb, the game will end when
    #  the cell is clicked. If there is not a bomb, then the cell will refresh and to be uncover, and probably
    #  show the neighboring cells
    #  @param r row number of the cell
    #  @param c column number of the cell
    def leftClick(self,r,c):
        if not (0 <= r and r <= self.rs) or not (0 <= c and c <= self.cs):
            raise InvalidIndex
        sound.lclick()
        cell = self.cells[r][c]
        if not cell.isFlagged() and not cell.isUnlocked():
            if cell.isBomb():
                sound.cbomb()
                cell.clickExplode(self.screen,cell.getRow(),cell.getCol(),self.w,self.h)
                self.looseGame()
            else:
                nbn = cell.getNumBombNeighbors()
                if nbn == 0:
                    self.unlockNeighbors(cell)
                else:
                    cell.unlock(self.screen,cell.getRow(),cell.getCol(),self.w,self.h)
                self.numCellsToUncover -= 1
                if self.numCellsToUncover == 0:
                    self.winGame()

    ## @brief unlock the neighboring cells
    #  @details uncover the neighboring cells while there is not a bomb nearby.
    #  @param currentCell the current cell to be clicked
    def unlockNeighbors(self,currentCell):
        stack = []
        stack.append(currentCell)
        while not len(stack)==0:
            cell = stack.pop()
            row = cell.getRow()
            col = cell.getCol()
            cell.unlock(self.screen,row,col,self.w,self.h)
        
            # check all neighbors
            for i in range(-1,2):
                for j in range(-1,2):
                    if self.isCell(col+j,row+i) and (not i==0 or not j==0):
                        thisCell = self.cells[row+i][col+j]
                        if thisCell.isBomb() and not thisCell.isFlagged():
                            self.looseGame()
                        if not thisCell.isUnlocked() and not thisCell.isFlagged():
                            thisCell.unlock(self.screen,thisCell.getRow(),thisCell.getCol(),self.w,self.h)
                            self.numCellsToUncover -= 1
                            if thisCell.getNumBombNeighbors()==0 and not thisCell.isBomb():
                                stack.append(thisCell)
                                
    ## @brief return the row number and column number of the cell
    #  @details return the row number and column number of the cell
    #  @param row row number of the cell
    #  @param col column number of the cell
    def isCell(self,col,row):
        return row >= 0 and row < self.rs and col >= 0 and col < self.cs
    
    ## @brief set the behavior when right and left click
    #  @details if the correct number of bomb is correctly flagged, then the neighboring cells will automatically
    #  uncover when left and right click, otherwise the game will lose. When all the cells are uncovered, the
    #  game will turn into winning animation
    #  @param r row number of the cell
    #  @param c column number of the cell
    def rightAndLeftClick(self,r,c):
        if not (0 <= r and r <= self.rs) or not (0 <= c and c <= self.cs):
            raise InvalidIndex
        cell = self.cells[r][c]
        if self.getNumFlagNeighbors(r,c) == cell.getNumBombNeighbors():
            self.unlockNeighbors(cell)
            if self.numCellsToUncover == 0:
                self.winGame()
    ## @brief get the number of flagged neighbors
    #  @details record the numberof flagged neighbors and outpt the number
    #  @param i row number of the cell
    #  @param j column number of the cell
    #  @return the number of flagged neighbors
    def getNumFlagNeighbors(self,i,j):
        if not (0 <= i and i <= self.rs) or not (0 <= j and j <= self.cs):
            raise InvalidIndex
        counter = 0

        startK = -1 if i > 0 else 0
        endK = 2 if i < self.rs-1 else 1
        startM = -1 if j > 0 else 0
        endM = 2 if j < self.cs-1 else 1

        for k in range(startK,endK):
            for m in range(startM,endM):
                centerBox = k==0 and m==0
                cell = self.cells[i+k][j+m]
                if (not centerBox and cell.isFlagged()):
                    counter+=1
        return counter
    ## @brief depress the neighbors
    #  @details depress the blank neighbors
    #  @param i row number of the cell while if it is uncovered, the process will pass that certain cell.
    #  @param j column number of the cell
    def depressNeighbors(self,r,c):
        if not (0 <= r and r <= self.rs) or not (0 <= c and c <= self.cs):
            raise InvalidIndex
        for k in range(-1,2):
            for m in range(-1,2):
                if self.isCell(r+k,c+m) and (not k == 0 or not m == 0):
                    cell = self.cells[r+k][c+m]
                    if not cell.isUnlocked() and not cell.isFlagged():
                        pass
    ## @brief transfer the reset button to the smile face
    #  @details transfer the reset button to the smile face and play the winning sound
    def winGame(self):
        sound.win()
        smilewin = pygame.image.load("pics/smilewin.jpg")
        smilewin = pygame.transform.scale(smilewin,(50,50))
        self.screen.blit(smilewin,(self.cs*self.w/2-50/2,0))
        self.win = True
    ## @brief transfer the reset button to the lose face
    #  @details transfer the reset button to the lose face and play the lose sound
    def looseGame(self):
        sound.lose()
        looseface = pygame.image.load("pics/loseface.jpg")
        looseface = pygame.transform.scale(looseface,(50,50))
        self.screen.blit(looseface,(self.cs*self.w/2-50/2,0))
        self.loose = True
        
