# import pygame
# from pygame.locals import *
# import time

# SIZE = 40

# class Apple:
#      def __init__(self,parent_surface) :
#           self.image = pygame.image.load("apple.jpg")
#           self.parent_surface = parent_surface
#           self.block_image_x =SIZE*3
#           self.block_image_y =SIZE*3
          
#      def draw(self):
#            self.parent_surface.blit(self.image, (self.block_image_x, self.block_image_y))
# class Snake:
#      def __init__(self,parent_surface,background_image,length):
#           self.parent_surface = parent_surface
#           self.background_image = background_image
#           self.block_image = pygame.image.load("block.jpg")
#           self.direction = 'down'
#           self.length = length
#           self.block_image_x =[40]*length
#           self.block_image_y =[40]*length
         

#      def move_left(self):
#           self.direction = 'left'

#      def move_right(self):
#           self.direction = 'right'

#      def move_up(self):
#           self.direction = 'up'

#      def move_down(self):
#           self.direction = 'down'

#      def walk(self):

#           for i in range(self.length-1,0,-1):
#                self.block_image_x[i] = self.block_image_x[i - 1]
#                self.block_image_y[i] = self.block_image_y[i - 1]

          
#           if self.direction == "left":
#                self.block_image_x[0] -= SIZE
#           if self.direction == "right":
#                self.block_image_x[0] += SIZE
#           if self.direction == "up":
#                self.block_image_y[0] -= SIZE
#           if self.direction == "down":
#                self.block_image_y[0] += SIZE
          
#           self.draw()

#      def draw(self):
#           self.parent_surface.blit(self.background_image,(0,0))
#           for i in range(self.length):
#                self.parent_surface.blit(self.block_image,(self.block_image_x[0],self.block_image_y[0]))
#           pygame.display.flip()
          
# class Game:
#      def __init__(self):
#           pygame.init()  #initialize the pygame module
#           self.surface = pygame.display.set_mode((1000,700))  #initialize a window or screen for display
#              #display a backgound of game
#           self.background_image = pygame.image.load("background.jpg")
#           self.background_image = pygame.transform.scale(self.background_image,(1000,700))
#           self.surface.blit(self.background_image,(0,0))
#           self.snake = Snake(self.surface,self.background_image,4)
#           self.apple = Apple(self.surface)

#           pygame.display.update()
          

#      def run(self):
#            #Make a event loop for game 
#     # here we can loop for screening view and quitting the screen
#           running = True
#           while running:
#             for event in pygame.event.get():
#                   if event.type == KEYDOWN:
#                         if event.key == K_ESCAPE:
#                              running = False

#                              #movement of block
#                         if event.key == K_UP:
#                               self.snake.move_up()
#                         if event.key == K_DOWN:
#                               self.snake.move_down()
#                         if event.key == K_LEFT:
#                              self.snake.move_left()
#                         if event.key == K_RIGHT:
#                              self.snake.move_right()
                              
#                   elif event.type == QUIT:
#                      running = False
          
#                   self.snake.walk()
#                   time.sleep(0.3)
          
    
# if __name__ == "__main__":
#     game = Game()
#     game.run()
  



# Convert block into a snake
# Draw apple at random locations

import pygame
from pygame.locals import *
import time
import random

SIZE = 40
BACKGROUND_COLOR = (110,110,5)

class Apple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("apple.jpg").convert()
        self.x = 120
        self.y = 120

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(1,19)*SIZE
        self.y = random.randint(1,13)*SIZE

class Snake:
    def __init__(self, parent_screen, length):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("block.jpg").convert()
        self.direction = 'down'

        self.length = length
        self.x = [40]*length
        self.y = [40]*length

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

    def move_left(self):
        self.direction = 'left'

    def move_right(self): 
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def walk(self):
        # update body
        for i in range(self.length-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        # update head
        if self.direction == 'left':
            self.x[0] -= SIZE
        if self.direction == 'right':
            self.x[0] += SIZE
        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] += SIZE

        self.draw()

    def draw(self):

        for i in range(self.length):
            self.parent_screen.blit(self.image, (self.x[i], self.y[i]))
        pygame.display.flip()

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Vivek Sharma Snake and Apple Game")

        pygame.mixer.init()
        self.play_background_music()
        pygame.mixer.music.play(-1)

        self.surface = pygame.display.set_mode((850, 700))
        self.snake = Snake(self.surface, 1)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()

    def is_collision(self,x1,y1,x2,y2):
        if x1 >= x2 and x1 < x2 + SIZE:
          if y1 >= y2 and y1 < y2 + SIZE:
              return True
        return False
    
    def render_background(self):
        bg = pygame.image.load("background.jpg")
        self.surface.blit(bg,(0,0))
    def play_background_music(self):
        pygame.mixer.music.load("bg_music_1.mpeg")
        pygame.mixer.music.play()

    def is_collision_with_wall(self, x, y):
        WALL_LEFT = 0
        WALL_RIGHT = 840
        WALL_TOP = 0
        WALL_BOTTOM = 700

        if x < WALL_LEFT or x >= WALL_RIGHT or y < WALL_TOP or y >= WALL_BOTTOM:
            return True
        return False    


    def play(self):
        self.render_background()
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()

        if self.is_collision_with_wall(self.snake.x[0], self.snake.y[0]):
            sound = pygame.mixer.Sound("crash.mp3")
            pygame.mixer.Sound.play(sound)
            raise "Game Over"

        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            sound = pygame.mixer.Sound("ding.mp3")
            pygame.mixer.Sound.play(sound)
            self.snake.increase_length()
            self.apple.move()


        # snake colliding with apple
        if self.is_collision(self.snake.x[0],self.snake.y[0],self.apple.x,self.apple.y):
          sound = pygame.mixer.Sound("ding.mp3")
          pygame.mixer.Sound.play(sound)
          self.snake.increase_length()
          self.apple.move()
       
        #snake colliding with itself
        for i in range(1,self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0],self.snake.x[i],self.snake.y[i]):
               sound = pygame.mixer.Sound("crash.mp3")
               pygame.mixer.Sound.play(sound)
               raise "Game Over"
            
    def show_game_over(self):
        self.render_background()
        font = pygame.font.SysFont('arial',30)
        line1 = font.render(f"Game is over! Your score is {self.snake.length}",True,(255,255,255))
        self.surface.blit(line1,(100,200))
        line2 = font.render("To Play again press Enter. To Exit enter Escape",True,(255,255,255))
        self.surface.blit(line2,(100,250))
        pygame.display.flip()
        
        pygame.mixer.music.unpause()
            
    def display_score(self):
        font = pygame.font.SysFont('04b_03.',30)
        score = font.render(f"Score:{self.snake.length}",True,(255,255,255))
        self.surface.blit(score,(600,10))


    def reset(self):
        self.snake = Snake(self.surface,1)
        self.apple=Apple(self.surface)

    def run(self):
        running = True
        pause = False
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_RETURN:
                        pygame.mixer.music.unpause()
                        pause = False

                    if not pause:
                      if event.key == K_LEFT:
                        self.snake.move_left()

                      if event.key == K_RIGHT:
                        self.snake.move_right()

                      if event.key == K_UP:
                        self.snake.move_up()

                      if event.key == K_DOWN:
                        self.snake.move_down()

                elif event.type == QUIT:
                    running = False
            try :
               if not pause:
                 self.play()
            except Exception as e:
               self.show_game_over()
               pause = True
               self.reset()
            time.sleep(.2)

if __name__ == '__main__':
    game = Game()
    game.run()

























