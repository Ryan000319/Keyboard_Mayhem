import pygame
import string
import random
import highscoremod


pygame.init()


display_width=1280
display_height=720

gameDisplay=pygame.display.set_mode((display_width,display_height))

deathscreenback=pygame.image.load("DEATHSCREEN.jpg")

x=random.choice(string.ascii_letters)
x2=0

##lifesystem
heart=pygame.image.load('Heart.png')
hearts=pygame.transform.scale(heart,(30,23))
lives=3
lifewidth=1180
lifeheight=15
a=190
counter=5
num_correct=5
i=0
##alive=True




gameinsImage=pygame.image.load("WELCOME.png")
gameinsbackImage=pygame.image.load("BACKGROUNDGAME.jpg")
gameinsplayImage=pygame.image.load("SPACETOPLAY.png")
gameinsline1=pygame.image.load("GAME-INSTRUCTIONS.png")
gameinsline2=pygame.image.load("LINE2.png")
gameinsline3=pygame.image.load("LINE3.png")
gameinsline4=pygame.image.load("LINE4.png")
gameinsline5=pygame.image.load("LINE5.png")
gameinsline6=pygame.image.load("LINE6.png")
gameinsline7=pygame.image.load("LINE7.png")
gameinsA=pygame.image.load("A.png")
gameinsB=pygame.image.load("B.png")
gameinsC=pygame.image.load("C.png")
gameinsD=pygame.image.load("D.png")
gameinsE=pygame.image.load("E.png")
gameinsF=pygame.image.load("F.png")
gameinsG=pygame.image.load("G.png")
gameinsH=pygame.image.load("H.png")
gameinsI=pygame.image.load("I.png")
gameinsJ=pygame.image.load("J.png")
gameinsK=pygame.image.load("K.png")
gameinsL=pygame.image.load("L.png")
gameinsM=pygame.image.load("M.png")
gameinsN=pygame.image.load("N.png")
gameinsO=pygame.image.load("O.png")
gameinsP=pygame.image.load("P.png")
gameinsQ=pygame.image.load("Q.png")
gameinsR=pygame.image.load("R.png")
gameinsS=pygame.image.load("S.png")
gameinsT=pygame.image.load("T.png")
gameinsU=pygame.image.load("U.png")
gameinsV=pygame.image.load("V.png")
gameinsW=pygame.image.load("W.png")
gameinsX=pygame.image.load("X.png")
gameinsY=pygame.image.load("Y.png")
gameinsZ=pygame.image.load("Z.png")


def gameinstructions():
    global x
##    pygame.mixer.music.load("menu_music2.mp3")
##    pygame.mixer.music.play(-1,0.0)
    
    display_width=1280
    display_height=720
    gameDisplay=pygame.display.set_mode((display_width,display_height))
##    pygame.mixer.music.load("menu_music2.mp3")
##    pygame.mixer.music.play(-1,0.0)

    
   
    

    gameinstab=False

    while not gameinstab:          
        for event3 in pygame.event.get():
    
            gameDisplay.blit(gameinsbackImage,[0,0])
            i=(display_width*0.080)
            j=(display_height*0.05)
            
            k=(display_width*0.33)
            l=(display_height*0.90)
            
            m=(display_width*0.080)
            n=(display_height*0.25)

            o=(display_width*0.080)
            p=(display_height*0.30)

            q=(display_width*0.080)
            r=(display_height*0.35)

            s=(display_width*0.080)
            t=(display_height*0.60)

            v=(display_width*0.080)
            w=(display_height*0.65)

            v2=(display_width*0.080)
            w2=(display_height*0.70)

            v3=(display_width*0.080)
            w3=(display_height*0.75)

            
            
            gameDisplay.blit(gameinsImage,(i,j))
            gameDisplay.blit(gameinsplayImage,(k,l))
            gameDisplay.blit(gameinsline1,(m,n))
            gameDisplay.blit(gameinsline2,(o,p))
            gameDisplay.blit(gameinsline3,(q,r))
            gameDisplay.blit(gameinsline4,(s,t))
            gameDisplay.blit(gameinsline5,(v,w))
            gameDisplay.blit(gameinsline6,(v2,w2))
            gameDisplay.blit(gameinsline7,(v3,w3))

            forbiddenletter(x)
            print(x)



            if event3.type==pygame.KEYDOWN:
                if event3.key==pygame.K_SPACE:
                    gamebackground(x)
                    continue
            print(event3)
            pygame.display.update()

