import pygame, sys
from pygame.locals import *
from random import *
import time

pygame.init()
screen=pygame.display.set_mode((800, 600))
luigi=pygame.image.load('mirino1.png')
luigi=pygame.transform.scale(luigi,(200, 200))
gato=pygame.image.load('gato.jpg')
gato=pygame.transform.scale(gato,(100,100))
colpo=pygame.image.load('esplosione.png')
colpo=pygame.transform.scale(colpo,(50,50))
ics=pygame.image.load('errore.png')
ics=pygame.transform.scale(ics,(50,50))
aimstudio=pygame.image.load('aimstudio.png')
aimstudio=pygame.transform.scale(aimstudio,(900,550))
rect=luigi.get_rect()
rectgato=gato.get_rect()
vel=[1,-1]
clock=pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, 1000)
screen.fill((255,255,255))
screen.blit(luigi,(200,300))
t=True
fine=False
tempo=-1
counter=-1
riavvia=False
traccia=1
asd=0
dsa=0
das=0
ads=0
time_limit=[-1,30,60,120,180,0]
misses=[0,1,2,3,5,0]
targets=["gatto","saddam","bambino","kennedy",""]
audio=[1,2,3]
errori=0
target="gatto"

#numero di errori massimi
i=0
miss=0
precisione=100
esplosione=False
musica=pygame.mixer.Sound('traccia1.wav')
shot=pygame.mixer.Sound('colpo.wav')
x=randint(10,690)
y=randint(40,490)
screen.blit(gato,(x,y))
punteggio=0
music=False
pygame.display.update()
menu=False
settings=False
while t:
    mouse=pygame.mouse.get_pressed()
    pos=pygame.mouse.get_pos()
    gatom=pygame.transform.scale(gato,(50,50))
    if menu and not settings and not fine:
        pygame.mouse.set_visible(False)
        if i==0:
            punteggio=0
            precisione=100
    else:
        pygame.mouse.set_visible(True)
    for event in pygame.event.get():
        if event.type==pygame.USEREVENT and counter>0 and menu:
            counter-=1
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
            t=False
        if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    if menu:
                        menu=False
                        i=0
                        miss=0
                        precisione=100
                        punteggio=0
                        tempo=time_limit[ads]
                        counter=tempo
                    else:
                        menu=True
                        settings=False
                elif event.key==pygame.K_i:
                    if settings:
                        settings=False
                    else:
                        settings=True
        if event.type==MOUSEBUTTONDOWN and menu and not fine:
            pygame.mixer.Channel(1).play(pygame.mixer.Sound(shot))
            i+=1
            if rect.x>rectgato.x-100 and rect.x<rectgato.x and rect.y>rectgato.y-100 and rect.y<rectgato.y:
                punteggio+=1
                esplosione=True
                screen.blit(colpo,(rect.x+75,rect.y+75))
                vecchiax=x
                vecchiay=y
                while vecchiax+150>x and vecchiax-150<x and vecchiay+150>y and vecchiay-150<y: 
                    x=randint(10,690)
                    y=randint(40,490)
            else:
                miss+=1
        if event.type==MOUSEBUTTONDOWN and settings:
            if pos[0]>50 and pos[0]<400 and pos[1]>90 and pos[1]<130:
                ads+=1
                if tempo==time_limit[4] or tempo==time_limit[5]:
                    tempo=time_limit[0]
                    ads=0
                tempo=time_limit[ads]
                counter=tempo
            if pos[0]>50 and pos[0]<400 and pos[1]>270 and pos[1]<310:
                asd+=1
                if traccia==audio[2]:
                    traccia=audio[0]
                    asd=0
                traccia=audio[asd]
            elif pos[0]>50 and pos[0]<400 and pos[1]>150 and pos[1]<190:
                dsa+=1
                if errori==misses[4]:
                    errori=misses[0]
                    dsa=0
                errori=misses[dsa]
            elif pos[0]>50 and pos[0]<500 and pos[1]>210 and pos[1]<250:
                das+=1
                if target==targets[3]:
                    target=targets[0]
                    das=0
                target=targets[das]
        if event.type==pygame.KEYDOWN and menu:
            if event.key==pygame.K_m:
                if music==False:
                    pygame.mixer.Channel(0).play(pygame.mixer.Sound(musica))
                    music=True
                else:
                    pygame.mixer.Channel(0).stop()
                    music=False
        if event.type==MOUSEBUTTONDOWN and fine:
            if pos[0]>275 and pos[0]<500 and pos[1]>400 and pos[1]<460:
                fine=False
                menu=True
                settings=False

                riavvia=True
            elif pos[0]>275 and pos[0]<500 and pos[1]>490 and pos[1]<550:
                fine=False
                menu=False
                settings=False
                riavvia=True
    rect.x=pos[0]-100
    rect.y=pos[1]-96
    if music:
        cum="On"
    else:
        cum="Off"
    if counter==0:
            fine=True
    if esplosione:
        screen.blit(gatom,(x+25,y+25))
        pygame.display.update()
        esplosione=False
        time.sleep(0.1)
    rectgato.x=rectgato.x-(rectgato.x-x)
    rectgato.y=rectgato.y-(rectgato.y-y)
    screen.fill((255,255,255))
    screen.blit(gato,(x,y))
    screen.blit(luigi, rect)
    contatore=pygame.font.Font('freesansbold.ttf', 25).render('Score: '+str(punteggio), True, (0,0,0))
    musica_si_no=pygame.font.Font('freesansbold.ttf', 25).render('Music (M): '+cum, True, (0,0,0))
    percentualeprecisione=pygame.font.Font('freesansbold.ttf', 25).render('Accuracy: '+str(round(precisione, 2))+"%", True, (0,0,0))
    tempo_rimasto=pygame.font.Font('freesansbold.ttf',50).render(str(counter),True,(0,0,0))
    screen.blit(contatore,(10,10))
    screen.blit(musica_si_no,(620,10))
    screen.blit(percentualeprecisione,(275,10))
    if tempo>-1:
        if len(str(counter))==3:
            screen.blit(tempo_rimasto,(710,540))
        elif len(str(counter))==2:
             screen.blit(tempo_rimasto,(730,540))
        else:
            screen.blit(tempo_rimasto,(750,540))
    if errori>0:
        if miss==1:
            screen.blit(ics,(10,550))
        if miss==2:
            screen.blit(ics,(10,550))
            screen.blit(ics,(60,550))
        if miss==3:
            screen.blit(ics,(10,550))
            screen.blit(ics,(60,550))
            screen.blit(ics,(110,550))
        if miss==4:
            screen.blit(ics,(10,550))
            screen.blit(ics,(60,550))
            screen.blit(ics,(110,550))
            screen.blit(ics,(160,550))
        if miss==5:
            screen.blit(ics,(10,550))
            screen.blit(ics,(60,550))
            screen.blit(ics,(110,550))
            screen.blit(ics,(160,550))
            screen.blit(ics,(210,550))
        if miss==errori:
            fine=True
    if not menu:
            precisione=100
            punteggio=0
            fine=False
            pygame.time.set_timer(pygame.USEREVENT, 1000)
            screen.fill((255,255,255))
            pygame.mixer.Channel(0).stop()
            music=False
            if settings:
