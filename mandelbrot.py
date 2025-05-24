import pygame,math
pygame.init()
screen=pygame.display.set_mode((1920,1000))
running=True
pixels=[[False]*1920]*1080
iter=80
iterated=False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    if not(iterated):
        for y,i in enumerate(pixels):
            for x,j in enumerate(i):
                Opoint=complex(x/700-2,y/700-1)
                point=Opoint
                for num,i in enumerate(range(iter)):
                    point=point**3+Opoint
                    if abs(point)>3:
                        pixels[y][x]=False
                        color=(255-(num*255/iter),255-(num*255/iter),255-(num*255/iter))
                        break
                if abs(point)<3:
                    pixels[y][x]=True
                    color=(0,0,0)
                screen.set_at((x,y),color)
            pygame.display.flip()    
        iterated=True
    pygame.display.flip()
pygame.quit()