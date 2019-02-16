## @file Minesweeper.py
#  @author Guiye Wu, Shuying Chen, Ziyang Huang
#  @biref Minesweeper
#  @date 30/11/2018
import pygame
from pygame.locals import *
from Animation import *
from Board import *
from timer import *
from MinesCounter import *
from sound import *

## @brief The play borad and setup of the minesweeper game.
class Minesweeper:
    ## @brief initiate the settings of the play borad
    #  @details initiate all the essential parts that should be displayed on the
    #  playing borad, including minescounter, timer, animation and the cells.
    #  Then preset the values of the length and width of the gaming screen, the
    #  playing board, and number of cells, number of bombs, in defferent levels,
    #  respectively. Then running the initial setup level screen, and manipulate
    #  that direct the user to choose different levels to play, by setting the
    #  size of the level selection block, position of the block and what will be
    #  the next step after click on the different levels, respectively.
    def __init__(self):
        self.MinesCounter = MinesCounter()
        self.Time = Timer()
        self.Animation = Animation()
        self.running  = True
        self.runningBackground = True
        self.ROWS = 16
        self.COLS = 30
        self.NUMBOMBS = 80
        self.WIDTH = 20
        self.HIGHT = 20
        self.ML = False
        self.MR = False
        widthx= 860
        heightx = 640
        x=0
        y=0
        pygame.init()
        pygame.display.set_caption("Press ESC to quit")
        width=140
        length=180
        screenx = pygame.display.set_mode((widthx,heightx))
        background = pygame.image.load("pics/minesweeperbackground.jpg")
        background = pygame.transform.scale(background,(widthx,heightx))
        setlevel = pygame.image.load("pics/level.jpg")
        setlevel = pygame.transform.scale(setlevel,(width,length))
        screenx.blit(background,(x,y))
        screenx.blit(setlevel,(360,380))
        pygame.display.flip()
        self.runningBackground = True
        while self.runningBackground:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.runningBackground = False
                    self.running = False
                elif event.type == KEYUP:
                    if event.key == K_ESCAPE:
                        self.runningBackground = False
                        self.running = False
                elif event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        rct = pygame.rect.Rect(pygame.mouse.get_pos(),(1,1))
                        beginnerblock = pygame.rect.Rect(360,380,width,length/4)
                        mediumblock = pygame.rect.Rect(360,380+length/4,width,length/4)
                        hardblock = pygame.rect.Rect(360,380+length/2,width,length/4)
                        nightmareblock = pygame.rect.Rect(360,380+3*length/4,width,length/4)
                        if rct.colliderect(beginnerblock):
                            sound.lclick()
                            self.ROWS = 16
                            self.COLS = 30
                            self.NUMBOMBS = 10
                            self.WIDTH = 20
                            self.HIGHT = 20
                            Minesweeper.on_init(self)
                            self.runningBackground = False
                        elif rct.colliderect(mediumblock):
                            sound.lclick()
                            self.ROWS = 16
                            self.COLS = 30
                            self.NUMBOMBS = 60
                            self.WIDTH = 20
                            self.HIGHT = 20
                            Minesweeper.on_init(self)
                            self.runningBackground = False
                        elif rct.colliderect(hardblock):
                            sound.lclick()
                            self.ROWS = 16
                            self.COLS = 30
                            self.NUMBOMBS = 99
                            self.WIDTH = 20
                            self.HIGHT = 20
                            Minesweeper.on_init(self)
                            self.runningBackground = False
                        elif rct.colliderect(nightmareblock):
                            sound.lclick()
                            self.ROWS = 16
                            self.COLS = 30
                            self.NUMBOMBS = 450
                            self.WIDTH = 20
                            self.HIGHT = 20
                            Minesweeper.on_init(self)
                            self.runningBackground = False
    ## @brief initiate the board
    #  @details initiate the game board and refresh the cells the the right manner.
    def on_init(self):
        pygame.init()
        pygame.display.set_caption("Press ESC to quit")
        self.board = Board(self.ROWS,self.COLS,self.NUMBOMBS,self.WIDTH,self.HIGHT)
        self.board.refreshCells()
    ## @brief the operations while the game is running
    #  @details when the game is not running, the screen is closed. When the board is running, the essential
    #  operations begin. There are three kinds of licks, left click, right click and left&right click.
    #  When left click, right click and the left&right click is inputted, the click collide with the block then the matching functions on board module is called,
    #  respectively. If the click is on the block, the sound animation will also compile.
    #  @param event the pygame event mode
    def on_event(self,event):
        if event.type == pygame.QUIT  or (event.type == KEYUP and event.key == K_ESCAPE):
            self.running = False
        elif event.type == MOUSEBUTTONDOWN:
            mouse_pressed = pygame.mouse.get_pressed()
            if (mouse_pressed[0] and mouse_pressed[2]) or mouse_pressed[1]:
                r = pygame.rect.Rect(pygame.mouse.get_pos(),(1,1))
                for i in range(self.ROWS):
                    for j in range(self.COLS):
                        rct = pygame.rect.Rect(j*self.WIDTH,i*self.HIGHT+50,self.WIDTH,self.HIGHT)
                        if rct.colliderect(r):
                            self.board.rightAndLeftClick(i,j)
            if event.button == 1:
                r = pygame.rect.Rect(pygame.mouse.get_pos(),(1,1))
                reset = pygame.rect.Rect(self.COLS*self.WIDTH/2-50/2,0,50,50)
                if reset.colliderect(r):
                    sound.lclick()
                    self.running = False
                    newMinesweeper = Minesweeper()
                    newMinesweeper.on_execute()
                else:
                    for i in range(self.ROWS):
                        for j in range(self.COLS):
                            rct = pygame.rect.Rect(j*self.WIDTH,i*self.HIGHT+50,self.WIDTH,self.HIGHT)
                            if rct.colliderect(r):
                                self.board.leftClick(i,j)
                                
            elif event.button == 3:
                r = pygame.rect.Rect(pygame.mouse.get_pos(),(1,1))
                for i in range(self.ROWS):
                    for j in range(self.COLS):
                        rct = pygame.rect.Rect(j*self.WIDTH,i*self.HIGHT+50,self.WIDTH,self.HIGHT)
                        if rct.colliderect(r):
                            self.board.rightClick(i,j)
    ## @brief Clean up the game
    #  @details quit the gameboard while it is called.
    def on_cleanup(self):
        pygame.quit()
    ## @brief Operations while playing
    #  @details after the initation the game is running. The different board shows up based on different
    #  situations. When winning, the board display the winning animation. When lose, the board display the
    #  lose animation and while running, the board should display the timer and running the event function.
    def on_execute(self):
        if self.on_init() == False:
            self.running = False
        
        while(self.running):
            if self.board.win:
                self.Animation.win(self.board.screen)
            elif self.board.loose:
                self.Animation.loose(self.board.screen)
            else:
                self.Time.show_time(self.board.screen)
                self.MinesCounter.show_counter(self.board.screen,self.board.nBs)
            pygame.display.flip()
            for event in pygame.event.get():
                self.on_event(event)

        self.on_cleanup()


theMinesweeper = Minesweeper()
theMinesweeper.on_execute()
