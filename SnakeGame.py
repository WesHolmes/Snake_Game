import random
import pygame
import time

pygame.init()  #initalizing pygame into python

surface = pygame.display.set_mode((600,600))
black = (0,0,0)
white = (255,255,255)
green = (24,134,45)
light_green = (65,169,76)
clock = pygame.time.Clock() # time for tick rate
snake_green = (0, 255, 0)
snake_size = 30 # size of snake
snake = pygame.Rect(10, 10, snake_size, snake_size)
vel = 30 # velocity
direction = (1,0) #x and y cord. for snake position
#Snake.render(surface)
start = False
once = False


# snake functions(location, updating head of self, draw self, check for crash)
class Snake():
    def __init__(self,x,y):
        global snakex
        global snakey
        snakex = x
        snakey = y
        
        self.segments = [(x,y)] #The snake's x and y cords
    
    def update(self):
        global direction
    
        head = (self.segments[0][0] + direction[0] * vel, self.segments[0][1] + direction[1] * vel) #snake head of x cord. and y cord.
        self.segments.insert(0, head) #inserts head at front of list
        self.segments = self.segments[:len(self.segments) - 1]

    def draw(self):
        for segment in self.segments:
            pygame.draw.rect(surface, snake_green, pygame.Rect(segment[0], segment[1], snake_size, snake_size)) # draws the snake and segments
            
    def eat(self):

        global applex 
        global appley
        
        appleCords = [(applex,appley)] # converts apple x and y cords
        
        if self.segments[0][0] == appleCords[0][0] and self.segments[0][1] == appleCords[0][1]: # compaires snake pos vs apple pos
            
            newApple() # generates new apple cords
            snake.grow() # grows the snake
            
        apple() # draws the apple

    def crash(self):
        if (self.segments[0][0] < 0 or self.segments[0][0] >= 600 or self.segments[0][1] < 0 or self.segments[0][1] >= 600): # checks for crashes on walls
            return True
        for segment in self.segments[1:]:
            if segment == self.segments[0]: # checks for crashes onto other parts of the sanke
                return True
        return False
    def grow(self):
        tail = (self.segments[-1][0] - direction[0], self.segments[-1][1] - direction[1]) # grows the snake's tail
        self.segments.append(tail)

#Board(x and y cord., grid display)
def board():
    global once
    gridx = 30
    gridy = 30

    surface.fill(light_green)

    for n in range(10):   
        for i in range(10):
            pygame.draw.rect(surface, (green), pygame.Rect(gridx + (60 * i), gridy + (60 * n), gridx, gridy))
            #pygame.draw.rect(surface, (24,134,45), pygame.Rect(gridx * i, gridy, (gridx * i) + 40, gridy + 40))
            pygame.display.flip()
    for n in range(10):
        for i in range(10):
            pygame.draw.rect(surface, (green), pygame.Rect(0 + (60 * i), 0 + (60 * n), gridx, gridy))
            #pygame.draw.rect(surface, (24,134,45), pygame.Rect(gridx * i, gridy, (gridx * i) + 40, gridy + 40))
            pygame.display.flip()
    once = True

# creates the cords for the apple when a new one is needed
def newApple():
    
    global applex
    global appley
    
    applex = random.randint(1,19) #Apple x
    appley = random.randint(1,19) #Apple y
    applex = applex * 30 #Fixing cords to board size
    appley = appley * 30

# draws the apple at the given cords
def apple():

    global applex
    global appley
    
    apple_block = pygame.Rect(applex,appley,snake_size,snake_size) # draws the apple
    pygame.draw.rect(surface,(255,0,0), apple_block)
    pygame.display.flip()

def game():
    global start
    start = True
    
    newApple()
    apple()
    
def welcome():
    
    board()
    
    font = pygame.font.Font(None, 52)

    # Create the text surface
    text_surface = font.render("Welcome to the Snake Game!", True, white)

    # Get the rectangle for the text surface
    text_rect = text_surface.get_rect()
    text_rect.center = (300, 250)
    surface.blit(text_surface, text_rect)  

    font = pygame.font.Font(None, 32)

    # Create the text surface
    text_surface = font.render("Click the SPACEBAR to begin", True, white)

    # Get the rectangle for the text surface
    text_rect = text_surface.get_rect()
    text_rect.center = (300, 315)
    surface.blit(text_surface, text_rect) 

    font = pygame.font.Font(None, 32)

    # Create the text surface
    text_surface = font.render("Click Q to quit", True, white)

    # Get the rectangle for the text surface
    text_rect = text_surface.get_rect()
    text_rect.center = (300, 350)
    surface.blit(text_surface, text_rect) 

#snake head
running = True
while running:
    if start == False and once == False:
        welcome()
    if start == False:
        snake = Snake(270,270)
        direction = (1,0)
    clear = True

    keys = pygame.key.get_pressed()
    #quit function of pygame display
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #keyboard movement
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and start == False:
                start = True
                game()
            if event.key == pygame.K_q:
                pygame.quit()
                exit()
            if event.key == pygame.K_RIGHT and direction != (-1,0) and clear == True and start == True:
                direction = (1,0)
                clear = False
                new_coord = snakex
                if snakex > new_coord:
                    clear = True
            if event.key == pygame.K_LEFT and direction != (1,0) and clear == True and start == True:
                direction = (-1,0)
                clear = False
                new_coord = snakex
                if snakex < new_coord:
                    clear = True
            if event.key == pygame.K_UP and direction != (0,1) and clear == True and start == True:
                direction = (0,-1)
                clear = False
                new_coord = snakey
                if snakey > new_coord:
                    clear = True
            if event.key == pygame.K_DOWN and direction != (0,-1) and clear == True and start == True:
                direction = (0,1)
                clear = False
                new_coord = snakey
                if snakey < new_coord:
                    clear = True
            print(pygame.key.name(event.key))

    #quit game if snake crashes
    if snake.crash():
        start = False

        surface.fill(black)
        
        font = pygame.font.Font(None, 32)

        # Create the text surface
        text_surface = font.render("Click the SPACEBAR to begin", True, white)

        # Get the rectangle for the text surface
        text_rect = text_surface.get_rect()
        text_rect.center = (300, 290)
        surface.blit(text_surface, text_rect) 

        font = pygame.font.Font(None, 32)

        # Create the text surface
        text_surface = font.render("Click Q to quit", True, white)

        # Get the rectangle for the text surface
        text_rect = text_surface.get_rect()
        text_rect.center = (300, 315)
        surface.blit(text_surface, text_rect) 
        
    
    pygame.display.flip()

    if start == True:
        surface.fill(black)
        clock.tick(5) #tick rate

        snake.update() # update snake
        snake.draw() # draw snake
        snake.eat() # calls eat

        #delay of tick rate to give updating display
        time.sleep(0.2)

pygame.quit()
exit()