def Timer(a):
    global i,num_correct
    timer=pygame.time.set_timer(pygame.USEREVENT,a)
    return timer

def Countdown(lives):
    global counter, minutes, seconds
    global a
    global time
    clock = pygame.time.Clock()
    counter, text = 4, '4'.ljust(4)
    Timer(a)
    frame_count = 0
    frame_rate = 60
    font = pygame.font.SysFont('Consolas', 30)
    white=(200,200,200)
    alive=True
    while alive:
        total_seconds = frame_count // frame_rate
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        time = "Time: {0:02}:{1:02}".format(minutes, seconds)
        text2 = font.render(time, True, white)
        frame_count += 1
        clock.tick(60)
        
        for e in pygame.event.get():
            if e.type == pygame.USEREVENT:
                if e.type == pygame.QUIT: alive=False
                elif counter > 0:
                    counter -= 1
                    text = str(counter).ljust(4)
                elif counter <= 0:
                    text = ('0')
                    lives -= 1
                    counter += 5
                    
                    if lives <= 0:
                        alive = False
                        print(time)
                        highscoremod.deathscreen1(time)
                        
                       
        gameDisplay.blit(gameinsbackImage,[0,0])
        gameDisplay.blit(text2, [550, 50]) 
        gameDisplay.blit(font.render(text, True, white), [32, 48])
        
    
        for i in range (lives):
            hearts_rect= hearts.get_rect()
            hearts_rect.x=lifewidth+30*i
            hearts_rect.y=lifeheight
            gameDisplay.blit(hearts,hearts_rect)
            
        pygame.display.update(0,0,1280,100)
        newletter(x,x2)
    
def gamebackground(x):
    
    gamerunning=True
    while gamerunning:
        for eventx2 in pygame.event.get():
            gameinstructionbackimage()
            playgame(x)
            
           
           
          

            
def gameinstructionbackimage():
    global gameDisplay
    gameDisplay.blit(gameinsbackImage,[0,0])
    pygame.display.update()
    
def forbiddenletter(x):
    
   
    
    global gameDisplay
     
    if x=="A" or x=="a":
        gameDisplay.blit(gameinsA,(602,295))
        
    elif x=="B" or x=="b":
        gameDisplay.blit(gameinsB,(602,295))
        
    elif x=="C" or x=="c":
        gameDisplay.blit(gameinsC,(602,295))
        
    elif x=="D" or x=="d":
        gameDisplay.blit(gameinsD,(602,295))
        
    elif x=="E" or x=="e":
        gameDisplay.blit(gameinsE,(602,295))
        
    elif x=="F" or x=="f":
        gameDisplay.blit(gameinsF,(602,295))
        
    elif x=="G" or x=="g":
        gameDisplay.blit(gameinsG,(602,295))
        
    elif x=="H" or x=="h":
        gameDisplay.blit(gameinsH,(602,295))
        
    elif x=="I" or x=="i":
        gameDisplay.blit(gameinsI,(602,295))
        
    elif x=="J" or x=="j":
        gameDisplay.blit(gameinsJ,(602,295))
        
    elif x=="K" or x=="k":
        gameDisplay.blit(gameinsK,(602,295))
        
    elif x=="L" or x=="l":
        gameDisplay.blit(gameinsL,(602,295))
        
    elif x=="M" or x=="m":
        gameDisplay.blit(gameinsM,(602,295))
        
    elif x=="N" or x=="n":
        gameDisplay.blit(gameinsN,(602,295))
        
    elif x=="O" or x=="o":
        gameDisplay.blit(gameinsO,(602,295))
        
    elif x=="P" or x=="p":
        gameDisplay.blit(gameinsP,(602,295))
        
    elif x=="Q" or x=="q":
        gameDisplay.blit(gameinsQ,(602,295))
        
    elif x=="R" or x=="r":
        gameDisplay.blit(gameinsR,(602,295))
        
    elif x=="S" or x=="s":
        gameDisplay.blit(gameinsS,(602,295))
        
    elif x=="T" or x=="t":
        gameDisplay.blit(gameinsT,(602,295))
        
    elif x=="U" or x=="u":
        gameDisplay.blit(gameinsU,(602,295))
        
    elif x=="V" or x=="v":
        gameDisplay.blit(gameinsV,(602,295))
        
    elif x=="W" or x=="w":
        gameDisplay.blit(gameinsW,(602,295))
        
    elif x=="X" or x=="x":
        gameDisplay.blit(gameinsX,(602,295))
        
    elif x=="Y" or x=="y":
        gameDisplay.blit(gameinsY,(602,295))
        
    elif x=="Z" or x=="z":
        gameDisplay.blit(gameinsZ,(602,295))

    
    
