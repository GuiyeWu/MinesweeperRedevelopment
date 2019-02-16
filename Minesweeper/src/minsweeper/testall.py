## @file Minesweeper.py
#  @author Guiye Wu, Shuying Chen, Ziyang Huang
#  @biref Minesweeper
#  @date 30/11/2018
import unittest
import pygame
from pygame.locals import *
from Cell import *
from Board import *

## @brief The unite test for the automating test of the functions in cell module
class CellTest(unittest.TestCase):
    ## @brief set up the unittest
    def setUp(self):
        row = 0
        col = 0
        row1 = 1
        col1 = 1
        row20 = 20
        col20 = 20
        self.screen = pygame.display.set_mode((8,6),pygame.DOUBLEBUF)
        self.cell0 = Cell(True,row,col)
        self.cell1 = Cell(True,row1,col20)
        self.cell2 = Cell(False,row1,col1)
        self.cell3 = Cell(False,row20,col20)
        
    ## @brief test the unlock function
    def testUnlock(self):
        with self.assertRaises(InvalidIndex):
            self.cell0.unlock(self.screen,-1,0,20,20)
        with self.assertRaises(InvalidIndex):
            self.cell0.unlock(self.screen,1,-1,20,20)
        with self.assertRaises(InvalidIndex):
            self.cell0.unlock(self.screen,1,1,-10,20)
        with self.assertRaises(InvalidIndex):
            self.cell0.unlock(self.screen,1,1,20,-20)
        self.cell1.unlock(self.screen,1,1,20,20)
        self.assertEqual(self.cell1.unlocked,True,"cell1 unlocked is set to be True")
        self.assertEqual(self.cell2.unlocked,False,"cell2 unlocked isnot set to be True")
        pygame.quit()
        
    ## @brief test the flagging function
    def testFlag(self):
        with self.assertRaises(InvalidIndex):
            self.cell0.flag(self.screen,-1,0,20,20)
        with self.assertRaises(InvalidIndex):
            self.cell0.flag(self.screen,1,-1,20,20)
        with self.assertRaises(InvalidIndex):
            self.cell0.flag(self.screen,1,1,-10,20)
        with self.assertRaises(InvalidIndex):
            self.cell0.flag(self.screen,1,1,20,-20)
        self.cell1.flag(self.screen,1,1,20,20)
        self.assertEqual(self.cell1.flagged,True,"cell1 flag is set to be True")
        self.assertEqual(self.cell3.flagged,False,"cell3 flag isnot set to be True")
        #pygame.quit()
        
    ## @brief test the un-flagging function
    def testUnflag(self):
        with self.assertRaises(InvalidIndex):
            self.cell0.unflag(self.screen,-1,0,20,20)
        with self.assertRaises(InvalidIndex):
            self.cell0.unflag(self.screen,1,-1,20,20)
        with self.assertRaises(InvalidIndex):
            self.cell0.unflag(self.screen,1,1,-10,20)
        with self.assertRaises(InvalidIndex):
            self.cell0.unflag(self.screen,1,1,20,-20)
        self.cell2.unflag(self.screen,1,1,20,20)
        self.cell1.flag(self.screen,1,1,20,20)
        self.assertEqual(self.cell2.flagged,False,"cell2 flag is set to be False")
        self.assertEqual(self.cell3.flagged,False,"cell3 flag isnot set to be True")
        self.assertEqual(self.cell1.flagged,True,"cell3 flag isnot set to be False")
        #pygame.quit()
    ## @brief test the click to explode function
    def testClickExplode(self):
        with self.assertRaises(InvalidIndex):
            self.cell0.clickExplode(self.screen,-1,0,20,20)
        with self.assertRaises(InvalidIndex):
            self.cell0.clickExplode(self.screen,1,-1,20,20)
        with self.assertRaises(InvalidIndex):
            self.cell0.clickExplode(self.screen,1,1,-10,20)
        with self.assertRaises(InvalidIndex):
            self.cell0.clickExplode(self.screen,1,1,20,-20)
        #pygame.quit()
    ## @brief test the isbomb function
    def testIsBomb(self):
        self.assertEqual(self.cell0.isBomb(),True,"cell0 has bomb")
        self.assertEqual(self.cell1.isBomb(),True,"cell1 has bomb")
        self.assertEqual(self.cell2.isBomb(),False,"cell2 has no bomb")
        self.assertEqual(self.cell3.isBomb(),False,"cell3 has no bomb")
        #pygame.quit()
    ## @brief test the isunlock function
    def testIsUnlocked(self):
        self.assertEqual(self.cell0.isUnlocked(),False,"cell0 is locked")
        self.assertEqual(self.cell1.isUnlocked(),False,"cell1 is locked")
        self.assertEqual(self.cell2.isUnlocked(),False,"cell2 is locked")
        self.assertEqual(self.cell3.isUnlocked(),False,"cell3 is locked")
        self.cell1.unlock(self.screen,1,1,20,20)
        self.assertEqual(self.cell1.isUnlocked(),True,"cell1 unlocked is set to be True")
        self.cell2.unlock(self.screen,1,1,20,20)
        self.assertEqual(self.cell2.isUnlocked(),True,"cell2 unlocked is set to be True")
    ## @brief test the isflagged function
    def testIsFlagged(self):
        self.assertEqual(self.cell0.isFlagged(),False,"cell0 is not flagged")
        self.assertEqual(self.cell1.isFlagged(),False,"cell1 is not flagged")
        self.assertEqual(self.cell2.isFlagged(),False,"cell2 is not flagged")
        self.assertEqual(self.cell3.isFlagged(),False,"cell3 is not flagged")
        self.cell1.flag(self.screen,1,1,20,20)
        self.assertEqual(self.cell1.isFlagged(),True,"cell1 is flagged")
        self.cell2.flag(self.screen,1,1,20,20)
        self.assertEqual(self.cell2.isFlagged(),True,"cell2 is flagged")
    ## @brief test the getrow function
    def testGetRow(self):
        self.assertEqual(self.cell0.getRow(),0,"cell0 is at row 0")
        self.assertEqual(self.cell1.getRow(),1,"cell1 is at row 1")
        self.assertEqual(self.cell2.getRow(),1,"cell2 is at row 1")
        self.assertEqual(self.cell3.getRow(),20,"cell3 is at row 20")
    ## @brief test the getcolumn function
    def testGetCol(self):
        self.assertEqual(self.cell0.getCol(),0,"cell0 is at column 0")
        self.assertEqual(self.cell1.getCol(),20,"cell1 is at column 20")
        self.assertEqual(self.cell2.getCol(),1,"cell2 is at column 1")
        self.assertEqual(self.cell3.getCol(),20,"cell3 is at column 20")
    ## @brief test the setnumbombneighbors function
    def testSetNumBombNeighbors(self):
        with self.assertRaises(InvalidIndex):
            self.cell0.setNumBombNeighbors(-1)
        with self.assertRaises(InvalidIndex):
            self.cell0.setNumBombNeighbors(9)
        with self.assertRaises(InvalidIndex):
            self.cell0.setNumBombNeighbors(10000)
        with self.assertRaises(InvalidIndex):
            self.cell0.setNumBombNeighbors(-10000)
        self.cell2.setNumBombNeighbors(0)
        self.cell1.setNumBombNeighbors(8)
        self.cell0.setNumBombNeighbors(6)
        self.cell3.setNumBombNeighbors(3)
        self.assertEqual(self.cell2.nBN,0,"cell2 has neightbor bomb number 0")
        self.assertEqual(self.cell1.nBN,8,"cell1 has neightbor bomb number 8")
        self.assertEqual(self.cell0.nBN,6,"cell0 has neightbor bomb number 6")
        self.assertEqual(self.cell3.nBN,3,"cell3 has neightbor bomb number 3")
    ## @brief test the setisunlocked function
    def testSetIsUnlocked(self):
        self.assertEqual(self.cell0.unlocked,False,"cell0 is not locked")
        self.assertEqual(self.cell1.unlocked,False,"cell1 is not locked")
        self.assertEqual(self.cell2.unlocked,False,"cell2 is not locked")
        self.assertEqual(self.cell3.unlocked,False,"cell3 is not locked")
        self.cell1.setIsUnlocked(True)
        self.assertEqual(self.cell1.unlocked,True,"cell1 unlocked is set to be True")
        self.cell3.setIsUnlocked(True)
        self.assertEqual(self.cell3.unlocked,True,"cell3 unlocked is set to be True")
    ## @brief test the getnumbombneighbors function
    def testGetNumBombNeighbors(self):
        self.assertEqual(self.cell0.getNumBombNeighbors(),0,"cell0 has neightbor bomb number 0")
        self.assertEqual(self.cell1.getNumBombNeighbors(),0,"cell1 has neightbor bomb number 0")
        self.assertEqual(self.cell2.getNumBombNeighbors(),0,"cell2 has neightbor bomb number 0")
        self.assertEqual(self.cell3.getNumBombNeighbors(),0,"cell3 has neightbor bomb number 0")
        self.cell1.setNumBombNeighbors(3)
        self.assertEqual(self.cell1.getNumBombNeighbors(),3,"cell1 has neightbor bomb number 3")
        self.cell3.setNumBombNeighbors(6)
        self.assertEqual(self.cell3.getNumBombNeighbors(),6,"cell3 has neightbor bomb number 6")
