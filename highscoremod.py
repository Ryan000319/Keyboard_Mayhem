import pygame
import playbuttonmod

import sys

pygame.init()

highscoreImage=pygame.image.load('HIGHSCORE.png')
backimage=pygame.image.load('BACK.png')
background2=pygame.image.load('BACKGROUND3.jpg')
deathscreenback=pygame.image.load("DEATHSCREEN.jpg")
gameinsline1=pygame.image.load("GAME-INSTRUCTIONS.png")
gameinsline2=pygame.image.load("LINE2.png")
gameinsline3=pygame.image.load("LINE3.png")
gameinsline4=pygame.image.load("LINE4.png")
gameinsline5=pygame.image.load("LINE5.png")
gameinsbackImage=pygame.image.load("BACKGROUNDGAME.jpg")
gameinsImage=pygame.image.load("WELCOME.png")
gameinsplayImage=pygame.image.load("SPACETOPLAY.png")
deathline1=pygame.image.load("YOUHAVEDIED.png")
deathline2=pygame.image.load("PRESSSPACETOCONTINUE2.png")
savegamebackimage=pygame.image.load("DEATHSCREEN.jpg")
savegameinsimage=pygame.image.load("WOULDYOULIKETO.png")
savegameinsimage2=pygame.image.load("SAVEYOURSCORE.png")
Yesimage=pygame.image.load("YES.png")
Noimage=pygame.image.load("NO.png")
savebackground=pygame.image.load("BACKGROUND.jpg")
typename=pygame.image.load("PLEASETYPEYOURNAME.png")
pressspacetocontinue=pygame.image.load("PRESSSPACETOCONTINUE.png")



x2=0    

## life system
display_width=1280
display_height=720
gameDisplay=pygame.display.set_mode((display_width,display_height))
black=(0,0,0)
white=(255,255,255)

bright_black=(40,40,40)

heart=pygame.image.load('Heart.png')
hearts=pygame.transform.scale(heart,(30,23))
lives=3
lifewidth=1180
lifeheight=15
a=100

alive=True



       
def Life(gameDisplay,lifewidth,lifeheight,hearts,lives):

    for i in range (lives):
        hearts_rect= hearts.get_rect()
        hearts_rect.x=lifewidth+30*i
        hearts_rect.y=lifeheight
        gameDisplay.blit(hearts,hearts_rect)
       
    pygame.display.update()

def highscore():
    display_width=1280
    display_height=720
    gameDisplay=pygame.display.set_mode((display_width,display_height))
    
    
    scoretab = False

    while not scoretab:
        displayname()
        continue
       
        

def deathscreen1(time):

    
    display_width=1280
    display_height=720
    gameDisplay=pygame.display.set_mode((display_width,display_height))
    
    pygame.mixer.music.load("death_music.mp3")
    pygame.mixer.music.play(-1,0)

    i=(display_width*0.17)
    j=(display_height*0.05)

    k=(display_width*0.13)
    l=(display_height*0.85)

    

    
    deathscreen=False

    while not deathscreen:
        
        for event5 in pygame.event.get():
            gameDisplay.blit(deathscreenback,[0,0])
            gameDisplay.blit(deathline1,(i,j))
            gameDisplay.blit(deathline2,(k,l))

            if event5.type==pygame.KEYDOWN:
                if event5.key==pygame.K_SPACE:
                    savename(time)
                    continue
##        print(event5)
            pygame.display.update()


def savename(time):
    screen = pygame.display.set_mode((1280,720))
    font = pygame.font.Font(None, 100)
    clock = pygame.time.Clock()
    input_box = pygame.Rect(535, 300, 500, 100)
    color_inactive = pygame.Color('goldenrod1')
    color_active = pygame.Color('black')
    color = color_inactive
    active = False
    text = ''
    done = False

    while not done:
        for event in pygame.event.get():
            screen.blit(savebackground,[0,0])
            screen.blit(typename,(30,100))
            screen.blit(pressspacetocontinue,(180,600))
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        writescoretofile(time)
                        writetofile(text)
                        
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

##        screen.fill((30, 30, 30))
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pygame.draw.rect(screen, color, input_box, 2)

        pygame.display.flip()
        clock.tick(60)


def writetofile(text):
    
    text2=[text]
    f=open("highscore.txt","a")
    for i in text2:
       f.write(i+"\n")
    f.close()
    import Mainmod
    Mainmod.mainmenu()


def writescoretofile(time):
    time2=[time]
    with open("score.txt","a") as f:
        for i in time2:
            f.write(i+"\n")

def displayname():
    
    running=True

    while running:
        for event2 in pygame.event.get():
            pos=pygame.mouse.get_pos()
            gameDisplay.blit(background2,[0,0])       
            e=(display_width*0.25)
            f=(display_height*0.05)
            g=(display_width*0.30)
            h=(display_height*0.90)
            gameDisplay.blit(highscoreImage,(e,f))
            gameDisplay.blit(backimage,(g,h))
            displayname2()
            displayscore()
        
            if event2.type==pygame.KEYDOWN:
                if event2.key==pygame.K_SPACE:
                    import Mainmod
                    Mainmod.mainmenu()

            print(event2)
            pygame.display.update()


def displayname2():
    
    with open ("highscore.txt","r") as highscore:
        for n,line in enumerate(highscore.readlines()[-10:]):
            line=line.strip()
            
            BLACK=(0,0,0)
            
            font=pygame.font.Font(None,50)
        
            text = font.render(line, 1, BLACK)

            text_rect = text.get_rect()

            text_rect.centerx = 425
        

            text_rect.centery = n*50 + 155

            gameDisplay.blit(text, text_rect)

def displayscore():
     with open("score.txt","r") as timescore:
         for n,line in enumerate(timescore.readlines()[-10:]):
             line=line.strip()
             
             BLACK=(0,0,0)
             
             font=pygame.font.Font(None,50)

             text=font.render(line,1,BLACK)

             text_rect=text.get_rect()

             text_rect.centerx=825

             text_rect.centery=n*50 + 155

             gameDisplay.blit(text, text_rect)





        
        


