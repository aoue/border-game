import pygame
import sys
from pygame.locals import *
import math


#settings
pygame.init()

pygame.display.set_caption('Slayer')
screen = pygame.display.set_mode((800,500), 0, 32)
font = pygame.font.SysFont('Calibri', 25)
background = pygame.Surface(screen.get_size())
background.fill((135,206,250))
white = (255,255,255)
#movement settings
keys = [False, False, False, False]


class Player(object):
    #player rect
    def __init__(self,x,y, name):        
        self.x = x
        self.y = y
        self.image = pygame.image.load(name)
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 200
        
        
        print(self.rect)

    def rotate(self,r):
        position = pygame.mouse.get_pos()
        angle = math.atan2(position[1]-(self.y+self.rect.height/2),position[0]-(self.x+self.rect.width/2))
        rot = pygame.transform.rotate(r, 360-angle*57.29)
        pos = (self.x-rot.get_rect().width/2, self.y-rot.get_rect().height/2)
        return rot, pos
        
    
    #player rotation
    def draw(self,screen):
        playerrot, playerpos = self.rotate(self.image)
        screen.blit(playerrot, playerpos)
        
        #screen.blit(playerrot, (self.x,self.y))
        
    #moving
    def move_x(self, dx):
        self.x += dx
        self.rect.x = self.x

        
        if pygame.Rect.colliderect(self.rect, borderRight):
            print ('collision')
            self.x -= dx
        if pygame.Rect.colliderect(self.rect, borderLeft):
            print ('collision')
            self.x -= dx
            
    def move_y(self, dy):
        self.y += dy
        self.rect.y = self.y

        
        if pygame.Rect.colliderect(self.rect, borderTop):
            print ('collision')
            self.y -= dy
        if pygame.Rect.colliderect(self.rect, borderBottom):
            print ('collision')
            self.y -= dy
        
player = Player(400,200,'C:\\Users\\Aaja\\Desktop\\Slayer game stuff\\images\\player.png')  





    
#music
sacrificeSong = pygame.mixer.music.load('C:\\Users\\Aaja\\Desktop\\Slayer game stuff\\music\\sacrificeSong.mp3')
pygame.mixer.music.play(-1)
musicCounter = 1





#define images
cartoonCat = pygame.image.load('C:\\Users\\Aaja\\Desktop\\Slayer game stuff\\images\\cute-cartoon-cat.png')






#main loop
while 1:
    
    #adds background colour and cat
    screen.blit(background, (0,0))
    screen.blit(cartoonCat, (0,50))
    
    #adds borders
    borderTop = pygame.draw.rect(screen, white,(0,0,800,0))
    borderBottom = pygame.draw.rect(screen, white,(0,500,800,0))
    borderLeft = pygame.draw.rect(screen, white,(0,0,0,500))   
    borderRight = pygame.draw.rect(screen, white,(800,0,0,500))

    r = player.image.get_rect()
    r.x = player.x - r.width/2
    r.y = player.y - r.height/2
    
    pygame.draw.rect(screen, white, r)    

   
    #rotating player to face mouse
    player.draw(screen)
    
    
  
    #adds text
    screen.blit(font.render('Do you have what it takes to be a slayahh??!!!!', True, (0,0,0)), (200, 0))
    screen.blit(font.render('Press q to quit', True, (0,0,0)), (665, 100))
    screen.blit(font.render('M to toggle music', True, (0,0,0)), (665, 125))


    #flip
    pygame.display.flip()
    




    ###keyboard commands###
    
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            #press q to quit
            if event.key == pygame.K_q:
                print('You quit the game.')
                pygame.display.quit()
                pygame.quit()
                sys.exit()                
            #press m to toggle music, 1 = on, 0 = 0ff
            elif event.key == pygame.K_m:
                if musicCounter == 1:
                    print('Music off.')
                    pygame.mixer.music.stop()
                    musicCounter = musicCounter - 1
                else:
                    print('Music on.')
                    pygame.mixer.music.play(-1)
                    musicCounter = musicCounter + 1




                    
    ##movement##
                    
        #collisions
        
        
        
        #
        if event.type == pygame.KEYDOWN:
            if event.key==K_w:
                keys[0] = True
            elif event.key == K_a:
                keys[1] = True
            elif event.key == K_s:
                keys[2] = True
            elif event.key == K_d:
                keys[3] = True
        #
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                keys[0] = False
            elif event.key == pygame.K_a:
                keys[1] = False
            elif event.key == pygame.K_s:
                keys[2] = False
            elif event.key == pygame.K_d:
                keys[3] = False
                
    #adjust x and y      
    if keys[0]:
        player.move_y(-1)
        
    elif keys[2]:
        player.move_y(+1)
    if keys[1]:
        player.move_x(-1)
    elif keys[3]:
        player.move_x(+1)    
    
    

    
    
                
    
     
    
    