def playgameletters(x):
    global x2
    global gameDisplay
    x2=0
    x2=random.choice(string.ascii_letters)
    print(x2)
    gameDisplay.blit(gameinsbackImage,[0,0])
##    for i in x2:
##    alive=True    
##    while alive:
##    for event4 in pygame.event.get():
    if x2=="A" or x2=="a":
        gameDisplay.blit(gameinsA,(602,295))
    
    elif x2=="B" or x2=="b":
        gameDisplay.blit(gameinsB,(602,295))
        
    elif x2=="C" or x2=="c":
        gameDisplay.blit(gameinsC,(602,295))
        
    elif x2=="D" or x2=="d":
        gameDisplay.blit(gameinsD,(602,295))
        
    elif x2=="E" or x2=="e":
        gameDisplay.blit(gameinsE,(602,295))
        
    elif x2=="F" or x2=="f":
        gameDisplay.blit(gameinsF,(602,295))
        
    elif x2=="G" or x2=="g":
        gameDisplay.blit(gameinsG,(602,295))
        
    elif x2=="H" or x2=="h":
        gameDisplay.blit(gameinsH,(602,295))
        
    elif x2=="I" or x2=="i":
        gameDisplay.blit(gameinsI,(602,295))
        
    elif x2=="J" or x2=="j":
        gameDisplay.blit(gameinsJ,(602,295))
        
    elif x2=="K" or x2=="k":
        gameDisplay.blit(gameinsK,(602,295))
        
    elif x2=="L" or x2=="l":
        gameDisplay.blit(gameinsL,(602,295))
        
    elif x2=="M" or x2=="m":
        gameDisplay.blit(gameinsM,(602,295))
        
    elif x2=="N" or x2=="n":
        gameDisplay.blit(gameinsN,(602,295))
        
    elif x2=="O" or x2=="o":
        gameDisplay.blit(gameinsO,(602,295))
        
    elif x2=="P" or x2=="p":
        gameDisplay.blit(gameinsP,(602,295))
        
    elif x2=="Q" or x2=="q":
        gameDisplay.blit(gameinsQ,(602,295))
        
    elif x2=="R" or x2=="r":
        gameDisplay.blit(gameinsR,(602,295))
        
    elif x2=="S" or x2=="s":
        gameDisplay.blit(gameinsS,(602,295))
        
    elif x2=="T" or x2=="t":
        gameDisplay.blit(gameinsT,(602,295))
        
    elif x2=="U" or x2=="u":
        gameDisplay.blit(gameinsU,(602,295))
        
    elif x2=="V" or x2=="v":
        gameDisplay.blit(gameinsV,(602,295))
        
    elif x2=="W" or x2=="w":
        gameDisplay.blit(gameinsW,(602,295))
        
    elif x2=="X" or x2=="x":
        gameDisplay.blit(gameinsX,(602,295))
        
    elif x2=="Y" or x2=="y":
        gameDisplay.blit(gameinsY,(602,295))
        
    elif x2=="Z" or x2=="z":
        gameDisplay.blit(gameinsZ,(602,295))

    
    newletter(x,x2)
    pygame.display.update(600,295,90,70)
    
    
      

