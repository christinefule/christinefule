import pygame
pygame.init()

game_win = pygame.display.set_mode((800,600))
pygame.display.set_caption("First Game")

#set the row,col
# x & y: top left corner, x + w : top right corner
#x,y +h: 
x = 50
y = 50
a = 50
b = 50 
radius = 15
width  = 40
height = 40
speed  = 5

run = True
while run:
    pygame.time.delay(100)#delay the game movement in ms

    for event in pygame.event.get():#loop through a list of any key or mouse event
        if event.type == pygame.QUIT:
            print("Thank You!")
            run = False #END THE GAME LOOP
    keys = pygame.key.get_pressed()#list of keys to use
    keys2 =pygame.key.get_pressed()
    #CHECK which key is pressed
    
    #KEYS for square object
    if keys[pygame.K_LEFT] and x > speed:
        x-= speed
    if keys[pygame.K_RIGHT] and x < 500 -speed -width:
        x+= speed
    if keys[pygame.K_UP] and y > speed:
        y-= speed
    if keys[pygame.K_DOWN] and y < 500 - height -speed:
        y+= speed
    #KEYS for circle object 
    if keys2[pygame.K_a]:
        a-= speed
    if keys2[pygame.K_d]:
        a+= speed
    if keys[pygame.K_w]:
        b-= speed
    if keys[pygame.K_s]:
        b+= speed
    
    game_win.fill((0,0,0))#fill with block
    pygame.draw.rect(game_win, (255,0,0),(x,y,width,height))#window surface drawing a square,
    pygame.draw.circle(game_win,(255,255,255),(int(a),int(b)),radius)
    pygame.display.update()#enable to update the screen

pygame.quit()
