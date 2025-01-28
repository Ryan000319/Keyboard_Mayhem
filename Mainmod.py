import pygame

from pygame.locals import *
import highscoremod
import playbuttonmod
pygame.init()

#screen resolution
display_width=1280
display_height=720

#background
background2_image=pygame.image.load("BACKGROUND2.jpg")

#music

 

#colours
black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
bright_black=(40,40,40)


gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Keyboard Mayhem.exe')
clock=pygame.time.Clock()

#Main menu
titleImage=pygame.image.load('KEYBOARD-MAYHEM.png')
playImage=pygame.image.load('PLAY.png')
scoreImage=pygame.image.load('SCORE.png')
highscoreImage=pygame.image.load('HIGHSCORE.png')
backimage=pygame.image.load('BACK.png')
menuinstrucimage=pygame.image.load('MENUGAMEINSTRUCTIONS.png')

def title(x,y):

    gameDisplay.blit(titleImage,(x,y))

x=(display_width*0.090)
y=(display_height*0.10)



def play(a,b):
    gameDisplay.blit(playImage,(a,b,))

a=(display_width*0.38)
b=(display_height*0.39)

def score(c,d):
    gameDisplay.blit(scoreImage,(c,d))


c=(display_width*0.35)
d=(display_height*0.555)




def button(x,y,w,h,ac,action=None): 
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x+w>mouse[0]>x and y+h>mouse[1]>y:
        pygame.draw.rect(gameDisplay,ac,(x,y,w,h))
        if click[0]==1 and action =="score":
            highscoremod.highscore()
    
        if click[0]==1 and action =="play":
            playbuttonmod.gameinstructions()

        
            
            
                

def mainmenu():
    pygame.mixer.music.load("menu_music2.mp3")
    pygame.mixer.music.play(-1,0.0)
    dead=False
    while not dead:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
    
        
        
        gameDisplay.blit(background2_image,[0,0])
        title(x,y)
        button(470,270,325,110,bright_black,"play")
        button(435,390,390,110,bright_black,"score")
    
        play(a,b)
        score(c,d)
        
##        print(event)
        pygame.display.update()
        clock.tick(60)
   

                



