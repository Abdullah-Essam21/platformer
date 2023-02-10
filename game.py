import pygame
import sys

pygame.init()
screen_dimensions = (400,400)
screen = pygame.display.set_mode(screen_dimensions)
bg_img = pygame.image.load("python small projects/Assets/bg2.jpg")
bg_width = bg_img.get_rect().width
bg_height = bg_img.get_rect().height
scaled_bg = pygame.transform.smoothscale(bg_img,(screen_dimensions[0],screen_dimensions[1]))

class Player:
    def __init__(self,x,y,width,height,x_vel,y_vel):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.jumping = False
    def jump(self):
        #jumping code 
        # I need to excute a full jump each click
        # for i in range(17)
        if self.jumping == True:
            self.y -= self.y_vel
            self.y_vel-=1
            if self.y_vel < -8:
                self.jumping = False
                self.y_vel = 8
            #print(self.y_vel)
    def goLeft(self):
        self.x -= self.x_vel
    def goRight(self):
        self.x += self.x_vel
    def draw(self):
        pygame.draw.rect(screen,red,pygame.Rect(self.x,self.y,self.width,self.height))        


clock = pygame.time.Clock()
width = 20
height = 20
x = 100
y = screen_dimensions[0] - height
x_vel = 8
y_vel = 8
red = (255,0,0)    
mainPlayer = Player(x,y,width,height,x_vel,y_vel)

running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()


        key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_LEFT] and mainPlayer.x >= 0:
        mainPlayer.goLeft()
    elif key_pressed[pygame.K_RIGHT] and mainPlayer.x < screen_dimensions[0] - mainPlayer.width:
        mainPlayer.goRight()
    if key_pressed[pygame.K_UP]:
        mainPlayer.jumping = True
        mainPlayer.jump()
    if key_pressed[pygame.K_UP] == False and mainPlayer.y_vel != 8:
        mainPlayer.jump() # completing the jump if the player left the jump key in the middle of the jump.


    mainPlayer.draw()
    pygame.display.flip()
    screen.blit(scaled_bg,(0,0))
    # screen.fill((255,255,255))


