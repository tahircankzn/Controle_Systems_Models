import pygame 
from math import exp

pygame.init() 

win = pygame.display.set_mode((1369, 875)) 

pygame.display.set_caption("Kontrol Sistemleri - Matematiksel Model Simülasyonu") 

x = 1369 // 3
y = (875 // 3) * 2.5

width = 100
height = 100

def model(M,fv,t):
    return (1/fv) - exp(((-1*(fv*t))/M)/fv)

def text(msg1,msg2):
    font = pygame.font.SysFont("Algeria",25)  
    font2 = pygame.font.SysFont("Algeria",50)  

    # F(t)
    text = font.render(msg1,1,(0,0,0)) # "F(t)"
    x1 = 50
    y1 = 25
    pygame.draw.line(win,(0,0,255),(x+50+x1,y+25+y1),(x+100+x1,y+25+y1),5)
    pygame.draw.line(win,(0,0,255),(x+100+x1,y+25+y1),(x+90+x1,y+20+y1),5) # ok
    pygame.draw.line(win,(0,0,255),(x+100+x1,y+25+y1),(x+90+x1,y+30+y1),5) # ok
    win.blit(text,(x+65+x1,y+y1))

    # Fv(t)
    text2 = font.render(msg2,1,(0,0,0)) # "Fv(t)"
    pygame.draw.line(win,(0,0,255),(x,y+25+y1),(x-50,y+25+y1),5)
    pygame.draw.line(win,(0,0,255),(x-50,y+25+y1),(x-40,y+20+y1),5) # ok
    pygame.draw.line(win,(0,0,255),(x-50,y+25+y1),(x-40,y+30+y1),5) # ok
    win.blit(text2,(x-45,y+y1)) 

    text = font2.render("M",1,(0,0,0))
    win.blit(text,(x+35,y+35))
    

BG = pygame.image.load("model1.png")

M = 10
fv = 0.5

t = 0

run = True

mode = 0

msg1 = "F(t)"
msg2 = "Fv(t)"

while run: 

    pygame.time.delay(10) 

    for event in pygame.event.get(): 

	    if event.type == pygame.QUIT: 

		    run = False
           
    if mode == 0:
        x+= model(M,fv,t)
        
        
    elif mode == 1:
        x-= model(M,fv,t)
        

    if x >= (1369 // 3) * 2:
        mode = 1
    elif x <= (1369 // 3):
        mode = 0  
    
    t+=1

    win.blit(BG,(0,0))
    
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height)) 
    if mode == 0:
        text(msg1,msg2)
    else:
        text(msg2,msg1)
   
    pygame.display.update() 


pygame.quit() 