## @brief test the functions in board module
class BoardTest(unittest.TestCase):
    ## @brief set up the test variables
    def setUp(self):
        self.rows = 16
        self.cols = 30
        self.numBombs = 88
        self.width = 20
        self.height = 20
        
    ## @brief initiate the test with exceptions
    def testInit(self):
        with self.assertRaises(InvalidIndex):
            Board(-1,self.cols,self.numBombs,self.width,self.height)
        with self.assertRaises(InvalidIndex):
            Board(self.rows,-100,self.numBombs,self.width,self.height)
        with self.assertRaises(InvalidIndex):
            Board(self.rows,self.cols,self.numBombs,-1000,self.height)
        with self.assertRaises(InvalidIndex):
            Board(self.rows,self.cols,self.numBombs,self.width,-10000)
    ## @brief test the refeshcell function
    def testRefreshCells(self):
        board = Board(self.rows,self.cols,self.numBombs,self.width,self.height)
        self.assertEqual(board.numCellsToUncover,0,"initial value cells")
        board.refreshCells()
        self.assertEqual(board.numCellsToUncover,16*30-88,"all value cells")
    ## @brief test the getnumbombneighbors function
    def testGetNumBombNeighbors(self):
        board = Board(self.rows,self.cols,self.numBombs,self.width,self.height)
        with self.assertRaises(InvalidIndex):
            board.getNumBombNeighbors(-1,30)
        with self.assertRaises(InvalidIndex):
            board.getNumBombNeighbors(16,-1)
        with self.assertRaises(InvalidIndex):
            board.getNumBombNeighbors(17,30)
        with self.assertRaises(InvalidIndex):
            board.getNumBombNeighbors(16,31)
    ## @brief test the rightclick function
    def testRightClick(self):
        board = Board(self.rows,self.cols,self.numBombs,self.width,self.height)
        with self.assertRaises(InvalidIndex):
            board.rightClick(-1,30)
        with self.assertRaises(InvalidIndex):
            board.rightClick(16,-1)
        with self.assertRaises(InvalidIndex):
            board.rightClick(17,30)
        with self.assertRaises(InvalidIndex):
            board.rightClick(16,31)
    ## @brief test the leftclick function
    def testLeftClick(self):
        board = Board(self.rows,self.cols,self.numBombs,self.width,self.height)
        with self.assertRaises(InvalidIndex):
            board.leftClick(-1,30)
        with self.assertRaises(InvalidIndex):
            board.leftClick(16,-1)
        with self.assertRaises(InvalidIndex):
            board.leftClick(17,30)
        with self.assertRaises(InvalidIndex):
            board.leftClick(16,31)
    ## @brief test the iscell function
    def testIsCell(self):
        board = Board(self.rows,self.cols,self.numBombs,self.width,self.height)
        self.assertEqual(board.isCell(-1,30),False,"Check if it is a cell")
        self.assertEqual(board.isCell(16,-1),False,"Check if it is a cell")
        self.assertEqual(board.isCell(17,30),False,"Check if it is a cell")
        self.assertEqual(board.isCell(16,31),False,"Check if it is a cell")
        self.assertEqual(board.isCell(29,0),True,"Check if it is a cell")
        self.assertEqual(board.isCell(0,0),True,"Check if it is a cell")
        self.assertEqual(board.isCell(15,8),True,"Check if it is a cell")
        self.assertEqual(board.isCell(29,15),True,"Check if it is a cell")
    ## @brief test the rightandleftclick function
    def testRightAndLeftClick(self):
        board = Board(self.rows,self.cols,self.numBombs,self.width,self.height)
        with self.assertRaises(InvalidIndex):
            board.rightAndLeftClick(-1,30)
        with self.assertRaises(InvalidIndex):
            board.rightAndLeftClick(16,-1)
        with self.assertRaises(InvalidIndex):
            board.rightAndLeftClick(17,30)
        with self.assertRaises(InvalidIndex):
            board.rightAndLeftClick(16,31)
    ## @brief test the getnumflagneighbors function
    def testGetNumFlagNeighbors(self):
        board = Board(self.rows,self.cols,self.numBombs,self.width,self.height)
        with self.assertRaises(InvalidIndex):
            board.getNumFlagNeighbors(-1,30)
        with self.assertRaises(InvalidIndex):
            board.getNumFlagNeighbors(16,-1)
        with self.assertRaises(InvalidIndex):
            board.getNumFlagNeighbors(17,30)
        with self.assertRaises(InvalidIndex):
            board.getNumFlagNeighbors(16,31)
    ## @brief test the depressneighbors function
    def testDepressNeighbors(self):
        board = Board(self.rows,self.cols,self.numBombs,self.width,self.height)
        with self.assertRaises(InvalidIndex):
            board.depressNeighbors(-1,30)
        with self.assertRaises(InvalidIndex):
            board.depressNeighbors(16,-1)
        with self.assertRaises(InvalidIndex):
            board.depressNeighbors(17,30)
        with self.assertRaises(InvalidIndex):
            board.depressNeighbors(16,31)
    ## @brief test the wingame function
    def testWinGame(self):
        board = Board(self.rows,self.cols,self.numBombs,self.width,self.height)
        self.assertEqual(board.win,False,"Winning is not reached")
        board.winGame()
        self.assertEqual(board.win,True,"Winning is reached")
    ## @brief test the losegame function
    def testLooseGame(self):
        board = Board(self.rows,self.cols,self.numBombs,self.width,self.height)
        self.assertEqual(board.loose,False,"Losing is not reached")
        board.looseGame()
        self.assertEqual(board.loose,True,"Losing is reached")

if __name__ == '__main__':
    unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAll)
    suite.run()

