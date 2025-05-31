import pygame,math
import threading
import keyboard
pygame.init()
screen=pygame.display.set_mode((1920,1080))
pygame.display.set_caption('Mandelbrot set')
running=True
pixels=[[False]*1920]*1080  
iter=240
iterated=0
drawnrows=0
center=(0,0)
zoom=-0.3
#things you should change!
#-----------------------
julia=True
juliacord=( 2.501)
fractal="mandelbrot set"
power=2
#-----------------------
def zfunc(z):
    global fractal
    global power
    if fractal.lower()=="mandelbrot set":
        return z**power
    if fractal.lower()=="burning ship":
        return complex(abs(z.real),abs(z.imag))**power
    if fractal.lower()=="diagonal mandelbrot":
        return z**complex(-(2**2)/2,-(2**2)/2)
    if fractal.lower=="custom":
        return z**2+z**3+1
        #add yours above!
def get_mousepos():
    (mousex,mousey)=pygame.mouse.get_pos()
    return (mousex/(700*(10**zoom))+center[0]-((10**-zoom)/0.66),mousey/(700*(10**zoom))+center[1]-((10**-zoom)/1.33))
def drawrow(n):
    global drawnrows
    global iterated
    global julia
    global juliacord
    for x,j in enumerate(pixels[n]):
        c=complex(x/(700*(10**zoom))+center[0]-((10**-zoom)/0.66),n/(700*(10**zoom))+center[1]-((10**-zoom)/1.33))
        if julia:
            z=c 
        else:
            z=0
        for num,i in enumerate(range(iter)):
            z=zfunc(z)
            if julia:
               z+=juliacord
            else:
               z+=c
            if abs(z)>=20 :
                pixels[n][x]=False
                color=(127-math.cos(num/10+(0.1*math.pi/2))*127,127-math.cos(num/10+(0.5*math.pi/2))*127,127-math.cos(num/10+(0.9*math.pi/2))*127)
                break
        if abs(z)<20:
            pixels[n][x]=True
            color=(0,0,0)
        screen.set_at((x,n),color)
    iterated+=1
center=(center[0],center[1]*-1)
for row in range(1080):
            t=threading.Thread(target=drawrow,args=(row,)) 
         
            t.start()   
            pygame.display.flip()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        
    if pygame.mouse.get_pressed()[2] and iterated>1070:
        center=get_mousepos()
        zoom+=1
        iterated=0
        screen.fill((0,0,0))
        for row in range(1080):
            t=threading.Thread(target=drawrow,args=(row,)) 
            t.daemon=True
            t.start()   
            pygame.display.flip()
    if keyboard.is_pressed('t'):
        iter*=3
        screen.fill((0,0,0))
        for row in range(1080):
            t=threading.Thread(target=drawrow,args=(row,)) 
            t.daemon=True
            t.start()   
            pygame.display.flip()
    if keyboard.is_pressed('g'):
        iter=int(iter/3)
        if iter<5:
            iter=5
            break
        screen.fill((0,0,0))
        for row in range(1080):
            t=threading.Thread(target=drawrow,args=(row,)) 
            t.daemon=True
            t.start()   
            pygame.display.flip()
pygame.quit()