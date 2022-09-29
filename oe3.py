import pygame
pygame.init()


pygame.display.set_caption("First Game")
yellow = pygame.Color(255, 255, 0)
game_win = pygame.display.set_mode((650, 450))

#set the row,col
# x & y: top left corner, x + w : top right corner
#x,y +h: bottom left
x = 50
y = 50
a = 55
b = 80
radius = 30
width  = 60
height = 60
speed  = 5

#jumping variables
isJump = False
jumpCount = 8
isJump2 = False
jumpCount2 = 8

run = True
while run:
    
    pygame.time.delay(100)#delay the game movement in ms

    for event in pygame.event.get():#loop through a list of any key or mouse event
        if event.type == pygame.QUIT:
            print("Thank You!")
            run = False #END THE GAME LOOP
    keys = pygame.key.get_pressed()#list of keys to use
    #CHECK which key is pressed
    
    #KEYS for SQUARE object
    if keys[pygame.K_LEFT] and x > speed: #there is no movement
        x-= speed
    if keys[pygame.K_RIGHT] and x < 650 - speed - width: #top right corner less then the screen width
        x+= speed
    
    #check the user if not jumping
    if not(isJump):
          if keys[pygame.K_UP] and y > speed: #same principle apply for the y coordinates
            y -= speed
          if keys[pygame.K_DOWN] and y < 450 - height -speed:
            y += speed
#------------------------------------------------------------------------------------------------------------------        
    #KEYS for CIRCLE object 
    if keys[pygame.K_a] and a > speed: #there is no movement
        a-= speed
    if keys[pygame.K_d]and a < 650 - speed - width: #top right corner less then the screen width
        a+= speed

    #check the user if not jumping
    if not(isJump):
         if keys[pygame.K_w] and b > speed: #same principle apply for the y coordinates
           b-= speed
         if keys[pygame.K_s] and b < 450 - height - speed:
           b+= speed
   
           
 #jumping condition 
    if not(isJump):#check the user not jumping
        if keys[pygame.K_SPACE]:
            isJump =True
    else:#happens if user is jumping
        if jumpCount >= -8:
            y-= (jumpCount*abs(jumpCount))*.5
            jumpCount -= 1
        else:
            jumpCount =8
            isJump = False
            
             #jumping condition 
    if not(isJump2):#check the user not jumping
        if keys[pygame.K_b]:
            isJump2 =True
    else:#happens if user is jumping
        if jumpCount2 >= -8:
            b-= (jumpCount2*abs(jumpCount2 ))*.5
            jumpCount2 -= 1
        else:
            jumpCount2 =8
            isJump2 = False 
            
    game_win.fill((160,160,160))#fill with block
    pygame.draw.rect(game_win, (0,102,204),(x,y,width,height))#window surface drawing a square,
    pygame.draw.circle(game_win,(0,152,76),(int(a),int(b)),radius)
    points = [(325, 0), (650, 225), (325, 450), (0, 225)]
    pygame.draw.lines(game_win, yellow, True, points, 5)
     
    pygame.display.update()#enable to update the screen

pygame.quit()