def newletter(x,x2):
    global i
    global a
    global counter
    num_correct=5
    i=0

    for event4 in pygame.event.get():
        if (x=="A" or x=="a")and (x2=="A" or x2=="a") and counter==1:
            counter+=4
            playgameletters(x)
            continue
        
        elif (x=="B" or x=="b")and (x2=="B" or x2=="b") and counter==1:
            counter+=4
            playgameletters(x)
            continue
        
        elif (x=="C" or x=="c")and (x2=="C" or x2== "c") and counter==1:
            counter+=4
            playgameletters(x)
            continue
        
        elif (x=="D" or x=="d")and (x2=="D" or x2=="d") and counter==1:
            counter+=4
            playgameletters(x)
            continue
        
        elif (x=="E" or x=="e")and (x2=="E" or x2=="e") and counter==1:
            counter+=4
            playgameletters(x)
            continue
        
        elif (x=="F" or x=="f")and (x2=="F" or x2=="f") and counter==1:
            counter+=4
            playgameletters(x)
            continue
        
        elif (x=="G" or x=="g")and (x2=="G" or x2=="g") and counter==1: 
            counter+=4
            playgameletters(x)
            continue
        
        elif (x=="H" or x=="h")and (x2=="H" or x2=="h") and counter==1:
            counter+=4
            playgameletters(x)
            continue
        
        elif (x=="I" or x=="i")and (x2=="I" or x2=="i") and counter==1:
            counter+=4
            playgameletters(x)
            continue
        
        elif (x=="J" or x=="j")and (x2=="J" or x2=="j") and counter==1:
            counter+=4
            playgameletters(x)
            continue
        
        elif (x=="K" or x=="k")and (x2=="K" or x2=="k") and counter==1:
            counter+=4
            playgameletters(x)
            continue
        
        elif (x=="L" or x=="l")and (x2=="L" or x2=="l") and counter==1:
            counter+=4
            playgameletters(x)
            continue
        
        elif (x=="M" or x=="m")and (x2=="M" or x2=="m") and counter==1:
            counter+=4
            playgameletters(x)
            continue
        
        elif (x=="N" or x=="n")and (x2=="N" or x2=="n") and counter==1:
            counter+=4
            playgameletters(x)
            continue
        
        elif (x=="O" or x=="o")and (x2=="O" or x2=="o") and counter==1:
            counter+=4
            playgameletters(x)
            continue
        
        elif (x=="P" or x=="p")and (x2=="P" or x2=="p") and counter==1:
            counter+=4
            playgameletters(x)
            continue
        
        elif (x=="Q" or x=="q")and (x2=="Q" or x2=="q") and counter==1:
            counter+=4
            playgameletters(x)
            continue
        
        elif (x=="R" or x=="r")and (x2=="R" or x2=="r")and counter==1:
            counter+=4
            playgameletters(x)
            continue
        
        elif (x=="S" or x=="s")and (x2=="S" or x2=="s") and counter==1:
            
            counter+=4
            playgameletters(x)
            continue
        
        elif (x=="T" or x=="t")and (x2=="T" or x2=="t") and counter==1:
            counter+=4
            playgameletters(x)
            continue
        
        elif (x=="U" or x=="u")and (x2=="U" or x2=="u") and counter==1:
            counter+=4
            playgameletters(x)
            continue
        
        elif (x=="V" or x=="v")and (x2=="V" or x2=="v") and counter==1:
            counter+=4
            playgameletters(x)
            continue
        
        elif (x=="W" or x=="w") and (x2=="W" or x2=="w")and counter==1:
            counter+=4
            playgameletters(x)
            continue
        
        elif (x=="X" or x=="x")and (x2=="X" or x2=="x") and counter==1:
            counter+=4
            playgameletters(x)
            continue
        
        elif (x=="Y" or x=="y") and (x2=="Y" or x2=="y")and counter==1:
            counter+=4
            playgameletters(x)
            continue
        
        elif (x=="Z" or x=="z")and (x2=="Z" or x2=="z") and counter==1:
            counter+=4
            playgameletters(x)
            continue
        elif event4.type==pygame.KEYDOWN:
            if (x=="A" or x=="a") and (x2=="A" or x2=="a") and event4.key==pygame.K_a:
                highscoremod.deathscreen1(time)
                continue
            elif (x=="B" or x=="b") and (x2=="B" or x2=="b") and event4.key==pygame.K_b:
                highscoremod.deathscreen1(time)
                continue
            elif (x=="C" or x=="c") and (x2=="C" or x2=="c") and event4.key==pygame.K_c:
                highscoremod.deathscreen1(time)
                continue
            elif (x=="D" or x=="d") and (x2=="D" or x2=="d") and event4.key==pygame.K_d:
                highscoremod.deathscreen1(time)
                continue
            elif (x=="E" or x=="e") and (x2=="E" or x2=="e") and event4.key==pygame.K_e:
                highscoremod.deathscreen1(time)
                continue
            elif (x=="F" or x=="f") and (x2=="F" or x2=="f") and event4.key==pygame.K_f:
                highscoremod.deathscreen1(time)
                continue
            elif (x=="G" or x=="g") and (x2=="G" or x2=="g") and event4.key==pygame.K_g:
                highscoremod.deathscreen1(time)
                continue
            elif (x=="H" or x=="h") and (x2=="H" or x2=="h") and event4.key==pygame.K_h:
                highscoremod.deathscreen1(time)
                continue
            elif (x=="I" or x=="i") and (x2=="I" or x2=="i") and event4.key==pygame.K_i:
                highscoremod.deathscreen1(time)
                continue
            elif (x=="J" or x=="j") and (x2=="J" or x2=="j") and event4.key==pygame.K_j:
                highscoremod.deathscreen1(time)
                continue
            elif (x=="K" or x=="k") and (x2=="K" or x2=="k") and event4.key==pygame.K_k:
                highscoremod.deathscreen1(time)
                continue
            elif (x=="L" or x=="l") and (x2=="L" or x2=="l") and event4.key==pygame.K_l:
                highscoremod.deathscreen1(time)
                continue
            elif (x=="M" or x=="m") and (x2=="M" or x2=="m") and event4.key==pygame.K_m:
                highscoremod.deathscreen1(time)
                continue
            elif (x=="N" or x=="n") and (x2=="N" or x2=="n") and event4.key==pygame.K_n:
                highscoremod.deathscreen1(time)
                continue
            elif (x=="O" or x=="o") and (x2=="O" or x2=="o") and event4.key==pygame.K_o:
                highscoremod.deathscreen1(time)
                continue
            elif (x=="P" or x=="p") and (x2=="P" or x2=="p") and event4.key==pygame.K_p:
                highscoremod.deathscreen1(time)
                continue
            elif (x=="Q" or x=="q") and (x2=="Q" or x2=="q") and event4.key==pygame.K_q:
                highscoremod.deathscreen1(time)
                continue
            elif (x=="R" or x=="r") and (x2=="R" or x2=="r") and event4.key==pygame.K_r:
                highscoremod.deathscreen1(time)
                continue
            elif (x=="S" or x=="s") and (x2=="S" or x2=="s") and event4.key==pygame.K_s:
                highscoremod.deathscreen1(time)
                continue
            elif (x=="T" or x=="t") and (x2=="T" or x2=="t") and event4.key==pygame.K_t:
                highscoremod.deathscreen1(time)
                continue
            elif (x=="U" or x=="u") and (x2=="U" or x2=="u") and event4.key==pygame.K_u:
                highscoremod.deathscreen1(time)
                continue
            elif (x=="V" or x=="v") and (x2=="V" or x2=="v") and event4.key==pygame.K_v:
                highscoremod.deathscreen1(time)
                continue
            elif (x=="W" or x=="w") and (x2=="W" or x2=="w") and event4.key==pygame.K_w:
                highscoremod.deathscreen1(time)
                continue 
            elif (x=="X" or x=="x") and (x2=="X" or x2=="x") and event4.key==pygame.K_x:
                highscoremod.deathscreen1(time)
                continue
            elif (x=="Y" or x=="y") and (x2=="Y" or x2=="y") and event4.key==pygame.K_y:
                highscoremod.deathscreen1(time)
                continue
            elif (x=="Z" or x=="z") and (x2=="Z" or x2=="z") and event4.key==pygame.K_z:
                highscoremod.deathscreen1(time)
                continue

            elif (x2=="A" or x2=="a") and event4.key==pygame.K_a:
                i+=1
                counter=4
                playgameletters(x)
                continue
            elif (x2=="B" or x2=="b") and event4.key==pygame.K_b:
                i+=1
                counter=4
                playgameletters(x)
                continue
            
            elif (x2=="C" or x2=="c") and event4.key==pygame.K_c:
                i+=1
                counter=4
                playgameletters(x)
                continue
             
            elif (x2=="D" or x2=="d") and event4.key==pygame.K_d:
                i+=1
                counter=4
                playgameletters(x)
                continue
              
            elif (x2=="E" or x2=="e") and event4.key==pygame.K_e:
                i+=1
                counter=4
                playgameletters(x)
                continue
             
            elif (x2=="F" or x2=="f") and event4.key==pygame.K_f:
                i+=1
                counter=4
                playgameletters(x)
                continue
             
            elif (x2=="G" or x2=="g") and event4.key==pygame.K_g:
                i+=1
                counter=4
                playgameletters(x)
                continue
             
            elif (x2=="H" or x2=="h") and event4.key==pygame.K_h:
                i+=1
                counter=4
                playgameletters(x)
                continue
                
            elif (x2=="I" or x2=="i") and event4.key==pygame.K_i:
                i+=1
                counter=4
                playgameletters(x)
                continue
             
            elif (x2=="J" or x2=="j") and event4.key==pygame.K_j:
                i+=1
                counter=4
                playgameletters(x)
                continue
                
            elif (x2=="K" or x2=="k") and event4.key==pygame.K_k:
                i+=1
                counter=4
                playgameletters(x)
                continue
                
            elif (x2=="L" or x2=="l") and event4.key==pygame.K_l:
                i+=1
                counter=4
                playgameletters(x)
                continue
                
            elif (x2=="M" or x2=="m") and event4.key==pygame.K_m:
                i+=1
                counter=4
                playgameletters(x)
                continue
                
            elif (x2=="N" or x2=="n") and event4.key==pygame.K_n:
                i+=1
                counter=4
                playgameletters(x)
                continue
                
            elif (x2=="O" or x2=="o") and event4.key==pygame.K_o:
                i+=1
                counter=4
                playgameletters(x)
                continue
                
            elif (x2=="P" or x2=="p") and event4.key==pygame.K_p:
                i+=1
                counter=4
                playgameletters(x)
                continue
                
            elif (x2=="Q" or x2=="q") and event4.key==pygame.K_q:
                i+=1
                counter=4
                playgameletters(x)
                continue
                
            elif (x2=="R" or x2=="r") and event4.key==pygame.K_r:
                i+=1
                counter=4
                playgameletters(x)
                continue
                
            elif (x2=="S" or x2=="s") and event4.key==pygame.K_s:
                i+=1
                counter=4
                playgameletters(x)
                continue
                
            elif (x2=="T" or x2=="t") and event4.key==pygame.K_t:
                i+=1
                counter=4
                playgameletters(x)
                continue
                
            elif (x2=="U" or x2=="u") and event4.key==pygame.K_u:
                i+=1
                counter=4
                playgameletters(x)
                continue
                
            elif (x2=="V" or x2=="v") and event4.key==pygame.K_v:
                i+=1
                counter=4
                playgameletters(x)
                continue
                
            elif (x2=="W" or x2=="w") and event4.key==pygame.K_w:
                i+=1
                counter=4
                playgameletters(x)
                continue
                
            elif (x2=="X" or x2=="x") and event4.key==pygame.K_x:
                i+=1
                counter=4
                playgameletters(x)
                continue
                
            elif (x2=="Y" or x2=="y") and event4.key==pygame.K_y:
                i+=1
                counter=4
                playgameletters(x)
                continue
                
            elif (x2=="Z" or x2=="z") and event4.key==pygame.K_z:
                i+=1
                counter=4
                playgameletters(x)
                continue
            
            
            else:
                counter=0

            return counter

        

            
def playgame(x):
    global a
    global lives 
    display_width=1280
    display_height=720
    gameDisplay=pygame.display.set_mode((display_width,display_height))
    
    playgameletters(x)
    Countdown(lives)

    
    