#tempo
                if tempo==-1:
                    limite_tempo=pygame.font.Font('freesansbold.ttf', 40).render('limite tempo: no', True, (0,0,0))
                elif tempo==30:
                    limite_tempo=pygame.font.Font('freesansbold.ttf', 40).render('limite tempo: 0:30', True, (0,0,0))
                elif tempo==60:
                    limite_tempo=pygame.font.Font('freesansbold.ttf', 40).render('limite tempo: 1:00', True, (0,0,0))
                elif tempo==120:
                    limite_tempo=pygame.font.Font('freesansbold.ttf', 40).render('limite tempo: 2:00', True, (0,0,0))
                elif tempo==180:
                    limite_tempo=pygame.font.Font('freesansbold.ttf', 40).render('limite tempo: 3:00', True, (0,0,0))
#errori 
                if errori==0:
                    limite_errori=pygame.font.Font('freesansbold.ttf', 40).render('limite errori: no', True, (0,0,0))
                else:
                    limite_errori=pygame.font.Font('freesansbold.ttf', 40).render('limite errori: '+str(errori), True, (0,0,0))
#musica
                if traccia==1:
                    scelta_musica=pygame.font.Font('freesansbold.ttf', 40).render('musica: Traccia 1', True, (0,0,0))
                    musica=pygame.mixer.Sound('traccia1.wav')
                elif traccia==2:
                    scelta_musica=pygame.font.Font('freesansbold.ttf', 40).render('musica: Traccia 2', True, (0,0,0))
                    musica=pygame.mixer.Sound('traccia2.wav')
                elif traccia==3:
                    scelta_musica=pygame.font.Font('freesansbold.ttf', 40).render('musica: Traccia 3', True, (0,0,0))
                    musica=pygame.mixer.Sound('traccia3.wav')
#bersaglio
                if target=="gatto":
                    bersaglio=pygame.font.Font('freesansbold.ttf', 40).render('bersaglio: Gatto', True, (0,0,0))
                    gato=pygame.image.load('gato.jpg')
                    gato=pygame.transform.scale(gato,(100,100))
                elif target=="saddam":
                    bersaglio=pygame.font.Font('freesansbold.ttf', 40).render('bersaglio: Saddam Hussein', True, (0,0,0))
                    gato=pygame.image.load('saddam.jpg')
                    gato=pygame.transform.scale(gato,(100,100))
                elif target=="bambino":
                    bersaglio=pygame.font.Font('freesansbold.ttf', 40).render('bersaglio: Bambino', True, (0,0,0))
                    gato=pygame.image.load('devcember.png')
                    gato=pygame.transform.scale(gato,(100,100))
                elif target=="kennedy":
                    bersaglio=pygame.font.Font('freesansbold.ttf', 40).render('bersaglio: J.F Kennedy', True, (0,0,0))
                    gato=pygame.image.load('kennedy.png')
                    gato=pygame.transform.scale(gato,(100,100))
                screen.blit(limite_tempo,(50,90))
                screen.blit(limite_errori,(50,150))
                screen.blit(bersaglio,(50,210))
                screen.blit(scelta_musica,(50,270))
            else:
                avvia=pygame.font.Font('freesansbold.ttf', 30).render('Premi SPAZIO per avviare', True, (0,0,0))
                impostazioni=pygame.font.Font('freesansbold.ttf', 30).render('Premi I per aprire le impostazioni', True, (0,0,0))
                screen.blit(aimstudio,(-20,0))
                screen.blit(avvia,(210,500))
                screen.blit(impostazioni,(160,550))
    elif fine:
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        screen.fill((255,255,255))
        menu=pygame.font.Font('freesansbold.ttf', 60).render('Menu principale', True, (0,0,0))
        riavvia=pygame.font.Font('freesansbold.ttf', 60).render('Riavvia', True, (0,0,0))
        screen.blit(contatore,(325,110))
        screen.blit(percentualeprecisione,(275,60))
        screen.blit(riavvia,(275,400))
        screen.blit(menu,(175,500))
        if riavvia:
            miss=0
            i=0
            counter=tempo
    pygame.display.update()
    time.sleep(0.0004)
    if i>0:
        precisione=((i-miss)/i*100)
        


    #roba da fare:
        
